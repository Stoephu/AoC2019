# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
#from itertools import product, permutations
from itertools import groupby
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import sys
sys.path.append("../intcode")
#import intcode

start = time.default_timer()

strings = [string for string in open("data.txt")]
more_strings = [string.replace("=>",",").split(",") for string in strings]
parsed = []

for tup in more_strings:
    tmp = [string.split() for string in tup]
    parsed.append(tmp)

reactions = {}
elements = {}

for reaction in parsed:
    for tup in reaction:
        elements[tup[-1]] = 0

elements["FUEL"] = 1

def create_reaction(reaction):
    def fun(times):
        product = reaction[-1]
        elements[product[-1]] -= times*int(product[0])
        for educt in reaction[:-1]:
            elements[educt[-1]] += times*int(educt[0])

    return fun

for reaction in parsed:
    product = reaction[-1]
    fun = create_reaction(reaction)
    reactions[product[-1]] = (int(product[0]),fun)

def reduce(element):
    number = elements[element]
    reduction, fun = reactions[element]
    while number > 0:
        times = int(np.ceil(number/reduction))
        fun(times)
        number = elements[element]

all_negative = False
while not all_negative:
    all_negative = True
    for element in elements.keys():
        if elements[element] > 0 and element != "ORE":
            reduce(element)
            all_negative = False
            break

cost_one_fuel = elements["ORE"]
print("1fuel",cost_one_fuel)

print(elements)
for reaction in parsed:
    for tup in reaction:
        elements[tup[-1]] = 0

trillion = 1000000000000

fuels = 0
while trillion - elements["ORE"] > cost_one_fuel:
    elements["FUEL"]  = int((trillion - elements["ORE"]) /cost_one_fuel)
    print(elements["FUEL"])
    fuels += elements["FUEL"]    
    all_negative = False
    while not all_negative:
        all_negative = True
        for element in elements.keys():
            if elements[element] > 0 and element != "ORE":
                reduce(element)
                all_negative = False
                break
print("totalfuel",fuels)
print(time.default_timer()-start)
