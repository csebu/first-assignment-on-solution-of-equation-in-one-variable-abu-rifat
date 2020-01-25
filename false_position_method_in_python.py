import math


def func(X):
    return 3 * X + math.sin(X) - math.exp(X)

def false(a,b):
    while(abs(b-a)>0):
       if (func(a)*func(b)<0):
           m=((a*func(b))-(b*func(a)))/(func(b)-func(a))
       if (func(m) == 0.0):
           break
       elif (func(a) * func(m)) < 0:
           b = m
       else:
           a = m
    print("Root : ", "%.8f" % m)
a=0
b=1
false(a,b)
