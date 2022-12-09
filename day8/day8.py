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

def game2(trees, verbose=False):
    count_trees = 0
    max_height,max_width = np.shape(trees)
    max_score = 0
    for i in range(1, max_height-1):
        for j in range(1, max_width - 1):
            scenic_score = 1
            current_tree = trees[i,j]
            is_visible = False
            up = trees[:i, j]
            if current_tree > max(up):
                is_visible = True
            down = trees[i+1:, j]
            if current_tree > max(down):
                is_visible = True
            right = trees[i, j+1:]
            if current_tree > max(right):
                is_visible = True
            left = trees[i, :j]
            if current_tree > max(left):
                is_visible = True         
            if is_visible:
                if verbose:
                    print(current_tree)
                for scenic in [reversed(up), down, right, reversed(left)]:
                    ss = 0
                    for x in scenic:
                        if x < current_tree:
                            ss += 1
                        else:
                            ss += 1
                            break
                    if verbose:
                        print('   ', ss, scenic)
                    scenic_score = scenic_score * ss
                if verbose:
                    print('Total ', scenic_score)    
                max_score = max(max_score, scenic_score)
    return max_score


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

print('\nSAMPLE INPUT 2')
print(game2(grid_tree_sample))

print(game2(grid_tree))
# 
