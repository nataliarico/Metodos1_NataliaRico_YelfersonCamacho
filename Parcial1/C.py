#C: Derivada Progresiva 

import numpy as np
import matplotlib.pyplot as plt 

def funcion:
    return np.sqrt(np.tan(x))

intervalo = np.linspace(0.1, 1.1, 0.01)

solucion=[]
for i in intervalo:
    derivada =  (funcion(x+0.01)- f(x))/0.01 
    solucion.append(derivada)
    i+1

    
