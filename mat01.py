
#Grafico de linhas 

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib import style
#estilos prontos
style.use('ggplot')

X = range(100)
Y = [valor**2 for valor in X]
Z = [valor*20 for valor in X]

plt.title('Placares Brasileirão Série A ')
# Labes 
plt.plot(X,Y,'g--',label = 'Placares') #muda o stilo de linha e cor
plt.plot(Y,X,label = 'Repetições')
plt.plot(Z,Y,label =  'Desvios')
plt.legend()
# estilo de grade personalizado
plt.grid(True,lw = 2, ls = '--')
plt.xlabel('Números')
plt.ylabel('score')
plt.show()