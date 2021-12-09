import numpy as np
lines = []
with open('day_9/input.txt') as f:
    lines = f.readlines()
lines = [[int(x) for x in list(line.strip())] for line in lines]
lines = np.array(lines)
total = 0
grid = np.full((lines.shape[0]+2, lines.shape[1]+2), np.max(lines))
grid[1:-1, 1:-1] = lines
for i, line in enumerate(grid):
    for j, h in enumerate(line):
        if i == 0 or j == 0 or i == grid.shape[0] or j == grid.shape[1]:
            pass
        if grid[i-1][j] > h and grid[i+1][j] > h and grid[i][j-1] > h and grid[i][j+1] > h:
             total +=1+h
print(total)
