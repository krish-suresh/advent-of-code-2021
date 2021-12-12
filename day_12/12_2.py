import numpy as np
from collections import Counter
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
# print(map)
path_list = []
def search_path(cave, map, path, l):
    if cave == 'end':
        path_list.append(path + [cave])
        return 1
    total = 0
    for next in map[cave]:
        if next.islower() and next in path and not(next==l and path.count(l)<2):
            continue
        total += search_path(next, map, (path + [cave]).copy(), l)
    return total
for c in map:
    if c.islower() and c != 'start' and c != 'end':
        search_path('start', map, [], c)
print(len(Counter(str(e) for e in path_list)))