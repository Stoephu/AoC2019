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
debug = False
start = time.default_timer()
#part1
inputs = [string for string in open("data.txt")]
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

#node for graph class
class tile:
    
    def __init__(self,tileValue, coord):
        self.value = tileValue
        self.neighbours = set()
        self.coord = coord
        self.important = {}
        
    def addNeighbour(self,neigh):
        self.neighbours.add(neigh)
    
    def add_important(self,tile,distance):
        self.important[tile] = distance
        
#generate big graph        
#convert map to graph
rand = deque()
time_needed = {}
index = np.where(dungeon==player)
orpcoord = (index[0][0],index[1][0])
dungeon[orpcoord[0]-1:orpcoord[0]+2,orpcoord[1]-1:orpcoord[1]+2] = np.array([[64,35,64],[35,35,35],[64,35,64]])
indices = np.where(dungeon == player)
pcoords = []
for i in range(len(indices[0])):
    pcoords.append((indices[0][i],indices[1][i]))
    
playertiles = [tile(ord("@"),pcoord) for pcoord in pcoords]
rand.extend(playertiles)
for playertile in playertiles:
    time_needed[playertile] = 0
checked = set()
checked.update(pcoords)
alltiles = {}
alldoors = set()
allkeys = set()

def get_unchecked_neighbours(current):
    #string = chr(current.value) + " => "
    y,x = current.coord
    neighbours = []
    x1 = (y,x+1)
    x2 = (y,x-1)
    x3 = (y+1,x)
    x4 = (y-1,x)
    xis = [x1,x2,x3,x4]
    for xi in xis:
        if not xi in checked:
            if xi[0] >= 0 and xi[0]< shape[0] and xi[1]>=0 and xi[1]< shape[1]:
                tilevalue = dungeon[xi[0],xi[1]]
                if  tilevalue == ord("#"):
                    pass
                else:
                    ntile = tile(tilevalue,xi)
                    if chr(tilevalue).isupper():
                        alldoors.add(ntile)
                    elif chr(tilevalue).islower():
                        allkeys.add(ntile)
                    ntile.addNeighbour(current)
                    current.addNeighbour(ntile)
                    #string += chr(ntile.value) +","
                    neighbours.append(ntile)
                    alltiles[xi] = ntile
                    time_needed[ntile] = time_needed[current] + 1
        else:
            if xi in alltiles:
                current.addNeighbour(alltiles[xi])
    for neigh in neighbours:
        checked.add(neigh.coord)
    #print(string)
    return neighbours




i = 0
while rand:
    current = rand.popleft()
    neigh = get_unchecked_neighbours(current)
    rand.extend(neigh)
    if not i%20000:
        print(len(rand))
        #print(neigh)
    i+= 1


def show_all_important(node):
    string = chr(node.value)+ " => "
    for ne in node.important:
        string += chr(ne.value) + str(node.important[ne]) + ","
    print(string)
    
    
#reduce graph to only important neighbours
print("reduce!")

def get_unchecked_neighbours_graph(node):
    neigh = node.neighbours
    a = []
    for ne in neigh:
        if not ne in checked:
            a.append(ne)
    for ne in a:
        checked.add(ne)
    return a

all_important = alldoors.union(allkeys)
all_important.update(playertiles)

for node in all_important:
    rand = deque()
    checked = set()
    time_needed = {}
    rand.append((node,0))
    checked.add(node)
    while rand:
        current, i = rand.popleft()
        neigh = get_unchecked_neighbours_graph(current)
        for ne in neigh:
            if ne in all_important:
                print(chr(node.value),"=>",chr(ne.value),i+1)
                node.add_important(ne,i+1)
                ne.add_important(node,i+1)
            else:
                rand.append((ne,i+1))
        if not i%20000:
            print(len(rand))
            #print(neigh)
            
#breitensuche

def get_graph_neighbours(coord):
    nodes,tilename, old = coord
    a = []
    for i in range(len(nodes)):
        node = nodes[i]
        for ne in node.important:
            if chr(ne.value).islower() and not chr(ne.value) in old:
                        l = list(old)
                        l.append(chr(ne.value))
                        new = tuple(sorted(l))
            else:
                new = old
            newnodes = list(nodes)
            newnodes[i] = ne
            newnodes = tuple(newnodes)
            necoord = (newnodes,1,new)
            if chr(ne.value).isupper() and not chr(ne.value + diffUpper) in new:
                pass
            else:
                if faster_time(necoord, time_needed[coord] + node.important[ne]):
                    a.append(necoord)
    return a

lowesttime = 10000
def faster_time(coord,time):
    global lowesttime
    faster = False
    if coord in time_needed:
        if time_needed[coord]>time:
            time_needed[coord] = time
            faster = True
    else:
        time_needed[coord] = time
        faster = True
    if len(coord[2]) == len(allkeys) and time < lowesttime:
        print("lower!")
        lowesttime = time
    return faster

def get_tree(node, tree = set(), indent = 0):
    tree.add(node)
    string = chr(node.value) + "\n"
    a = set()
    for ne in node.important:
        if not ne in tree:
            a.add(ne)
    tree.update(node.important)
    for ne in a:
            string += " "*indent + "¦" + "\n"
            string += " "*indent + "-" + str(node.important[ne]) +" " + get_tree(ne,tree, indent + 1)
    return string
for playertile in playertiles:
    print(get_tree(playertile))            

rand = deque()
time_needed = {}
old  = ()
coord = (tuple(playertiles),chr(playertile.value),old)
rand.append(coord)
time_needed[coord] = 0
current = coord
i = 0
last12 =[]
while rand or len(allkeys)>len(current[2]):
    current = rand.popleft()
    neigh = get_graph_neighbours(current)
    rand.extend(neigh)
    if debug:
        print("current =", chr(current[0][0].value),chr(current[0][1].value),chr(current[0][2].value),chr(current[0][3].value))
        print("keys",current[2])
        for ne in current[0][0].important:
            print(chr(ne.value))
        print("rand:")
        #for r in rand:
        #    print(r[1],r[2])
        print("#rand",len(rand))
        print("diff keys",len(allkeys), len(current[2]))
    if not i%20000:
        print(len(rand))
        print(current[2])
        last12.append(len(current[2]))
        if len(last12)>12:
            last12.pop(0)
        print("last12",sum(last12)/12)
        print(len(allkeys), len(current[2]))
    i += 1
print("steps needed", lowesttime)
print(time.default_timer()-start)