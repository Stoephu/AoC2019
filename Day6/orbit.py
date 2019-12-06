# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product
import matplotlib.pyplot as plt 
import math

start = time.default_timer()
orbits = [orbit.strip().split(")") for orbit in open("data.txt")]

class node():
    def __init__(self, name):
        self.parent = None
        self.moons = []
        self.distance_to_com = 0
        self.name = name
        pass
    
    def be_adopted(self, parent):
        self.parent = parent
        parent.adopt(self)
        
    def adopt(self, moon):
        self.moons.append(moon)
        pass
    
    def calc_distance(self):
        if self.parent:
            self.distance_to_com = self.parent.distance_to_com + 1
            #print(self.name, self.distance_to_com)
            return True
        return False
    
    def determine_number_orbits(self):
        number = 0
        for moon in self.moons:
            moon.calc_distance()
            number += moon.determine_number_orbits()
        return number + self.distance_to_com

all_of_em = {}
orphan_pair = []

com = node("COM")
all_of_em["COM"] = com
com.distance_to_com = 0

for pair in orbits:
    planetoid = node(pair[1])
    all_of_em[pair[1]] = planetoid
    #print(pair[1],pair[0] in all_of_em)
    if(pair[0] in all_of_em):
        planetoid.be_adopted(all_of_em[pair[0]])
    else:
        #print(pair[1], "orphan")
        orphan_pair.append(pair)
        
while len(orphan_pair)>0:
    for pair in orphan_pair:
        if(pair[0] in all_of_em):
            all_of_em[pair[1]].be_adopted(all_of_em[pair[0]])
            orphan_pair.remove(pair)
        else:
            #print(pair[1], "still orphan")
            pass

tot_orbits = com.determine_number_orbits()
print("tot orbits",tot_orbits)

you_to_com = set()
san_to_com = set()
you_pointer = all_of_em["YOU"]
san_pointer = all_of_em["SAN"]

while san_pointer != com:
    parent = san_pointer.parent
    if parent != com:
        san_to_com.add(san_pointer.parent)
        san_pointer = parent
    else:
        break

while you_pointer != com:
    parent = you_pointer.parent
    if parent != com:
        you_to_com.add(you_pointer.parent)
        you_pointer = parent
    else:
        break

transfer_planets = you_to_com.symmetric_difference(san_to_com)
print("transfers", len(transfer_planets)+1-1)

print(time.default_timer()-start)