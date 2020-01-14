#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 00:09:36 2020

@author: juan
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

#Leer la imagen
f = io.imread('Dia.jpg')

#Ver dimensiones de la imagen
Nx = len(f)
Ny = len(f[0])

#Convertir la imagen a negativo
fN = np.zeros((Nx,Ny,3))
for i in range(Nx):
    for j in range(Ny):
        fgris = 0
        for k in range(3):
            fN[i][j][k] = 1-f[i][j][k]/255
            
plt.imshow(fN)
plt.savefig('DiaNegativo.eps')
plt.show()