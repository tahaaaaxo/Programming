from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=(2, 3))
print(x)


x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

sns.distplot(random.normal(size=100), hist=False)
plt.show()
