# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product
start = time.default_timer()
text = open("data.txt").read()
opcodes = [int(code) for code in text.split(",")]
backup = opcodes.copy()
result = np.zeros((100,100))
def run(noun, verb, data):
    opcodes[1] = noun
    opcodes[2] = verb
    for i in range(int(len(opcodes)/4)):
        opcode = opcodes[i*4]
        #print(opcode)
        if opcode == 1:
            opcodes[opcodes[i*4+3]] = opcodes[opcodes[i*4+1]]+opcodes[opcodes[i*4+2]]
        elif opcode == 2:
            opcodes[opcodes[i*4+3]] = opcodes[opcodes[i*4+1]]*opcodes[opcodes[i*4+2]]
        elif opcode == 99:
            #print("Halted program")
            return opcodes[0]
        else :
            #print("Error Code")
            return -1
for i,j in product(range(100),range(100)):
    result[i,j] = run(i,j,opcodes)
    opcodes = backup.copy()
coords = np.argwhere(result == 19690720)[0]
print(100*coords[0]+coords[1])
print(time.default_timer()-start)