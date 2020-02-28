# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:56:37 2020

@author: Stoephu
"""

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
doors = set()
shape = dungeon.shape

for string in strings:
    for char in string:
        if (not char in non_keys) and char.islower():
            keys.add(ord(char))
            if (not char in non_keys) and char.isupper():
                doors.add(ord(char))


class tile:
    
    def __init__(self,tileValue, coord):
        self.value = tileValue
        self.neighbours = set()
        self.coord = coord
        self.shortest_to_important = {}
        
    def addNeighbour(self,neigh):
        self.neighbours.add(neigh)
    
    def add_important(self,tile,distance):
        self.shortest_to_important[tile] = distance
        
rand = deque()
time_needed = {}
index = np.where(dungeon==player)
pcoord = (index[0][0],index[1][0])
playertile = tile(ord("@"),pcoord)
rand.append(playertile)
time_needed[playertile] = 0
checked = set()
checked.add(pcoord)
alltiles = {}
alldoors = set()
allkeys = set()

def get_unchecked_neighbours(current):
    y,x = current.coord
    tilevalue = dungeon[y,x]
    neighbours = []
    x1 = (y,x+1)
    x2 = (y,x-1)
    x3 = (y+1,x)
    x4 = (y-1,x)
    xis = [x1,x2,x3,x4]
    for xi in xis:
        if not xi in checked:
            if xi[0] >= 0 and xi[0]< shape[0] and xi[1]>=0 and xi[1]< shape[1]:
                if  dungeon[xi[0],xi[1]] == ord("#"):
                    pass
                else:
                    ntile = tile(tilevalue,xi)
                    if chr(tilevalue).isupper:
                        alldoors.add(ntile)
                    elif chr(tilevalue).isupper:
                        allkeys.add(ntile)
                    ntile.addNeighbour(current)
                    current.addNeighbour(ntile)
                    neighbours.append(ntile)
                    alltiles[xi] = ntile
                    time_needed[ntile] = time_needed[current] + 1
        else:
            if xi in alltiles:
                current.addNeighbour(alltiles[xi])
    for neigh in neighbours:
        checked.add(ntile.coord)
    return neighbours
#convert map to graph
def get_unchecked_neighbours_graph(node):
    neigh = node.neighbours
    a = []
    for ne in neigh:
        if not ne in checked:
            a.append(ne)
    for ne in a:
        checked.add(ne)
    return a


i = 0
while rand:
    current = rand.popleft()
    neigh = get_unchecked_neighbours(current)
    rand.extend(neigh)
    if not i%20000:
        print(len(rand))
        #print(neigh)
    i+= 1

#reduce nodes only important neighbours
print("reduce!")
all_important = alldoors.union(allkeys)
all_important.add(playertile)

for node in all_important:
    rand = deque()
    checked = set()
    time_needed = {}
    rand.append(node)
    checked.add(node)
    i = 0
    while rand:
        i+= 1
        current = rand.popleft()
        neigh = get_unchecked_neighbours_graph(current)
        for ne in neigh:
            if ne in all_important:
                neigh.remove(ne)
                current.add_important(ne,i)
                ne.add_important(current,i)
        rand.extend(neigh)
        if not i%20000:
            print(len(rand))
            #print(neigh)
print(time.default_timer()-start)