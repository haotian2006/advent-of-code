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
moveDirs = [[1,3],[0,2],[1,3],[0,2]]
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
    pq  = [(0,0,start[0],start[1],[],[],0)]
    visited = set()
    path = []
    max_score = 0
    while len(pq) > 0:
        score,direction,x,y,path,data,prev = heapq.heappop(pq)
        if (x,y) == end:
            max_score = score
            path = path + [end]
            data = data + [(score,direction,prev)]
            break
        if (direction,x,y) in visited:
            continue
        visited.add((direction,x,y))
        dx,dy = dirs[direction]
        nx,ny = x+dx,y+dy
        
        if inBounds(maze, nx, ny) and maze[nx][ny] != '#':
            heapq.heappush(pq,(score+1,direction,nx,ny,path + [(x, y)],data + [(score,direction,prev)],direction))
        for d in sideDirs[direction]:
            heapq.heappush(pq,(score+1000,d,x,y,path,data,direction))
    for i in path:
        maze[i[0]][i[1]] = 'O'
    posToData = {}
    for i in range(len(path)):
        posToData[path[i]] = data[i]
    mapClone = [list(i) for i in maze]
    cache = set()
    def branch(x,y,dir,score,path):
        dx,dy = dirs[dir]
        if (x, y, dir, score) in cache:
            return False, path
        if not inBounds(maze,x,y) or maze[x][y] == '#':
            return False,path
        if score > max_score:
            return False,path
        if maze[x][y] == 'O':
            sc,pDir,prevDir = posToData[(x,y)]
            pdx,pdy = dirs[prevDir]
            isS = (dx == pdx and dy == pdy) or (dx == -pdx and dy == -pdy)
            if pDir!=prevDir:
                sc += 1000
            if not isS:
                score +=1000
            if sc == score:
                return True,path
            else:
                return False,path
        newP = path + [(x,y)]
        nx,ny = x+dx,y+dy
        passed,p = branch(nx,ny,dir,score+1,newP)
        hasPass = 0
        if passed:
            hasPass+=1
            for i in p:
                mapClone[i[0]][i[1]] = 'O'
        # else:
        #     cache.add((nx,ny,dir))
        for d in sideDirs[dir]:
            dx,dy = dirs[d]
            nx,ny = x+dx,y+dy
            passed,p = branch(nx,ny,d,score+1001,newP)
            if passed:
                hasPass+=1
                for i in p:
                    mapClone[i[0]][i[1]] = 'O'
            # else:
            #     cache.add((nx,ny,d))
        if hasPass > 0:
            return True,newP
        cache.add((x, y, dir, score))
        return False,path
    for i in range(len(path)):
        r,c = path[i]
        sc,dir,prevDir = data[i]
        pdx,pdy = dirs[prevDir]
        if prevDir != dir:
            sc -= 1000
        for d in range(4):
            dx,dy = dirs[d]
            isS = (dx == pdx and dy == pdy) or (dx == -pdx and dy == -pdy)
            value = sc
            if not isS:
                value += 1000
            nr,nc = r+dx,c+dy
            
            branch(nr,nc,d,value+1,[])
    for i in mapClone:
        for j in i:
            if j == 'O':
                output += 1
    printMap(mapClone)
print(output)
print((time.time()-START_TIME) * 1000, "ms")
