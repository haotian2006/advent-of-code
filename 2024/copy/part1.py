import math
import numpy as np
import pandas as pd
import collections 
import re 
import time
import sympy as sp
from sympy.abc import x, y

def printMap(m):
    for i in m:
        print(''.join(i))

def inBounds(l:list,x,y):
    return x >= 0 and x < len(l) and y >= 0 and y < len(l[0])

output = 0
START_TIME = time.time()
with open('input.txt') as f:

print(output)
print((time.time()-START_TIME) * 1000, "ms")
