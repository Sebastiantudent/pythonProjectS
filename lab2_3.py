import numpy as np
import math as m
def zad1():
    a=np.arange(3)
    b=np.arange(3)
    print(a)
    print(b)
    print(a.dot(b))
    print(np.dot(a,b))
    for b in b.flat:
        print(b)

def zad2():
    x=np.arange(3,12).reshape((3,3))
    y=np.arange(3,19).reshape((4,4))
    print(x)
    print(y)
    print(x.min(axis=1))
    print(x.min(axis=0))
    print(y.min(axis=1))
    print(y.min(axis=0))

def zad3():
    a=np.arange(3)
    b=np.arange(3)
    print(a*b)

def zad4():
    a=np.ones(3,dtype="int32")
    print(a.dtype)
    b=np.linspace(0,10,3)
    print(b.dtype)
    print()
    c=np.dot(a,b)
    print(c)
    print(c.dtype)
#zad 5, 6, 7
def zad567():
    x=np.arange(6).reshape(2,3)
    print(x)
    for a in x.flat:
        print(m.sin(a))
    y=np.arange(6).reshape(2,3)
    print(y)
    for b in y.flat:
        print(m.cos(b))
    
def main():

    #zad1()
    #zad2()
    #zad3()
    #zad4()
    zad5()




if __name__ == '__main__':
    main()