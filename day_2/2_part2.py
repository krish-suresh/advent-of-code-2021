import numpy as np
lines = []
with open('day_2/dive.txt') as f:
    lines = f.readlines()
count = 0
prev = None
lines = [x.split(' ') for x in lines]
x,y,aim=0,0,0
for line in lines:
    if line[0] == 'forward':
        x += int(line[1])
        y += int(line[1])*aim
    elif line[0] == 'down':
        aim += int(line[1])
    else:
        aim -= int(line[1])
print(f'Total measurements: {x*y}')    