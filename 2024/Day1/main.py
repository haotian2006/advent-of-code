import math
import numpy as np
import pandas as pd
import collections 
import re 

total = 0
list1 = []
list2 = []
with open('input.txt') as f:
    data = f.read().splitlines()
    for i in range(len(data)):
        data[i] = re.split('   ', data[i])
        list1.append(data[i][0])
        list2.append(data[i][1])
data = collections.Counter(list2)
for i in list1:
    total += (data[i] or 0)*int(i)

print(total)

