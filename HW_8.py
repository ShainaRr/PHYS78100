from math import sin
from math import cos
from math import pi
from math import sqrt
import numpy as np
from numpy import arange
import matplotlib.pyplot as plt
import array as ar

R = 0.08
Alpha = pi/6
vo = 100
Rho = 1.22
C = 0.47
g = 9.81

def f(r,t, M):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    fx = vx
    fy = vy
    fvx = (-pi * R * R * Rho * C * vx * sqrt (vx * vx + vy * vy)) / (2 * M)
    fvy = - g + (-pi * R * R * Rho * C * vy * sqrt (vx * vx + vy * vy)) / (2 * M)
    return np.array([fx, fy, fvx, fvy],float)

a = 0.0
b = 10
N = 100
h = (b-a)/N
tpoints = arange(a,b,h)

def trajectory(M):
    xpoints = []
    ypoints = []
    r = ar.array('f', [0, 0, vo * cos(Alpha), vo * sin(Alpha)])

    for t in tpoints:
        if r[1] < 0:
            return [xpoints, ypoints]
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*f(r,t, M)
        k2 = h*f(r+0.5*k1,t+0.5*h, M)
        k3 = h*f(r+0.5*k2,t+0.5*h, M)
        k4 = h*f(r+k3,t+h, M)
        r += (k1+2*k2+2*k3+k4)/6
    return [xpoints, ypoints]

t1 = trajectory(1)
t2 = trajectory(3)
t3 = trajectory(10)

plt.figure()
plt.subplot(211)
plt.ylabel('y, m')
plt.xlabel('x, m')
plt.title('M = 1 kg')
plt.plot(t1[0], t1[1])
plt.subplot(212)
plt.title('M = 1 kg, M = 3 kg, M = 10 kg')
plt.ylabel('y, m')
plt.xlabel('x, m')
plt.plot(t1[0], t1[1])
plt.plot(t2[0], t2[1])
plt.plot(t3[0], t3[1])
plt.tight_layout()
plt.show()


