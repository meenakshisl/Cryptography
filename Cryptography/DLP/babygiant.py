#!/usr/bin/env python3

from Crypto.Util.number import *
from gmpy2 import *


def solve(g,p,y) :
    """ solves dlp using baby-step giant step algorithm assuming n is prime :
    Parameters : g,p,y"""
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


if __name__ == "__main__" :
    g,p,y = map(int,input().split(' '))
    print(solve(g,p,y))
