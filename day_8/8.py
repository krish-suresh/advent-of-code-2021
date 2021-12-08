import numpy as np
lines = []
with open('day_8/input.txt') as f:
    lines = f.readlines()
inputs = []
outputs = []
for line in lines:
    a = line.strip().split(' | ')
    inputs.append(a[0].split(' '))
    outputs.append(a[1].split(' '))
total = 0
for output in outputs:
    for digit in output:
        if len(digit) in [2,3,4,7]:
            total+=1
print(total)
