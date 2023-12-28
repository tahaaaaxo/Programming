import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(np.pi)
print(np.__version__)
print(type(arr))

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr[1][1][1])
print(arr.ndim)
