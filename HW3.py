# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:57:28 2022

@author: Shaina
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr

x,y = np.meshgrid(np.linspace(-50,50,51),np.linspace(-50,50,51))
xp = -5
yp = 0
xn = 5
yn = 0
k = 9.0e11
q = 1
phi = k*q*(1/np.sqrt((x - xp)**2+(y - yp)**2)-1/np.sqrt((x - xn)**2+(y - yn)**2))
Ex = k*q*((x-xp)/(np.sqrt((x - xp)**2+(y - yp)**2))**3-(x-xn)/(np.sqrt((x - xn)**2+(y - yn)**2))**3)
Ey = k*q*((y-yp)/(np.sqrt((x - xp)**2+(y - yp)**2))**3-(y-yn)/(np.sqrt((x - xn)**2+(y - yn)**2))**3)

norms = np.sqrt(Ex[...]**2 + Ey[...]**2)
Ex = Ex/norms
Ey = Ey/norms

#levels = np.linspace(phi.min(), phi.max(), 100)
levels = np.linspace(-9.0e11, 9.0e11, 200)

#plt.pcolormesh(x, y, phi, norm=clr.SymLogNorm(linthresh=3.0e10, vmin=-9.0e11, vmax=9.0e11), cmap='Spectral_r')
plt.contourf(x, y, phi, levels=levels, norm=clr.SymLogNorm(linthresh=3.0e10), cmap='Spectral_r')
plt.colorbar()
plt.title('Potential')
plt.show()

plt.quiver(x,y,Ex,Ey, np.log(norms))
#plt.quiver(x,y,Ex,Ey, norms, norm=clr.LogNorm(vmin=10.0, vmax=1.0e15, clip=True), cmap='Spectral_r')
plt.colorbar()
plt.title('Electric Field')
plt.show()

