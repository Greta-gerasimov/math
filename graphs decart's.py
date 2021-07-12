#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4*np.pi, 3*np.pi,301)
plt.plot(x,2*np.cos(x-np.pi/2)+3)#blue
plt.plot(x,3*np.cos(x-np.pi)+1)#orange
plt.plot(x,3*np.cos(x-1)+4)#green
plt.plot(x,3*np.cos(x-1)+1)#red
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[ ]:




