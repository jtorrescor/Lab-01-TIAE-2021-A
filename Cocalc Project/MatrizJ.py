import numpy as np
import math as m

#### Matriz Rxyz #############################

def Rxyz(phi,theta,psi):
    return np.matrix([[m.cos(psi), 
                       m.sin(psi) * m.cos(phi) + m.cos(psi) * m.sin(theta) * m.sin(psi), 
                       m.sin(psi) * m.sin(phi) + m.cos(psi) * m.cos(phi) * m.sin(theta)], 
                      [m.sin(psi)* m.cos(theta), 
                       m.cos(psi)* m.cos(phi)+ m.sin(phi)* m.sin(theta)* m.sin(psi), 
                       -m.cos(psi)* m.sin(phi)+ m.sin(theta)* m.sin(psi)* m.cos(phi)], 
                      [-m.sin(theta), m.cos(theta)*m.sin(phi), m.cos(theta)*m.cos(phi)]])

#### Matriz T #############################

def T(phi,theta,psi):
    return np.matrix([[1, m.sin(phi)* m.tan(theta), m.cos(phi)* m.tan(theta)], 
                      [0, m.cos(phi), -m.sin(phi)],
                      [0,  m.sin(phi)/m.cos(theta), m.cos(phi)/m.cos(theta)]])

#### Matriz Zeros #############################

zeros = np.matrix([[ 0, 0, 0], [ 0, 0, 0], [ 0, 0, 0]])
    
Aphi=m.pi*1/2
Atheta=m.pi*1
Apsi=m.pi*1/2

Rn= Rxyz(Aphi,Atheta,Apsi)
mT=T(Aphi,Atheta,Apsi)

A=np.hstack((Rn,zeros))
B=np.hstack((zeros,mT))

J=np.vstack((A,B))

print("Matriz J(n)")
print(np.round(J, decimals=2))

