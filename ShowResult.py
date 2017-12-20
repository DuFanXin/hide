# -*- coding:utf-8 -*-
'''  
#====#====#====#====
# Project Name:     hide 
# File Name:        ShowResult 
# Date:             12/20/17 1:21 PM 
# Using IDE:        PyCharm Community Edition  
# From HomePage:    https://github.com/DuFanXin/hide
# Author:           DuFanXin 
# BlogPage:         http://blog.csdn.net/qq_30239975  
# E-mail:           18672969179@163.com
# Copyright (c) 2017, All Rights Reserved.
#====#====#====#==== 
'''
import matplotlib.pyplot as plt
import matplotlib
import h5py

with h5py.File("./2016/03/21/TEST_MP_PXX_20160321_000000.h5", "r") as fp:
    tod = fp["P/Phase1"].value
    time = fp["TIME"].value

plt.imshow(tod, aspect="auto",
           extent=(time[0], time[-1],990, 1260),
           cmap="gist_earth", norm=matplotlib.colors.LogNorm())
plt.colorbar()
plt.show()