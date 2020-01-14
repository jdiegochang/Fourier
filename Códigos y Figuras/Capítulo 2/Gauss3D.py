#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 02:53:43 2020

@author: juan
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

a = 1.5

X = np.arange(-a, a, 0.1)
Y = np.arange(-a, a, 0.1)
X, Y = np.meshgrid(X, Y)
R = X**2 + Y**2
Z = np.exp(-np.pi*R)

surf = ax.plot_surface(X, Y, Z, cmap='viridis', rstride=1, cstride=1,
                       linewidth=1, antialiased=False)
ax.set_zlim(-0.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig('Gauss3D.eps')
plt.show()
