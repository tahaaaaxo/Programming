
import time
import numpy as np

x = time.time()
# print(x)

arr1 = np.array([3999991, 28543985932539, 3, 4])
arr2 = np.array([174923749237492, 1048923850345392, 3, 4])
arr3 = np.power(arr1, arr2)
print("power", arr3)
print("product: ", np.prod(arr3))

y = time.time()
print(f"time taken : {y-x}")
