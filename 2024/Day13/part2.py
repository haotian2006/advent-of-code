import math
import numpy as np
import pandas as pd
import collections 
import re 
import time
import sympy as sp
from sympy.abc import x, y
#A 3
#B 1

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

p = re.compile(r'(\d+)\D+(\d+)')
def inBounds(l:list,x,y):
    return x >= 0 and x < len(l) and y >= 0 and y < len(l[0])

output = 0
START_TIME = time.time()
with open('input.txt') as f:
    rules = []
    lines = f.readlines()
    d = None
    for i, line in enumerate(lines):
        if i%4 == 0:
            if d:
                rules.append(d)
            d = []
            d.append(p.findall(line))
            continue
        if line == '\n':
            continue
        d.append(p.findall(line))
    rules.append(d)
    
    def findShortest(data):
        bAX,bAY = data[0][0]
        bBX,bBY = data[1][0]
        pX,pY = data[2][0]
        bAX = int(bAX)
        bAY = int(bAY)
        bBX = int(bBX)
        bBY = int(bBY)
        pX = int(pX)+10000000000000
        pY = int(pY)+10000000000000
        # bAX*x + bBX*y = pX
        # bAY*x + bBY*y = pY
        #bAX(pY/bAY - bBY*y/bAY) + bBX*y = pX
        
        eq1 = sp.Eq(bAX*x+bBX*y,pX)
        eq2 = sp.Eq(bAY*x+bBY*y,pY)
        
        sol = sp.solve((eq1,eq2), (x, y))
        xx,yy = sol[x],sol[y]
        if int(xx) == xx and int(yy) == yy:
            return int(xx)*3+int(yy)
        return 0
         
    for rule in rules:
        output += findShortest(rule)
        
       
        
   
print(output)
print((time.time()-START_TIME) * 1000, "ms")
