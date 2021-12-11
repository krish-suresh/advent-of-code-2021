import numpy as np
lines = []
with open('day_10/input.txt') as f:
    lines = f.readlines()
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }
matches = {
'(': ')',
'[': ']',
'{': '}',
'<': '>'
}
lines = [line.strip() for line in lines]
total = 0
for line in lines:
    a= []
    for char in line:
        if not char in points:
            a.append(char)
        else:
            if matches[a[-1]] == char:
                a.pop(-1)
            else:
                total += points[char]
                break

print(total)