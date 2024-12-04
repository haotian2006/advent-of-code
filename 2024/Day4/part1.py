import math
import numpy as np
import pandas as pd
import collections 
import re 

output = 0

dir = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
l2 = 'MAS'
with open('input.txt') as f:
    data = [list(l.strip()) for l in f]
    checked = {}
    def check(x,y,dx,dy):
        for s in l2:
            x += dx
            y += dy
            if x < 0 or y < 0:
                return False
            if data[x][y] != s:
                return False
        return True

    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == 'X':
                for i in dir:
                    try:
                        if check(x,y,i[0],i[1]):
                            output += 1
                    except:
                        pass
print(output)


        

