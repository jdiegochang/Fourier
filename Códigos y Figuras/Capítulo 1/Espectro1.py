#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:04:51 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 20

c = []
n = []

for i in range(2*N+1):
	n.append(i-N)
	if n[i]%2==0:
		c.append(0.0)
	else:
		c.append((4/(n[i]*np.pi))**2)
		
fig,ax = plt.subplots()
ax.stem(n,c)
plt.title('Espectro')
plt.grid()
plt.savefig('Espectro.eps')
plt.show()
