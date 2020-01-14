#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:40:28 2019

@author: juan
"""

import numpy as np
import matplotlib.pylab as plt

N = 1000

t = np.linspace(-1.0,1.0,N)	
f = []

for i in range(N):
	if np.abs(t[i]) < 0.5:
		f.append(1.0)
	else:
		f.append(0)
		
plt.plot(t,f)
plt.grid()
plt.savefig('FuncionRectangulo.eps')
plt.show()

fp = []
tp = np.linspace(-16.0,16.0,N)

for i in range(N):
	if np.abs(tp[i]) < 0.5:
		fp.append(1.0)
	elif tp[i] < -14.5 and tp[i] > -15.5:
		fp.append(1.0)
	elif tp[i] > 14.5 and tp[i] < 15.5:
		fp.append(1.0)
	else:
		fp.append(0.0)
		
plt.plot(tp,fp)
plt.grid()
plt.savefig('Periodizacion.eps')
plt.show()

M = 80

n = []
T = [2.0,4.0,8.0,16.0]
c = np.zeros((len(T),2*M+1))
w = np.zeros((len(T),2*M+1))

for k in range(len(T)):
	n = []
	for i in range(2*M+1):
		n.append(i-M)
		w[k,i] = 1.0/T[k] * n[i]
		if n[i] != 0:
			c[k,i] = T[k]/(n[i]*np.pi) * np.sin(n[i]*np.pi/T[k])
		else:
			c[k,i] = 1.0
		


fig, ax = plt.subplots(4,sharex=True,sharey=False, gridspec_kw={'hspace':0})
ax[0].stem(w[0,70:90],c[0,70:90])
ax[0].grid()
ax[1].stem(w[1,60:100],c[1,60:100])
ax[1].grid()
ax[2].stem(w[2,40:120],c[2,40:120])
ax[2].grid()
ax[3].stem(w[3],c[3])
ax[3].grid()
plt.xlabel('Frecuencia')
plt.ylabel('Coeficientes normalizados')
plt.savefig('Periodos.eps')
plt.show()

sinc = []
tsinc = [5*i for i in t]

for i in range(N):
	sinc.append(np.sin(np.pi*tsinc[i])/(np.pi*tsinc[i]))
	
plt.plot(tsinc,sinc)
plt.ylabel('sinc($x$)')
plt.xlabel('$x$')
plt.grid()
plt.savefig('sinc.eps')
plt.show()