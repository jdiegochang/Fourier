#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 22:10:45 2020

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 1000

s = np.linspace(-5.0,5.0,N)    
f = []
vc = 2.0

for i in range(N):
    if np.abs(s[i]) < vc:
        f.append(0.0)
    else:
        f.append(1.0)
        
plt.plot(s,f)
plt.grid()
plt.savefig('FuncionTransfPasaAlto.eps')
plt.show()

t = []

for i in range(N):
    t.append(2.0*i/N-1.0)
    
b = []

for i in range(N):
    if t[i] == 0:
        b.append(3 - np.sinc(2*vc*t[i]))
    else:
        b.append(- np.sinc(2*vc*t[i]))
    
plt.plot(t,b)
plt.grid()
plt.savefig('FuncionRespImpulsoPasaAlto.eps')
plt.show()