#!/usr/bin/env python
# coding: utf-8

# # Importamos librerias 
# El presente documento da los ángulos con errores menores al 3% respecto al seno para un péndulo simple.
# 
# Primero importamos librerias.

# In[1]:


import numpy as np
import math as mt


# Valores fijos que necesitaremos para hallar los ángulos.

# In[2]:


theta=0.01
T=0
v=[]


# Creamos una función utilizando el ciclo 'for' 

# In[3]:


for i in range (0,10,1):
    a = mt.sin(theta)/theta
    e=1-a #error
    por= e*100 #Porcentaje de error
    if(0.97<= a<=1): #como se requiere un error máximo de 3% concluimos que el valor debe estar entre 0.97 y 1
            T=(theta*180)/np.pi #Convertimos de radianes a grados
            print(" '{}' '{}' '{}' '{}%'".format(a,theta,T,por))
            v.append(theta) #creamos como resultado una lista 
    theta+=0.05 
