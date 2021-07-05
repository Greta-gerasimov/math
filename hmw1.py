import matplotlib as mpl    
mpl.use('Agg')                          
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 21)                   
y1 =cos(1 * x)
y2 =cos(3 * x)

fig, ax = plt.subplots()                      
ax.plot(x, y1, color="blue", label="y(k,x)=cos(k1*x)")  

ax.plot(x, y2, color="yellow",label="y(k,x)=cos(k2*x)")
ax.set_xlabel("x")                              
ax.set_ylabel("y")                          
ax.legend()                                     


fig.savefig('Kate1.png')