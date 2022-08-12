# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:45:39 2021

@author: NI
"""

import numpy as np
import matplotlib.pylab as plt
t,y=np.loadtxt('Euler.txt',unpack=True)
plt.figure()
plt.title("Euler Method")
plt.plot(t, y,'x', t,y,'r-')
plt.savefig('Euler.png')
plt.show()


t,y=np.loadtxt('Euler2.txt',unpack=True)
plt.figure()
plt.title("Euler Method")
plt.plot(t, y,'x', t,y,'r-')
plt.savefig('Euler2.png')
plt.show()
t,y=np.loadtxt('Euler3.txt',unpack=True)
plt.figure()


plt.title("Euler Method")
plt.plot(t, y,'x', t,y,'r-')
plt.savefig('Euler3.png')
plt.show()



