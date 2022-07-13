# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:38:37 2022

@author: emily
"""

#import libraries
import netCDF4
from matplotlib import pyplot as plt
import xarray as xr

#ab
#look at variables and information about netCDF
a = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1005_1min.nc_\TPOS-2017_SD1005_1min.nc")
print(a)

print(a.variables.keys())
for b in a.dimensions.items():
    print(b)

ds1 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1005_1min.nc_\TPOS-2017_SD1005_1min.nc")
print(ds1)
print(ds1['UWND_MEAN'])
print(ds1['VWND_MEAN'])

#swap dimensions to correct x-y axes
ds1 = ds1.swap_dims({'row':'time'})
#if there are gaps in the dataset, .dropna() handles the missing values by dropping them from the dataset
ds1['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1005 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1005_2017.png', transparent = False, bbox_inches = 'tight', dpi=200)

###################
#cd
c = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1006_1min.nc_\TPOS-2017_SD1006_1min.nc")
print(c)

print(c.variables.keys())
for d in c.dimensions.items():
    print(d)

ds2 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2017_SD1006_1min.nc_\TPOS-2017_SD1006_1min.nc")
print(ds2)
print(ds2['UWND_MEAN'])
print(ds2['VWND_MEAN'])

ds2 = ds2.swap_dims({'row':'time'})
ds2['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1006 2017', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1006_2017.png', transparent = False, bbox_inches = 'tight', dpi=200)

#####################
#ef
e = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1005_1min.nc_\TPOS-2018_SD1005_1min.nc")
print(e)

print(e.variables.keys())
for f in e.dimensions.items():
    print(f)

ds3 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1005_1min.nc_\TPOS-2018_SD1005_1min.nc")
print(ds3)
print(ds3['UWND_MEAN'])
print(ds3['VWND_MEAN'])

ds3 = ds3.swap_dims({'row':'time'})
ds3['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1005 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1005_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

######################
#gh
g = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1006_1min.nc_\TPOS-2018_SD1006_1min.nc")
print(g)

print(g.variables.keys())
for h in g.dimensions.items():
    print(h)

ds4 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1006_1min.nc_\TPOS-2018_SD1006_1min.nc")
print(ds4)
print(ds4['UWND_MEAN'])
print(ds4['VWND_MEAN'])

ds4 = ds4.swap_dims({'row':'time'})
ds4['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1006 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1006_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

########################
#ij
i = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1029_1min.nc_\TPOS-2018_SD1029_1min.nc")
print(i)

print(i.variables.keys())
for j in i.dimensions.items():
    print(j)

ds5 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1029_1min.nc_\TPOS-2018_SD1029_1min.nc")
print(ds5)
print(ds5['UWND_MEAN'])
print(ds5['VWND_MEAN'])

ds5 = ds5.swap_dims({'row':'time'})
ds5['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1029 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1029_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

#######################
#kl
k = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1030_1min.nc_\TPOS-2018_SD1030_1min.nc")
print(k)

print(k.variables.keys())
for l in k.dimensions.items():
    print(l)

ds6 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2018_SD1030_1min.nc_\TPOS-2018_SD1030_1min.nc")
print(ds6)
print(ds6['UWND_MEAN'])
print(ds6['VWND_MEAN'])

ds6 = ds6.swap_dims({'row':'time'})
ds6['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1030 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1030_2018.png', transparent = False, bbox_inches = 'tight', dpi=200)

#########################
#mn
m = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1066_1min.nc_\TPOS-2019_SD1066_1min.nc")
print(m)

print(m.variables.keys())
for n in m.dimensions.items():
    print(n)

ds7 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1066_1min.nc_\TPOS-2019_SD1066_1min.nc")
print(ds7)
print(ds7['UWND_MEAN'])
print(ds7['VWND_MEAN'])

ds7 = ds7.swap_dims({'row':'time'})
ds7['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1066 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1066_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

###########################
#op
o = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1067_1min.nc_\TPOS-2019_SD1067_1min.nc")
print(o)

print(o.variables.keys())
for p in o.dimensions.items():
    print(p)

ds8 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1067_1min.nc_\TPOS-2019_SD1067_1min.nc")
print(ds8)
print(ds8['UWND_MEAN'])
print(ds8['VWND_MEAN'])

ds8 = ds8.swap_dims({'row':'time'})
ds8['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1067 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1067_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

############################
#qr
q = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1068_1min.nc_\TPOS-2019_SD1068_1min.nc")
print(q)

print(q.variables.keys())
for r in q.dimensions.items():
    print(r)

ds9 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1068_1min.nc_\TPOS-2019_SD1068_1min.nc")
print(ds9)
print(ds9['UWND_MEAN'])
print(ds9['VWND_MEAN'])

ds9 = ds9.swap_dims({'row':'time'})
ds9['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1068 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1068_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)

###############################
#st
s = netCDF4.Dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1069_1min.nc_\TPOS-2019_SD1069_1min.nc")
print(s)

print(s.variables.keys())
for t in s.dimensions.items():
    print(t)

ds10 = xr.open_dataset(r"C:\Users\emily\Downloads\Saildrone Data\TPOS-2019_SD1069_1min.nc_\TPOS-2019_SD1069_1min.nc")
print(ds10)
print(ds10['UWND_MEAN'])
print(ds10['VWND_MEAN'])

ds10 = ds10.swap_dims({'row':'time'})
ds10['VWND_MEAN'].dropna(dim='time').plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.ylim(-15, 20)
plt.xlabel('Time')
plt.title('Meridional Wind - SD 1069 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/saildronemeridionalwind_1069_2019.png', transparent = False, bbox_inches = 'tight', dpi=200)