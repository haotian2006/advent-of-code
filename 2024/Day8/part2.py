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
    checked = {}
    for k,v in chars.items():
        for x,y in v:
            for ox,oy in v:
                if ox == x and oy == y:
                    continue
                dx = x - ox
                dy = y - oy
                
                px,py = x+dx,y+dy
                while inBounds(py,px): 
                    antiNodes[f'{py},{px}'] = 1
                    t[py][px] = '#'
                    px+=dx
                    py+=dy
                    
                px,py = ox+dx,oy+dy
                while inBounds(px,py):
                    antiNodes[f'{py},{px}'] = 1
                    t[py][px] = '#' 
                    px+=dx
                    py+=dy
                    
                    
                    

    output = len(antiNodes)

for x in t:
    print(''.join(x))

print(output)
