import numpy as np
import math as m
def Rz(psi):
    return([[m.cos(psi),    -m.sin(psi),   0],
            [m.sin(psi),    m.cos(psi),    0],
            [0,             0,             1]])
psi=m.pi/2
print("the test angle , psi =" , psi)
R=Rz(psi)
print(np.round(R, decimals=2))