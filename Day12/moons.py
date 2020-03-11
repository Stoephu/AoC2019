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
v_moons = np.zeros_like(x_moons)
v = v_moons.copy()
for i, string in enumerate(strings):
    tmp = string.replace("<x=","")
    tmp = tmp.replace(">","")
    tmp = tmp.replace("y=","")
    tmp = tmp.replace("z=","")
    tmps = tmp.split(",")
    print(tmps)
    x_moons[i] = np.array([int(tmps[0]),int(tmps[1]),int(tmps[2])])

total_energy = lambda x,v: np.sum(np.abs(x))*np.sum(np.abs(v))
def grav(x,v):
    for i in range(x.shape[0]):
        for j in range(x.shape[0]-i):
            m = np.sign(x[j+i]-x[i])
            v[i] += m 
            v[j+i] -= m
    return v
x = x_moons.copy()
for i in range(1000):
    v = grav(x,v)
    x += v
    if 0:#not (i+1)% 10::
        print(i+1,":")
        for j in range(x.shape[0]):
            print("os",x[j], v[j], total_energy(x[j],v[j]))
end_energy = lambda x,v:np.sum(np.abs(x),axis = 1)*np.sum(np.abs(v), axis = 1)

#part 2

init_x = x_moons.copy()[:,0]
init_v = v.copy()[:,0]
x = x_moons.copy()[:,0]
v = v_moons.copy()[:,0]
i = 0
while  not np.all(x[0] == init_x[0]) or not np.all(v[0] == init_v[0]) or i == 0:
    i+=1
    v = grav(x,v)

    x += v
    if not i%100000:
        print(i)

print(time.default_timer()-start)