import numpy as np
import math as m
def Ry(theta):
    return([[m.cos(theta),    0,    m.sin(theta)],
            [0,             1,    0],
            [-m.sin(theta),   0,    m.cos(theta)]])
theta=m.pi/2
print("the test angle , theta =" , theta)
R=Ry(theta)
print(np.round(R, decimals=2))