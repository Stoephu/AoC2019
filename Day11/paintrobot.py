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
import sys
sys.path.append("../intcode")

start = time.default_timer()
#part1
import intcode
probot = intcode.computer()
probot.load_program_txt("data.txt")
coords_painted = {}
verbose = False
last_output = probot.start_program([1],verbose = verbose)
robot_pos = (0,0)
facing = (0,1)
i = 0 
while last_output[-1] != -1:
    i+=1
    coords_painted[robot_pos] = last_output[0]
    facing = (facing[1]*(-1 + 2*last_output[1]),facing[0]*(1 - 2*last_output[1]))
    robot_pos = (robot_pos[0]+facing[0],robot_pos[1]+facing[1])
    if robot_pos in coords_painted:
        last_output = probot.continue_program([coords_painted[robot_pos]],verbose = verbose)
    else:
        last_output = probot.continue_program([0],verbose = verbose)

"""
0 left
1,0 0,1
0,1 -1,0
-1,0 0,-1
0,-1 1,0
1 right 
1,0 0,-1
0,-1 -1,0
-1,0 0,1
0,1 1,0 
"""
print(time.default_timer()-start)
ar = np.zeros((100,100))
for tup in coords_painted:
    ar[tup[0]+50,tup[1]+50] = coords_painted[tup]
plt.imshow(ar)