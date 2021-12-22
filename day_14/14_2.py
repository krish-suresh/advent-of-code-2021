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
o = Counter(template)
d = {}
def combine(l, j):
    a = l.copy()
    b = j.copy()
    for k, v in a.items():
        if k in b:
            b[k] += v
        else:
            b[k] = v
    return b

def rec(s, i):
    if i == 0:
        return {}
    if s+str(i) in d:
        return d[s+str(i)]
    ret = combine(rec(s[0]+pairs[s], i-1), rec(pairs[s]+s[1], i-1))
    if pairs[s] not in ret:
        ret[pairs[s]] = 0
    ret[pairs[s]] += 1 
    d[s+str(i)] = ret
    return ret
# template = 'NNC'

for l_0,l_1 in zip(template[:-1],template[1:]):
    o = combine(o,rec(l_0+l_1, 40))
print(max(o.values())-min(o.values()))