# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:52:44 2020

@author: Stoephu
"""

import timeit as time
import numpy as np
from itertools import product, permutations
from itertools import groupby
import matplotlib.pyplot as plt 
import sys
sys.path.append("../intcode")

start = time.default_timer()
#part1
strings = [string for string in open("data.txt")]
x_moons = np.zeros((len(strings),3))
v = np.zeros_like(x_moons)
for i, string in enumerate(strings):
    tmp = string.replace("<x=","")
    tmp = tmp.replace(">","")
    tmp = tmp.replace("y=","")
    tmp = tmp.replace("z=","")
    tmps = tmp.split(",")
    print(tmps)
    x_moons[i] = np.array([int(tmps[0]),int(tmps[1]),int(tmps[2])])

def grav(x):
    t = np.zeros_like(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):
            t[i] += np.sign(x[j]-x[i])
    return t
x = x_moons.copy()
for i in range(10):
    a = grav(x)
    v += a
    x += v
total_energy = np.sum(np.abs(x))*np.sum(np.abs(v))
print(time.default_timer()-start)
