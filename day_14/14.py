import numpy as np
from collections import Counter
lines = []
with open('day_14/input.txt') as f:
    lines = f.readlines()
template = lines[0].strip()
pairs = {}
for i in lines[2:]:
    i = i.strip().split(' -> ')
    pairs[i[0]] = i[1]
o = {}
def rec(s, i, first = False):
    if i == 0:
        pass
    else:
        for l_0,l_1 in zip(s[:-1],s[1:]):
            l = l_0+l_1
            if pairs[l] not in o:
                o[pairs[l]] = 0
            o[pairs[l]] += 1 
            rec(l_0+pairs[l]+l_1, i-1)
        if first:
            for k,v in Counter(s).items():
                if k not in o:
                    o[k] = 0
                o[k] += v     
rec(template, 40, first = True)
print(max(o.values())-min(o.values()))
