# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:23:52 2016

@author: kushal

Program to generate Fibonacci series swap and unpack method
"""

import numpy as np

n = input('Enter the number of terms required: ')
f = np.zeros(n+1)

a = 0
b = 1

for i in range(1, n+1):
    a, b = b, a+b
    f[i] = a

print f