import numpy as np
lines = []
with open('day_5/vents.txt') as f:
    lines = f.readlines()
lines = [[[int(z) for z in y.split(',')]for y in x.strip().split(' -> ')] for x in lines]
grid_dim = np.max(lines)+1
grid = np.zeros((grid_dim,grid_dim))
for line in lines:
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]
    if x1 == x2:
        if y2<y1:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            grid[y][x1] += 1
    if y1 == y2:
        if x2<x1:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            grid[y1][x] += 1
    if y2-y1 == x2-x1:
        if x2<x1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for i, x in enumerate(range(x1, x2+1)):
            grid[y1+i][x] += 1
    if y2-y1 == x1-x2:
        if x2<x1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for i, x in enumerate(range(x1, x2+1)):
            grid[y1-i][x] += 1

print((grid>1).sum())
