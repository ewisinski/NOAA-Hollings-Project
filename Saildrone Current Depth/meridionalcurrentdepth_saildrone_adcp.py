# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:01:49 2022

@author: emily
"""

import netCDF4
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import xarray as xr
import matplotlib.patches as mpatches
import cmocean as cmo

#look at variables and information about netCDF
a = netCDF4.Dataset(r"C:\Users\emily\Downloads\SD1005adcp.cdf\SD1005adcp.cdf")
print(a)

print(a.variables.keys())
for b in a.dimensions.items():
    print(b)

#uses xarray to open netCDF
ds1 = xr.open_dataset(r"C:\Users\emily\Downloads\SD1005adcp.cdf\SD1005adcp.cdf")
print(ds1['VADCP'])

#using .isel() to return a new dataset index for what was specified (trajectory=0)
U_t = ds1['VADCP'].isel(TRAJECTORY=0).transpose()
#.pcolormesh() plots a non-regular rectangular grid
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1005 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1005_2017.png', transparent = False, bbox_inches = 'tight', dpi=200)

#########################

c = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp.cdf\SD1006adcp.cdf")
print(c)

print(c.variables.keys())
for d in c.dimensions.items():
    print(d)

ds2 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp.cdf\SD1006adcp.cdf")
print(ds2['VADCP'])

U_t = ds2['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1006 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1006_2017.png', transparent = False, bbox_inches = 'tight', dpi=200)

##########################

e = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1005adcp2018.cdf\SD1005adcp2018.cdf")
print(e)

print(e.variables.keys())
for f in e.dimensions.items():
    print(e)

ds3 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1005adcp2018.cdf\SD1005adcp2018.cdf")
print(ds3['VADCP'])

U_t = ds3['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1005 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1005_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

#############################

g = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp2018.cdf\SD1006adcp2018.cdf")
print(g)

print(g.variables.keys())
for h in g.dimensions.items():
    print(h)

ds4 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp2018.cdf\SD1006adcp2018.cdf")
print(ds4['VADCP'])

U_t = ds4['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1006 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1006_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

############################

i = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1029adcp2018.cdf\SD1029adcp2018.cdf")
print(i)

print(i.variables.keys())
for j in i.dimensions.items():
    print(j)

ds5 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1029adcp2018.cdf\SD1029adcp2018.cdf")
print(ds5['VADCP'])

U_t = ds5['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1029 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1029_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

#############################

k = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1030adcp2018.cdf\SD1030adcp2018.cdf")
print(k)

print(k.variables.keys())
for l in k.dimensions.items():
    print(l)

ds6 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1030adcp2018.cdf\SD1030adcp2018.cdf")
print(ds6['VADCP'])

U_t = ds6['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1030 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1030_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

#############################

m = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1066adcp2019.cdf\SD1066adcp2019.cdf")
print(m)

print(m.variables.keys())
for n in m.dimensions.items():
    print(n)

ds7 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1066adcp2019.cdf\SD1066adcp2019.cdf")
print(ds7['VADCP'])

U_t = ds7['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1066 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1066_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

#############################

o = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1067adcp2019.cdf\SD1067adcp2019.cdf")
print(o)

print(o.variables.keys())
for p in o.dimensions.items():
    print(p)

ds8 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1067adcp2019.cdf\SD1067adcp2019.cdf")
print(ds8['VADCP'])

U_t = ds8['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1067 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1067_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

#############################

q = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1068adcp2019.cdf\SD1068adcp2019.cdf")
print(q)

print(q.variables.keys())
for r in q.dimensions.items():
    print(r)

ds9 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1068adcp2019.cdf\SD1068adcp2019.cdf")
print(ds9['VADCP'])

U_t = ds9['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1068 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1068_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

###############################

s = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1069adcp2019.cdf\SD1069adcp2019.cdf")
print(s)

print(s.variables.keys())
for t in s.dimensions.items():
    print(t)

ds10 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1069adcp2019.cdf\SD1069adcp2019.cdf")
print(ds10['VADCP'])

U_t = ds10['VADCP'].isel(TRAJECTORY=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth')
plt.xlabel('Time')
plt.title('Meridional Current Depth - ADCP SD 1069 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionaldepth_1069_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)