# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product, permutations
from itertools import groupby
import matplotlib.pyplot as plt 
from collections import deque

start = time.default_timer()
#part1
inputs = [string for string in open("data.txt")]
strings = [string.strip() for string in inputs]
dungeon = np.empty((len(strings),len(strings[0])),dtype="int")
for y in range(dungeon.shape[0]):
    for x in range(dungeon.shape[1]):
        dungeon[y,x] = ord(strings[y][x])

#setup
diffUpper = ord("a")-ord("A")
player = 64
non_keys = set(["@","#","."])
keys = set()
for string in strings:
    for char in string:
        if (not char in non_keys) and char.islower():
            keys.add(ord(char))
rand = deque()
time_needed = {}
index = np.where(dungeon==player)
pcoord = (index[0][0],index[1][0],())
rand.append(pcoord)
time_needed[pcoord] = 0
shape = dungeon.shape
#coord  = (y,x,keys_found)
shortesttime = shape[0]*shape[1]

def get_unchecked_neighbours(coord):
    global shortesttime
    y,x,oldkeys = coord
    neighbours = []
    x1 = (y,x+1)
    x2 = (y,x-1)
    x3 = (y+1,x)
    x4 = (y-1,x)
    xis = [x1,x2,x3,x4]
    for xi in xis:
        ntile = dungeon[xi[0],xi[1]]
        if not ntile == ord("#"):
#        if xi[0] >= 0 and xi[0]< shape[0] and xi[1]>=0 and xi[1]< shape[1]:
            new = oldkeys
            if (chr(ntile).isupper() and not ntile+diffUpper in new):
               pass
            else:
                if chr(ntile).islower():
                    if not ntile in oldkeys:
                        new = list(oldkeys)
                        new.append(ntile)
                        new = tuple(sorted(new))
                ncoord = (xi[0],xi[1],new)    
                if ncoord in time_needed and time_needed[coord] + 1 > time_needed[ncoord]:
                    pass
                else:
                    neighbours.append(ncoord)
                    time_needed[ncoord] = time_needed[coord] + 1
                    if len(new) == len(keys) and shortesttime > time_needed[ncoord]:
                        shortesttime = time_needed[ncoord]
    return neighbours

current = pcoord
i = 0
while rand:
    i += 1
    current = rand.popleft()
    if not(i%50000):
        print(len(current[2]))
        print(current)
    neigh = get_unchecked_neighbours(current)
    rand.extend(neigh)
print(shortesttime)
"""
plt.imshow(dungeon)
plt.show()
print(time.default_timer()-start)

import matplotlib.animation as animation

"""