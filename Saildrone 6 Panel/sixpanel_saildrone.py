# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:43:44 2022

@author: emily
"""

#import libraries
import matplotlib.pyplot as plt
from matplotlib import image

#variables defined by fig, axes
#plt.subplots() creates multiple subplots
#.ravel() return contiguous flattened array
fig, axes = plt.subplots(2,3)
axes = axes.ravel()
#copy path of .png images desired
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1005_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1005_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1005_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1005_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1005_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1005_2017.png"
       ]

#for loop that loops through each image linked and performs the following actions:
#enumerate adds a 'counter' to the iterables in the for loop
for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    #this removes the black box surrounding the .png image
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    #sharex means that x axis will be shared across plots. Do not necessairly want for y because could be different limits
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
#removes extra white space in figure
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1005_2017_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

####################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1006_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1006_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1006_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1006_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1006_2017.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1006_2017.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1006_2017_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

#####################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1005_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1005_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1005_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1005_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1005_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1005_2018.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1005_2018_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

######################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1006_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1006_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1006_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1006_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1006_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1006_2018.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1006_2018_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

#######################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1029_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1029_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1029_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1029_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1029_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1029_2018.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1029_2018_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

#####################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1030_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1030_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1030_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1030_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1030_2018.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1030_2018.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1030_2018_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

##########################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1066_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1066_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1066_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1066_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1066_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1066_2019.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1066_2019_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

###########################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1067_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1067_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1067_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1067_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1067_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1067_2019.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1067_2019_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

##########################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1068_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1068_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1068_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1068_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1068_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1068_2019.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1068_2019_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()

###########################

fig, axes = plt.subplots(2,3)
axes = axes.ravel()
img = [
       r"C:\Users\emily\Downloads\Saildrone Latitude Plots\saildronelatitude_1069_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Winds Plots\saildronemeridionalwind_1069_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Meridional Depth Plots\saildronemeridionaldepth_1069_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Longitude Plots\saildronelongitude_1069_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Wind Plots\saildronezonalwind_1069_2019.png",
       r"C:\Users\emily\Downloads\Saildrone Zonal Depth Plots\saildronezonaldepth_1069_2019.png"
       ]

for i, ax in enumerate(axes):
    im = image.imread(img[i])
    ax.imshow(im)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    sharex=True

#fig.suptitle("SD 1005 2017", fontweight="bold", size=10)
plt.subplots_adjust(wspace=0, hspace=0)
plt.draw()
plt.savefig(r"C:\Users\emily\Downloads\SD_1069_2019_6panel.png", transparent = False, bbox_inches = 'tight', dpi=200)
plt.show()