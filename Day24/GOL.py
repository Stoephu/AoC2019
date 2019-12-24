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


def get_cell(now,i,j):
    if i >= 0 and i < 5:
        if j >= 0 and j < 5:
            return now[i][j]
        else:
            return 0
    else:
        return 0

def get_future(now):
    future = []
    for i in range(5):
        row = []
        for j in range(5):
            neighbors = 0
            neighbors += get_cell(now,i-1,j)
            neighbors += get_cell(now,i+1,j)
            neighbors += get_cell(now,i,j-1)
            neighbors += get_cell(now,i,j+1)
            row.append(neighbors == 1 or (neighbors == 2 and not now[i][j]))
        future.append(row)
    return future

def get_biodeversitiy(grid):
    #grid[1].reverse()
    #grid[3].reverse()
    tot = ""
    arr = np.array(grid).flatten()
    for i, cell in enumerate(arr):
        tot += str(int(cell))
    return int("".join(reversed(tot)) ,2)

def to_tuple(li):
    return tuple(tuple(row) for row in li)


no_duplicate = True
bios = set()
bios.add(to_tuple(grid))
result_1 = 0

i = 0
images = []
#fig = plt.figure(2)

while no_duplicate and i < 1000:
    i += 1
    #images.append([plt.imshow(grid, animated = True)])
    future_grid = get_future(grid)
    signature = to_tuple(future_grid)
    if signature in bios:
        result_1 = get_biodeversitiy(future_grid)
        no_duplicate = False
    else:
        bios.add(signature)
    grid = future_grid.copy()


#ani = animation.ArtistAnimation(fig,images,interval = 500)
#ani.save('dynamic_images.gif',extra_args=['-vcodec', 'libx264'])
print(result_1)
print(time.default_timer()-start)
