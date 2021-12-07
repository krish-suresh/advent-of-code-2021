import numpy as np
lines = []
with open('day_1/measurements.txt') as f:
    lines = f.readlines()
count = 0
prev = None
lines = [int(x) for x in lines]
for i in range(len(lines)-2):
    avg = np.mean(lines[i:i+3])
    print(lines[i:i+3])
    if prev:
        if avg>prev:
            count += 1
    prev = avg
print(f'Total measurements: {count}')    