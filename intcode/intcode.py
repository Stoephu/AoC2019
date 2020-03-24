# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product
import matplotlib.pyplot as plt 



class computer():
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
    
    def inp(self,adr):
        if self.program_input:
            return self.program_input.pop(0)
        else:
            self.wait_for_input = True
            return self.memory[adr[-1]]
        
    def set_relativ_base(self, adr):
        self.relative_base += self.memory[adr[0]]
        return self.memory[adr[-1]]
    
    def load_program(self, program):
        self.memory = {}
        for i,mem in enumerate(program):
            self.memory[i] = mem
    
    def load_program_txt(self, txt = "data.txt"):
        self.strings = [string for string in open(txt)]
        opcodes = list(map(int,self.strings[0].split(",")))
        self.load_program(opcodes)
    
    def __init__(self):
        # initialize stuff
        self.verbose = False
        self.program_input = []
        self.output = []
        self.pointer = 0
        self.relative_base = 0
        self.wait_for_input = False
        #defining opcodes
        self.add = lambda adr: self.memory[adr[0]] + self.memory[adr[1]]
        self.multiply = lambda adr: self.memory[adr[0]] * self.memory[adr[1]]
    
        
        self.opcodes = {1 : (self.add, 4), 2 : (self.multiply, 4), 3 : (self.inp, 2), 4 : (self.out, 2), 5 : (self.jump_true, 3), 6 : (self.jump_false, 3), 7 : (self.less_than, 4), 8 : (self.equals, 4), 9 : (self.set_relativ_base, 2)}
    
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
                
            elif digits[i+1] == 1:
                adr.append(pos + i)
                
            elif digits[i+1] == 2:
                adr.append(self.relative_base+self.memory[pos + i])
            else:
                if self.verbose: print("invalid adr code")
            if not adr[-1] in self.memory:
                self.memory[adr[-1]] = 0
        return adr
    
    def execute(self, opcode, position):
        digits = self.get_digits(opcode)
    
        fun, step_size = self.opcodes[digits[0]]
        
        adresses = self.get_adresses(digits, position, step_size)
        if self.verbose: print("digits",digits)
        if self.verbose: print("adr",adresses)
        result = fun(adresses)
        if self.verbose: print("function output", result)
        self.memory[adresses[-1]] = result
        return step_size
    
    
    def start_program(self,  user_input, verbose = False):
        self.verbose = verbose
        self.output = []
        self.pointer = 0
        
    
        return self.continue_program(user_input,verbose = verbose)
    
    
    def continue_program(self, input_1, verbose = False):
        self.verbose = verbose
        self.program_input.extend(input_1)
        if self.verbose: print(self.program_input)
        while self.pointer < len(self.memory.keys()):
            if self.memory[self.pointer] == 99:
                print("Halted program")
                self.output.append(-1)
                return self
                
            
            else:
                step_size = self.execute(self.memory[self.pointer], self.pointer)
                if self.wait_for_input:
                    self.wait_for_input = False
                    if self.verbose: print("pausing computer, waiting for input",self.memory[self.pointer - step_size],self.pointer)
                    return self
                self.pointer += step_size
                """
                if step_size == 2 and self.memory[self.pointer - step_size] == 4:
                    if self.verbose: print("pausing computer",self.memory[self.pointer - step_size],self.pointer,step_size)
                    result = self.output.copy()
                    self.output = []
                    return result
                """
                #print(memory)
    
        result = self.output.copy()
        self.output = []
        return result
    
    
    def get_output(self):
        result = self.output.copy()
        self.output = []
        return result