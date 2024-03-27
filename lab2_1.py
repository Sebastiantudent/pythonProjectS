import numpy as np

def zad1():
    tablica = np.arange(15)*3
    return tablica

def zad2():
    lista1=np.arange(2,dtype=float)
    print(lista1.dtype)
    lista2=lista1.astype("int64")
    print(lista2.dtype)

def zad3(n):
    t=np.array(n*([np.arange(1,n+1)]))
    print(t)

def zad4(n,k):
    m=np.logspace(1,k,k,base=n,dtype="int64")
    print(m)

def zad5(n):
    mat_diag=np.diag([a for a in range(n,0,-1)])
    print(mat_diag)

def zad6():
    marcin=b'Marcin'
    Mar=marcin.lower()[::-1]
    nazwa=np.frombuffer(marcin,dtype="S1")
    print(nazwa)

def zad7(n):
    mat_diag = np.diag([2 for a in range(n)])
    k=1
    for i in range(2,n+1):
        mat_2 = np.diag([2*i for j in range((n+1)-i)],-k)
        mat_3 = np.diag([2*i for j in range((n+1)-i)],k)
        k+=1
        mat_diag+=mat_2+mat_3
    print(mat_diag)



def zad9():
    a=0
    mat_fib=np.zeros((5,5),dtype="int64")
    for i in range(0,25):
        a=i
        mat_fib+=a


    print(mat_fib)












def main():

    #n = int(input("wprowadź liczbę całkowitą: "))
    #k = int(input("wprowadź liczbę całkowitą: "))
    #print(zad1())
    #zad2()
    #zad3(n)
    #zad4(n,k)
    #zad5(n)
    #zad6()
    #zad7(n)
    zad9()



if __name__ == '__main__':
    main()