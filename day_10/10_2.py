import numpy as np
lines = []
with open('day_10/input.txt') as f:
    lines = f.readlines()
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
    }
matches = {
'(': ')',
'[': ']',
'{': '}',
'<': '>'
}
lines = [line.strip() for line in lines]
scores = []
for line in lines:
    a= []
    score = 0
    cor = True
    for char in line:
        if not char in points:
            a.append(char)
        else:
            if matches[a[-1]] == char:
                a.pop(-1)
            else:
                cor = False
                break
    if cor:
        for c in reversed(a):
            score = 5*score + points[matches[c]]
        scores.append(score)    
mid = int((len(scores)-1)/2)
scores.sort()
print(scores[mid])