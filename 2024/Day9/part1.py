import math
import numpy as np
import pandas as pd
import collections 
import re 
import time

output = 0

START_TIME = time.time()
with open('input.txt') as f:
    line = f.read()
    newStr = ''
    id = 0
    l = []
    freeSpaces = []
    for i in range(len(line)):
        char = line[i]
        if i%2 == 0:
            l.extend([id]*int(char))
            id+=1
        else:
            l.extend(['.']*int(char))
    _str = []
    newStr = l
    print("parsed")
    

    for z in range(len(newStr)):
        if newStr[z] != '.': 
            _str.append(int(newStr[z]))
            continue  
        for i in range(len(newStr)-1,0,-1):
            if i < z:
                break
            if newStr[i] != '.':
                _str.append(int(newStr[i]))
                newStr[i] = '.'
                break

    for i in range(len(_str)):
        output += _str[i] * (i)
        
print(output)
print("Part1",(time.time()-START_TIME) * 1000, "ms")


