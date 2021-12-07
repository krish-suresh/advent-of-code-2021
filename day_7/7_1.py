import numpy as np
lines = []
with open('day_7/input.txt') as f:
    lines = f.readlines()
crabs = [int(x) for x in lines[0].split(',')]
fuels = [0]*len(crabs)
min = 99999999
for crab in crabs:
    a = sum([abs(crab-x) for x in crabs])
    if min > a:
        min = a
print(min)