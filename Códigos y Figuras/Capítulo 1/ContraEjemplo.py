#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:33:50 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

x1 = []
x2 = []

N = 10000
w1 = 1
w2 = np.sqrt(2.0)
t = np.linspace(0,10,N)

for n in range(N):
	x1.append(np.cos(w1*t[n]))
	x2.append(np.cos(w2*np.pi*t[n]))

SUM = np.array(x1) + np.array(x2)

fig, ax = plt.subplots(3,sharex=True,sharey=True, gridspec_kw={'hspace':0})
ax[0].plot(t,x1)
ax[0].grid()
ax[1].plot(t,x2)
ax[1].grid()
ax[2].plot(t,SUM)
ax[2].grid()
plt.savefig('NoPeriodica.eps')
plt.show()

x1 = []
x2 = []

w1 = 2*np.sqrt(2.0)
w2 = np.sqrt(2.0)

for n in range(N):
	x1.append(np.cos(w1*t[n]))
	x2.append(np.cos(w2*t[n]))

SUM = np.array(x1) + np.array(x2)

fig, ax = plt.subplots(3,sharex=True,sharey=True, gridspec_kw={'hspace':0})
ax[0].plot(t,x1)
ax[0].grid()
ax[1].plot(t,x2)
ax[1].grid()
ax[2].plot(t,SUM)
ax[2].grid()
plt.savefig('Periodica.eps')
plt.show()