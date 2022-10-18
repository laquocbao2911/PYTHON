from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, projections
from mpl_toolkits.mplot3d import Axes3D

def graph(a1,b1,c1,d1,a2,b2,c2,d2):
    x,y = np.meshgrid(np.arange(-10,10),np.arange(-10,10))
    z1 = (d1 - a1*x - b1*y)/c1
    z2 = (d2 - a2*x - b2*y)/c2
    fig = plt.figure()
    ax = fig.add_subplot(111,projection= '3d')
    ax.plot_surface(x,y,z1,cmap = plt.cm.cool,alpha= 0.8)
    ax.plot_surface(x,y,z2,cmap = plt.cm.ocean,alpha = 0.8)
    plt.show()

print("Câu a")
graph(2,9,1,3,4,18,2,6)
print("Câu b")
graph(2,9,1,3,1,3,8,1)
print("Câu c")
graph(2,9,1,3,2,9,1,3)