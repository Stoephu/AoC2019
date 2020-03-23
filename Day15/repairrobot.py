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
import matplotlib.animation as animation 
import sys
from collections import deque
sys.path.append("../intcode")
sys.path.append("../algorithms")
import intcode
import bfs

debug = False
start = time.default_timer()
# 0 is wall, 1 is path, 2 is goal
ccoord = (0,0)
coords_visited = {ccoord:1}
robot = intcode.computer()
robot.load_program_txt()
path = deque()
direction = {}
robot.start_program([])

def set_direction(coord):
    global direction
    direction[1] = tuple(np.array((coord))+np.array([1,0]))
    direction[2] = tuple(np.array((coord))+np.array([0,1]))
    direction[3] = tuple(np.array((coord))+np.array([-1,0]))
    direction[4] = tuple(np.array((coord))+np.array([0,-1]))

set_direction(ccoord)
hidden = set(direction.values())
nmove = 0
while hidden and len(coords_visited)<1000:
    for command in direction:
            if not direction[command] in coords_visited:
                nmove = command
                break
            else:
                nmove = 0
    if not nmove:
        lastcommand = path.pop()
        nmove = (lastcommand+2)%4 if (lastcommand+2)%4 else 4
    not_wall = robot.continue_program([nmove]).get_output()[0]
    if debug:print(nmove,not_wall)
    #remove bug backtracking not in hidden
    coords_visited[direction[nmove]] = not_wall
    hidden.remove(direction[nmove])
    if not_wall:
        if debug: print("direction before:",direction)
        set_direction(direction[nmove])
        if debug: print("direction after:",direction)
        path.append(nmove)
        for command in direction:
            if not direction[command] in coords_visited:
                hidden.add(direction[command])
    x = 0
    
m = 0
for tup in coords_visited.keys():
    for i in tup:
        if abs(i)>m:
            m = abs(i)
im = np.zeros((2*m,2*m))
for tup in coords_visited.keys():
    x,y = tup
    im[x+m,y+m] = coords_visited[tup]
plt.imshow(im)


print(time.default_timer()-start)
