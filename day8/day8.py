from collections import OrderedDict
import numpy as np

    
def load_input(input, verbose_cmd=False, verbose=False):
    trees = []
    zone_trees = input.split('\n')
    for trees_line in zone_trees:
        if trees_line:
           trees.append([int(x) for x in trees_line]) 
    return np.array(trees)

def game(trees, verbose=False):
    count_trees = 0
    max_height = len(trees)
    for i, tree_line in enumerate(trees):
        max_width = len(tree_line)
        for j, current_tree in enumerate(tree_line):
            w = ((i - 1), j)
            x = ((i+1), j)
            a = (i, (j-1))
            d = (i, (j +1))
            other_trees = {'col': [w, x],  'row': [a, d]}
            the_others = {current_tree: {'col': [],  'row': []}}
            for pos in other_trees:
                for pos_trees in other_trees[pos]:
                    if pos_trees[0] < 0 or pos_trees[0] == max_width:
                        continue
                    if pos_trees[1] < 0 or pos_trees[1] == max_height:
                        continue
                    the_others[current_tree][pos].append(trees[pos_trees[0]][pos_trees[1]])                    
            for pos, values in the_others.items():
                if len(values['col']) < 2 or len(values['row']) < 2:
                    count_trees += 1
                else:
                    if min(values['col']) < current_tree  or min(values['row']) < current_tree:
                        print('current i,j {},{} : {} - {} - v'.format(i,j,current_tree, values))
                        count_trees += 1
                    else:
                        print('current i,j {},{} : {} - {}'.format(i,j,current_tree, values))
    return count_trees

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
grid_tree_sample = load_input(sample_game, verbose=True)
print(grid_tree_sample)
print(game(grid_tree_sample, verbose=True))


print('\nFIRST GAME')
with open('input', 'r') as f:
    input_game = f.read()
grid_tree = load_input(input_game, verbose_cmd=False)
print(game(grid_tree))
# 
# print('\nSAMPLE INPUT 2')
# print(game2(sample_directories))
# 
# print(game2(directories))
# # 
