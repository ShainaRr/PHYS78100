# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:21:36 2022

@author: Shaina
"""

import numpy as np
import matplotlib.pyplot as plt


def xa(t):
    return 2*np.cos(t) + np.cos(2*t)
def ya(t):
    return 2*np.sin(t) - np.sin(2*t)
ta = np.arange(0.0, 2*np.pi, 0.1)

def rb(t):
    return t*t
def xb(t):
    return rb(t)*np.cos(t) 
def yb(t):
    return rb(t)*np.sin(t) 
tb = np.arange(0.0, 10*np.pi, 0.1)

def rc(t):
    return np.exp(np.cos(t))-2*np.cos(4*t)+np.power(np.sin(t/12), 5)
def xc(t):
    return rc(t)*np.cos(t) 
def yc(t):
    return rc(t)*np.sin(t) 
tc = np.arange(0.0, 24*np.pi, 0.1)

fig=plt.figure()
fig.subplots_adjust(top=2)
axa=fig.add_subplot(311)
plt.plot(xa(ta), ya(ta), color='tab:blue')
axa.set_title('deltoid curve')

axb=fig.add_subplot(312)
plt.plot(xb(tb), yb(tb), color='tab:blue')
axb.set_title('Galilean spiral')

axc=fig.add_subplot(313)
plt.plot(xc(tc), yc(tc), color='tab:blue')
axc.set_title('Fey’s function')

plt.show()