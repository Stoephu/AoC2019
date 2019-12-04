# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product
import matplotlib.pyplot as plt 

start = time.default_timer()
strings = [string for string in open("data.txt")]
wire1Instruc = strings[0].split(",")
wire2Instruc = strings[1].split(",")

#part 1
wire_1_coords = set()
wire1selfcross = set()
wire_2_coords = set()
wire2selfcross = set()
x = y = 0

for instruc in wire1Instruc:
    if instruc[0]=="R":
        for coord in product([y],x+np.array(range(int(instruc.replace("R",""))+1))):
            if coord in wire_1_coords:
                wire1selfcross.add(coord)
            else:
                wire_1_coords.add(coord)
        x += int(instruc.replace("R",""))
    elif instruc[0]=="L":
        for coord in product([y],x-np.array(range(int(instruc.replace("L",""))+1))):
            if coord in wire_1_coords:
                wire1selfcross.add(coord)
            else:
                wire_1_coords.add(coord)
        x -= int(instruc.replace("L",""))
    elif instruc[0]=="U":
        for coord in product(y+np.array(range(int(instruc.replace("U",""))+1)),[x]):
            if coord in wire_1_coords:
                wire1selfcross.add(coord)
            else:
                wire_1_coords.add(coord)
        y += int(instruc.replace("U",""))
    elif instruc[0]=="D":
        for coord in product(y-np.array(range(int(instruc.replace("D",""))+1)),[x]):
            if coord in wire_1_coords:
                wire1selfcross.add(coord)
            else:
                wire_1_coords.add(coord)
        y -= int(instruc.replace("D",""))
    else:
        print("ERROR",instruc)
        
x = y = 0

for instruc in wire2Instruc:
    if instruc[0]=="R":
        for coord in product([y],x+np.array(range(int(instruc.replace("R",""))+1))):
            if coord in wire_2_coords:
                wire2selfcross.add(coord)
            else:
                wire_2_coords.add(coord)
        x += int(instruc.replace("R",""))
    elif instruc[0]=="L":
        for coord in product([y],x-np.array(range(int(instruc.replace("L",""))+1))):
            if coord in wire_2_coords:
                wire2selfcross.add(coord)
            else:
                wire_2_coords.add(coord)
        x -= int(instruc.replace("L",""))
    elif instruc[0]=="U":
        for coord in product(y+np.array(range(int(instruc.replace("U",""))+1)),[x]):
            if coord in wire_2_coords:
                wire2selfcross.add(coord)
            else:
                wire_2_coords.add(coord)
        y += int(instruc.replace("U",""))
    elif instruc[0]=="D":
        for coord in product(y-np.array(range(int(instruc.replace("D",""))+1)),[x]):
            if coord in wire_2_coords:
                wire2selfcross.add(coord)
            else:
                wire_2_coords.add(coord)
        y -= int(instruc.replace("D",""))
    else:
        print("ERROR",instruc)
        
hits = wire_1_coords.intersection(wire_2_coords)
hits.remove((0,0))

def manhat(coord):
    return np.sum(np.abs(coord))

print(hits)
smallest = min(hits,key=manhat)
print(smallest,manhat(smallest))

#part 2

x = y = 0
delay = 0
cableTime = {}

def step():
    global delay 
    delay += 1
    coord = (y,x)
    if coord in cableTime:
        """
        if delay > cableTime[coord]:
            delay = cableTime[coord]
        """
        pass
    else:
        cableTime[coord] = delay

for instruc in wire1Instruc:
    if instruc[0]=="R":
        for _ in range(int(instruc.replace("R",""))):
            x += 1
            step()
            
    elif instruc[0]=="L":
        for _ in range(int(instruc.replace("L",""))):
            x -= 1
            step()
            
    elif instruc[0]=="U":
        for _ in range(int(instruc.replace("U",""))):
            y += 1
            step()
            
    elif instruc[0]=="D":
        for _ in range(int(instruc.replace("D",""))):
            y -= 1
            step()


cable_1_delays = cableTime.copy()
x = y = 0
delay = 0
cableTime = {}


for instruc in wire2Instruc:
    if instruc[0]=="R":
        for _ in range(int(instruc.replace("R",""))):
            x += 1
            step()
            
    elif instruc[0]=="L":
        for _ in range(int(instruc.replace("L",""))):
            x -= 1
            step()
            
    elif instruc[0]=="U":
        for _ in range(int(instruc.replace("U",""))):
            y += 1
            step()
            
    elif instruc[0]=="D":
        for _ in range(int(instruc.replace("D",""))):
            y -= 1
            step()

        
cable_2_delays = cableTime
np.savetxt("cablepos.txt",list(cable_1_delays.values()),fmt = "%i")
signaltime = {}
for coord in hits:
    signaltime[coord] = cable_1_delays[coord]+cable_2_delays[coord]

mincoord = min(signaltime, key=signaltime.get)
print(mincoord, signaltime[mincoord])

print(time.default_timer()-start)
