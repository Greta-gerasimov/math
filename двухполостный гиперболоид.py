#!/usr/bin/env python
# coding: utf-8

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-100,100, 0.5)
Y = np.arange(-100, 100, 0.5)
X,Y = np.meshgrid(X,Y)
Z = X**2 - Y**2
ax.plot_wireframe(X, Y, Z,color = 'y')
show()


# In[ ]:





# In[ ]:





# In[ ]:




