#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 00:40:58 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 10000
t = np.linspace(-1.0,1.0,N)

f = []

for i in range(N):
	if np.abs(t[i]) < 1:
		f.append(1.0 - np.abs(t[i]))
	else:
		f.append(0.0)
		
plt.plot(t,f)
plt.grid()
plt.savefig('FuncionTriangulo.eps')
plt.show()

sinc2 = []
tsinc2 = np.linspace(-5.0,5.0,N)

for i in range(N):
	sinc2.append((np.sin(np.pi*tsinc2[i])/(np.pi*tsinc2[i]))**2)
	
plt.plot(tsinc2,sinc2)
plt.ylabel('$sinc^{2}(x)$')
plt.xlabel('$x$')
plt.grid()
plt.savefig('sinc2.eps')
plt.show()