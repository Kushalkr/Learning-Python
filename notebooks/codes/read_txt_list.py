# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f = open('data/rain_data.txt','r') # Create a file pointer with syntax as open(filename,access type)
contents = f.readlines()      # Reads contents of the file into a list
y = []
sec = []
rain = []
for line in contents:
    a, b, c = line.split()
    y.append(a)
    sec.append(b)
    rain.append(c)