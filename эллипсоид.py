#!/usr/bin/env python
# coding: utf-8

# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
coefs = (8, 5, 7)  # Coefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1 
#почему не прописывается само уравнение?
# Radii corresponding to the coefficients:
rx, ry, rz = 1/np.sqrt(coefs) # нашла в сети такой код. не очень понятно ,
#почему радиус 1/на корень из a,b,c


u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))
ax.plot_wireframe(x, y, z,  rstride=4, cstride=4, color='y')


plt.show()


# In[ ]:




