import numpy as np
import scipy.constants as sp
g = sp.g

n = int(input('Valor de n: '))
m = int(input('Valor de m: '))
surface_tension = 31.6e-3
density = 997
height = .01
Lx = .08
Ly = .04
k = np.pi*np.sqrt((n/Lx)**2 + (m/Ly)**2)
w = np.sqrt((g*k + surface_tension*(k**3)/density)*np.tanh(k*height))

print("W_{n,m} = " + str(w) + " [rad/s]")