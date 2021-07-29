#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([2,5,11])
Q,R = np.linalg.qr(A)

print(A)
print(B)
print(Q)
print(R)
print(np.dot(Q,R))
print(np.dot(np.transpose(Q),Q))


# In[4]:


R1 = R[:2,:2]
R1


# In[8]:


B1 = np.dot(np.transpose(Q), B)[:2]
B1


# In[9]:


X1 = np.linalg.solve(R1,B1)
X1


# In[11]:


X = np.append(X1,0)
print(X)
np.linalg.norm(X)


# In[ ]:




