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
import matplotlib.animation as animation 
import sys
sys.path.append("../intcode")
import intcode

start = time.default_timer()
pong = intcode.computer()
pong.load_program_txt("data.txt")
print(pong.start_program([]))
output = np.array(pong.get_output()[:-1])
frames = []
max_x = max(output[0::3])
max_y = max(output[1::3])
display = np.zeros((max_y+1,max_x+1))
for i in range(int((len(output))/3)):
    display[output[i*3+1],output[i*3]] = output[i*3+2]
frames.append(display.copy())

def draw_image(data):
    global display
    for i in range(int((len(data))/3)):
        if data[i*3] != -1:
            display[data[i*3+1],data[i*3]] = data[i*3+2]
    return display


pong.load_program_txt("data2.txt")
pong.pointer = 0
number_of_blocks = len(np.where(np.array(output[2::3])==2)[0])
old_bx = 0
old_by = 0

def get_next_move(data):
    global old_bx
    global old_by
    paddle_index = np.where(np.array(data[2::3])==3)[0][0]*3+2
    px,py = data[paddle_index-2],data[paddle_index-1]
    ball_index = np.where(np.array(data[2::3])==4)[0][0]*3+2
    bx,by = data[ball_index-2],data[ball_index-1]
    direction = bx-old_bx
    old_bx = bx
    print(bx,by,px,py)
    print(direction)
        
    old_by = by
    nmove = np.sign(bx+direction-px)
    if py-1 == by:
        nmove *= 0
    print(nmove)
    return nmove

op = pong.continue_program([]).get_output()

while number_of_blocks > 0:
    frames.append(draw_image(op).copy())
    shift = get_next_move(op)
    op = pong.continue_program([shift]).get_output()
    print(op)
    if len(op) <= 6: break
    number_of_blocks = len(np.where(np.array(output[2::3])==2)[0])
    print(number_of_blocks)

psi = np.where(np.array(output[0::3])==-1)*3
ims = []

fig = plt.figure()
for image in frames:
    im = plt.imshow(image, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True,
                                repeat_delay=0)

ani.save('filename.gif', writer='imagemagick')

print(time.default_timer()-start)
