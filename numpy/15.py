import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

# ------OR---------

x = [1, 2, 3, 4]
y = [499999999999999999, 99999999999995, 6999999999999999999999999999, 799999999999]
z = []
print(np.prod(y))
for i, j in zip(x, y):
    z.append(i + j)
print(z)
