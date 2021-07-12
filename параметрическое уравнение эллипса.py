#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
from math import pi

get_ipython().run_line_magic('matplotlib', 'inline')

u = 1. #x в центре
v = 0.5 #y в центре
a = 2.  #радиус по оси x
b = 1.5 #радиус по оси y

m = np.linspace(0, 2*pi, 100)
plt.plot(u + a*np.cos(m), v + b*np.sin(m))
plt.show()


# In[ ]:




