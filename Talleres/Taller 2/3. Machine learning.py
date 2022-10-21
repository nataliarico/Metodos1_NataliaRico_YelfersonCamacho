import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sympy as sym

intervalo = np.linspace(-1,1,100)
h = lambda x: 1/(sqrt(1+ np.exp(-x^2)))

for i in range(1,n+1):
    kernel = sym.lambdify([h],Laguerre[i],'numpy')

sumatoria(kernel, intervalo)
