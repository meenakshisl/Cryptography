from modinv import *
from phi import *

def power(a,b,c) :
    if(b<0) :
        a=inv(a,c)
        b=abs(b)

    return calc(a,phi(c),c)* calc(a,b-phi(c),c)

def calc(a,b,c) :
    p=1
    for i in range(b) :
        p=p*a
    return p%c


