import numpy as np

#Sistema de ecuaciones visto en clase
a = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])

#Utilizando el ejemplo de clase como guía
def Gaus_Seide(self):
  x = np.zeros(self.col_a)
  sum = x.copy()
  x= a
  it = 0
  residuo = np.linalg.norm(self.b - np.dot(self.A,x))
  while ( residuo > error and it < itmax ):
    it += 1
    for i in range(a):
      sum = 0
      for j in range(a): #Este segundo for es para que se pueda hacer una iteración interna 
        if i != j:
          sum += A[i][j]*x[j]
        sumk[i] = sum
          
    residuo = np.linalg.norm( b - np.dot(A,x) )
        
    return x,it,residuo
  
  
