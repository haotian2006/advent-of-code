import math
import numpy as np
import pandas as pd
import collections 
import re  

output = 0

with open('input.txt') as f:
    data = f.read()
    match = re.finditer(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)", data)
    f = True
    for m in match:
        x = m.group(0)
        if x == "do()":
           f = True
        elif x == "don't()":
            f = False
        elif f:
            g = m.groups()
            output += int(g[0]) * int(g[1])

print(output)

