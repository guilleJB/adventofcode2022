from collections import OrderedDict

def get_elf_carrying_calories(input):
    calories = input.split('\n')
    elves = {}
    elf_num = 1
    for cal in calories:
        if cal:
            elves.setdefault(elf_num, 0)
            elves[elf_num] += int(cal)
        else:
            elf_num +=1
    
    return elves

def get_top_elves_carrying(elves_repartiment, top_elves=1):
    order_calories = OrderedDict(
        {k: v for k, v in sorted(elves_repartiment.items(), key=lambda item: item[1], reverse=True)}
        )
    elves_top = list(order_calories.keys())[:top_elves]
    return {'elves': elves_top, 'total_calories': sum([order_calories[elf] for elf in elves_top])}

with open('input', 'r') as f:
    elves_calories = f.read()

elves_repart = get_elf_carrying_calories(elves_calories)
max_calories = get_top_elves_carrying(elves_repart, top_elves=1)
print('Top one')
print(max_calories)
print('Top three')
max_calories = get_top_elves_carrying(elves_repart, top_elves=3)
print(max_calories)