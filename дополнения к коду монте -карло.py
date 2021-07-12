#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from math import *

def fac(n):
    if n == 0:
        return 1
    return fac(n-1)*n
print((fac(20)/(fac(0)*fac(20)))*(0.5**0)*(0.5**20))



# In[ ]:




