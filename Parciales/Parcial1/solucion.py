#C

import numpy as np
import matplotlib.pyplot as plt 

def funcion(x):
    return np.sqrt(np.tan(x))

intervalo = np.linspace(0.1, 1.1, 0.01)

solucion_derivadaprog=[]
for i in intervalo:
    derivada =  (funcion(x+0.01)- funcion(x))/0.01 
    solucion.append(derivada)
    i+1
    
#D
import numpy as np
import matplotlib.pyplot as plt 

def funcion(x):
    return np.sqrt(np.tan(x))

intervalo = np.linspace(0.1, 1.1, 0.01)

solucion_derivadacent=[]
for i in intervalo:
    derivada =  (funcion(x+0.01)- funcion(x-0.01))/(2*0.01) 
    solucion.append(derivada)
    i+1

#E
plt.plot(intervalo, solucion_derivadacent)
plt.plot(intervalo,solucion_derivadaprog)

#F
def error_central(x):
    return np.abs(funcion(x)- solucion_derivadacent(x))
plt.plot(error_central)

def error_progresivo(x):
    return np.abs(funcion(x)- solucion_derivadaprog(x))
plt.plot(error_progresivo)
