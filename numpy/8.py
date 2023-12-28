import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = [True, False, False, False, True]

new_arr = arr[x]

print(new_arr)


newnewarr = arr > 3

print(newnewarr, arr[newnewarr])
