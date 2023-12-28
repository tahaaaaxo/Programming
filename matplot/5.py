import matplotlib.pyplot as plt
import numpy as np 

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(3,3,9)
plt.plot(x,y)
plt.title("SALES")

x = np.array([0, 1, 4, 3])
y = np.array([1, 3, 1, 9])

plt.subplot(3,3,8)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
