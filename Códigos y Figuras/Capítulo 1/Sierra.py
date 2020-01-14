#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:44:36 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 1000
t = np.linspace(-2.5,2.5,N)

f = []

for i in range(N):
	f.append(t[i]-t[i]//1)
	
plt.plot(t,f)
plt.grid()
plt.savefig('FuncionSierra.eps')
plt.show()

M = [2,8,100]
fh = np.zeros((len(M),N))

for k in range(len(M)):
	for i in range(N):
		fh[k,i] = 0.5
		for j in range(M[k]):
			if j > 0:
				fh[k,i] += np.real(1.0j/(2*np.pi*j)*np.exp(2*np.pi*1.0j*j*t[i]) - 1.0j/(2*np.pi*j)*np.exp(-2*np.pi*1.0j*j*t[i]))

fig, ax = plt.subplots(4,sharex=True,sharey=True, gridspec_kw={'hspace':0})
ax[0].plot(t,f)
ax[0].grid()
ax[1].plot(t,fh[0])
ax[1].grid()
ax[2].plot(t,fh[1])
ax[2].grid()
ax[3].plot(t,fh[2])
ax[3].grid()
plt.savefig('Ejemplo2.eps')
plt.show()