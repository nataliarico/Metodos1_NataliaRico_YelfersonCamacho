import numpy as np
import matplotlib.pyplot as plt

#Utilizando un código similar al del punto 1, el cual fue basado en las notas de clase se tiene que:

A = np.array([[3,1,0,1],[1,2,1,1],[-1,0,2,-1]])

def diagonal(A):
  A_t = A.copy().astype(float)
  n = A_t.shape[0]
  for i in range(n - 1, -1):
    for j in range(i - 1, -1):
      A_t[j] = (A_t[j, i]/A_t[i, i]) * A_t[i] - A_t[j]

    A_t[i] = A_t[i] / A_t[i, i]
  return A_t

AT = diagonal(A)
b = np.array([[-3,-3,8,9]])
x = AT* b
#ortogonal
solucion = AT*x

#Grand-Schmidt
def GrandSchmidt(A):
  u= A.shape[0]
  v= A.shape[1]
  for k in range(1,u):
    u[k]=v[k]
    for j in range(len(k)):
      u[k]= v[k] - ((v[k]*u[j])/(u[j]*u[j]))*u[j] #se aplica la formula 

  return u

