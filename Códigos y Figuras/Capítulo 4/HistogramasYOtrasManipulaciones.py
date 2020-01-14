#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 00:25:43 2020

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

#Construyamos el histograma
plt.hist(fGris,bins=256)
plt.savefig('HistogramaGris.eps')
plt.show()

#------------------------------------------------------------------------------
#NEGATIVO
#------------------------------------------------------------------------------

fN = np.zeros((Nx,Ny))
for i in range(Nx):
    for j in range(Ny):
        neg = 1-fGris[i][j]
        fN[i][j] = neg

plt.imshow(fN,cmap='gray')
plt.colorbar()
plt.savefig('DiaGrisNegativo.eps')
plt.show()

#Construimos el histograma
plt.hist(fN,bins=256)
plt.savefig('HistogramaNegativo.eps')
plt.show()

#Funcion aplicada
x = np.arange(0.0, 1.0, 0.01)
y = 1-x
plt.plot(x,y)
plt.grid()
plt.savefig('FuncionNegativo.eps')
plt.show()

#------------------------------------------------------------------------------
#CORRECCION GAMMA
#------------------------------------------------------------------------------

gamma = 0.4
fGamma = np.zeros((Nx,Ny))

for i in range(Nx):
    for j in range(Ny):
        fg = fGris[i][j]**gamma
        fGamma[i][j] = fg

plt.imshow(fGamma,cmap='gray')
plt.colorbar()
plt.savefig('DiaGrisGamma.eps')
plt.show()

#Construimos el histograma
plt.hist(fGamma,bins=256)
plt.savefig('HistogramaGamma.eps')
plt.show()

#Funcion aplicada
x = np.arange(0.0, 1.0, 0.01)
y = x**gamma
plt.plot(x,y)
plt.grid()
plt.savefig('FuncionGamma.eps')
plt.show()

#------------------------------------------------------------------------------
#NORMALIZACION
#------------------------------------------------------------------------------

MIN = fGris.min()
MAX = fGris.max()
fNorm = np.zeros((Nx,Ny))

for i in range(Nx):
    for j in range(Ny):
        norm = (fGris[i][j]-MIN)/(MAX-MIN)
        fNorm[i][j] = norm

plt.imshow(fNorm,cmap='gray')
plt.colorbar()
plt.savefig('DiaGrisNorm.eps')
plt.show()

#Construimos el histograma
plt.hist(fNorm,bins=256)
plt.savefig('HistogramaNorm.eps')
plt.show()

#Funcion aplicada
x = np.arange(0.0, 1.0, 0.01)
y = (x-MIN)/(MAX - MIN)
plt.plot(x,y)
plt.grid()
plt.savefig('FuncionNorm.eps')
plt.show()