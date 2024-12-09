import math
import numpy as np
import pandas as pd
import collections 
import re 

output = 0

with open('input.txt') as f:
    chars = {}
    antiNodes = {}
    h,w = 0,0
    t = []
    for y,line in enumerate(f.readlines()):
        line = line.strip()
        t.append(list(line))
        w = len(line)
        h=y+1
        for x in range(w): 
            c = line[x]
            if c == '.':
                continue 
            if not c in chars:
                chars[c] = []
            chars[c].append((x,y))
    def inBounds(x,y):
        return x >= 0 and x < w and y >= 0 and y < h 
    for k,v in chars.items():
        for x,y in v:
            for ox,oy in v:
                if ox == x and oy == y:
                    continue
                dx = x - ox
                dy = y - oy
                if inBounds(y+dy,x+dx): 
                    antiNodes[f'{y+dy},{x+dx}'] = 1
                    t[y+dy][x+dx] = '#'

                if inBounds(oy-dy,ox-dx):
                    antiNodes[f'{oy-dy},{ox-dx}'] = 1
                    t[oy-dy][ox-dx] = '#'
    output = len(antiNodes.keys())

for x in t:
    print(''.join(x))
    
print(output)

