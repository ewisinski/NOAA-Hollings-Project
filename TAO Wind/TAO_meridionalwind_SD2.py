# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:15:08 2022

@author: emily
"""

#corresponds to 2nd saildrone mission
#import libraries
import netCDF4
from matplotlib import pyplot as plt
import xarray as xr

#look at variables and information about netCDF
a = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n110w_10m_SD2.cdf")
print(a)

print(a.variables.keys())
for b in a.dimensions.items():
    print(b)

ds1 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n110w_10m_SD2.cdf")
print(ds1)
print(ds1['WU_422'])
print(ds1['WV_423'])
print(ds1['WS_401'])
print(ds1['QWS_5401'])
print(ds1['SWS_6401'])
print(ds1['WD_410'])
print(ds1['QWD_5410'])
print(ds1['SWD_6410'])

#ds1 = ds1.swap_dims({'row':'time'})
ds1['WV_423'].plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.xlabel('Time')
plt.title('Meridional Wind - TAO 0, 110W Oct 2018 - Feb 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_110W_SD2.png', transparent = False, bbox_inches = 'tight', dpi=200)

######################
#cd
c = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n140w_10m_SD2.cdf")
print(c)

print(c.variables.keys())
for d in c.dimensions.items():
    print(d)

ds2 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n140w_10m_SD2.cdf")
print(ds2)
print(ds2['WU_422'])
print(ds2['WV_423'])
print(ds2['WS_401'])
print(ds2['QWS_5401'])
print(ds2['SWS_6401'])
print(ds2['WD_410'])
print(ds2['QWD_5410'])
print(ds2['SWD_6410'])

#ds1 = ds1.swap_dims({'row':'time'})
ds2['WV_423'].plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.xlabel('Time')
plt.title('Meridional Wind - TAO 0, 140W Oct 2018 - Feb 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_140W_SD2.png', transparent = False, bbox_inches = 'tight', dpi=200)

######################
#ef
e = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n170w_10m_SD2.cdf")
print(e)

print(e.variables.keys())
for f in e.dimensions.items():
    print(f)

ds3 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n170w_10m_SD2.cdf")
print(ds3)
print(ds3['WU_422'])
print(ds3['WV_423'])
print(ds3['WS_401'])
print(ds3['QWS_5401'])
print(ds3['SWS_6401'])
print(ds3['WD_410'])
print(ds3['QWD_5410'])
print(ds3['SWD_6410'])

#ds1 = ds1.swap_dims({'row':'time'})
ds3['WV_423'].plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.xlabel('Time')
plt.title('Meridional Wind - TAO 0, 170W Oct 2018 - Feb 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_170W_SD2.png', transparent = False, bbox_inches = 'tight', dpi=200)

######################
#gh
g = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n165e_10m_SD2.cdf")
print(g)

print(g.variables.keys())
for h in g.dimensions.items():
    print(h)

ds4 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n165e_10m_SD2.cdf")
print(ds4)
print(ds4['WU_422'])
print(ds4['WV_423'])
print(ds4['WS_401'])
print(ds4['QWS_5401'])
print(ds4['SWS_6401'])
print(ds4['WD_410'])
print(ds4['QWD_5410'])
print(ds4['SWD_6410'])

#ds1 = ds1.swap_dims({'row':'time'})
ds4['WV_423'].plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.xlabel('Time')
plt.title('Meridional Wind - TAO 0, 165E Oct 2018 - Feb 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_165E_SD2.png', transparent = False, bbox_inches = 'tight', dpi=200)

#######################
#ij
i = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n125w_10m_SD2.cdf")
print(i)

print(i.variables.keys())
for j in i.dimensions.items():
    print(j)

ds5 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_oct2018_feb2019_SD1005_1006\w0n125w_10m_SD2.cdf")
print(ds5)
print(ds5['WU_422'])
print(ds5['WV_423'])
print(ds5['WS_401'])
print(ds5['QWS_5401'])
print(ds5['SWS_6401'])
print(ds5['WD_410'])
print(ds5['QWD_5410'])
print(ds5['SWD_6410'])

#ds1 = ds1.swap_dims({'row':'time'})
ds5['WV_423'].plot(color='blue')

plt.ylabel('Wind Velocity (m/s)')
plt.xlabel('Time')
plt.title('Meridional Wind - TAO 0, 125W Oct 2018 - Feb 2019', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_125W_SD2.png', transparent = False, bbox_inches = 'tight', dpi=200)