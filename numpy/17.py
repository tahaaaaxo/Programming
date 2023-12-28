import numpy as np

arr = np.arange(1, 1000000)

print(arr, np.cumprod(arr))
# print(np.lcm.reduce(arr))
