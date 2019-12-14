from Crypto.Util.number import *
from gmpy import *
import random

def F(x,g,h,p) :
    if x%3 == 2 :
        return h*x%p
    elif x%3 == 0 :
        return x**2 %p
    else :
        return x*g %p


def G(x,a,n) :
    if x%3 == 2 : 
        return a%n
    elif x%3 == 0 :
        return 2*a %n
    else : 
        return (a+1) %n


def H(x,b,n) :
    if x%3 == 2 : 
        return (b+1)%n
    elif x%3 == 0 :
        return 2*b %n
    else : 
        return b%n


def pollard_rho(g,h,p,n) :
    if(is_prime(n)==0) :
        print"Pollard rho cannot be applied"
        return -1
    
    a1=0
    a2=0
    b1=0
    b2=0
    x1 = 1
    x2 = 1
    i=1
    
    while(i<=n) :
        
        #x1 = F(x1,g,h,p)
        a1 = G(x1,a1,n)
        b1 = H(x1,b1,n)
        x1 = F(x1,g,h,p)
        
        #x2 = F(F(x2,g,h,p),g,h,p)
        a2 = G(F(x2,g,h,p),G(x2,a2,n),n)
        b2 = H(F(x2,g,h,p),H(x2,b2,n),n)
        x2 = F(F(x2,g,h,p),g,h,p)
        
        if (x1==x2) :
            r = (b1 - b2)%n
            
            if(r==0) : 
                print "bs are equal"
                return -1
            else :
                gcd = GCD(r,n)
                if gcd < 10 :
                    return (inverse(r,n)*(a2-a1))%n
        else :
            i=i+1

if __name__ == "__main__" :
    num = random.randint(3,381)
    y = pow(2,num,383)
    assert pow(2,pollard_rho(2,y,383,191),383) == y

