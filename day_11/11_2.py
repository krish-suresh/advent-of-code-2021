import numpy as np
lines = []
with open('day_11/input.txt') as f:
    lines = f.readlines()
grid = np.array([[int(y) for y in z.strip()] for z in lines])
total= 0
flashes = np.ones(grid.shape)
def flash(i,j):
    global grid, flashes
    total = 0
    if flashes[i,j] != 0 and grid[i, j] > 9:
        flashes[i,j]=0
        total += 1
        temp_grid = np.zeros((grid.shape[0]+2, grid.shape[1]+2))
        temp_grid[1:-1, 1:-1] = grid
        temp_grid[i-1+1:i+3, j-1+1:j+3] += 1
        grid = temp_grid[1:-1, 1:-1]
        flash_grid = np.zeros((grid.shape[0]+2, grid.shape[1]+2))
        flash_grid[i-1+1:i+3, j-1+1:j+3] = temp_grid[i-1+1:i+3, j-1+1:j+3]
        # print(flash_grid)
        # print(np.transpose(np.where(flash_grid > 9)))
        for f in np.transpose(np.where(flash_grid > 9)):
            total += flash(f[0]-1,f[1]-1)
    return total


days = 0
while not np. all((grid == 0)):
    grid += 1
    flashes = np.ones(grid.shape)
    for f in np.transpose(np.where(grid > 9)):
        total += flash(f[0], f[1])
    grid = grid*flashes
    days +=1
print(grid)
print(days)