import numpy as np
lines = []
with open('day_6/input.txt') as f:
    lines = f.readlines()
fishes = [int(x) for x in lines[0].split(',')]
# print(fishes)
fpd = [0]*9
for fish in fishes:
    fpd[fish] += 1
days = 256
total = len(fishes)
for i in range(days):
    new = fpd[0]
    fpd[7] += new
    total += new
    fpd.pop(0)
    fpd.append(new)
print(total)