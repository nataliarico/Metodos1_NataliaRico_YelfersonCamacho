import numpy as np

#Construir matrices:
A= np.array([[1,0,0],[5.,1.,0.],[-2,3,1]])
B= np.array([[4,-2,1],[0.,3.,7.],[0,0,2]])

#Utilizando el método de Jacobi se puede calcular la multiplicación entre dos matrices. (Usando el código realizado en clase)

def GetJacobi(A,B,h=1e-6):
    
    dim = len(A)
    
    J = np.zeros((dim,dim))
    
    for i in range(dim):
        J[i,0] = (  A[i](B[0]+h,B[1],B[2]) - A[i](B[0]-h,B[1],B[2]) )/(2*h)
        J[i,1] = (  A[i](B[0],B[1]+h,B[2]) - A[i](B[0],B[1]-h,B[2]) )/(2*h)
        J[i,2] = (  A[i](B[0],B[1],B[2]+h) - A[i](B[0],B[1],B[2]-h) )/(2*h)
        
    return J.T
  
  
