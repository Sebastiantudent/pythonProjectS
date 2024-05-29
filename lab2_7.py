import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.axis((0,6,0,20))
#plt.axis([0,6,0,20])
#plt.xlim(0,6)
#plt.ylim(0,20)
#plt.xticks([0,2,4,6])

#x=np.arange(-5,6)
#y=x**2

#plt.plot(x,y,label='linia 1/x')
#plt.show()

#plt.plot(y,label='linia 1/x')
#plt.legend()
#plt.show()
# zad 1,2
x=np.arange(1,20)
y=1/x

plt.plot(x,y,'g:>',label='f(x)=1/x')
plt.legend()
plt.show()

#zad 3
x1=np.arange(0,30,0.1)
x2=np.arange(0,30,0.1)
y1=np.sin(x1)
y2=np.cos(x2)
plt.plot(x1,y1,'g',label='f(x)=sin(x)')
plt.plot(x2,y2,label='f(x)=cos(x)')
plt.legend()
plt.show()

#zad 4

#zad 5
xlsx = pd.ExcelFile('imiona.xlsx')
zad =pd.read_excel(xlsx,header=0)
grupa1=zad.groupby(['Plec']).agg({'Liczba':['sum']})
plt.subplots(1,3,1)
plt.title()
plt.bar(heights=grupa1)


