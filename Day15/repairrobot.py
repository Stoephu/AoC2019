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
start_time = time.default_timer()
# 0 is wall, 1 is path, 2 is goal
ccoord = (0,0)
coords_visited = {ccoord:1}
robot = intcode.computer()
robot.load_program_txt("data.txt")
path = deque()
direction = {}
robot.start_program([])

def set_direction(coord):
    global direction
    direction[1] = tuple(np.array((coord))+np.array([1,0]))
    direction[2] = tuple(np.array((coord))+np.array([-1,0]))
    direction[3] = tuple(np.array((coord))+np.array([0,-1]))
    direction[4] = tuple(np.array((coord))+np.array([0,1]))

set_direction(ccoord)
hidden = set(direction.values())
nmove = 0
i = 0

all_nodes = {}
start = bfs.node(ccoord)
all_nodes[ccoord] = start

    
while hidden and i < 10000:
    i+= 1
    backtracking = False
    for command in direction:
            if not direction[command] in coords_visited:
                nmove = command
                break
            
            else:
                nmove = 0
    
    if not nmove:
        backtracking = True
        lastcommand = path.pop()
        nmove = lastcommand+1 if (lastcommand)%2 else lastcommand-1
    
    not_wall = robot.continue_program([nmove]).get_output()[0]
    
    if debug:print("move",nmove,not_wall)
    
    coords_visited[direction[nmove]] = not_wall
    
    if direction[nmove] in hidden: hidden.remove(direction[nmove])
    
    if not_wall:
        if debug: print("direction before:",direction)
        
        node = None
        if direction[nmove] in all_nodes:
            node = all_nodes[direction[nmove]]
        else:
            node = bfs.node(direction[nmove])
            all_nodes[direction[nmove]] = node
        set_direction(direction[nmove])
        
        for coord in direction.values():
            if coord in all_nodes:
                neighbour = all_nodes[coord]
                node.add_neighbour(neighbour)
                neighbour.add_neighbour(node)
            
                
        
        if debug: print("direction after:",direction)
        
        if not backtracking: path.append(nmove)
        if debug: print("path",path)
        
        for command in direction:
            if not direction[command] in coords_visited:
                hidden.add(direction[command])
        
        if debug: print("hidden after:",hidden)

end_coord = None
for key, value in coords_visited.items():
    if value == 2:
        end_coord = key
        break
    
end = all_nodes[end_coord]
print("bfs")
length = bfs.get_shortest_path(start,end)
print(length)

all_times = bfs.get_time_to_all(end)
max_time = 0
for length in all_times.values():
    if max_time < length: max_time = length
print("minutes to fill ship",max_time)

m = 0
for tup in coords_visited.keys():
    for i in tup:
        if abs(i)>m:
            m = abs(i)
m += 1
im = np.zeros((2*m,2*m))
for tup in coords_visited.keys():
    x,y = tup
    im[x+m,y+m] = coords_visited[tup]
plt.figure()
plt.imshow(im)


print(time.default_timer()-start_time)
