#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt

def Q(x, y, z):
    return (x**2 + y**2 + z**2)
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X,Y = np.meshgrid(X,Y)
ax.plot_surface(X, Y, Q(X, 10*X - 14, 21*X - 29))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
show()

a = np.array([[1, 2, -1], [4, -2.5, 1]])
b = np.array([[1], [6]])
np.linalg.lstsq(a, b)


# In[ ]:





# In[ ]:




