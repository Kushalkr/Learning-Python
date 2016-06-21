# -*- coding: utf-8 -*-

"""
Created on Thu Jun 16 22:49:45 2016

@author: kushal
"""

###############################################################################
#                          Reading in the data
###############################################################################


from netCDF4 import Dataset as dt # note the change of case in netCDF4
import numpy as np
# Dataset is a netcdf object, similar to a dictionary

filestr = '../data/ncfile2.nc' # This is the file name

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
#v = np.array(T)
E = np.array(T)

Tk = (Ts+273.15) - ((g*z*1000)/Cp)
T = Tk - 273.15
es = A * np.exp(-B/Tk)
e = (rh/100.) * es
P = Ps * np.exp((-g*z*1000)/(R*Tk))
rho = P/(R*Tk)
q = 0.622 * (e/P)
W = q * rho
h = (L*q) + (Cp * Tk)
mse = h + (g*z*1000)
Zs = R * ((Ts + 273.15)/g)
#v = v0 * (np.exp((z*1000/Zs)) - 1)
#E = mse + 0.5 * (v**2)

###############################################################################
#                          Line Plots
###############################################################################
# Basic Plot of Pressure vs Altitude

import matplotlib.pyplot as plt
plt.figure()
plt.plot(z*1000,P, label='P')
plt.show()
###############################################################################

# Previous plot is incorrect because altitude generally goes in the Y-Axis.
# So, Let's try again
plt.figure()
plt.plot(P,z*1000,label='P')
plt.show()
###############################################################################

# Let's make a slightly advanced plot where we the X-Axis is common to two 
# different plots
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(z*1000, P, 'r', label='P')
ax2.plot(z*1000, es, 'b', label='e_s')
plt.show()
#plt.close('all')
###############################################################################

# Superimposing plots
plt.plot(e,z*1000,'r')
plt.plot(es, z*1000,'b')
plt.show()
###############################################################################

# Fancier line plot
plt.figure()
xt = np.linspace(0, 5000,11)              # For creating the required xticks
yt = np.linspace(0,10000,11)              # For creating the required yticks
plt.plot(es, z*1000,'r', label='$e_s$')   # Plots e_s Vs Z
plt.plot(e, z*1000, 'b',label='$e$')        # Plots Vapour Pressure vs Z
plt.xlabel('Vapour Pressure in Pa')       # Labels the X-Axis
plt.ylabel('Altitude in m')               # Labels the Y-Axis
plt.suptitle('Exercise 4')                # Creates a Supertitle
plt.title('Vertical Profiles of Vapur Pressure') # Create a Title
plt.xticks(xt)                            # Draws the required xicks
plt.yticks(yt)                            # Draws the required yticks
plt.axis([0, 5000, 0, 10000])             # Forces the plot to have limits as required
#[X_start, X_end, Y_start, Y_end]
plt.legend()                              # Draws the Legend
plt.grid('on')                            # Draws the grid
plt.show()
###############################################################################
#                          Scatter Plot
###############################################################################
plt.figure()
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
###############################################################################
#                          Histogram Plot
###############################################################################
import matplotlib.mlab as mlab 

m , s = 100 , 15
iq = np.random.normal(m, s, 1000) 
# Setting a random Human IQ data, normally distributed with mean = 100, sd = 15

num_bins = 50 # Number of groups we want
plt.figure()
n, bins, patches = plt.hist(iq, num_bins, normed=1, facecolor='green')
# n = counts in each group
# bins = array of edges. (n groups have n+1 edges)
# patches = other variables for making the histogram plot (not needed)
# normed = 1 or True, then it returns n as fraction. Else, returns n as plain numbers
# Sum of fractions = 1 and, sum of counts = total number of entries
l = mlab.normpdf(bins, m, s) # Creates the pdf of normal distribution
plt.plot(bins, l, 'r', label='pdf')
plt.xlabel('IQ bins')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
plt.axis()
plt.legend()
plt.grid('on')
plt.show()
###############################################################################
#                          Contour Plot
###############################################################################
# Filled Contours
plt.figure()
plt.contourf(lon, lat, u[5,:,:]) # Plots Filled contours only without contour lines
plt.colorbar() # Displays the colorbar
plt.show()
###############################################################################

# Contour Lines
plt.figure()
plt.contour(lon, lat, u[5,:,:]) # Plots only the contour lines
plt.colorbar()
plt.show()
###############################################################################
#                          Streamline Plot
###############################################################################
um = np.mean(u, axis=0)     # averaging of u-winds along the time axis
vm = np.mean(v, axis=0)     # averaging of v-winds along the time axis

uv = (um**2 + vm**2)**0.5   # Wind speed calculation

plt.contourf(lon, lat, uv)
#plt.contour(lon, lat, uv)
plt.xticks(np.arange(0,360,30))
plt.yticks(np.arange(-90,100,15))
plt.xlabel('Longitude', fontsize=10)  # X axis label
plt.ylabel('Latitude', fontsize=10)  # Y axis label
plt.axis([0, 360, -90, 90])
plt.grid('on') 
plt.streamplot(lon, lat, um, vm, density=2, linewidth=2, color='k')
#plt.show()
###############################################################################
#                          Map Plot
###############################################################################
# Basic Map Plot
import cartopy as cart  # import the cartopy module

fig = plt.figure(figsize=(10,7))   # set the figure size with the figsize keyword, (width, height)
ax = plt.subplot(projection=cart.crs.PlateCarree())  # creates a GeoAxes with the PlateCarree projection
ax.coastlines() # Draws the coastlines
ax.stock_img()  # sample image
plt.show()
###############################################################################

# Map Plot with Latitude and Longitude labels
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter  # for formatting the latitudes and longitudes

plt.figure(figsize=(10,7))
ax = plt.subplot(projection=ccrs.PlateCarree(central_longitude=180))
ax.coastlines()
ax.set_global() # this method is used for global plots
ax.set_xticks(np.arange(-180, 181,60), crs=ccrs.PlateCarree()) # Generate xticks manually
ax.set_yticks(np.arange(-90,91, 30), crs=ccrs.PlateCarree())   # Generate yticks manually
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.stock_img()
plt.show()
###############################################################################

# Map with Data plotted onto it
plt.figure(figsize=(10,7))
ax = plt.subplot(projection=ccrs.PlateCarree(central_longitude=180))
ax.coastlines()
ax.set_global() # this method is used for global plots
ax.set_xticks(np.arange(-180, 181,60), crs=ccrs.PlateCarree()) # Generate xticks manually
ax.set_yticks(np.arange(-90,91, 30), crs=ccrs.PlateCarree())   # Generate yticks manually
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plot = ax.contourf(lon, lat, u[0,:,:], levels=np.linspace(-24, 24, 13), cmap=plt.cm.viridis)
plt.colorbar(plot, shrink=0.58)
plt.show()
