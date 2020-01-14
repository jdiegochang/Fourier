#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:28:59 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

x = []
x1 = []
x2 = []
x3 = []
x4 = []

N = 1000
w = 2.0*np.pi/2

t = np.linspace(0,4.0,N)
	
for i in range(len(t)):
	x.append(0)
	for n in range(2):
		j = 2.0*n+1.0
		x[i] += 4/np.pi * (1.0/j * np.sin(j*w*t[i])) 

for i in range(len(t)):
	x1.append(0)
	for n in range(3):
		j = 2.0*n+1.0
		x1[i] += 4/np.pi * (1.0/j * np.sin(j*w*t[i])) 

for i in range(len(t)):
	x2.append(0)
	for n in range(4):
		j = 2.0*n+1.0
		x2[i] += 4/np.pi * (1.0/j * np.sin(j*w*t[i])) 

for i in range(len(t)):
	x3.append(0)
	for n in range(5):
		j = 2.0*n+1.0
		x3[i] += 4/np.pi * (1.0/j * np.sin(j*w*t[i])) 

for i in range(len(t)):
	x4.append(0)
	for n in range(100):
		j = 2.0*n+1.0
		x4[i] += 4/np.pi * (1.0/j * np.sin(j*w*t[i])) 
		

fig, ax = plt.subplots(5,sharex=True,sharey=True, gridspec_kw={'hspace':0})
ax[0].plot(t,x)
ax[0].grid()
ax[1].plot(t,x1)
ax[1].grid()
ax[2].plot(t,x2)
ax[2].grid()
ax[3].plot(t,x3)
ax[3].grid()
ax[4].plot(t,x4)
ax[4].grid()
plt.savefig('Ejemplo1.eps')
plt.show()

x5 = []
M = int(N/4)

for n in range(M):
	x5.append(1)
for n in range(M):
	x5.append(-1)
for n in range(M):
	x5.append(1)
for n in range(M):
	x5.append(-1)
	
plt.plot(t,x5)
plt.grid()
plt.savefig('Ejemplo1Original.eps')
plt.show()

	