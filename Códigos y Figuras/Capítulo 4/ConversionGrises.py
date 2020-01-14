#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:52:11 2020

@author: juan
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

#Leer la imagen
f = io.imread('Dia.jpg')

#Desplegar los valores de los pixeles en la imagen
print(f)
#Ver dimensiones de la imagen
Nx = len(f)
Ny = len(f[0])

print('La imagen es de '+ str(Nx) + 'x' + str(Ny) + ' pixeles.')
#Convertir la imagen a escala de grises en un primer intento
fGris = np.zeros((Nx,Ny))
for i in range(Nx):
    for j in range(Ny):
        fgris = 0
        for k in range(3):
            fgris += (f[i][j][k])/3/255
            fGris[i][j] = fgris
            
plt.imshow(fGris, cmap='gray')
plt.colorbar()
plt.savefig('DiaGris.eps')
plt.show()

#Una mejor forma
fGris2 = np.zeros((Nx,Ny))
for i in range(Nx):
    for j in range(Ny):
        fgris = (0.2125*f[i][j][0] + 0.7154*f[i][j][1] + 0.0721*f[i][j][2])/255
        fGris2[i][j] = fgris


            
plt.imshow(fGris2, cmap='gray')
plt.colorbar()
plt.savefig('DiaGrisMejor.eps')
plt.show()

#Muestra la imagen original
plt.imshow(f)
plt.savefig('Dia.eps')
plt.show()