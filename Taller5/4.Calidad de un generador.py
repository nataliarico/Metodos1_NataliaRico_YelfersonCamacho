import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy import integrate

#Como guía se utilizó el código de clase y las notas de complementaria

#Primero se muestra el generador de puntos aleatorio
n_random = 10000
x = np.random.rand(n_random) 
y = np.random.rand(n_random)

#Después se mira la calidad de correlación
def funcion(x,y):
    return x,y

N = int(1e4)
K = np.zeros(30)

for i in range(N):
    K[i] = funcion(x,y)
    
