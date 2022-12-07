
def proces_config(input, verbose=False):
    crates = input.split('\n')
    positions = {}
    for x in crates[-1].split(' '):
        if x:
            positions[x] = []

    for crate in crates[:-1]:
        for x in list(positions.keys()):
            index = crates[-1].index(str(x))
            if verbose:
                print(x, index, crate)
            create_name = crate[index]
            if create_name.strip():
                positions[x].append(create_name)
    return positions

def do_move(positions, total_moves, from_stack, to_stack):
    mv_crates = []
    for x in range(0, total_moves):
        v = positions[from_stack].pop(0)
        positions[to_stack].insert(0, v)

def do_crate_move_9001(positions, total_moves, from_stack, to_stack):
    mv_crates = []
    for x in range(0, total_moves):
        v = positions[from_stack].pop(0)
        mv_crates.append(v)
    for x in reversed(mv_crates):
        positions[to_stack].insert(0, x)

def extract_move(input):
    return [x for x in input.split() if x.isdigit()]

def get_final_step(positions):
    msg = ''
    for key, values in positions.items():
        msg += values[0]
    return msg
    
def game(positions, input, verbose=False):
    score = 0
    moves = input.split('\n')
    for move in moves:
        if move:
            total_move, from_stack, to_stack = extract_move(
                move
            )
            do_move(positions, int(total_move), from_stack, to_stack)
    
    return get_final_step(positions)

def game2(positions, input, verbose=False):
    score = 0
    moves = input.split('\n')
    for move in moves:
        if move:
            total_move, from_stack, to_stack = extract_move(
                move
            )
            do_crate_move_9001(positions, int(total_move), from_stack, to_stack)
    
    return get_final_step(positions)


print('\nSAMPLE INPUT')
with open('sample_input', 'r') as f:
    sample_game = f.read()
with open('move_sample', 'r') as f:
    move_game_sample = f.read()
positions = proces_config(sample_game)
print(game(positions, move_game_sample))

with open('config_input', 'r') as f:
    config_game = f.read()
with open('move_input', 'r') as f:
    move_game = f.read()
positions = proces_config(config_game, verbose=False)
print(game(positions, move_game))

print('\nSAMPLE SECOND GAME')
positions = proces_config(sample_game)
print(game2(positions, move_game_sample))

positions = proces_config(config_game, verbose=False)
print(game2(positions, move_game))
