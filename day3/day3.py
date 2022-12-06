from string import ascii_letters

def get_letter(input):
    word_list = []
    for i in input:
        if i:
            word_list.append(set(i))
    if word_list:
        letter = word_list[0].intersection(*word_list[1:])
        letter = letter.pop()
    else:
        letter = False
    return letter

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

def get_score_rucksack(input, verbose=False):
    letter = get_letter(input)
    if not letter:
        return {'score': 0, 'letter': letter}
    score = ascii_letters.index(letter) + 1
    if verbose:
        print(input[0], input[1], letter, score)
    return {'score': score, 'letter': letter}

def game(input):
    score = 0
    rucksacks = input.split('\n')
    for rucksack in rucksacks:
        rucksack_parts = []
        if rucksack:
            rucksack_parts.append(
                rucksack[:int(len(rucksack)/2.0)]
            )
            rucksack_parts.append(
                rucksack[int(len(rucksack)/2.0):]
            )
            score += get_score_rucksack(rucksack_parts)['score']            
    return score

def game2(input):
    score = 0
    rucksacks = input.split('\n')
    for rucksack in chunks(rucksacks, 3):        
        score += get_score_rucksack(rucksack)['score']            
    return score


print('\nSAMPLE INPUT')
with open('sample_input', 'r') as f:
    sample_game = f.read()

total_score = game(sample_game)
print('Total score {}'.format(total_score))

print('\nINPUT')
with open('input', 'r') as f:
    input_game = f.read()

total_score = game(input_game)
print('Total score {}'.format(total_score))

print('\nSAMPLE SECOND GAME')
total_score = game2(sample_game)
print('Total score {}'.format(total_score))

print('\nSECOND GAME')
total_score = game2(input_game)
print('Total score {}'.format(total_score))
