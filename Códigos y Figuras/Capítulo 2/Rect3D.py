e#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 02:27:13 2020

@author: juan
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-1.0, 1.0, 0.01)
Y = np.arange(-1.0, 1.0, 0.01)
Z = np.zeros((len(X),len(Y)))
for i in range(len(X)):
    for j in range(len(Y)):
       if np.abs(X[i])<0.5 and np.abs(Y[j])<0.5:
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
plt.savefig('Rect3D.eps')
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5.0, 5.0, 0.1)
Y = np.arange(-5.0, 5.0, 0.1)
Z = np.zeros((len(X),len(Y)))
for i in range(len(X)):
    for j in range(len(Y)):
       Z[i,j] = np.sinc(X[i])*np.sinc(Y[j])
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y, Z, cmap='viridis', rstride=1, cstride=1,
                       linewidth=1, antialiased=False)
ax.set_zlim(-0.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig('sinc3D.eps')
plt.show()