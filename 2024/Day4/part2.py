import math
import numpy as np
import pandas as pd
import collections 
import re 

output = 0

dir = [(1,1),(1,-1),(-1,1),(-1,-1)]

with open('input.txt') as f:
    data = [list(l.strip()) for l in f]
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == 'A':
                c = 0
                for i in dir:
                    try:
                        nx = x + i[0]
                        ny = y + i[1]
                        if nx < 0 or ny < 0:
                            continue
                        ox = x - i[0]
                        oy = y - i[1]
                        if ox < 0 or oy < 0:
                            continue
                        if data[nx][ny] == 'M' and data[ox][oy] == 'S':
                            c += 1
                    except:
                        pass
                if c == 2:
                    output += 1

print(output)


        

