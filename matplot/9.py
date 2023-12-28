import matplotlib.pyplot as plt 
import numpy as np 
from numpy import random

x=np.array(random.randint(100,size=100))
y=np.array(random.randint(100,size=100))
colors=np.array(random.randint(100,size=100))
sizes=10*np.array(random.randint(100,size=100))
plt.ylabel("y-axis")
plt.xlabel("x-axis")

plt.title("Title of the graph")

plt.scatter(x,y,c=colors,s=sizes,alpha=0.6,cmap="nipy_spectral")
plt.colorbar()
plt.show()


