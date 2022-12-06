LETTERS_MAP = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSOR = ['C', 'Z']

WIN = 6
LOSS = 0
DRAW = 3

RESULT = {
    'X': LOSS,
    'Y': DRAW,
    'Z': WIN
}

def action(move):
    if move in ROCK:
        return 'ROCK'
    elif move in PAPER:
        return 'PAPER'
    elif move in SCISSOR:
        return 'SCISSOR'

def round_score(oponent, me, verbose=True):    
    if LETTERS_MAP[oponent] == LETTERS_MAP[me]:
        result =  DRAW + LETTERS_MAP[me]
    else:
        if oponent in ROCK:
            if me in PAPER:
                result =  WIN + LETTERS_MAP[me]
            else: 
                result =  LOSS + LETTERS_MAP[me]
        elif oponent in PAPER:
            if me in SCISSOR:
                result =  WIN + LETTERS_MAP[me]
            else: 
                result =  LOSS + LETTERS_MAP[me]
        elif oponent in SCISSOR:
            if me in ROCK:
                result =  WIN + LETTERS_MAP[me]
            else: 
                result =  LOSS + LETTERS_MAP[me]
    if verbose:
        print('{}-{}->{}'.format(
            action(oponent), action(me), result
            )
        )
    return result


def next_move(outcoume, oponent, verbose=True):
    if RESULT[outcoume] == DRAW:
        result = oponent    
    elif RESULT[outcoume] == WIN:
        if oponent in ROCK:
            result =  PAPER[0]
        elif oponent in PAPER:
            result =  SCISSOR[0]            
        elif oponent in SCISSOR:
            result =  ROCK[0]
    else:
        if oponent in ROCK:
            result =  SCISSOR[0]
        elif oponent in PAPER:
            result =  ROCK[0]            
        elif oponent in SCISSOR:
            result =  PAPER[0]
    if verbose:
        print('{}-{}'.format(
            action(oponent), action(result)
            )
        )
    return result    

def game(input):
    score = 0
    rounds = input.split('\n')
    for game in rounds:
        if game:
            openent, me = game.split(' ')
            openent = openent.strip()
            me = me.strip()
            print(openent, me)
            score += round_score(openent, me)
            
    return score

def game2(input):
    score = 0
    rounds = input.split('\n')
    for game in rounds:
        if game:
            openent, outcome = game.split(' ')
            openent = openent.strip()
            outcome = outcome.strip()
            me = next_move(outcome, openent)
            print(openent, me)
            score += round_score(openent, me)
            
    return score


with open('input', 'r') as f:
    bigband_game = f.read()

total_score = game(bigband_game)
print('Total score {}'.format(total_score))

print('\nSAMPLE INPUT')
with open('sample_input', 'r') as f:
    sample_game = f.read()
total_score = game(sample_game)
print('Total score {}'.format(total_score))

total_score = game2(bigband_game)
print('Total GAME 2 score {}'.format(total_score))

print('\nSAMPLE INPUT')
total_score = game2(sample_game)
print('Total score {}'.format(total_score))
