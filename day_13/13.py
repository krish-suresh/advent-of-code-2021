import numpy as np
from collections import Counter
lines = []
with open('day_13/input.txt') as f:
    lines = f.readlines()

num_coords = 12
folds = [x.strip().split(' ')[-1].split('=') for x in lines[-num_coords:]]
for i, fold in enumerate(folds):
    folds[i][1] = int(fold[1])

lines = np.array([[int(y) for y in x.strip().split(',')] for x in lines[0:-num_coords-1]])
grid = np.zeros((np.max(lines[:, 1])+1, np.max(lines[:, 0])+1))

for line in lines:
    grid[line[1], line[0]] = 1

for fold in folds:
    if fold[0] == 'y':
        new_grid = np.zeros((max(fold[1], grid.shape[0] - fold[1]-1), grid.shape[1]))
        new_grid[0:fold[1], 0:grid.shape[1]] += grid[0:fold[1], 0:grid.shape[1]]
        flip = np.flip(grid[fold[1]+1:, 0:grid.shape[1]], 0)
        new_grid[-flip.shape[0]:, 0:grid.shape[1]] += flip
        grid = np.copy(new_grid)
    if fold[0] == 'x':
        new_grid = np.zeros((grid.shape[0], max(fold[1], grid.shape[1] - fold[1]-1)))
        new_grid[0:grid.shape[0], 0:fold[1]] += grid[0:grid.shape[0], 0:fold[1]]
        flip =  np.flip(grid[0:grid.shape[0],fold[1]+1:], 1)
        new_grid[0:grid.shape[0], -flip.shape[1]:] += flip
        grid = np.copy(new_grid)
# print(folds)
# print(lines)
print((grid > 0).astype(int))
