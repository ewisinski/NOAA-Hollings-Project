# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 07:39:22 2022

@author: emily
"""

#corresponds to the 5th saildrone mission 
#import libraries
import netCDF4
from matplotlib import pyplot as plt
import xarray as xr

#look at variables and information about netCDF
a = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n110w_10m_SD5.cdf")
print(a)

print(a.variables.keys())
for b in a.dimensions.items():
    print(b)

ds1 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n110w_10m_SD5.cdf")
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
plt.title('Meridional Wind - TAO 0, 110W July 2019 - Feb 2020', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_110W_SD5.png', transparent = False, bbox_inches = 'tight', dpi=200)

######################
#cd
c = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n140w_10m_SD5.cdf")
print(c)

print(c.variables.keys())
for d in c.dimensions.items():
    print(d)

ds2 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n140w_10m_SD5.cdf")
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
plt.title('Meridional Wind - TAO 0, 140W July 2019 - Feb 2020', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_140W_SD5.png', transparent = False, bbox_inches = 'tight', dpi=200)

######################
#gh
g = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n165e_10m_SD5.cdf")
print(g)

print(g.variables.keys())
for h in g.dimensions.items():
    print(h)

ds4 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n165e_10m_SD5.cdf")
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
plt.title('Meridional Wind - TAO 0, 165E July 2019 - Feb 2020', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_165E_SD5.png', transparent = False, bbox_inches = 'tight', dpi=200)

#######################
#ij
i = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n125w_10m_SD5.cdf")
print(i)

print(i.variables.keys())
for j in i.dimensions.items():
    print(j)

ds5 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_july2019_feb2020_SD1068_1069\w0n125w_10m_SD5.cdf")
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
plt.title('Meridional Wind - TAO 0, 125W July 2019 - Feb 2020', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_vwnd_125W_SD5.png', transparent = False, bbox_inches = 'tight', dpi=200)