#!/usr/bin/env python
# coding: utf-8

# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-4, 10, 2)
Y = np.arange(-4, 10, 2)
X,Y = np.meshgrid(X,Y)
Z = 20*X + 6 *Y
ax.plot_wireframe(X, Y, Z,color = 'y')
ax.plot_surface(X + 5, Y + 5, Z + 5, color = 'gray')
show()


# In[ ]:




