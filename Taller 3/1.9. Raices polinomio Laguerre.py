#5 Calcular todas las raices reales de los primeros 20 polinomios de Laguerre

import numpy as np
import sympy as sym

def Laguerre(n):
    
    x = sym.Symbol('x')
    y = sym.Symbol('y')
    
    ecuacion = ((sym.exp(x)*sym.exp(-x)* x^n)/(np.math.factorial(n)))*sym.diff(y,x,n) 
    
    return ecuacion

solucion = []

n=20
for i in range(n+1):
    solucion.append(GetLaguerre(i))

    print (solucion)
