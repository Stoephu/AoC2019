# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 08:15:08 2020

@author: Stoephu
"""

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
import math

start = time.default_timer()
strings = [string for string in open("data.txt")]

#asteroid_coordinates index 295
observation_station = (31, 20)

asteroid_coordinates = []

for y, string in enumerate(strings):
    for x, c in enumerate(string):
        if(c == "#"):
           asteroid_coordinates.append((x,y))
        elif c == "X":
            observation_station = (x,y)
            #asteroid_coordinates.append((x,-y))

"""
for y in range(len(strings)):
    string = strings[y]
"""

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


#part 2
"""
rel_coords = np.array([(coord[0]-observation_station[0],coord[1]-observation_station[1]) for coord in asteroid_coordinates])
polarcoordinates = [(coord[0]**2+coord[1]**2,math.atan2(coord[1],coord[0])) for coord in rel_coords]
polarcoordinates = sorted(polarcoordinates,key = lambda x : x[0])
polarcoordinates = sorted(polarcoordinates,key = lambda x : ((x[1])-1.5*math.pi)%(2*math.pi))
polar = polarcoordinates.copy()
sortedlist = []
i = 0
while polarcoordinates:
    if not sortedlist:
        sortedlist.append(polarcoordinates.pop(i%len(polarcoordinates)))
    elif polarcoordinates[i%len(polarcoordinates)][1] != sortedlist[-1][1]:
        sortedlist.append(polarcoordinates.pop(i%len(polarcoordinates)))
    else:
        i += 1
print("observation station at",observation_station)
for i in range(len(sortedlist)):
    r2, phi = sortedlist[i]
    y,x = math.sqrt(r2)*math.sin(phi)+observation_station[1],math.sqrt(r2)*math.cos(phi)+observation_station[0]
    print( i+1,"th asteroid at (",x,",",y,")", sortedlist[i] )
r2,phi = sortedlist[199]
y,x = math.sqrt(r2)*math.sin(phi)+observation_station[1],math.sqrt(r2)*math.cos(phi)+observation_station[0]
print(y,x)
print((x)*100 + y)

print(time.default_timer()-start)
