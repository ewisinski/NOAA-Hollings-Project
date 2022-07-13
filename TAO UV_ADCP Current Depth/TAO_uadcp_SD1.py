# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:05:48 2022

@author: emily
"""
#import libraries
import netCDF4
from matplotlib import pyplot as plt
import numpy as np
import xarray as xr

a = netCDF4.Dataset(r"C:\Users\emily\Downloads\adcp0n110w_hr_SD1.cdf")
print(a)

print(a.variables.keys())
for b in a.dimensions.items():
    print(b)

#xarray and print information on variables    
ds1 = xr.open_dataset(r"C:\Users\emily\Downloads\adcp0n110w_hr_SD1.cdf")
print(ds1)
print(ds1['depth'])
print(ds1['u_1205'])
print(ds1['QU_5205'])
print(ds1['v_1206'])
print(ds1['QV_5206'])

#filters out missing values
for v in list(['u_1205', 'v_1206']):
    ds1[v] = ds1[v].where(ds1[v] < 1.e34, other=np.nan)

#indexing data 
U_t = ds1['u_1205'].isel(lat=0, lon=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth (m)')
plt.xlabel('Time')
plt.ylim([325,0])
plt.title('Zonal Current Depth - TAO ADCP 0, 110W Sep 2017 - May 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_uadcp_110W_SD1.png', transparent = False, bbox_inches = 'tight', dpi=200)

######################
#cd
c = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_sep2017_may2018_SD1005_1006\TAO Data 2017_2018\adcp0n140w_hr_SD1.cdf")
print(c)

print(c.variables.keys())
for d in c.dimensions.items():
    print(d)
    
ds2 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_sep2017_may2018_SD1005_1006\TAO Data 2017_2018\adcp0n140w_hr_SD1.cdf")
print(ds2)
print(ds2['depth'])
print(ds2['u_1205'])
print(ds2['QU_5205'])
print(ds2['v_1206'])
print(ds2['QV_5206'])

for v in list(['u_1205', 'v_1206']):
    ds2[v] = ds2[v].where(ds2[v] < 1.e34, other=np.nan)

U_t = ds2['u_1205'].isel(lat=0, lon=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth (m)')
plt.xlabel('Time')
plt.ylim([325,0])
plt.title('Zonal Current Depth - TAO ADCP 0, 140W Sep 2017 - May 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_uadcp_140W_SD1.png', transparent = False, bbox_inches = 'tight', dpi=200)

##########################
#ef
e = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_sep2017_may2018_SD1005_1006\TAO Data 2017_2018\adcp0n170w_hr_SD1.cdf")
print(e)

print(e.variables.keys())
for f in e.dimensions.items():
    print(f)
    
ds3 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_sep2017_may2018_SD1005_1006\TAO Data 2017_2018\adcp0n170w_hr_SD1.cdf")
print(ds3)
print(ds3['depth'])
print(ds3['u_1205'])
print(ds3['QU_5205'])
print(ds3['v_1206'])
print(ds3['QV_5206'])

for v in list(['u_1205', 'v_1206']):
    ds3[v] = ds3[v].where(ds3[v] < 1.e34, other=np.nan)

U_t = ds3['u_1205'].isel(lat=0, lon=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth (m)')
plt.xlabel('Time')
plt.ylim([325,0])
plt.title('Zonal Current Depth - TAO ADCP 0, 170W Sep 2017 - May 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_uadcp_170W_SD1.png', transparent = False, bbox_inches = 'tight', dpi=200)

########################
#gh
g = netCDF4.Dataset(r"C:\Users\emily\Downloads\TAO_sep2017_may2018_SD1005_1006\TAO Data 2017_2018\adcp0n165e_hr_SD1.cdf")
print(g)

print(g.variables.keys())
for h in g.dimensions.items():
    print(h)
    
ds4 = xr.open_dataset(r"C:\Users\emily\Downloads\TAO_sep2017_may2018_SD1005_1006\TAO Data 2017_2018\adcp0n165e_hr_SD1.cdf")
print(ds4)
print(ds4['depth'])
print(ds4['u_1205'])
print(ds4['QU_5205'])
print(ds4['v_1206'])
print(ds4['QV_5206'])

for v in list(['u_1205', 'v_1206']):
    ds4[v] = ds4[v].where(ds4[v] < 1.e34, other=np.nan)

U_t = ds4['u_1205'].isel(lat=0, lon=0).transpose()
xr.plot.pcolormesh(U_t, yincrease=False, cmap='seismic', vmin=-100, vmax=100)

plt.ylabel('Depth (m)')
plt.xlabel('Time')
plt.ylim([325,0])
plt.title('Zonal Current Depth - TAO ADCP 0, 165E Sep 2017 - May 2018', fontweight='bold')
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('C:/Users/emily/Downloads/TAO_uadcp_165E_SD1.png', transparent = False, bbox_inches = 'tight', dpi=200)