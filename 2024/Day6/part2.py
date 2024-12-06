import math
import numpy as np
import pandas as pd
import collections 
import re 

output = 0
paths = [[-1,0] , [0,1], [1,0], [0,-1]]

with open('input.txt') as f:
    map = [list(line.strip()) for line in f.readlines()]
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                x,y = i,j
                break
    def search(x,y,mapCopy):
        dir = 0
        count = 0
        visited = {}
        while True:
            dirL = paths[dir]
            nx = x + dirL[0]
            ny = y + dirL[1]
            if nx < 0 or nx >= len(mapCopy) or ny < 0 or ny >= len(mapCopy[0]):
                return False
            if mapCopy[nx][ny] == '#':
                dir = (dir + 1) % 4
                continue
            x,y = nx,ny 
            if not (f'{x},{y}' in visited):
                visited[f'{x},{y}'] = 1
            else:
                visited[f'{x},{y}'] += 1
                if visited[f'{x},{y}'] > 4:
                    return True
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                continue
            if map[i][j] == '#':
                continue
            map[i][j] = '#'
            if search(x,y,map):
                output += 1
            map[i][j] = '.'

# for line in mapCopy:
#     print(''.join(line))
print(output) 

