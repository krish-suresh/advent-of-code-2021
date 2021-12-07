import numpy as np
lines = []
with open('day_7/input.txt') as f:
    lines = f.readlines()
crabs = [int(x) for x in lines[0].split(',')]
fuels = [0]*len(crabs)
min = 9999999999
for crab in range(max(crabs)+1):
    a = sum([(abs(crab-x)*(abs(crab-x)+1))/2 for x in crabs])
    if min > a:
        min = a
        print(crab)
print(min)