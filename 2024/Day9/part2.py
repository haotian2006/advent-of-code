import math
import numpy as np
import pandas as pd
import collections 
import re 
import time

output = 0
START_TIME = time.time()
with open('input.txt') as f:
    line = f.read()
    newStr = ''
    id = 0
    l = []
    freeSpaces = []
    for i in range(len(line)):
        char = line[i]
        if i%2 == 0:
            l.extend([id]*int(char))
            id+=1
        else:
            l.extend(['.']*int(char))
    print("parsed")

    gs = []
    last = -1
    start = 0
    for i in range(len(l)):
        cAt = l[i]
        if cAt == '.':
            if last != -1:
                gs.insert(0,(last, i-start, start))
            last = -1
            continue
        if last != cAt:
            if last != -1 and last != -1:
                gs.insert(0,(last, i-start, start))
            start = i
            last = cAt
    if last != 0:
        gs.insert(0,(last, len(l)-start, start))
    print("matched")
    r = [False]*(len(l)+1)
    for i in range(len(l)):
        if l[i] != '.':
            continue
        ii = 0
        for c,le,s in gs:
            if s < i:
                break
            p = True
            for j in range(i,i+le):
                if j >= len(l):
                    p = False
                    break
                if l[j] != '.':
                    p = False
                    break
            if p:
                for j in range(i,i+le):
                    l[j] = c
                for j in range(s,s+le):
                    r[j] = True
                gs.pop(ii)
                break
            ii+=1
    
    for i in range(len(l)):
        if l[i] != '.' and not r[i]:
            output += int(l[i]) * i
                
        

print(output)
print("Part2",(time.time()-START_TIME) * 1000, "ms")


