import sys
sys.path.insert(0,'/home/meenakshi/Desktop/bi0s/Crypto/RSA/basics/Task1')

from sieve import *
import math

def phi(n) :
    p=1
    i=2
    for i in range(2,n+1,):
        if n%i==0 and sieve(i)=="Prime" :
            p=p*(i-1)
            n=n/i
            
        while(n%i==0) :
            p*=i
            n=n/i
    return p


if __name__=="__main__" :
    a=input()
    print phi(a)



        
        
