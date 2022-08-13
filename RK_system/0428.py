# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:27:55 2021

@author: NI
"""


import numpy as np
import matplotlib.pylab as plt

t1,y1,w1=np.loadtxt('ex.txt',unpack=True)
t2,y2,w2=np.loadtxt('ex2.txt',unpack=True)
t3,y3,w3=np.loadtxt('ex3.txt',unpack=True)
plt.figure()
plt.title("RK_system")
plt.xlim(-4,4)
plt.plot(y1,w1,'r', y2,w2,'b',y3,w3,'g')
plt.savefig('RK_system.png')
plt.show()