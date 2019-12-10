# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product
import matplotlib.pyplot as plt 
from fractions import Fraction

start = time.default_timer()
strings = [string for string in open("data.txt")]

#asteroid_coordinates index 295
observation_station = (31, 20)

asteroid_coordinates = []

for y, string in enumerate(strings):
    for x, c in enumerate(string):
        if(c == "#"):
           asteroid_coordinates.append((x,y))


#part1
"""
asteroid_coordinates.sort()
line_of_sights_tuples = set()

for i, asteroid_1 in enumerate(asteroid_coordinates):
    for asteroid_2 in asteroid_coordinates[i:]:
        if not asteroid_1 == asteroid_2:
            line_of_sights_tuples.add((asteroid_1,asteroid_2))

slope = {}

for tup in line_of_sights_tuples:
    if tup[0][1] == tup[1][1]:
        slope[tup] = "inf"
    else:
        slope[tup] = Fraction(tup[1][0]-tup[0][0],tup[1][1]-tup[0][1])

line_of_sight_counts = []

for asteroid in asteroid_coordinates:
    all_slopes = set()
    for tup in slope.keys():
        x = 0
        if tup[1] == asteroid:
            x = 1
            all_slopes.add((slope[tup],x))
        elif tup[0] == asteroid:
            all_slopes.add((slope[tup],x))
    line_of_sight_counts.append(len(all_slopes))
print(max(line_of_sight_counts))
"""
#part 2

asteroid_coordinates.sort(key = lambda coord: coord[1])

asteroid_coordinates.remove(observation_station)

rel_asteroid_coordinates = [(coord[0]-observation_station[0],coord[1]-observation_station[1]) for coord in asteroid_coordinates]
rel_slope = {}
def get_slope(coord):
    if coord[1] != 0:
        return Fraction(coord[0],coord[1])
    else:
        return np.sign(coord[0])
    
for coord in rel_asteroid_coordinates:
    rel_slope[coord] = get_slope(coord)
    
def man(coord):
    return np.abs(coord[0])+np.abs(coord[1])

def get_all_visible(coords):
    visible = {}
    for coord in coords:
        slope = get_slope(coord)
        if slope in visible:
            if visible[slope] > coord:
                visible[slope] = coord
        else:
            visible[slope] = coord
    return visible


print(time.default_timer()-start)
