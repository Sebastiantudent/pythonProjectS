import math
import random
def zad1():
    x=round((math.e**4 - math.log2(34))**(1/3),2)
    y=round((math.log10(20)+math.cos(45)+math.e)**(1/3),2)
    z=round((math.log(20,3)+math.sin(45)*(5/8))**(1/4),2)
    t=round(math.log(23,3)+(math.sin(34)+5)**(1/3),2)
    u=round((math.log2(32)+math.pi+math.sin(56))**(1/4),2)
    print(x, y, z, t, u)
def zad2():
    n=int(input("Wprowadź liczbę nie wiekszą niż 10: \n"))
    A="A"
    if(n<=10):
        for i in range(1,n+1):
            B=A*i
            print(B)
    else:
        print("liczba jest wieksza od 10!!")
def zad3():
    n=int(input("Wprowadź liczbę nie wiekszą niż 10: \n"))
    A="A"
    B=" "
    k=n
    if(n<=10):
        for i in range(1,n+1,2):
            B=k*" "+A*i
            print(f"{B}")
            k-=1

    else:
        print("liczba jest wieksza od 10!!")

def zad5():
    suma=0
    lista=[]
    n=int(input("podaj liczbe wierszy i kolumn: "))
    for i in range(1,n+1):
        for j in range(1,n+1):
            lista.append(random.randint(1,100))
        for l in lista:
            suma = suma + l
        print(f"{lista}={suma}")
        suma=0
        lista=[]
def zad5_2():
    suma=0
    lista=[]
    n=int(input("podaj liczbe wierszy i kolumn: "))
    for i in range(1,n+1):
        for j in range(1,n+1):
            lista.append(random.randint(1, 100))
            for l in lista:
                if(len(lista)==n):
                    suma+=l
                    print(f'suma wiersza={suma}')
                    suma=0
                    break
                else:
                    suma +=l
                    break
    print(f"{lista}")













def main():


    zad1()
    #zad2()
    #zad3()
    zad5_2()






main()