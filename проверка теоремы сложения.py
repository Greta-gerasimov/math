#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import random
a = ['orel','reshka']
res = []
for i in range(100):
    rnd=random.random()
    if rnd < 0.5:
        res.append(a[0])
    else:
        res.append(a[1])
print(res.count(a[0]), res.count(a[1]))
        


# In[ ]:




