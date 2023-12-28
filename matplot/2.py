import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints,"*:",ms=30,mec="r",mfc="#4CAF50",linewidth=4)
plt.plot(ypoints,"o:")
plt.show()

