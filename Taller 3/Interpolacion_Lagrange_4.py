#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as mplt
import numpy as np
import sympy as sym
import os.path as path
import pandas as pd
import wget


# In[5]:


file='Parabolico.csv'
url='https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    Path_ = file


# In[6]:


Data = pd.read_csv(Path_,sep=',')
X = np.float64(Data['X'])
Y = np.float64(Data['Y']) 


# In[9]:


from scipy.interpolate import lagrange

def coeficientesinterpolacionlagrange(x, y):
    a = lagrange(x, y)
    b = []
    for i in a:
        b.append(i)
    print("Los coeficientes de lagrange(ordenados desde el mayor grado)")
    print(" ")
    return b


# In[13]:


coeficientes=coeficientesinterpolacionlagrange(X,Y)
print(coeficientes)


# Tenemos la ecuación cartesiana del tiro parabolico
# 
# $$y=xtan(\theta)-\frac{gx^2}{2(v_0cos(\theta))^2}$$
# 
# De aquí se puede demostrar que si el polinomio interpolador es:
# 
# $$y=ax+bx^2$$
# 
# Entonces
# 
# $$\theta=arctan(a) \ y$$
# 
# $$v_0=\frac{1}{cos(\theta)} \sqrt{\frac{g}{-2b}}$$

# In[24]:


theta=np.arctan(coeficientes[1])
v0=(1/np.cos(theta))*np.sqrt(9.8/(-2*coeficientes[0]))
print("La velocidad inicial es: "+str( round(v0) )+" m/s (Suponemos que los datos de X y Y estan en metros)")
print("")
print("El angulo inicial es:"+str( round(theta*180/3.14) )+" °")


# In[ ]:





# In[ ]:





# In[ ]:




