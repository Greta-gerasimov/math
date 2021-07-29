#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
A = np.array([[1,2,3],[4,0,6],[7,8,9]])
B = np.array([2,5,1])
np.linalg.solve(A,B)
A1 = np.linalg.inv(A)
print(A1)
print('det=',np.linalg.det(A))
np.dot(A1,B)


# In[ ]:





# In[ ]:




