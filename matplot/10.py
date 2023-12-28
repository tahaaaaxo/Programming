import matplotlib.pyplot as plt 
import numpy as np 

x=np.array(["A","B","C","D"])
y=np.array([5,3,2,6])

plt.bar(x,y,width=0.4)
plt.show()

# plt.barh(x, y, height = 0.1)
# plt.show()