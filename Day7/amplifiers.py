# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
from itertools import product, permutations
import matplotlib.pyplot as plt 
import interpreter as preter

start = time.default_timer()

results = {}


def part_2():
    combinations = permutations(range(5,10))


    for comb in combinations:
        amplifiers = [preter.preter() for i in range(5)]
        output = [0]
        """
        for phase,amp in zip(comb,amplifiers):
            print(phase,comb,output)
            if not len(output) > 0:
                output = [0,-1]
                print("break")
                break
            output = amp.start_continues_program(phase, output[-1])
            print(output)
        """
        i = 0
        
        for phase,amp in zip(comb,amplifiers):
            amp.add_phase(phase)
            
        results[comb] = 0
        print("comb",comb)
        
        while output[-1] != -1:
            i += 1
            
            if i > 10000:
                print("Shiiiiiiiiiiiiiiiit")
                break
            
            for amp in amplifiers:
                print("amp in",output)
                output = amp.continue_program(output[-1])
                #print("amp out",output)
                
            if(output[-1] != -1):
                results[comb] = output[-1]
                
        print(comb,results[comb])
        
    print("result", max(results.values()))
def part_1():
    combinations = permutations(range(5))
    amplifiers = [preter.preter() for i in range(5)]
    
    for comb in combinations:
        output = [0]
        for phase,amp in zip(comb,amplifiers):
            #print(phase,output)
            output = amp.start_program(phase, output[-1])
            #print(output[-1])
        results[comb] = output[-1]
    print(max(results.values()))
print(time.default_timer()-start)
