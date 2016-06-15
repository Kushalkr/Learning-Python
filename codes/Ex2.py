# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:26:33 2016

@author: kushal

Program for Problem 4
"""

import numpy as np

z = np.array([0.00, 0.10, 0.30, 0.50, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.0])
rh = np.array([60.0, 70.0, 80.0, 75.0, 60.0, 50.0, 80.0, 90.0, 60.0, 40.0, 20.0, 5.0, 2.0, 1.0])

print 'Z (Altitude in km): ', z
print 'RH (Relative Humidity in %): ', rh

Ts = 30.
Ps = 1.e5
A = 2.53e11
B = 5420.
g = 9.806
Cp = 1005.
R = 287.
L = 2.5006e6
v0 = 100.

T = np.zeros(z.shape[0])
Tk = np.array(T)
es = np.array(T)
e = np.array(T)
P = np.array(T)
rho = np.array(T)
q = np.array(T)
W = np.array(T)
h = np.array(T)
mse = np.array(T)
v = np.array(T)
E = np.array(T)

Tk = (Ts+273.15) - ((g*z*1000)/Cp)
T = Tk - 273.15
es = A * np.exp(-B/Tk)
e = (rh/100.) * es
