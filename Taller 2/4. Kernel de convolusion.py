import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sympy as sym

#Para esta nueva mascara se implementa un kernel de [1,-2,1] por los coeficientes en la definicion de derivada

intervalo = np.linspace(-1,-2,1)
h = lambda x: 1/(sqrt(1+ np.exp(-x^2)))

for i in range(1,n+1):
    convolucion = sym.lambdify([h],Laguerre[i],'numpy')

sumatoria(convolucion, intervalo)



