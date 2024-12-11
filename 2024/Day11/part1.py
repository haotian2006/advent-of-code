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
    
    def blink(arr:list):
        new_arr = []
        for i in arr:
            if i ==0:
                new_arr.append(1)
            elif len(str(i)) % 2 == 0:
                i = str(i)
                new_arr.append(int(i[:len(i)//2]))
                new_arr.append(int(i[len(i)//2:]))    
            else:
                new_arr.append(i * 2024)
        return new_arr
    for i in range(25):
        nums = blink(nums)
    output = len(nums)
print(output)
print((time.time()-START_TIME) * 1000, "ms")
