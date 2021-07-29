#!/usr/bin/env python
# coding: utf-8

# In[52]:


# задание 1.
import numpy as np
import matplotlib.pyplot as plt
A = np.array([[1,2,3],[4,0,6],[7,8,9]])
B = np.array([12,2,1])
np.linalg.solve(A,B)

# print('det=',np.linalg.det(A))


# In[53]:


# задание 3.

import numpy as np
import matplotlib.pyplot as plt
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[2 ,5 , 1]])
print('det=',np.linalg.det(A))



C = np.concatenate((A,B.T), axis = 1)
print(C)

np.linalg.matrix_rank(A, 0.00001), np.linalg.matrix_rank(C, 0.00001)


# In[54]:


#   нет решений


# In[55]:


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[0, 0, 0]])
C = np.concatenate((A,B.T), axis = 1)
print(C)

np.linalg.matrix_rank(A, 0.00001), np.linalg.matrix_rank(C, 0.00001)


# In[50]:


# система имеет решение по теореме кронекера-капелли (совместна)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([0, 0, 0])
np.linalg.solve(A,B)


# In[ ]:





# In[ ]:




