#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:20:13 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 10000
t = np.linspace(-2.0,6.0,N)
  
a = [2.0,1.5,1.0,0.5,0.25]
f = np.zeros((len(a),N))

for A in range(len(a)):
    for i in range(N):
        if t[i] <= 0:
            f[A,i] = 0.0
        else:
            f[A,i] = np.exp(-a[A]*t[i])
        
for i in range(len(a)):
    plt.plot(t,f[i],label='$a$='+ str(a[i]))
plt.legend()
plt.grid()
plt.savefig('ExponencialDecay.eps')
plt.show()

L = np.zeros((len(a),N))
tL = np.linspace(-1.0,1.0,N)
    
for A in range(len(a)):
    for i in range(N):
        L[A,i] = 1.0/(a[A]**2 + 4*np.pi**2*tL[i]**2)
        
for i in range(len(a)):
    plt.plot(tL,L[i],label='$a$='+ str(a[i]))
plt.legend()
plt.grid()
plt.savefig('Lorenziana.eps')
plt.show()