# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:10:44 2021

@author: NI
"""

import numpy as np
import matplotlib.pylab as plt

t1,y1=np.loadtxt('Euler.txt',unpack=True)
t2,y2=np.loadtxt('ImEuler.txt',unpack=True)
plt.figure()
plt.title("Euler& ImEuler Method")
plt.plot(t1, y1,'x', t2,y2,'r-')
plt.savefig('ImEuler.png')
plt.show()