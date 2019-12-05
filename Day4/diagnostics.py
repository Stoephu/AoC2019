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
memory = list(map(int,strings[0].split(",")))

# initialize stuff
program_input = 5
pointer = 0
#defining opcodes
add = lambda adr: memory[adr[0]] + memory[adr[1]]
multiply = lambda adr: memory[adr[0]] * memory[adr[1]]
inp = lambda adr: program_input

def out(adr):
    print(memory[adr[0]])
    return memory[adr[-1]]

def jump_true(adr):
    global pointer
    if memory[adr[0]]: 
        pointer = memory[adr[1]] - 3
    return memory[adr[-1]]

def jump_false(adr):
    global pointer
    if not memory[adr[0]]: 
        pointer = memory[adr[1]] - 3
    return memory[adr[-1]]
   
def less_than(adr):
    if memory[adr[0]] < memory[adr[1]]:
        return 1
    
    else:
        return 0

def equals(adr):
    if memory[adr[0]] == memory[adr[1]]:
        return 1
    
    else:
        return 0
    
opcodes = {1 : (add, 4), 2 : (multiply, 4), 3 : (inp, 2), 4 : (out, 2), 5 : (jump_true, 3), 6 : (jump_false, 3), 7 : (less_than, 4), 8 : (equals, 4)}

#execution of opcodes

def get_digits(opcode):
    digits = []
    tmp = opcode
    
    for i in range(5):
        digits.append(int(tmp%10))
        tmp = (tmp - digits[-1])/10
        
    return digits

def get_adresses(digits, pos, step_size):
    adr = []
    
    for i in range(1,step_size):
        if not digits[i+1]:
            adr.append(memory[pos + i])
            
        else:
            adr.append(pos + i)
            
    return adr

def execute(opcode, position):
    digits = get_digits(opcode)

    fun, step_size = opcodes[digits[0]]

    adresses = get_adresses(digits, position, step_size)

    result = fun(adresses)
    memory[adresses[-1]] = result
    
    return step_size





while pointer < len(memory):
    if memory[pointer] == 99:
        print("Halted program")
        break
    
    else:
        step_size = execute(memory[pointer], pointer)
        pointer += step_size

print(time.default_timer()-start)
