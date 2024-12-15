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
pat = re.compile('p=(.+),(.+) v=(.+),(.+)')
with open('input.txt') as f:
    sizeX = 101
    sizeY = 103
    hx = sizeX//2
    hy = sizeY//2
    
    robots = []
    for y, line in enumerate(f.readlines()):
        px, py, vx, vy = map(int, pat.match(line).groups())
        robots.append([px, py, vx, vy])
    mp = [[0 for i in range(sizeX)] for j in range(sizeY)]
    def parse(x):
        if x == 0:
            return '.'
        return '#'
    def simulate(robot:list):
        px, py, vx, vy = robot
        nx = px + vx
        ny = py + vy
        if nx < 0:
            nx += sizeX
        elif nx >= sizeX:
            nx -= sizeX
        if ny < 0:
            ny += sizeY
        elif ny >= sizeY:
            ny -= sizeY
        robot[0] = nx
        robot[1] = ny
        mp[py][px] -= 1
        mp[ny][nx] += 1
        
    for robot in robots:
        mp[robot[1]][robot[0]] += 1
    for i in range(100000):
        for robot in robots:
            simulate(robot)
        p = False
        for v in mp:
            str = ''.join(map(parse,v))
            if str.find('#'*8) != -1:
                p = True
                break
        if p:
            print('-----------',i)
            for row in mp:
                print(''.join(map(parse,row)) ) 
   # print(q1,q2,q3,q4)
print(output)
print((time.time()-START_TIME) * 1000, "ms")
 