import numpy as np
from sympy import *

x1,x2,x3,x4=symbols('x1,x2,x3,x4')

print(solve([Eq(3*x1-x3,0),Eq(8*x1-2*x4,0),Eq(2*x2-2*x3-x4,0)]))