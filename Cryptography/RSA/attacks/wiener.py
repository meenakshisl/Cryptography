#bash

from sage.all import *
from Crypto.Util.number import *

def wiener(e,n,C) :
    c=(e/n).continued_fraction()
    for i in c.convergents() :
        k=numerator(i)
        d=denominator(i)
        if(k==0):
            continue
        phi=(e*d-1)/k
        if(d%2!=0 and phi.is_integer()) :
            b=(n-phi+1)
            D=((b**2) - 4*n)
            if(D>0) :
                p= (b+sqrt(D))/2
                q= (b-sqrt(D))/2
                if(p.is_integer() and q.is_integer()) :
                    d=inverse_mod(e,phi)
                    m=long(pow(C,d,n))
                    print long_to_bytes(m)
                    return d

