#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


from random import randint
 
class Rul:
 
    def __init__(self):
        self.reds = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
        self.blacks = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
 
    def roll(self):
        n = randint(0, 36)
        if n == 0:
            print('zero')
        elif n in self.reds:
            print(n, 'красное')
            red = True
        elif n in self.blacks:
            print(n, 'черное')
            black = True
r = Rul()
print(r.roll())


# In[ ]:





# In[ ]:




