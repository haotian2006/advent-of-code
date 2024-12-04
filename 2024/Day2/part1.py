import math
import numpy as np
import pandas as pd
import collections 
import re 

total = 0

with open('input.txt') as f:
    while True:
        line:str = f.readline()
        if not line:
            break
        d = line.strip().split(' ')
        last=0
        nums = {}
        for i,v in enumerate(d):
            if i == 0:
                last = v
                continue
            n = int(v) - int(last)
            nums[n] = True
            last = v
        keys = list(nums.keys())
        keys.sort()
        last = keys[0]
        safe = last != 0
        sign = keys[0] > 0 
        for i in range(0,len(keys)):
            if sign != (keys[i] > 0) or keys[i] == 0:
                safe = False 
                break
            if abs(keys[i]) >3 :

                safe = False
                break
            last = keys[i]
        if safe:
            total += 1

print(total)

