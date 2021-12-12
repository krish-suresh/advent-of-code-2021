import numpy as np
lines = []
with open('day_12/input.txt') as f:
    lines = f.readlines()
lines = [x.strip().split('-') for x in lines]
map = {}
for line in lines:
    if line[0] not in map:
        map[line[0]] = []
    map[line[0]].append(line[1])
    if line[1] not in map:
        map[line[1]] = []
    map[line[1]].append(line[0])
print(map)

def search_path(cave, map, path):
    if cave == 'end':
        return 1
    total = 0
    for next in map[cave]:
        if next.islower() and next in path:
            continue
        total += search_path(next, map, (path + [cave]).copy())
    return total
print(search_path('start', map, []))