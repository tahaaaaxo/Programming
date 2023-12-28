import numpy as np
from numpy import random

arr = np.array([1, 2, 3, 4, 5])
print(arr)
random.shuffle(arr)
print("Shuffled : ", arr)
print("Permutation : ", random.permutation(arr))
