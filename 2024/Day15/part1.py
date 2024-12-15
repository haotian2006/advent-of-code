import math
import numpy as np
import pandas as pd
import collections 
import re 
import time
import sympy as sp
from sympy.abc import x, y

def inBounds(l:list,x,y):
    return x >= 0 and x < len(l) and y >= 0 and y < len(l[0])

output = 0
START_TIME = time.time()
dirs = {
    '^': (0,-1),
    'v': (0,1),
    '<': (-1,0),
    '>': (1,0)
}
with open('input.txt') as f:
    m = []
    isMap = True
    dir = ''
    for line in f.readlines():
        if line[0] != '#':
           dir += line.strip()
           continue
        m.append(list(line.strip())) 

    x,y = 0,0

    sX,sY = len(m[0]),len(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '@':
                x,y = j,i
                break
            
    def moveBoxes(x,y,dx,dy):
        nx,ny = x+dx,y+dy
        if m[y][x] == '#':
            return False
        if m[y][x] == '.':
            return True
        
        canMove = moveBoxes(nx,ny,dx,dy)
        if canMove:
            m[y][x] = '.'
            m[ny][nx] = 'O'
            return True
        return False
        
    for i in dir:
        dx,dy = dirs[i]
        nx,ny = x+dx,y+dy
        if m[ny][nx] == '#':
            continue
        if m[ny][nx] == 'O':
            moveable = moveBoxes(nx,ny,dx,dy)
            if not moveable:
                continue
        m[y][x] = '.'
        x,y = nx,ny
        m[ny][nx] = '@'
    for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 'O':
                    output += 100*(i)+(j)
    for a in m:
        print(' '.join(a))


print(output)
print((time.time()-START_TIME) * 1000, "ms")
