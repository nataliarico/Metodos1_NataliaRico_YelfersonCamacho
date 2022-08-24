# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:35:34 2022

@author: LENOVO 4
"""
import matplotlib.pyplot as plt

fib = [0,1]
def fibo(n: int):
    for i in range (2, n):
        fib.append(fib[i-1]+fib[i-2])
    return fib
suc = fibo(20)

plt.plot(suc)
plt.show()
        

