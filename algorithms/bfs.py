# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:37:39 2020

@author: chris
"""
from collections import deque


def get_shortest_path(start,end):
    checked = {}
    queue = deque()    
    queue.append((start,[]))
    checked[start] = (0,[])
    while queue:
        node, path = queue.popleft()
        time = checked[node][0]
        for distance, neighbour in node.neighbour:
            if not (neighbour in checked and checked[neighbour][0] < time + distance):                
                npath = path + [neighbour]
                checked[neighbour] = (time + distance, npath)
                queue.append((neighbour,npath))
    length, path = checked[end]
    return length, path