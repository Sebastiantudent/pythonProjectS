import sys as system
def zad1():

    zdanie = input("wprowadź zdanie: ")
    liczba = len(zdanie)
    print(f"liczba słów wynosi: {liczba}")


def zad2():
    a = int(input("wpisz dowolną liczbę: "))
    b = int(input("wpisz dowolną liczbę: "))
    c = int(input("wpisz dowolną liczbę: "))
    x=a^b+c
    return x

def zad3():
    system.stdout.write("wpisz napis: ")
    napis=system.stdin.readline()
    napis2=napis
    if napis2==napis:
        print(f"napis {napis} jest palindromem")


def zad4():
    x=int(input("wprowadź liczbę"))
    for i in range(1,x):
        if x%i==0:
            k = i
    if k==1:
        print("k jest liczbą pierwszą")
    else:
        print("k nie jest liczbą pierwszą")


def zad5():
    k=0
    lista=[]
    for i in range(1,1001):
        for j in range(1,i):
            if i%j==0:
                k+=j
                if k==j & i%k==0:
                    lista.append(k)

def zad6():
    lista2=[]
    lista=[1,4,3.0,2.0,2.5]
    for i in lista:
        j=i**2
        lista2.append(j)
    print(lista2)

def zad7():

    list=[]
    for i in range(1,11):
        k=int(input("wprowadź liczbę :"))
        if k%2==0:
            list.append(k)
    return list
def zad8():
    slownik={}
    lista=[2,"k","j","tw",5,2,3,4,"j",1]
    j=1
    #for i in lista:
        #slownik[i]=














def main():


    print(zad1())
    #print(zad2())
    #print(zad6())
    #print(zad5())
    #print(zad4())
    #print(zad7())




main()
