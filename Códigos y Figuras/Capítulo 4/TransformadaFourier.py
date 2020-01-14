#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:14:30 2020

@author: juan
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from scipy import fftpack

#Leer la imagen
f = io.imread('Dia.jpg')

#Ver dimensiones de la imagen
Nx = len(f)
Ny = len(f[0])

#Convertimos la imagen a escala de grises
fGris = np.zeros((Nx,Ny))
for i in range(Nx):
    for j in range(Ny):
        fgris = (0.2125*f[i][j][0] + 0.7154*f[i][j][1] + 0.0721*f[i][j][2])/255
        fGris[i][j] = fgris
           
plt.imshow(fGris, cmap='gray')
plt.colorbar()
plt.savefig('DiaGrisMejor.eps')
plt.show()

#Transformada rapida de Fourier
    
ftGris = fftpack.fft2(fGris)
FTGris = fftpack.fftshift(ftGris)

FTGrisMod = np.abs(FTGris)
FTGrisFase = np.angle(FTGris)

plt.imshow(FTGrisMod, cmap = 'gray')
plt.savefig('DiaGrisFTMod.eps')
plt.show()

plt.imshow(FTGrisFase, cmap = 'gray')
plt.savefig('DiaGrisFTFase.eps')
plt.show()   