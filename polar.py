#!/usr/bin/env python
# coding: utf-8

# In[4]:



import numpy as np
import matplotlib.pyplot as plt
phi = np.linspace(0,5*np.pi)
rho= 20
x = rho*np.cos(phi)
y = rho*np.sin(phi)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[9]:




def xy2pol(x,y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(x,y)*180/np.pi
    return(rho, phi)

t = np.linspace(0,np.pi,1000)
x = np.cos(t)
y = np.sin(t)
rho,phi = xy2pol(x,y)
plt.polar(phi,rho)


# In[11]:


def xy2pol(x,y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(x,y)*180/np.pi
    return(rho, phi)

t = np.linspace(0,np.pi,1000)
x = np.sin(t)
y = np.sin(t)
rho,phi = xy2pol(x,y)
plt.polar(phi,rho)


# In[ ]:




