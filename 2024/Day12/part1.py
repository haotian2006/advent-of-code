import math
import numpy as np
import pandas as pd
import collections 
import re 
import time

def inBounds(l:list,x,y):
    return x >= 0 and x < len(l) and y >= 0 and y < len(l[0])


output = 0
START_TIME = time.time()
map = []
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
with open('input.txt') as f:
    for line in f.readlines():
        map.append(list(line.strip()))
        
        searched = set()
        groups = []
    def search(x,y,group:list):
        if not inBounds(map,x,y) or (x,y) in searched:
            return
        char = map[x][y]
        if char != group[0]:
            return
        searched.add((x,y))
        group.append((x,y))
        search(x+1,y,group)
        search(x-1,y,group)
        search(x,y+1,group)
        search(x,y-1,group)
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x,y) in searched:
                continue
            group = [map[x][y]]
            search(x,y,group)
            groups.append(group)
    def getSides(x,y):
        char = map[x][y]
        count = 0 
        for dx,dy in dirs:
            if (not inBounds(map,x+dx,y+dy)) or map[x+dx][y+dy] != char:
                count += 1
        return count

    for g in groups: 
        area = len(g)-1
        p = 0
        for i in range(1,len(g)):
            x,y = g[i]
            p += getSides(x,y)
        output += area * p
print(output) 
print((time.time()-START_TIME) * 1000, "ms")
