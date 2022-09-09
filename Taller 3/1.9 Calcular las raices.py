#3 Calcular todas las raíces reales de

import numpy as np 


def ecuacion (x):
    return 3x^5 + 5x^4 - x^3
def derivada(x):
    return 15x^4 + 20x^3 - 3x^2

def newtrap(x):
    newx = x - ecuacion(x)/derivada(x)
    return newx

solucion=100
for i in range(10):
    solution_a = newtrap(solucion)
    
    print("Las raices reales del polinomio son", solucion)
