import numpy as np
lines = []
with open('day_3/binary.txt') as f:
    lines = f.readlines()
for i,x in enumerate(lines):
    x = x.strip()
    lines[i] = [int(x) for x in list(x)]
lines = np.array(lines)
oxygen,carbon=lines.copy(), lines.copy()
for i in range(len(oxygen[0])):
    bit_max = np.bincount(oxygen[:, i]).argmax()
    bit_min = np.bincount(oxygen[:, i]).argmin()
    bit = bit_max
    if len(oxygen)==1:
        break
    elif len(oxygen) == 2 or bit_max == bit_min:
        bit = 1
    oxygen = oxygen[np.in1d(oxygen[:, i], np.asarray([bit]))]

for i in range(len(carbon[0])):
    bit_max = np.bincount(carbon[:, i]).argmax()
    bit_min = np.bincount(carbon[:, i]).argmin()
    bit = bit_min
    if len(carbon)==1:
        break
    elif len(carbon) == 2 or bit_max == bit_min:
        bit = 0
    carbon = carbon[np.in1d(carbon[:, i], np.asarray([bit]))]
oxy = int("".join(str(x) for x in oxygen.flatten()), 2)
c02 = int("".join(str(x) for x in carbon.flatten()), 2)

print(f'Total: {oxy*c02}')    