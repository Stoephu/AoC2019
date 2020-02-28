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

start = time.default_timer()
#part1
inputs = [string for string in open("test.txt")]
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
        if not char in non_keys and char.islower():
            keys.add(ord(char))
rand = []
checked = set()
time_needed = {}
index = np.where(dungeon==player)
pcoord = (index[0][0],index[1][0],())
rand.append(pcoord)
time_needed[pcoord] = 0
shape = dungeon.shape
#coord  = (y,x,keys_found)

def get_unchecked_neighbours(coord):
    y,x,old = coord
    tile = dungeon[y,x]
    neighbours = []
    if chr(tile).islower() and not tile in coord[2]:
        new = list(coord[2])
        new.append(tile)
        neighbours.append((y,x,tuple(new)))
    else:
        x1 = (y,x+1,old)
        x2 = (y,x-1,old)
        x3 = (y+1,x,old)
        x4 = (y-1,x,old)
        xis = [x1,x2,x3,x4]
        for xi in xis:
            if not xi in checked:
                if xi[0] > 0 and xi[0]< shape[0] and xi[1]>0 and xi[1]< shape[1]:
                    if chr(dungeon[xi[0],xi[1]]).isupper() and not dungeon[xi[0],xi[1]]+diffUpper in old:
                        pass
                    else:
                        neighbours.append(xi)
    for neigh in neighbours:
        time_needed[neigh] = time_needed[coord] + 1
        checked.add(neigh)
    return neighbours

current = pcoord

while len(keys) != len(current[2]) and rand:
    current = rand.pop(0)
    checked.add(current)
    neigh = get_unchecked_neighbours(current)
    rand.extend(neigh)
print(time_needed[current])
"""
plt.imshow(dungeon)
plt.show()
"""
print(time.default_timer()-start)

import matplotlib.animation as animation

