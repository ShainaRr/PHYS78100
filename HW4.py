import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons
import scipy.optimize as opt

m = 7.348e22
M = 5.972e24
w = 2.662e-6
R = 3.844e8
G = cons.G

def f(r):
    return ((w ** 2) * (r ** 3) * ((R - r) ** 2)) - G * M * ((R - r) ** 2) + G * m * (r ** 2)


def fd(r):
    return ((w ** 2) * 3 * (r ** 2) * ((R - r) ** 2)) + ((w ** 2) * (r ** 3) * (-2 * (R - r))) - G * M * (
                -2 * (R - r)) + G * m * (2 * r)


def find_root(r0, n):
    r = r0
    for i in range(n):
        r = r - (f(r) / fd(r))
    return r

print(find_root(10 ** 6, 20))

sol = opt.root_scalar(f, x0=10 ** 6, fprime=fd, method='newton')
print(sol.root)
