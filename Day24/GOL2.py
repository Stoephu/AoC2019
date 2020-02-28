# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product, permutations
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

start = time.default_timer()
rows = [row.strip() for row in open("data.txt")]
#translate to boolean
grid = []
for row in rows:
    boo = []
    for c in row:
        boo.append(c == "#")
    grid.append(boo)
levels = {0:grid}


def get_cell(level,i,j):
    now = levels[level]
    if i >= 0 and i < 5:
        if j >= 0 and j < 5:
            return now[i][j]
        else:
            return 0
    else:
        return 0

def get_future(level):
    future = []
    for i in range(5):
        row = []
        for j in range(5):
            neighbors = 0
            neighbors += get_cell(level,i-1,j)
            neighbors += get_cell(level,i+1,j)
            neighbors += get_cell(level,i,j-1)
            neighbors += get_cell(level,i,j+1)
            row.append(neighbors == 1 or (neighbors == 2 and not now[i][j]))
        future.append(row)
    return future


print(time.default_timer()-start)
