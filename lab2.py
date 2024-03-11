import math
def zad1():

    A=[i-1 for i in range(1,11)]
    B=[4**i for i in range(0,7)]
    C=[i for i in B if i%2==0]
    print(A)
    print(B)
    print(C)


def zad2():
    lista1=[1,4,23,12,33,5,7,9,2,8]
    lista=[i for i in lista1 if i%2==0]
    print(lista)

def zad3():
    Słownik={'pomidor':'kg','kukurydza':'kg','baton':'sztuki','kawa':'sztuki'}
    lista=[i for i,j in Słownik.items() if j=='sztuki']
    print(lista)

def zad4(a,b,c):
    if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
        print('trójkąt jest prostokątny!')
    else:
        print('trójkąt nie jest prostokątny')

def zad5(a=1,b=1,h=1):
    x=(a+b)*h/2
    return x

def zad6(a=1,b=4,ile=10):
    for i in range(1,ile+1):
        a*=b
    return a
def zad7(x):
    try:
        wynik=math.sqrt(x)
        print(wynik)
    except ValueError:
        print("bez wartości ujemnych!!!")






def main():
    zad1()
    zad2()
    zad3()
    zad4(3,4,5)
    print(f"Pole trapezu wynosi: {zad5()}")
    print(f"iloczyn elementów ciągu wynosi: {zad6(1,2,4)}")
    zad7(-4)








if __name__ == '__main__':
    main()