import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr)

for x in np.nditer(arr):
    print(x)


for indx, x in np.ndenumerate(arr):
    print(indx, x)
