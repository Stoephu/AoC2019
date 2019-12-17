# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product, permutations
import matplotlib.pyplot as plt 

start = time.default_timer()
#part1
import intcode
intersection_value = 35*5
preter = intcode.preter()
strings = [string for string in open("data.txt")]
program = [int(string) for string in strings[0].split(",")]
preter.load_program(program)
program_output = preter.start_program()
width = program_output.index(10)+1
scaffold_map = np.zeros((width, len(program_output)//width))

for i, tile in enumerate(program_output[:-1]):
    #print((i+1)%10, tile)
    scaffold_map[(i) % width,(i)//width] = tile
plt.imshow(scaffold_map)
intersections = set()
for coord in product(range(scaffold_map.shape[0]-2),range(scaffold_map.shape[1]-2)):
    sumt = scaffold_map[coord[0]+1, coord[1]+1] + scaffold_map[coord[0]+1, coord[1]+2] + scaffold_map[coord[0]+2, coord[1]+1] + scaffold_map[coord[0]+1, coord[1]] + scaffold_map[coord[0], coord[1]+1]
    if int(sumt) == intersection_value:
        intersections.add((coord[0]+1,coord[1]+1))
sumt = 0
for coord in intersections:
    sumt += coord[0]*coord[1]
print(sumt)
print(time.default_timer()-start)
