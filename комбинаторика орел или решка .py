#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import random
orel = 0
reshka = 0
count = 0
while count != 10:
    coin = random.randint(1,2)
    count +=1
    if coin == 1:
        orel+=1
    elif coin == 2:
        reshka += 1
print('выпадание орла', orel)
print('выпадание решки',reshka)


# In[ ]:




