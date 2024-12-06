import math
import numpy as np
import pandas as pd
import collections 
import re 

output = 0

with open('input.txt') as f:
    lines = f.readline()
    back = {}
    front = {}
    while lines !='\n':
        x = lines.strip().split('|')
        if x[1] not in back:
            back[x[1]] = []
        if x[0] not in front:
            front[x[0]] = []
        back[x[1]].append(x[0])
        front[x[0]].append(x[1])
        lines = f.readline()
    l = [x.strip().split(',') for x in f.readlines()]

    def check(line):
        for i,v in enumerate(line):
            f = front.get(v, []) # v should be in front of it
            b = back.get(v, []) # b items should be behind
            
            for j in f:
                if j not in line:
                    continue
                pos = line.index(j)
                if pos < i:
                    return False
            for j in b:
                if j not in line:
                    continue
                pos = line.index(j)
                if pos > i:
                    return False
        return True
    
            
    for i in l: 
        if check(i):
            output += int(i[len(i)//2]) 
    # for k in showUp:
    #     if check(k):
    #         output += 1   
        

print(output)

