import math
import numpy as np
import pandas as pd
import collections 
import re 
import time

output = 0
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
START_TIME = time.time()
with open('input.txt') as f:
    m = [list(map(int,list(l.strip()))) for l in f.readlines()]
    def branch(v:dict, x, y,lHeight):
        if ((x,y) in v )or x < 0 or y < 0 or x >= len(m[0]) or y >= len(m):
            return 0
        value = m[y][x]  
        if value - lHeight != 1:
            return 0 
        if value == 9:   
            v[((x,y))] = 1 
            return 1
        sum = 0
        for dx, dy in dirs:
            sum+=branch(v, x+dx, y+dy,value)
        return sum 
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == 0:
                output += branch({}, x, y, -1)
print(output) 
print((time.time()-START_TIME) * 1000, "ms")
