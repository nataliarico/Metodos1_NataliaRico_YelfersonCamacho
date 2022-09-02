import numpy as np
import matplotlib.pyplot as plt


intervalo = np.linspace(-10,10)
h = lambda x: 1/(sqrt(1+ np.exp(-x^2)))

def derivative(f,a,h=0.05):
  return (f(a + h) - f(a))/h

derivative(h, intervalo)







  


