#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:50:15 2020

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

#Convertir la imagen a blanco y negro
fBN = np.zeros((Nx,Ny))
for i in range(Nx):
    for j in range(Ny):
        fgris = 0
        for k in range(3):
            fgris += f[i][j][k]/3/255
        if fgris < 0.5:
            fBN[i,j] = 0
        else:
            fBN[i,j] = 1.0
            
plt.imshow(fBN, cmap='gray')
plt.colorbar()
plt.savefig('DiaBN.eps')
plt.show()