import numpy as np
import matplotlib.pyplot as plt

# Symmetric hard limit transfer function


def symmetric_hard_limit(x):
    return np.where(x >= 0, 1, -1)


# Generate input values
x = np.linspace(-5, 5, 400)

# Calculate outputs using the symmetric hard limit function
y = symmetric_hard_limit(x)

# Plotting the function
plt.figure(figsize=(8, 7))
plt.plot(x, y, label='Symmetric Hard Limit', color='blue')
plt.title('Symmetric Hard Limit Transfer Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x=0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()
plt.show()
