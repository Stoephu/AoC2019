# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product
import matplotlib.pyplot as plt 
from fractions import Fraction

start = time.default_timer()
strings = [string for string in open("data.txt")]
digits = [int(char) for _ in range(10000) for char in strings[0] ]
skip = int(strings[0][:7])
max_input = len(digits)
base_pattern = [0,1,0,-1]
"""
inputs = digits.copy()

i = 0
while i < 100:
    i += 1
    output = []
    for _ in digits:
        total_sum = 0
        for j,digit in enumerate(inputs):
            total_sum += digit*base_pattern[int(np.floor((j+1)/(len(output)+1))%len(base_pattern))]
            #print(len(output),int(np.floor((j+1)/(len(output)+1))), base_pattern[int(np.floor((j+1)/(len(output)+1))%len(base_pattern))],digit)
        #print(total_sum)
        output.append(np.abs(total_sum)%10)
        
    print("Phase",i)
    inputs = output.copy()
result = ""
for digit in inputs:
    result += str(digit)
print(result)
"""

phase = 0
while phase <100:
    phase += 1
    current_total = 0
    for i in reversed(range(skip,max_input)):
        current_total += digits[i]
        digits[i] = current_total%10
    print(phase)
print(digits[skip:skip+8])
print(time.default_timer()-start)