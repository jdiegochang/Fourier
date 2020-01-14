#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 23:54:40 2020

@author: juan
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import scipy.special as sp

fig = plt.figure()
ax = fig.gca(projection='3d')

a = 3.0

X = np.arange(-a, a, 0.01)
Y = np.arange(-a, a, 0.01)
Z = np.zeros((len(X),len(Y)))
for i in range(len(X)):
    for j in range(len(Y)):
       if X[i]**2 + Y[j]**2 < 1.0:
           Z[i,j] = 1.0
       else:
           Z[i,j] = 0.0
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, Z, cmap='viridis', rstride=1, cstride=1,
                       linewidth=1, antialiased=False)
ax.set_zlim(-0.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig('Circ.eps')
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

a = 3.0

X = np.arange(-a, a, 0.1)
Y = np.arange(-a, a, 0.1)
X, Y = np.meshgrid(X, Y)
R = X**2 + Y**2
Z = 4 * sp.jv(1,2*np.pi*R) / (4*R)

surf = ax.plot_surface(X, Y, Z, cmap='viridis', rstride=1, cstride=1,
                       linewidth=1, antialiased=False)
ax.set_zlim(-0.1, 3.0)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig('Jinc.eps')
plt.show()