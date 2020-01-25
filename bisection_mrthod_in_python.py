import math

def func(X):
    return 3 * X + math.sin(X) - math.exp(X)

def bisection(a,b):
    while(abs(b-a)>=0):
        m = (a + b) / 2
        if (func(m) == 0.0):
            break
        if(func(a)*func(m))<0:
            b=m
        else:
            a=m
    print("Root : ", "%.8f" % m)
a =0.35
b =0.38
bisection(a, b)