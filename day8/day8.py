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
    max_height,max_width = np.shape(trees)
    for i in range(1, max_height-1):
        for j in range(1, max_width - 1):
            current_tree = trees[i,j]
            is_visible = False
            if current_tree > max(trees[:i, j]):
                is_visible = True
            if current_tree > max(trees[i+1:, j]):
                is_visible = True
            if current_tree > max(trees[i, j+1:]):
                is_visible = True
            if current_tree > max(trees[i, :j]):
                is_visible = True         
            if is_visible:
                count_trees += 1
    count_trees += (max_height * 2) + ( (max_width -2) * 2)
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
