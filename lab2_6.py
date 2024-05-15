import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# zad1
xlsx = pd.ExcelFile('imiona.xlsx')
zad =pd.read_excel(xlsx,header=0)
grupa=zad.groupby(['Rok']).agg({'Liczba':['sum']})
grupa.plot()
plt.show()

# zad2
grupa2=zad.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa2)
#grupa2=grupa2.cumsum()
wykres = grupa2.plot.bar()
wykres.set_ylabel('')
wykres.set_xlabel('Plec')
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
wykres.set_title('suma liczby chlopcow i dziewczyn')
plt.savefig(fname='imiona.jpg')
plt.show()
# zad3
grupa3=zad[zad['Rok']>2011]
grupa3=grupa3.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa3)
grupa3.plot(kind='pie',subplots=True,autopct='%.2f%%', fontsize=20,figsize=(6.4,4.8),colors=['red','blue'])
#wykres2=grupa3.plot.pie(subplots=True,autopct='%.2f%%', fontsize=20,figsize=(6.4,4.8))
plt.legend(loc='lower right')
plt.title('suma chlopcow do dziewcząt')
plt.show()
# zad4
df=pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
pg=df.groupby(['Sprzedawca']).agg({'zamowienia':['sum']})
print(pg)
wykres3 = pg.plot.bar()
wykres3.set_ylabel('zamowienia')
wykres3.set_xlabel('sprzedawca')
wykres3.tick_params(axis='x', labelrotation=0)
wykres3.legend()
wykres3.set_title('suma zamowien')
plt.savefig(fname='zamowienia.jpg')
plt.show()