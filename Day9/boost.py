# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:45:15 2019

@author: chris
"""
import timeit as time
import numpy as np
from itertools import product
import matplotlib.pyplot as plt 

start = time.default_timer()
import interpreter as interpreter

intcode = interpreter.preter()

output = intcode.start_program("data.txt",2,0)
print(output)
print(time.default_timer()-start)