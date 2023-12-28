import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 200, 310, 320, 330])

plt.plot(x,y)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'times','color':'darkred','size':15}

plt.title("testing Title",fontdict=font1, loc="left")
plt.xlabel("x axis",fontdict=font2)
plt.ylabel("y axis")

plt.grid(color="green",linestyle="--",linewidth=1.2)

plt.show()

