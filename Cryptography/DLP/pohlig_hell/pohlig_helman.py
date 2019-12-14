#!/usr/bin/env python3

from Crypto.Util.number import *
from gmpy2 import *
from sympy.ntheory import factorint



def babygiant(g,p,y) :
    d={}
    m = iroot(p-1,2)[0]
    for j in range(m) :
        d[pow(g,j,p)] = j
    i=0
    while(i*m < p-1) :
        tmp = inverse(i*m,p)
        sol = pow(y*pow(g,tmp,p),1,p)
        if sol in d.keys() :
            x = i*m+d[sol]
            return(x)
            break
        i=i+1

def pohlig_hellman(g,h,p,ql,cl) :
    ginv = inverse(g,p)
    X=[]
    N=[]
    for q,e in zip(ql,cl) :
        x=0
        a=0
        for i in range(e) :
            _h = pow(h*pow(ginv,a,p),1,p)
            a = babygiant(pow(g,pow(q,e-1)),p,pow(_h,pow(q,e-1)))
            x+=a* q**i
        X.append(x)
        N.append(q**e)
    return crt(X,N)

def pohlig_p2(g,h,p,e) :
    
    if 2**e != p-1 :
        print ("Invalid case")
        return
    k=e
    a=0
    s=""
    for i in range(1,e+1) :
        
        gin =pow(h*pow(inverse(g,p),a,p),1,p)
        _h = pow(gin,2**(k-i),p)
        print(_h)
        if _h == 1 : 
            s="0"+s
            a=int(s,2)
        elif _h == p-1 : 
            s="1"+s
            a=int(s,2)
        else :
            print("Some error")
            return
    x = int(s,2)
    return x

def brute_dlp(g, y, p):
    mod_size = len(bin(p-1)[2:])
    sol = pow(g, 2, p)
    if y == 1:
        return 0
    if y == g:
        return 1
    if sol == y:
        return y
    i = 3
    while i <= p-1:
        sol = sol*g % p
        if sol == y:
            return i
        i += 1
    return None

