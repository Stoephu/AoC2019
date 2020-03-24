# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:37:39 2020

@author: chris
"""
from collections import deque


def get_shortest_path(start,end):
    time_needed = {}
    queue = deque()    
    queue.append(start)
    time_needed[start] = 0
    while queue:
        node = queue.popleft()
        time = time_needed[node]
        for neighbour, distance in node.neighbours:
            if neighbour in time_needed:
                if time_needed[neighbour] > time + distance:                
                    time_needed[neighbour] = time + distance
                    queue.append(neighbour)
            else:
                time_needed[neighbour] = time + distance
                queue.append(neighbour)
        if not len(queue)%100: print(len(queue))
    length = time_needed[end]
    return length

def get_time_to_all(start):
    time_needed = {}
    queue = deque()    
    queue.append(start)
    time_needed[start] = 0
    while queue:
        node = queue.popleft()
        time = time_needed[node]
        for neighbour, distance in node.neighbours:
            if neighbour in time_needed:
                if time_needed[neighbour] > time + distance:                
                    time_needed[neighbour] = time + distance
                    queue.append(neighbour)
            else:
                time_needed[neighbour] = time + distance
                queue.append(neighbour)
        if not len(queue)%100: print(len(queue))
    return time_needed

class node:
    def __init__ (self,coord):
        self.coord = coord
        self.neighbours = []
    def add_neighbour(self,node,time = 1):
        self.neighbours.append((node,time))