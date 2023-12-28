from numpy import random

x = random.randint(100, size=115)
print(x, "\n", random.choice(x, size=(3, 2)))
