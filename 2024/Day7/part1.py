import math
import numpy as np
import pandas as pd
import collections 
import re 
from itertools import product
import time

output = 0

def run(eq,vals):
    ops = ["*","+"]
    op = product(ops,repeat=len(vals)-1)
    for o in op:
        s = vals[0]
        for i in range(len(o)):
            if o[i] == "+":
                s += vals[i+1]
            else:
                s *= vals[i+1]

        if s == eq:
            return True
sTime = time.time()
with open('input.txt') as f:
    line = f.readline()
    while line:
        line = line.strip().split(':')
        eq,equation = int(line[0]),line[1].strip()
        vals = [int(x) for x in equation.split(' ')]
       
        if run(eq,vals):
            output += eq
        line = f.readline()
print(output)

