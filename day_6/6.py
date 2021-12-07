import numpy as np
lines = []
with open('day_6/input.txt') as f:
    lines = f.readlines()
fishes = [int(x) for x in lines[0].split(',')]
# print(fishes)
days = 256
for i in range(days):
    fishes = [fish-1 for fish in fishes]
    for i, fish in enumerate(fishes):
        if fish == -1:
            fishes[i] = 6
            fishes.append(8)
print(len(fishes))
