import math
import numpy as np
import pandas as pd
import collections 
import re 

output = 0

with open('input.txt') as f:
    data = f.read()
    match = re.findall(r'mul\((\d+),(\d+)\)', data)
    for m in match:
        output += int(m[0]) * int(m[1])
print(output)
 
