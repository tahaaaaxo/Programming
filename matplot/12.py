import matplotlib.pyplot as plt  
import numpy as np                    

x=np.array([35, 25, 25, 15])
label_x=["Apples", "Bananas", "Cherries", "Dates"]
explode_x=[0.1,0,0,0.5]


plt.pie(x,labels=label_x,startangle=90,explode=explode_x,shadow=True)

plt.legend(title="four fruits")
plt.show()

