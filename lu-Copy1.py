#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg

A = np.array([[1,2,3],
             [2,16,21],
             [4,28,73]])
print(A)


# In[3]:


P,L,U = scipy.linalg.lu(A)
print(P)
print(U)
print(L)

print(np.dot(P,A) - np.dot(L,U))


# In[ ]:




