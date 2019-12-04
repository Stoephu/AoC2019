# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product
import matplotlib.pyplot as plt 
import math

start = time.default_timer()
min_num = 168630
max_num = 718098

#generate all numbers
numbers =  range(min_num,max_num+1)

def valid(number):
    digits = [int(number/10**i)%10 for i in range(6)]
    has_double = False
    for i in range(len(digits)-1):
        if(digits[i]<digits[i+1]):
            return False
        if digits[i]==digits[i+1]:
            has_double = True
    return has_double

#count valid combinations
"""
#part1
number_of_valid = 0
for i,number in enumerate(numbers):
    if not i % 1000: print(i)
    if(valid(number)):
        number_of_valid += 1
print(number_of_valid)
"""

def strict_valid(number):
    digits = [int(number/10**i)%10 for i in range(6)]
    has_double = False
    for i in range(len(digits)-1):
        if(digits[i]<digits[i+1]):
            return False
    current_number = -1
    number_of_sequential = 0
    for i in digits:
        if i == current_number:
            number_of_sequential += 1
        else:
            if(number_of_sequential == 2):
                has_double = True
                break
            else:
                current_number = i
                number_of_sequential = 1
    if number_of_sequential == 2:
        has_double = True
    return has_double

#part 2

number_of_valid = 0
for i,number in enumerate(numbers):
    if not i % 10000: print(i)
    if(strict_valid(number)):
        number_of_valid += 1
        
print(number_of_valid)
print(time.default_timer()-start)
plt.show()