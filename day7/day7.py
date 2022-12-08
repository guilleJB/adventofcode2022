from collections import OrderedDict

class FileSystem:
    def __init__(self, name, type_file, size=0):
        self._name = name
        self._type_file = type_file
        self._size = size
        self._sub_files = []
    
    @property
    def name(self):
        return self._name

    def is_directory(self):
        return self._type_file == 'dir'
    
    def print_files(self, filesytem, tab_num=0):
        repf = ''
        tab_num = tab_num + 1
        if filesytem._type_file == 'file':
            repf = '({}, size={})'.format(filesytem._type_file, filesytem._size)
        else:
            repf = '({})'.format(filesytem._type_file)
        if filesytem._type_file == 'dir':
            repf += ' - ({})'.format(filesytem.size_of())
        rep = '{}- {} {}'.format('    '*tab_num, filesytem._name, repf)
        
        if filesytem._sub_files:
            for f in filesytem._sub_files:
                rep += '\n {}'.format(
                    self.print_files(f, tab_num=tab_num+1)
                    )
        return rep

    def add_file(self, file_system):
        if self._type_file == 'file':
            raise Exception('Error not put file into ')
        if isinstance(file_system, (list, tuple)):
            for x in file_system:
                self._sub_files.append(x)
        else:
            self._sub_files.append(file_system)
    
    def size(self):
        return sum([x._size for x in self._sub_files if x._type_file == 'file'])

    def size_of(self):
        total_size = 0
        if self._type_file == 'file':
            total_size = self._size
        else:
            if self._sub_files:
                for f in self._sub_files:
                    total_size += f.size_of()
        return total_size

    def __repr__(self):
        if self._type_file == 'file':
            repf = '({}, size={})'.format(self._type_file, self._size)
        else:
            repf = '({}) - ({})'.format(self._type_file, self.size_of())
        rep = '- {} {}'.format(self._name, repf)

        if  self._sub_files:
            for f in self._sub_files:
                rep += '\n {}'.format(self.print_files(f))
        return rep

class FileType(FileSystem):
    def __init__(self, name, size=0):
        self._name = name
        self._type_file = 'file'
        self._size = size
        self._sub_files = None

class DirType(FileSystem):
    def __init__(self, name):
        self._name = name
        self._type_file = 'dir'
        self._size = 0
        self._sub_files = []
    def get_ls(self):
        ls = {}
        for x in self._sub_files:
            if x.is_directory():
                ls[x.name] = x
        return ls



def get_start_message(msg, group_words=4):
    for i, letter in enumerate(msg):
        sub = msg[i:i+group_words]
        count = Counter(sub)
        if len(count) == group_words:
            return i+group_words
    return -1

    
def load_directory(input, verbose_cmd=False, verbose=False):
    pwd = []
    all_directoris = []
    current_dir = None
    global_ls = {}
    ls = {}
    commands = input.split('\n')
    if verbose:
        verbose_cmd = True
    for command in commands:
        if verbose:
            print('pwd {}'.format(pwd))
            print('ls {}'.format(ls))
            print('current dir \n{}'.format(current_dir))
        if verbose_cmd:
            print('### - {}'.format(command))
        if not command.strip():
            continue
        if '$' in command:
            to_do = command.split(' ')
            if 'cd' in to_do:
                if to_do[-1] == '..':
                    pwd.pop()
                    full_dir = '-'.join(pwd)
                    ls = global_ls[full_dir]['ls']
                else:
                    if to_do[-1] == '/':
                        root = DirType('/')
                        all_directoris.append(root)
                        current_dir = root
                    else:
                        current_dir = ls[to_do[-1]]
                    pwd.append(to_do[-1])                 
            elif 'ls' in to_do:
                ls = {}
                full_dir = '-'.join(pwd)
                global_ls[full_dir] = {'dirs': {}, 'ls':ls}
        else:
            is_file = command.split(' ')
            if 'dir' in is_file:
                file_system = DirType(is_file[1])
                all_directoris.append(file_system)
                full_dir = '-'.join(pwd)
                global_ls[full_dir]['dirs'][is_file[1]] = file_system
                ls[is_file[1]] = file_system
            else:
                file_system = FileType(is_file[1], size=int(is_file[0]))
            current_dir.add_file(file_system)
    if verbose:
        print(all_directoris[0])
    return all_directoris

def game(directories, verbose=False):
    total_sum = 0
    for d in directories:
        if not isinstance(d, FileSystem):
            print(d)
            continue
        size = d.size_of()
        if size <= 100000:
            if verbose:
                print(d.name)
            total_sum += size
    return total_sum

def game2(directories, verbose=False):
    min_space = 30000000
    spaces = []
    for d in directories:
        size = d.size_of()
        calc_space = min_space - size
        if calc_space >0:
            spaces.append((calc_space, size))

    spaces.sort(key=lambda a: a[0])
    return spaces[0]


print('\nSAMPLE INPUT')
with open('sample_input', 'r') as f:
    sample_game = f.read()
sample_directories = load_directory(sample_game, verbose=True)
print(game(sample_directories, verbose=True))


print('\nFIRST GAME')
with open('input', 'r') as f:
    input_game = f.read()
directories = load_directory(input_game, verbose_cmd=False)
#print(directories)
print(game(directories))

print('\nSAMPLE INPUT 2')
print(game2(sample_directories))

print(game2(directories))
# 
# with open('config_input', 'r') as f:
#     config_game = f.read()
# with open('move_input', 'r') as f:
#     move_game = f.read()
# positions = proces_config(config_game, verbose=False)
# print(game(positions, move_game))
# 
# print('\nSAMPLE SECOND GAME')
# positions = proces_config(sample_game)
# print(game2(positions, move_game_sample))
# 
# positions = proces_config(config_game, verbose=False)
# print(game2(positions, move_game))
