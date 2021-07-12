#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


x = np.linspace(-2,3,201)
plt.plot(x, np.exp(x) + x*(2 -x**2) - 1)


plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show



def equation(x):
    return (np.exp(x)  + x *(2 -x**2) - 1)

x1 = fsolve(equation, -2)
print(x1)

x2 = fsolve(equation, 2)
print(x2)


x3 = fsolve(equation, .1)
print(x2)



# In[35]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


x = np.linspace(-2,3,201)
plt.plot(x, (np.exp(x) -1)/x + 1)
plt.plot(x,x**2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-10,10)
plt.grid(True)
plt.show

from scipy.optimize import fsolve

def equations(p):
    x,y = p
    return (y - x**2 + 1, np.exp(x)  + x - x*y - 1)

x1, y1 = fsolve(equations, (-2,1))
print(x1,y1)

x2, y2 = fsolve(equations, (2,2))
print(x2,y2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




