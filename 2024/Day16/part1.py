import math
import numpy as np
import pandas as pd
import collections 
import re 
import time
import sympy as sp
from sympy.abc import x, y
import heapq
import sys
sys.setrecursionlimit(10000)

def printMap(m):
    for i in m:
        print(''.join(map(str,i)))

def inBounds(l:list,x,y):
    return x >= 0 and x < len(l) and y >= 0 and y < len(l[0])

output = 0
START_TIME = time.time()
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
sideDirs = [[1,3],[0,2],[1,3],[0,2]]
with open('input.txt') as f:
    maze = []
    start = None
    end = None
    for c,line in enumerate(f.readlines()):
        chars = []
        maze.append(chars)
        for r,char in enumerate(line):
            if char == 'S':
                start = (c,r)
                chars.append('.')  
            elif char == 'E':
                end = (c,r)
                chars.append('E')
            elif char == '#':
                chars.append('#')
            elif char == '.':
                chars.append('.')
    pq  = [(0,0,start[0],start[1])]
    visited = set()
    while len(pq) > 0:
        score,direction,x,y = heapq.heappop(pq)
        if (x,y) == end:
            output = score
            break
        if (direction,x,y) in visited:
            continue
        visited.add((direction,x,y))
        dx,dy = dirs[direction]
        nx,ny = x+dx,y+dy
        if  maze[nx][ny] != '#':
            heapq.heappush(pq,(score+1,direction,nx,ny))
        for d in sideDirs[direction]:
            heapq.heappush(pq,(score+1000,d,x,y))
        
     


print(output)
print((time.time()-START_TIME) * 1000, "ms")
