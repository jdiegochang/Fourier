#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:53:09 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

x1 = []
x2 = []

N = 1000
t = np.linspace(0,10,N)

for n in range(N):
	x1.append(np.cos(2.0*np.pi*t[n]))
	x2.append(0.5*np.cos(4.0*np.pi*t[n]))

SUM = np.array(x1) + np.array(x2)

fig, ax = plt.subplots(3,sharex=True,sharey=True, gridspec_kw={'hspace':0})
ax[0].plot(t,x1)
ax[0].grid()
ax[1].plot(t,x2)
ax[1].grid()
ax[2].plot(t,SUM)
ax[2].grid()
plt.savefig('SuperposicionDeOndas.eps')
plt.show()
