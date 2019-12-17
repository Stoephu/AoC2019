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
#part 2
#find path
start_coord = np.where(scaffold_map == 94)
current_pos = np.array([start_coord[0][0],start_coord[1][0]])
end = False
direction = np.array([0,-1])
left = np.array([[0,1],[-1,0]])
right = np.array([[0,-1],[1,0]])
path = ""
zero = np.array((0,0))
map_size = np.array(scaffold_map.shape)
while end == False:
    fx,fy = current_pos+direction
    #print(current_pos)
    rx,ry = current_pos+np.dot(right,direction)
    lx,ly = current_pos + np.dot(left,direction)
    if all((fx,fy) >= zero) and all((fx,fy) < map_size) and scaffold_map[fx,fy] == 35:
        path += "F"
        current_pos += direction
    elif scaffold_map[rx,ry] == 35:
        direction = np.dot(right,direction)
        path += "R"
    elif scaffold_map[lx,ly] == 35:
        direction = np.dot(left,direction)
        path += "L"
    else:
        end = True



#print(path)


groups = groupby(path)
result = [(label, sum(1 for _ in group)) for label, group in groups]
#print(result)
command = ""
for tup in result:
    if tup[0] == "F":
        command += str(tup[1])
    else:
        command += tup[0]
#print(command)

#zipping

a = ""
b = ""
c = ""

def find_repeat(string):
    aas = {}
    #print("string",string)
    for i in range(1,len(string)):
        if i > 11:
            break
        tempa = string[:i]
        aas[string.count(tempa)] = tempa
    keys = list(aas.keys())
    #print(keys)
    keys.sort()
    #print(aas.values())
    #keys.reverse()
    return aas.values()

aas = list(find_repeat(command))
bbs = []
ccs = []
for a in aas:
    temp = command.replace(a,"")
    bbs.extend( list(find_repeat(temp)))
for a,b in product(aas,bbs):
    temp = command.replace(a,"").replace(b,"")
    ccs.extend((list(find_repeat(temp))))

results = []
for a,b,c in product(aas,bbs,ccs):
    if not len(command.replace(a,"").replace(b,"").replace(c,"")):
        results.append((a,b,c))
        
#print("Results",results)
a,b,c = results[0]
#print("a",a,"b",b,"c",c,"command",command.replace(a,"").replace(b,"").replace(c,""))
temp = command
main = ""
while len(temp)>0:
    #print(temp)
    if temp[:len(a)] == a:
        temp = temp.replace(a,"",1)
        main += "A"
    if temp[:len(b)] == b:
        temp = temp.replace(b,"",1)
        main += "B"
    if temp[:len(c)] == c:
        temp = temp.replace(c,"",1)
        main += "C"
            

def to_ascii(text):
    asc = []
    for ch in text:
        asc.append(ord(ch))
    return asc

Main = ""
for ch in main:
    Main += ch +","
Main = Main[:-1]
Main = to_ascii(Main)

A = ""
next_digit = False
for i,ch in enumerate(a):
    if ch.isdigit():
        if i+1 < len(a):
            if a[i+1].isdigit():
                next_digit = True
        if next_digit:
            A += ch
            next_digit = False
        else:
            A += ch + ","
    else:
        A += ch + ","
A = A[:-1]
#print(A)
A = to_ascii(A)

B = ""
next_digit = False
for i,ch in enumerate(b):
    if ch.isdigit():
        if i+1 < len(b):
            if b[i+1].isdigit():
                next_digit = True
        if next_digit:
            B += ch
            next_digit = False
        else:
            B += ch + ","
    else:
        B += ch + ","
B = B[:-1]
#print(B)
B = to_ascii(B)

C = ""
next_digit = False
for i,ch in enumerate(c):
    if ch.isdigit():
        if i+1 < len(c):
            if c[i+1].isdigit():
                next_digit = True
        if next_digit:
            C += ch
            next_digit = False
        else:
            C += ch + ","
    else:
        C += ch + ","
C = C[:-1]
#print(C)
C = to_ascii(C)


Main.append(10)
A.append(10)
B.append(10)
C.append(10)



if True:
    robot_program = program.copy()
    robot_program[0] = 2
    preter.load_program(robot_program)
    robot_input = []
    robot_input.extend(Main)
    robot_input.extend(A)
    robot_input.extend(B)
    robot_input.extend(C)
    robot_input.extend([ord("n"),10])
    output = preter.start_program(*robot_input)
    output_string = ""
    for i in output:
        output_string += chr(i)
    print(output_string)
    print(output[-1])

print(time.default_timer()-start)
