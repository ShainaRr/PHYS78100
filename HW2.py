# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:34:01 2022

@author: Shaina
"""

import numpy as np
import matplotlib.pyplot as plt

def integrate(x, N):
    t = np.linspace((x)/(2*N), x-(x)/(2*N), N)
    ft = np.exp(-t*t)
    area = np.sum(ft)*(x)/N
    return area

def E(x):
    return integrate(x, 100)

xx = np.arange(0.0, 3.1, 0.1)

EE = np.zeros(31, dtype=float)

for i in range(31) :
    EE[i]=E(i*0.1)

print(EE)

plt.plot(xx, EE, color='tab:blue')