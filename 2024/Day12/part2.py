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
dirCheck = [[2,3],[2,3],[0,1],[0,1]]
names = ['right','left','down','up']
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
    def checkSide(x,y,dir):
        char = map[x][y]
        dx,dy = dirs[dir] 
        if not inBounds(map,x+dx,y+dy) or map[x+dx][y+dy] != char:
            return True
        return False
    def check(x,y,dir,dir2,checked:dict):
        #dir is the direction we are checking
        #dir2 is the direction we are moving in
        dx,dy = dirs[dir2]
     
        if not checkSide(x,y,dir):
            return
        
        if not (x,y,dir) in checked:
            checked['count'] += 1
        checked[(x,y,dir)] = True

        char = map[x][y]
        while True:
            x += dx 
            y += dy
            checked[(x,y,dir)] = True
            if (not inBounds(map,x,y) )or map[x][y] != char:
                break
            if not checkSide(x,y,dir):
                break
           
    for g in groups:  
        area = len(g)-1
        p = 0
        d = {}
        d['count'] = 0
        for i in range(1,len(g)):
            x,y = g[i]
            for j in range(4):
                for z in dirCheck[j]:
                    check(x,y,j,z,d)
        output += area * d['count']
print(output) 
print((time.time()-START_TIME) * 1000, "ms")
 