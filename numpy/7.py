import numpy as np

arr = np.array([1, 4, 5, 62, 3])

print(np.searchsorted(arr, [4, 3, 1]))
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([True, False, True])

print(np.sort(arr))


arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
