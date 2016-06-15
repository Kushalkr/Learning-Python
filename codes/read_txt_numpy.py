# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:32:50 2016

@author: kushal
"""

import numpy as np

f = open('data/rain_data.txt','r')
contents = f.readlines()
l = len(contents)
y = np.zeros(l,dtype=np.int16)
sec = np.zeros(l)
rain = np.zeros(l)

i = 0
for line in contents:
    y[i], sec[i], rain[i] = line.split()
    i += 1
print sec
print sec.shape
print np.shape(sec)