#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:58:24 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

t = []
N = 10000

for i in range(N):
	t.append(6.0*i/N-3.0) #no usamos linspace, porque sino no aparece el 0
	
f = []

for i in range(N):
    if t[i] == 0.0:
        f.append(1000.0)
    else:
        f.append(0.0)
    
plt.plot(t,f)
plt.grid()
plt.savefig('deltaDirac.eps')
plt.show()