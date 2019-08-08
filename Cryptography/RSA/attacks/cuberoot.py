from Crypto.Util.number import *

import gmpy

def cubeattack(n,c,e=3) :
    i=0
    m=gmpy.root(i*n+c,3)
    while(m[1]!=1) :
        m=gmpy.root(i*n + c,3)
        i=i+1
    return (int(m[0]))

