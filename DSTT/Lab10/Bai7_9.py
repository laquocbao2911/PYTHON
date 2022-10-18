import numpy as np
import matplotlib.pyplot as plt
import math as m

print("Ma tran [x, y]: ")
v = np.array([[2],
              [3]])
print(v)
print("a)")
S = np.array([[2, 0],
              [0, 2]])
nv = S@v
vA = np.array([[nv[0,0]],
              [nv[1,0]]])
print(vA)

print("b)")
S = np.array([[0.5, 0],
              [0, 0.5]
              ])
nv = S@v
vB = np.array([[nv[0,0]],
            [nv[1,0]]])
print(vB)

print("c)")
S = np.array([[1, 0],
              [0, -1]
              ])
nv = S@v
vC = np.array([[nv[0,0]],
            [nv[1,0]]])
print(vC)

print("d)")
v = np.array([[2],
              [3]
              ])

S = np.array([[-1, 0],
              [0, 1]
              ])
nv = S@v
vD = np.array([[nv[0,0]],
            [nv[1,0]]])
print(vD)