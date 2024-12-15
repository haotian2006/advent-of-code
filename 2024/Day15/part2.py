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
def printMap(m):
    for i in m:
        print(''.join(i))
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
        c = []
        for i in line.strip():
            if i == '#':
                c.append('#')
                c.append('#')  
            elif i == 'O':
                c.append('[')
                c.append(']')
            elif i == '.':
                c.append('.')
                c.append('.')
            elif i == '@':  
                c.append('@')
                c.append('.')
        m.append(c)

    x,y = 0,0

    sX,sY = len(m[0]),len(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '@':
                x,y = j,i
                break
    
    def moveBoxesHorizontal(x,y,dx,dy):
        nx,ny = x+dx,y+dy
        icon = m[y][x]
        if m[y][x] == '#':
            return False
        if m[y][x] == '.':
            return True
        
        canMove = moveBoxesHorizontal(nx,ny,dx,dy)
        if canMove:
            m[y][x] = '.'
            m[ny][nx] = icon
            return True
        return False
    def moveBoxesVertical(x,y,dy,value,visited = None):
        rx = x
        lx = x
        ny = y+dy
        if value == ']':
            rx = x 
            lx = x-1
        elif value == '[':
            rx = x+1
            lx = x 
        if m[y][rx] == '#':
            return False
        if m[y][lx] == '#':
            return False
        if m[y][rx] == '.' and  m[y][lx] == '.':
            return True 
        
        toSend = visited or []
        toSend.append((lx,y))

        canMove = moveBoxesVertical(lx,ny,dy,m[ny][lx] ,toSend)
        if not canMove:
            return False
        canMove = moveBoxesVertical(rx,ny,dy,m[ny][rx] ,toSend)
        if not canMove:
            return False
        if visited == None:
            for i in range(len(toSend)-1,0,-1):
                ix,iy = toSend[i]
                n_y = iy+dy
                m[n_y][ix] = '[' 
                m[n_y][ix+1] = ']'
                if m[iy][ix] == '[':
                    m[iy][ix] = '.'
                if m[iy][ix+1] == ']':
                    m[iy][ix+1] = '.'
            m[y][lx] = '.'
            m[y][rx] = '.'
            m[ny][lx] = '['
            m[ny][rx] = ']'
        return True  
    def move(v):
        global x,y,m,output,dirs
        dx,dy = dirs[v]
        nx,ny = x+dx,y+dy
        if m[ny][nx] == '#':
            return
        if m[ny][nx] == '[' or m[ny][nx] == ']':
            moveable = False
            if v == '<' or v == '>':
                moveable = moveBoxesHorizontal(nx,ny,dx,dy)
            else:
                moveable = moveBoxesVertical(nx,ny,dy,m[ny][nx])
            if not moveable:
                return
        m[y][x] = '.'
        x,y = nx,ny
        m[ny][nx] = '@'
    for i in range(len(dir)):
        v = dir[i]
        move(v)
        s = ''
        # print(v)
        # printMap(m)
        # printMap(m)
    for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == '[':
                    output += 100*(i)+(j)
                     
 



print(output)
print((time.time()-START_TIME) * 1000, "ms")
