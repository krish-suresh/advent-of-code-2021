import numpy as np
from collections import Counter
lines = []
with open('day_15/inputT.txt') as f:
    lines = f.readlines()
lines = np.array([[int(x) for x in list(y.strip())] for y in lines])
grid = np.full((lines.shape[0]+2, lines.shape[1]+2), np.max(lines)+1)
grid[1:-1, 1:-1] = lines
min_grid = np.zeros(grid.shape)
def path(i,j):
    path(i-1, j)
    path(i, j-1)
print(grid)