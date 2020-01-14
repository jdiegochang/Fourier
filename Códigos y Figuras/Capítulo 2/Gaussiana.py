#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:56:36 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 10000
t = np.linspace(-3.0,3.0,N)
	
f = []

for i in range(N):
    f.append(np.exp(-t[i]**2))
    
plt.plot(t,f)
plt.grid()
plt.savefig('DistribucionGaussiana.eps')
plt.show()