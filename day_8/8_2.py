import numpy as np
lines = []
with open('day_8/input.txt') as f:
    lines = f.readlines()
inputs = []
outputs = []
numbers = [[0,1,2,3,4,5],
[2,5],
[0,2,3,4,6],
[0,2,3,5,6],
[1,2,3,5],
[0,1,3,5,6],
[0,1,3,4,5,6],
[0,2,5],
[0,1,2,3,4,5,6]]
for line in lines:
    a = line.strip().split(' | ')
    inputs.append(a[0].split(' '))
    outputs.append(a[1].split(' '))
# list of 
def find_value(inputs, outputs):
    options = [None]*10
    for digits in inputs:
        if len(digits) == 2:
            options[1] = digits
        elif len(digits) == 3:
            options[7] = digits
        elif len(digits) == 4:
            options[4] = digits
        elif len(digits) == 7:
            options[8] = digits
    left_mid = list(set(options[4]) - set(options[1]))
    for digits in inputs:
        if len(digits) == 6:
            if not all(elem in digits for elem in options[1]):
                options[6] = digits
            elif not all(elem in digits for elem in left_mid):
                options[0] = digits
            else:
                options[9] = digits
        if len(digits) == 5:
            if all(elem in digits for elem in options[1]):
                options[3] = digits
            elif all(elem in digits for elem in left_mid):
                options[5] = digits
            else:
                options[2] = digits
    a = ''
    for output in outputs:
        for i,digit in enumerate(options):
            if sorted(digit) == sorted(output):
                a +=str(i)
    return int(a)

total = 0
for input, output in zip(inputs, outputs):
    total += find_value(input, output)
print(total)
