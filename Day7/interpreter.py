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

class preter():
    def out(self,adr):
        self.output.append(self.memory[adr[0]])
        return self.memory[adr[-1]]
    
    def jump_true(self,adr):
        if self.memory[adr[0]]: 
            self.pointer = self.memory[adr[1]] - 3
        return self.memory[adr[-1]]
    
    def jump_false(self,adr):
        if not self.memory[adr[0]]: 
            self.pointer = self.memory[adr[1]] - 3
        return self.memory[adr[-1]]
       
    def less_than(self,adr):
        if self.memory[adr[0]] < self.memory[adr[1]]:
            return 1
        
        else:
            return 0
    
    def equals(self,adr):
        if self.memory[adr[0]] == self.memory[adr[1]]:
            return 1
        
        else:
            return 0
    def __init__(self):
        self.strings = [string for string in open("data.txt")]
        self.memory = list(map(int,self.strings[0].split(",")))
        # initialize stuff
        self.program_input = []
        self.output = []
        self.pointer = 0
        #defining opcodes
        self.add = lambda adr: self.memory[adr[0]] + self.memory[adr[1]]
        self.multiply = lambda adr: self.memory[adr[0]] * self.memory[adr[1]]
        self.inp = lambda adr: self.program_input.pop(0)
    
        
        self.opcodes = {1 : (self.add, 4), 2 : (self.multiply, 4), 3 : (self.inp, 2), 4 : (self.out, 2), 5 : (self.jump_true, 3), 6 : (self.jump_false, 3), 7 : (self.less_than, 4), 8 : (self.equals, 4)}
    
    #execution of opcodes
    
    def get_digits(self,opcode):
        digits = []
        tmp = opcode
        
        for i in range(5):
            digits.append(int(tmp%10))
            tmp = (tmp - digits[-1])/10
            
        return digits
    
    def get_adresses(self, digits, pos, step_size):
        adr = []
        
        for i in range(1,step_size):
            if not digits[i+1]:
                adr.append(self.memory[pos + i])
                
            else:
                adr.append(pos + i)
                
        return adr
    
    def execute(self, opcode, position):
        digits = self.get_digits(opcode)
    
        fun, step_size = self.opcodes[digits[0]]
        
        adresses = self.get_adresses(digits, position, step_size)
        print("digits",digits)
        print("adr",adresses)
        result = fun(adresses)
        print("output fun", result)
        self.memory[adresses[-1]] = result
        return step_size
    
    def start_program(self, input_1, input_2):
        self.memory =  list(map(int,self.strings[0].split(",")))
        self.output = []
        self.pointer = 0
        self.program_input = [input_1, input_2]
        while self.pointer < len(self.memory):
            if self.memory[self.pointer] == 99:
                print("Halted program")
                break
            
            else:
                step_size = self.execute(self.memory[self.pointer], self.pointer)
                self.pointer += step_size
                
                #print(memory)
    
        return self.output
    
    
    def continue_program(self, *input_1):
        self.program_input.extend(input_1)
        while self.pointer < len(self.memory):
            if self.memory[self.pointer] == 99:
                #print("Halted program")
                self.output.append(-1)
                break
            
            else:
                step_size = self.execute(self.memory[self.pointer], self.pointer)
                self.pointer += step_size
                if step_size == 2 and self.memory[self.pointer - step_size] == 4:
                    print("pausing amp",self.memory[self.pointer - step_size],self.pointer,step_size)
                    result = self.output.copy()
                    self.output = []
                    return result
                #print(memory)
    
        result = self.output.copy()
        self.output = []
        return result
    def add_phase(self,phase):
        self.program_input.append(phase)
print(time.default_timer()-start)
