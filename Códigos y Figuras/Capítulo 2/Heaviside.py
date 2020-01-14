#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 01:10:30 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 10000

t = np.linspace(-0.25,0.25,N)	
f = []

for i in range(N):
	if t[i] < 0:
		f.append(0.0)
	else:
		f.append(1.0)
		
plt.plot(t,f)
plt.grid()
plt.savefig('Heaviside.eps')
plt.show()

FH = []

for i in range(N):
    if t[i] == 0:
        FH.append(0.0)
    else:
        FH.append(1/(2*np.pi*t[i]))
    
plt.plot(t,FH)
plt.grid()
plt.savefig('FTHeaviside.eps')
plt.show()