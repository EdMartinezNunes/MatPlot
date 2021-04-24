# grafico de barra 
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

x = (1,5,10,18,20)
y = ('4x0','2x2','1x0','0x0','2x0')

plt.barh(x,y) #plt.bar na vertical
plt.show()