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

asteroid_coordinates

asteroid_coordinates.remove(observation_station)

rel_asteroid_coordinates = set([(coord[0]-observation_station[0],coord[1]-observation_station[1]) for coord in asteroid_coordinates])
rel_slope = {}

def get_slope(coord):
    if coord[1] != 0:
        return Fraction(coord[0],coord[1])
    else:
        return np.sign(coord[0])
    
def man(coord):
    return np.abs(coord[0])+np.abs(coord[1])

def get_visible(coords):
    visible = {}
    for coord in coords:
        slope = get_slope(coord)
        if slope in visible:
            if man(visible[slope]) > man(coord):
                visible[slope] = coord
        else:
            visible[slope] = coord
    return visible


for coord in rel_asteroid_coordinates:
    rel_slope[coord] = get_slope(coord)

asteroids_hit = {}
i = 0
visible = get_visible(rel_asteroid_coordinates)
def increment_i(coord):
    global i
    i += 1
    asteroids_hit[i] = coord
    
while i <= 201:
    right_half = []
    middle = []
    left_half = []
    for slope in visible.keys():
        
            if slope>0:
                right_half.append(visible[slope])
            elif slope == 0:
                middle.append(visible[slope])
            else:
                left_half.append(visible[slope])
#    for coord in left_half:
#        print(coord)
#        print(np.arctan(coord[1]/coord[0]))            
    right_half.sort(key = lambda coord: np.arctan(coord[1]/coord[0]))
    left_half.sort(key = lambda coord: -np.arctan(coord[1]/coord[0]))
    for coord in middle:
        if coord[1]>0:
            increment_i(coord)
                
    for coord in right_half:
        increment_i(coord)
    
    for coord in middle:
        if coord[1]<0:
            increment_i(coord)
    
    for coord in left_half:
        increment_i(coord)
    rest = rel_asteroid_coordinates.difference(visible.values())
    visible = get_visible(rest)
asteroid_200 = asteroids_hit[200]
print((asteroid_200[0]+observation_station[0],asteroid_200[1]+observation_station[1]),(asteroid_200[0]+observation_station[0])*100+(asteroid_200[1]+observation_station[1]))
print(time.default_timer()-start)
