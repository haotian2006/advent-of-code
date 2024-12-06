import math
import numpy as np
import pandas as pd
import collections 
import re 

output = 0
paths = [[-1,0] , [0,1], [1,0], [0,-1]]

with open('input.txt') as f:
    visited = {}
    map = [list(line.strip()) for line in f.readlines()]
    mapCopy = map.copy()
    x,y = 0,0
    dir = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                x,y = i,j
                break
    while True:
        dirL = paths[dir]
        nx = x + dirL[0]
        ny = y + dirL[1]
        if nx < 0 or nx >= len(map) or ny < 0 or ny >= len(map[0]):
            mapCopy[x][y] = 'Z'
            break
        if map[nx][ny] == '#':
            dir = (dir + 1) % 4
            continue
        mapCopy[x][y] = 'X'
        x,y = nx,ny 
        if not (f'{x},{y}' in visited):
            output += 1
            visited[f'{x},{y}'] = True

print(output) #+1 for some reason in the actual input not need to +1 for testcase

