#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as mplt
import numpy as np
import sympy as sym
import os.path as path
import pandas as pd
import wget


# In[2]:


file='InterpolacionNewtonNoequi'
url='https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    Path_ = file


# In[4]:


Data = pd.read_csv(Path_,sep=',')
X = np.float64(Data['X'])
Y = np.float64(Data['Y']) 


# In[22]:


Diff = np.zeros((len(X),len(Y)))
Diff[:,0] = Y

for i in range(1,len(X)):
    for j in range(i,len(Y)):
        Diff[j,i] = Diff[j,i-1]-Diff[j-1,i-1]/(X[j]-X[j-i])


# In[15]:


def NewtonGregory(X,Y,x):
    
    Sum = Y[0]
    
    Diff = np.zeros((len(X),len(Y)))
    Diff[:,0] = Y

    for i in range(1,len(X)):
        for j in range(i,len(Y)):
            Diff[j,i] = Diff[j,i-1]-Diff[j-1,i-1]
            Diff[j,i] = Diff[j,i]/(X[j]-X[j-i])
        


        poly=1.0
        for h in range(0,i):
            poly*=(x-X[h])
        
            
        Sum += poly*(Diff[i,i])
        
    
    return Sum,np.round(Diff,2)


# In[16]:


x = np.linspace(np.min(X),np.max(X),100)
y,_=NewtonGregory(X,Y,x)


# In[17]:


plt.scatter(X,Y,color='r')
plt.plot(x,y)


# In[20]:


x = sym.Symbol('x',Real='True')
y,_ = NewtonGregory(X,Y,x)
y


# In[21]:


y.simplify()


# In[ ]:




