#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-10, 10,  10)
z = np.linspace(-10,10, 10)

# X,Y = np.meshgrid(X,Y)
plt.plot(x, -x + (-0.5)*z + 0.5 )
plt.plot(x, 0.75*x- 0*z + 1.75)
plt.plot(x, 1.6*x + 0.4*z -2.4)
plt.plot(x, 2*x - 5*z -7)
# не уверена, что так можно  4 уравнение выражать
plt.plot(x, -2.75*x - 1.75 * z + 3.75)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()





A = np.array([[1,2,-1], [3,-4,0],[8,-5,2],[2,0,-5],[11,4,-7]],float)
B = np.array([1,7,12,7,15])
np.linalg.lstsq(A,B)


# In[ ]:




