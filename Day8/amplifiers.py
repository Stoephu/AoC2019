# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:32:38 2019

@author: Stoephu
"""
import timeit as time
import numpy as np
import numpy.ma as ma
from itertools import product, permutations
import matplotlib.pyplot as plt 


start = time.default_timer()
image_size_data = (6,25)
image_size_test = (2,3)

data_string_list = [c for c in open("data.txt")]
pixel_values = [int(i) for i in data_string_list[0]]

data_string_list = [c for c in open("test.txt")]
test_pixel_values = [int(i) for i in data_string_list[0]]

def count_layers(data_size,size):
    return int(data_size/size[0]/size[1])

def create_image_data(data,size):
    a = np.array(data)
    return np.reshape(a,(int(count_layers(len(data),size)),int(size[0]),int(size[1])))


test = create_image_data(test_pixel_values,image_size_test)
print(test)

test_layers = count_layers(len(test_pixel_values),image_size_test)
counts = np.zeros((test_layers,3))

for i,value in enumerate(test_pixel_values):
    if not value > 2:
        counts[int(i/image_size_test[0]/image_size_test[1])%test_layers,value] += 1

counts = np.array(counts)
most_zeros = np.argmin(counts,axis=0)
print("1*2", counts[most_zeros[0],1]*counts[most_zeros[0],2])


layers = count_layers(len(pixel_values),image_size_data)
counts = np.zeros((layers,3))

for i,value in enumerate(pixel_values):
    if not value > 2:
        counts[int(i/image_size_data[0]/image_size_data[1])%layers,value] += 1

counts = np.array(counts)
most_zeros = np.argmin(counts,axis=0)
print("1*2", counts[most_zeros[0],1]*counts[most_zeros[0],2])

pictures = create_image_data(pixel_values,image_size_data)

result = np.full_like(pictures[0],-1)
pictures_masks = []
for i,j,k in product(range(pictures.shape[0]),range(pictures.shape[1]),range(pictures.shape[2])):
    if result[j,k] == -1 and pictures[i,j,k] < 2:
        result[j,k] = pictures[i,j,k]
plt.imshow(result)

print(time.default_timer()-start)
