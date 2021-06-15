import numpy as np
import math as m
def Rx(phi):
    return([[1,    0,             0],
            [0,    m.cos(phi),    -m.sin(phi)],
            [0,    m.sin(phi),    m.cos(phi)]])
phi=m.pi/2
print("the test angle , phi =" , phi)
R=Rx(phi)
print(np.round(R, decimals=2)