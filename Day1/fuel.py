# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
start = time.default_timer()
data = np.array([float(mass) for mass in open("data.txt")])
def calc(data):
    extrafuel = np.floor(data /3)-2
    if extrafuel <=0:
        return 0
    else:
        return extrafuel + calc(extrafuel)
data = np.floor(data /3)-2
result = np.sum(data)
result = np.sum([calc(fuel) for fuel in data]) + result
print(result)
print(time.default_timer()-start)