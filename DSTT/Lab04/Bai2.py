from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def graph(a1,a2,b1,b2,c1,c2):
    x = np.arange(-10,10)
    y1 = (c1 - a1*x)/b1
    y2 = (c2 - a2*x)/b2
    fig = plt.figure()
    plt.plot(x,y1,'red')
    plt.plot(x,y2,'brown')
    plt.show()

print("Câu a")
graph(2,9,4,18,3,6)
print("Câu b")
graph(2,9,1,1,20,3)
print("Câu c")
graph(2,2,9,9,20,20)