# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:58:18 2016

@author: 10
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import netCDF4 as nc
import numpy as np
myFmt = mdates.DateFormatter('%H:%M')




year = 2013

file = '%s-01-16T000000Z.nc'%year
name = '%s-01-16'

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

lon2, lat2 = np.meshgrid(lons,lats)

#m = Basemap(projection='merc'%year,llcrnrlat=22.5,urcrnrlat=28.4,\
#            llcrnrlon=52.27083, urcrnrlon=59.27083,lat_ts=20,resolution='l')

m = Basemap(projection='merc',llcrnrlat=23,urcrnrlat=27.6,\
            llcrnrlon=52.27083, urcrnrlon=59.27083,lat_ts=20,resolution='l')
x, y = m(lon2, lat2)


fig = plt.figure(figsize=(30,14))
plt.subplots_adjust(wspace=-0.76,hspace=0.1)
im = plt.imread('colorbar.jpeg')


file = '%s-01-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']
ax1 = fig.add_subplot(431)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
m.drawparallels(np.arange(-80,81,1),labels=[1,0,0,0], size=12, linewidth=0.0)
plt.title('Jan %d'%year, y=0.15, x=0.50, size=16)

newax = fig.add_axes([0.44, 0.136, 0.3, 0.75], zorder=-1)
cbar = m.colorbar(ms,location='right',pad="4%", size="5%")
font_size = 14 # Adjust as appropriate.
cbar.ax.tick_params(labelsize=font_size, gridOn=True)

plt.clim(-1.5,2.5)
#newax.imshow(im)
newax.axis('off')

file = '%s-02-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax2 = fig.add_subplot(432)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
plt.title('Feb %d'%year, y=0.15, x=0.50, size=16)

file = '%s-03-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']
ax3 = fig.add_subplot(433)

m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
plt.title('Mar %d'%year, y=0.15, x=0.50, size=16)

file = '%s-04-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax4 = fig.add_subplot(434)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
m.drawparallels(np.arange(-80,81,1),labels=[1,0,0,0], size=12,linewidth=0.0)
plt.title('Apr %d'%year, y=0.15, x=0.50, size=16)

file = '%s-05-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax5 = fig.add_subplot(435)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
plt.title('May %d'%year, y=0.15, x=0.50, size=16)

file = '%s-06-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax6 = fig.add_subplot(436)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
plt.title('Jun %d'%year, y=0.15, x=0.50, size=16)

file = '%s-07-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax7 = fig.add_subplot(437)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
m.drawparallels(np.arange(-80,81,1),labels=[1,0,0,0], size=12,linewidth=0.0)
plt.title('Jul %d'%year, y=0.15, x=0.50, size=16)

file = '%s-08-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax8 = fig.add_subplot(438)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
plt.title('Aug %d'%year, y=0.15, x=0.50, size=16)

file = '%s-09-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax9 = fig.add_subplot(439)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
plt.title('Sep %d'%year, y=0.15, x=0.50, size=16)

file = '%s-10-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax10 = fig.add_subplot(4,3,10)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
m.drawparallels(np.arange(-80,81,1),labels=[1,0,0,0], size=12,linewidth=0.0)
m.drawmeridians(np.arange(0,360,2),labels=[0,0,0,1], size=12,linewidth=0.0)
plt.title('Oct %d'%year, y=0.15, x=0.50, size=16)

file = '%s-11-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax11 = fig.add_subplot(4,3,11)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
m.drawmeridians(np.arange(0,360,2),labels=[0,0,0,1], size=12,linewidth=0.0)
plt.title('Nov %d'%year, y=0.15, x=0.50, size=16)

file = '%s-12-16T000000Z.nc'%year

dataset = nc.Dataset(file)
lats = dataset['latitude']
lons = dataset['longitude']
sst = dataset['sstAnom']

ax12 = fig.add_subplot(4,3,12)
m.drawcoastlines()
m.drawcountries()
ms = m.pcolormesh(x,y,sst[0,:,:])
m.fillcontinents(color='white',lake_color='aqua')
m.drawmeridians(np.arange(0,360,2),labels=[0,0,0,1], size=12,linewidth=0.0)
plt.title('Dec %d'%year, y=0.15, x=0.50, size=16)


plt.savefig('0%s.jpeg'%year, bbox_inches='tight', dpi=300)
