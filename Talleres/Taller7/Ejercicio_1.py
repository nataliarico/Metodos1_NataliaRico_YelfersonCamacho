import numpy as np
import matplotlib.pyplot as plt

# El método mínimos cuadrados dice A'Ax = A'b. Por lo tanto, el punto entre las tres lineas es x.

A = np.array([[2,-1],[1,2],[1,1]])
#Utilizando de guía las notas del repositorio de complementaria:
def triangular(A):
    n = A.shape[0]
    for i in range(n): 
        for j in range(i+1, n): 
            A[j] = ((A[j, i])/A[i, i]) * A[i] - A[j]
    return A
A_t= A
def transpuesta(A_t):
  n = A_t.shape[0]
  for i in range(n - 1, -1):
    for j in range(i - 1, -1):
      A_t[j] = (A_t[j, i]/A_t[i, i]) * A_t[i] - A_t[j]

    A_t[i] = A_t[i] / A_t[i, i]
  return A_t
AT = transpuesta(A_t)[:,-1]

b = np.array([[2,1,4]])
x = AT* b

#Grafica
plt.plot(x)
plt.plot([x[0], x[-1]], 'r', linewidth=3)
plt.show()


h=0.03
X = np.linspace(-5,5)
Y = np.linspace(-5,5)
def min(X,Y):   
    p = 0
    for n in range(len(Y)):
        h += Y[n]*X**n  
    return h

#Grafica
plt.plot(h)
plt.show()
