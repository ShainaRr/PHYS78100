import numpy as np
import numpy.random as nr

N = 1000000
x = nr.power(0.5, N)
I = 2/N * np.sum(1/(1 + np.exp(x)))

print(I)