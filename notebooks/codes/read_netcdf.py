# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:49:45 2016

@author: kushal
"""

from netCDF4 import Dataset as dt # note the change of case in netCDF4
import numpy as np
# Dataset is a netcdf object, similar to a dictionary

filestr = 'data/ncfile2.nc' # This is the file name

ncfile = dt(filestr, 'r') # Create a netcdf object in read mode

#print ncfile.variables # To print all the variables

lat = np.array(ncfile.variables['latitude'][:],dtype=np.float32)

'''
Extract a variable named 'latitude' from the netcdf object as a
numpy array, having all it's entries as real numbers of type
float32 (32 bit real numbers).

The numpy array's name is lat
'''

lon = np.array(ncfile.variables['longitude'][:],dtype=np.float32)
t = np.array(ncfile.variables['time'][:],dtype=np.int32)
u = np.array(ncfile.variables['u10'][:],dtype=np.float32)
v = np.array(ncfile.variables['v10'][:],dtype=np.float32)
T = np.array(ncfile.variables['t2m'][:],dtype=np.float32)
al = np.array(ncfile.variables['al'][:],dtype=np.float32)