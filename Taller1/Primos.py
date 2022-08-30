# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:13:57 2022

@author: LENOVO 4
"""
import matplotlib.pyplot as plt
num_prim = []

#Punto 1
def es_primo(numero: int)->bool:
    """ Encontrar si un número es primo
    Parámetros:
      numero (int): Entero que se busca ver si es primo
    Retorno:
      bool: Booleano que indica si el número entero recibido por parámetro es primo
    """
    pass
    cent = 1
    divisible = 0
    primo = True
    for cent in range(1,(numero+1)):
        if (numero % cent ) == 0:
            divisible += 1
        if divisible > 2:
            primo = False
    return primo
i = 2
while len(num_prim) < 1000:
    if es_primo(i) == True:
        num_prim.append(i)
    i += 1

#Punto 2
j = 0
while j < 10:
    print(num_prim[j])
    j += 1

#Punto 3
x = range(1000)
plt.plot(x, num_prim)
