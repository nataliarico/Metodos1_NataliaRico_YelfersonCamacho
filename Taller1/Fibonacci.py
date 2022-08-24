# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:35:34 2022

@author: LENOVO 4
"""
import matplotlib.pyplot as plt
from sympy.series.limits import limit
from sympy.core.numbers import (Rational, oo, pi)
from sympy.core.symbol import Symbol

fib = [0,1]
#Punto 1
def fibo(n):
    for i in range (2, n):
        fib.append(fib[i-1]+fib[i-2])
    return fib
fibo(20)

#Punto 2
plt.plot(fib, 'bo')
plt.show()
        
#Punto 3
x = Symbol('x')
assert limit(fibo((x+1))/fibo(x), x, oo)
