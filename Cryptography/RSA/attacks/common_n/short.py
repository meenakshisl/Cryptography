from gmpy import *

def common_mod(c1,c2,e1,e2,n):
    gcd,u,v = gcdext(e1,e2)
    if u<0:
        k1 = pow(inverse(c1,n),abs(u),n)
    else:
        k1 = pow(c1,u,n)
    if v<0:
        k2 = pow(inverse(c2,n),abs(v),n)
    else:
        k2 = pow(c2,v,n)
    return pow(k1*k2,1,n)

