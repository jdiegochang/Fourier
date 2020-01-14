#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:53:09 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

t = []
N = 1000

for i in range(N):
    t.append(10.0*i/N-5.0)

f = []
ft = []
x = [0.5 for i in range(N)]
tt = [t[i]-x[i] for i in range(N)]
sigma = 0.1

for i in range(N):
    f.append(t[i]-t[i]//1)
    ft.append(tt[i]-tt[i]//1)

fr = []

for i in range(N):
    fr.append((-tt[i])+tt[i]//1+1)
    
sinc = []

for i in range(N):
	sinc.append(np.sin(np.pi*t[i])/(np.pi*t[i]))

mult = [sinc[i]*fr[i] for i in range(N)]
    
fig, ax = plt.subplots(4,sharex=True,sharey=True, gridspec_kw={'hspace':0})
ax[0].plot(t,f)
ax[0].grid()
ax[1].plot(t,ft)
ax[1].grid()
ax[2].plot(t,fr)
ax[2].grid()
ax[3].plot(t,mult)
ax[3].grid()
plt.savefig('FuncionMultiplicada.eps')
plt.show()

	
