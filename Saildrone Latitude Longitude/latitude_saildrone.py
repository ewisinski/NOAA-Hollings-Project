# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 08:32:03 2022

@author: emily
"""

#import libraries
import netCDF4
from matplotlib import pyplot as plt
import xarray as xr

#look at variables and information about netCDF
a = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1005_1min.nc_\TPOS-2017_SD1005_1min.nc")
print(a)

print(a.variables.keys())
for b in a.dimensions.items():
    print(b)

ds1 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1005_1min.nc_\TPOS-2017_SD1005_1min.nc")
print(ds1)
ds1 = ds1.swap_dims({'row':'time'})
ds1['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1005 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1005_2017_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

########################

#next mission
c = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1006_1min.nc_\TPOS-2017_SD1006_1min.nc")
print(c)

print(c.variables.keys())
for d in c.dimensions.items():
    print(d)

ds2 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1006_1min.nc_\TPOS-2017_SD1006_1min.nc")
print(ds2)
ds2 = ds2.swap_dims({'row':'time'})
ds2['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1006 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1006_2017_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

#########################

#next mission
e = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1005_1min.nc_\TPOS-2018_SD1005_1min.nc")
print(e)

print(e.variables.keys())
for f in e.dimensions.items():
    print(f)

ds3 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1005_1min.nc_\TPOS-2018_SD1005_1min.nc")
print(ds3)
ds3 = ds3.swap_dims({'row':'time'})
ds3['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1005 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1005_2018_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

##########################

#next mission
g = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1006_1min.nc_\TPOS-2018_SD1006_1min.nc")
print(g)

print(g.variables.keys())
for h in g.dimensions.items():
    print(h)

ds4 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1006_1min.nc_\TPOS-2018_SD1006_1min.nc")
print(ds4)
ds4 = ds4.swap_dims({'row':'time'})
ds4['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1006 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1006_2018_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

###########################

#next mission
i = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1029_1min.nc_\TPOS-2018_SD1029_1min.nc")
print(i)

print(i.variables.keys())
for j in i.dimensions.items():
    print(j)

ds5 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1029_1min.nc_\TPOS-2018_SD1029_1min.nc")
print(ds5)
ds5 = ds5.swap_dims({'row':'time'})
ds5['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1029 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1029_2018_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

############################

#next mission
k = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1030_1min.nc_\TPOS-2018_SD1030_1min.nc")
print(k)

print(k.variables.keys())
for l in k.dimensions.items():
    print(l)

ds6 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1030_1min.nc_\TPOS-2018_SD1030_1min.nc")
print(ds6)
ds6 = ds6.swap_dims({'row':'time'})
ds6['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1030 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1030_2018_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

###########################

#next mission
m = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1066_1min.nc_\TPOS-2019_SD1066_1min.nc")
print(m)

print(m.variables.keys())
for n in m.dimensions.items():
    print(n)

ds7 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1066_1min.nc_\TPOS-2019_SD1066_1min.nc")
print(ds7)
ds7 = ds7.swap_dims({'row':'time'})
ds7['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1066 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1066_2019_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

##########################

#next mission
o = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1067_1min.nc_\TPOS-2019_SD1067_1min.nc")
print(o)

print(o.variables.keys())
for p in o.dimensions.items():
    print(p)

ds8 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1067_1min.nc_\TPOS-2019_SD1067_1min.nc")
print(ds8)
ds8 = ds8.swap_dims({'row':'time'})
ds8['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1067 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1067_2019_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

#############################

#next mission
q = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1068_1min.nc_\TPOS-2019_SD1068_1min.nc")
print(q)

print(q.variables.keys())
for r in q.dimensions.items():
    print(r)

ds9 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1068_1min.nc_\TPOS-2019_SD1068_1min.nc")
print(ds9)
ds9 = ds9.swap_dims({'row':'time'})
ds9['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1068 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1068_2019_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)

###############################

#next mission
s = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1069_1min.nc_\TPOS-2019_SD1069_1min.nc")
print(s)

print(s.variables.keys())
for t in s.dimensions.items():
    print(t)

ds10 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1069_1min.nc_\TPOS-2019_SD1069_1min.nc")
print(ds10)
ds10 = ds10.swap_dims({'row':'time'})
ds10['latitude'].plot(color='blue')

plt.ylabel('Latitude')
plt.xlabel('Time')
plt.title('Latitude - SD 1069 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronelatitude_1069_2019_nonadcp.png', transparent = False, bbox_inches = 'tight', dpi=200)