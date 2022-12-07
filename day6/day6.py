from collections import Counter

def get_start_message(msg, group_words=4):
    for i, letter in enumerate(msg):
        sub = msg[i:i+group_words]
        count = Counter(sub)
        if len(count) == group_words:
            return i+group_words
    return -1

    
def game(input, group_words=4, verbose=False):
    score = 0
    messages = input.split('\n')
    for msg in messages:
        if msg:
            first_position = get_start_message(msg, group_words=group_words)
            print(first_position)
    
    return True

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
game(sample_game)

print('\nFIRST GAME')
with open('input', 'r') as f:
    input_game = f.read()
game(input_game)

print('\nSAMPLE INPUT 2')
game(sample_game, group_words=14)

game(input_game, group_words=14)
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
