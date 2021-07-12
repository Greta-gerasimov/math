#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import decimal
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
xmin = -20
xmax = 20
dx = 0.1

xlist = np.around(np.arange (xmin, xmax, dx), decimals = 4)
ylist = 1/xlist

plt.plot(xlist,ylist)
plt.show


# In[ ]:





# In[ ]:





# In[ ]:




