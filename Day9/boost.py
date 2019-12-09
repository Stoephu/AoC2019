# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:45:15 2019

@author: chris
"""

import interpreter as interpreter

intcode = interpreter.preter()

output = intcode.start_program("data.txt",2,0)
print(output)