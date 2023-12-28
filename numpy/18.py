import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
print(np.where(x >= 0, 1, -1))
