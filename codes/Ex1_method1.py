# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:20:16 2016

@author: kushal

Program to generate Fibonacci series formula method
"""

import numpy as np

n = input('Enter the number of terms required: ')
f = np.zeros(n+1)
f[1] = 1

for i in range(2, n+1):
    f[i] = f[i-1] + f[i-2]

print f