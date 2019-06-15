from modinv import *
from sieve  import *

def power(a,b,c) :
    if(b<0) :
        a=inv(a,c)
        b=abs(b)
    i=optimize(a,b,c)

    return optimize(a,b/i,c)* optimize(a,b%i,c)

def optimize(a,b,c) :
    p=1
    for i in range(b) :
        p=p*a
    return p%c


