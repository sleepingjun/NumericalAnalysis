# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:27:55 2021

@author: NI
"""


import numpy as np
import matplotlib.pylab as plt

t1,y1=np.loadtxt('ex.txt',unpack=True)
t2,y2=np.loadtxt('ex2.txt',unpack=True)
t3,y3=np.loadtxt('ex3.txt',unpack=True)
plt.figure()
plt.title("RK_system")
plt.plot(t1, y1,'x', t2,y2,'r-',t3,y3)
plt.savefig('RK_system.png')
plt.show()