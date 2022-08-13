# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:17:25 2021

@author: NI
"""

import numpy as np
import matplotlib.pylab as plt

"""
## Crank-Nicolson method

   du(x,t)/dt  - alpha^2*d^2u(x,t)/dt^2 = 0
   0 < x < l
   0 < t < T
   
   Boundary Conditions
   u(0,t) = u(l,t) = 0 ,  0 < t < T
   
   Initial Conditions
   u(x,0) = f(x) ,   0 <= x <= l

INPUT: endpoint l, maximum time T, constant coefficiant alpha,
       integer m >= 3; N >= 1
OUTPUT: aproximation wij to u(xi,tj) for each i = 1, ... , m-1 and j = 1, ... , N
"""

#numerical_analysis, 9th, Burden
#p734-p735
def CrankNicolson(l,T,alpha,m,N):
    #step1. set parameter
    h = l/m
    k = T/N
    lam = alpha**2*k/(h**2)
    
    w = np.zeros([m])
    l = np.zeros([m])
    u = np.zeros([m])
    z = np.zeros([m])
    W = np.zeros([m+1,N])
    
    #step2. # initial values
    for i in range(1,m): w[i-1] = f(i*h) 
    
    #step3-11. solve a tridiagnal linear system using Algorithm 6.7
    #step3.
    l[0] = 1 + lam
    u[0] = -lam/(2*l[0])
    
    #step4. i=2~m-2 (in python, end step m-1)
    for i in range(2,m-1):
        l[i-1] = 1 + lam + lam*u[i-2]/2 #l2 in python is l1
        u[i-1] = -lam/(2*l[i-1]) # u2 in python is u1
        
    #step5. lm-1→lm-2; um-2→um-3
    l[m-2] = 1 + lam + lam*u[m-3]/2
    
    #step6. j=1~N (~N+1 in python) do step7-11
    record_t=[]
    record_x=[]    
    for j in range(1,N+1):
        #step7
        t=j*k #current tj
        record_t.append(t)
        z[0] = ((1-lam)*w[0] + lam*w[1]/2)/l[0]
        
        #step8. i=1~m-1 (~m in py)
        for i in range(2,m):
            z[i-1] = ((1-lam)*w[i-1] + lam*(w[i] + w[i-2] + z[i-2])/2 )/l[i-1]#z1,z2...
        
        #step9
        w[m-2] = z[m-2]
        
        #step10. i=m-2~1
        for i in range(m-2,0,-1):
            w[i-1] = z[i-1] - u[i-1]*w[i]

        W[0,j-1] = f(0) # restriction
        W[1:,j-1] = w
        
        if j==N:
            for i in range(1,m):
                x=i*h
                record_x.append(x)
        else:
            continue
        
    return record_t,record_x,W
        
def f(x):
    return np.sin((1/2)*np.pi*x)

def g(x,t):# exact solution
    return np.exp(-((np.pi**2)/4)*t)*np.sin((1/2)*np.pi*x)


l = 2.0 #0<x<l
T = 0.1 #0<t<T
alpha = 1.0
m = 5
N = 2


t,x,w = CrankNicolson(l,T,alpha,m,N)
print("approximate value:\n",w[:,:])

xx=[]
xx.append(0)
for i in range(len(x)):
    xx.append(x[i])
xx.append(l)

def draw_exact(num,t,color):
    E=[]
    
    x1=np.linspace(0,l,num=num)
    for i in x1:
        E.append(g(i,t))
    label='exact value with t='+str(t)
    plt.plot(x1,E[:],color,label=label)
    return x1,E
x1,E1=draw_exact(len(xx),t[0],'b-')
print('E1=',E1)
x2,E2=draw_exact(len(xx),t[1],'c-')
print('E2=',E2)

label3='approximate value with t='+str(t[0])
plt.plot(xx,w[:,0],'r--',label=label3)
label4='approximate value with t='+str(t[1])
plt.plot(xx,w[:,1],'g--',label=label4)

plt.legend(loc = 'lower right')
plt.title('compare with approximate and exact value')
plt.savefig('compare.png')
plt.plot()