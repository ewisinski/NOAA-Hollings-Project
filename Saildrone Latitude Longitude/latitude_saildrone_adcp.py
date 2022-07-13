# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:35:16 2022

@author: emily
"""

#import libraries
import netCDF4
from matplotlib import pyplot as plt
import xarray as xr

#look at variables and information about netCDF
#can also specify a variable with the path and then reference the variable in line 18
a = netCDF4.Dataset(r"C:\Users\emily\Downloads\SD1005adcp.cdf\SD1005adcp.cdf")
print(a)

print(a.variables.keys())
for b in a.dimensions.items():
    print(b)
    
ds1 = xr.open_dataset(r"C:\Users\emily\Downloads\SD1005adcp.cdf\SD1005adcp.cdf")
print(ds1)
ds1['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1005 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1005_2017.png', transparent = False, bbox_inches = 'tight', dpi=200)

########################

#next mission
c = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp.cdf\SD1006adcp.cdf")
print(c)

print(c.variables.keys())
for d in c.dimensions.items():
    print(d)

ds2 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp.cdf\SD1006adcp.cdf")
print(ds2)
ds2['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1006 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1006_2017.png', transparent = False, bbox_inches = 'tight', dpi=200)

#########################

#next mission
e = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1005adcp2018.cdf\SD1005adcp2018.cdf")
print(e)

print(e.variables.keys())
for f in e.dimensions.items():
    print(f)

ds3 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1005adcp2018.cdf\SD1005adcp2018.cdf")
print(ds3)
ds3['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1005 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1005_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

##########################

#next mission
g = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp2018.cdf\SD1006adcp2018.cdf")
print(g)

print(g.variables.keys())
for h in g.dimensions.items():
    print(h)

ds4 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1006adcp2018.cdf\SD1006adcp2018.cdf")
print(ds4)
ds4['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1006 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1006_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

###########################

#next mission
i = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1029adcp2018.cdf\SD1029adcp2018.cdf")
print(i)

print(i.variables.keys())
for j in i.dimensions.items():
    print(j)

ds5 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1029adcp2018.cdf\SD1029adcp2018.cdf")
print(ds5)
ds5['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1029 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1029_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

############################

#next mission
k = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1030adcp2018.cdf\SD1030adcp2018.cdf")
print(k)

print(k.variables.keys())
for l in k.dimensions.items():
    print(l)

ds6 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1030adcp2018.cdf\SD1030adcp2018.cdf")
print(ds6)
ds6['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1030 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1030_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

###########################

#next mission
m = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1066adcp2019.cdf\SD1066adcp2019.cdf")
print(m)

print(m.variables.keys())
for n in m.dimensions.items():
    print(n)

ds7 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1066adcp2019.cdf\SD1066adcp2019.cdf")
print(ds7)
ds7['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1066 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1066_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

##########################

#next mission
o = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1067adcp2019.cdf\SD1067adcp2019.cdf")
print(o)

print(o.variables.keys())
for p in o.dimensions.items():
    print(p)

ds8 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1067adcp2019.cdf\SD1067adcp2019.cdf")
print(ds8)
ds8['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1067 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1067_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

#############################

#next mission
q = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1068adcp2019.cdf\SD1068adcp2019.cdf")
print(q)

print(q.variables.keys())
for r in q.dimensions.items():
    print(r)

ds9 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1068adcp2019.cdf\SD1068adcp2019.cdf")
print(ds9)
ds9['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1068 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1068_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

###############################

#next mission
s = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1069adcp2019.cdf\SD1069adcp2019.cdf")
print(s)

print(s.variables.keys())
for t in s.dimensions.items():
    print(t)

ds10 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\SD1069adcp2019.cdf\SD1069adcp2019.cdf")
print(ds10)
ds10['LATADCP'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude Time Series - ADCP SD 1069 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1069_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)