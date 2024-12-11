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
with open('input.txt') as f:
    nums = [int(x) for x in f.read().split(' ')] 

    cache = {}
    def checkNum(num,tries):
        if tries == 0:
            return 1
        if (num,tries) in cache:
            return cache[(num,tries)]
        if num == 0:
            return checkNum(1,tries-1) 
        if len(str(num)) % 2 == 0:
            n = str(num)
            v = checkNum(int(n[:len(n)//2]),tries-1) + checkNum(int(n[len(n)//2:]),tries-1)
            cache[(num,tries)] = v
            return v
        v = checkNum(num * 2024,tries-1)
        cache[(num,tries)] = v
        return v
            
    for i in nums:
        output += checkNum(i,75)
print(output)
print((time.time()-START_TIME) * 1000, "ms")
