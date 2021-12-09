import numpy as np
lines = []
with open('day_9/input.txt') as f:
    lines = f.readlines()
lines = [[int(x) for x in list(line.strip())] for line in lines]
lines = np.array(lines)
total = 0
grid = np.full((lines.shape[0]+2, lines.shape[1]+2), np.max(lines))
grid[1:-1, 1:-1] = lines
max_basins = [0]*3
count_grid = np.zeros(grid.shape)
def basin_size(i,j):
    h = grid[i][j]
    total = 0
    # print(f"i: {i} j: {j}")
    if not (grid[i-1][j] < h or grid[i-1][j] == 9) and count_grid[i-1][j] == 0:
        count_grid[i-1][j] = 1
        total += basin_size(i-1,j)
    if not (grid[i+1][j] < h or grid[i+1][j] == 9) and count_grid[i+1][j] == 0:
        count_grid[i+1][j] = 1
        total += basin_size(i+1,j)
    if not (grid[i][j-1] < h or grid[i][j-1] == 9) and count_grid[i][j-1] == 0:
        count_grid[i][j-1] = 1
        total += basin_size(i,j-1)
    if not (grid[i][j+1] < h or grid[i][j+1] == 9) and count_grid[i][j+1] == 0:
        count_grid[i][j+1] = 1
        total += basin_size(i,j+1)
    return 1 + total
    

for i, line in enumerate(grid):
    for j, h in enumerate(line):
        if i == 0 or j == 0 or i == grid.shape[0] or j == grid.shape[1]:
            pass
        if grid[i-1][j] > h and grid[i+1][j] > h and grid[i][j-1] > h and grid[i][j+1] > h:
            # print(f"dfgi: {i} j: {j}")
            count_grid = np.zeros(grid.shape)
            size = basin_size(i,j) 
            if size> min(max_basins):
                max_basins[max_basins.index(min(max_basins))] = size
                # print(max_basins)
print(np.prod(max_basins))
