#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:26:19 2020

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 1000

s = np.linspace(-15.0,15.0,N)    
f = []
v0 = 10.0
vc = 2.0

for i in range(N):
    if np.abs(s[i]) < v0+vc and np.abs(s[i])>v0-vc:
        f.append(1.0)
    else:
        f.append(0)
        
plt.plot(s,f)
plt.grid()
plt.savefig('FuncionTransfPasaBanda.eps')
plt.show()

t = np.linspace(-1.0,1.0,N)    
b = []

for i in range(N):
    b.append(4*vc*np.cos(2*np.pi*v0*t[i])*np.sinc(2*vc*t[i]))
    
plt.plot(t,b)
plt.grid()
plt.savefig('FuncionRespImpulsoPasaBanda.eps')
plt.show()