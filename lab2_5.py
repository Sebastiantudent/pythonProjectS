import pandas as pd
import numpy as np
import openpyxl as xl
# zad1
xlsx = pd.ExcelFile('imiona.xlsx')
zad =pd.read_excel(xlsx,header=0)
# imiona.to_excel('imiona.xlsx',sheet_name="Zadanie 1")
print(zad)
# zad2
#print(zad)
#print(zad[zad.Liczba > 1000])
#print(zad[zad['Imie']=='SEBASTIAN'])
#print(zad.Liczba.dtype)
#print(sum(zad.Liczba))
#print(sum(zad.Liczba[(zad["Rok"] >= 2000) & (zad['Rok'] <= 2005)]))
#print(sum(zad.Liczba[zad['Rok']<2006]))
#print(zad.groupby(['Rok','Plec']).agg({'Imie':['max']}))







#path = "imiona.xlsx"
#wb_obj = xl.load_workbook(path)
#sheet = wb_obj.active
#cell=sheet.cell(row=1, column=1)
#print(cell.value)












