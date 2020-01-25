import math


def func(X):
    return 3 * X + math.sin(X) - math.exp(X)
def derivfun(X):
    return 3  + math.cos(X) - math.exp(X)

def newton(a,b) :
    if (func(a) * func(b) < 0):
        m = (a + b) / 2
    else:
        print("No Root in here.")
    while (derivfun(m) > 0):
        h=func(m)/derivfun(m)
        if(h==0.0):
            break
        m=m-h
    print("Root : ", "%.8f" % m)

a=0
b=0.5
newton(a,b)
