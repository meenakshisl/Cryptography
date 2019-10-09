import random
from Crypto.Util.number import *
import gmpy2
from Crypto.PublicKey import RSA





def attack(c1,e1,c2,e2,n) :
    """ This function is used to decipher a message when the same message is sent by someone to two people but use the same modulus .One had in hand only the public key parameters and the cipher text :

    attack(c1,e1,c2,e2,n) :
        c1,c2 - ciphertext 1 and 2
        e1,e2 - public key parameters 1 and 2
        n     - the common modulus \n """
    l=egcd(e1,e2)
    d={max(e1,e2) : l[1] , min(e1,e2) : l[2]}
    if l[0]==0 :
        print("Cant be attacked viz this method")
    else :
        if d[e1] < 0 :
            c1,c2=c2,c1
            e1,e2=e2,e1
            u=l[2]
            v=l[1]
        else :
            u=l[1]
            v=l[2]

        c2_inv=inverse(c2,n)
        m=pow((pow(c1,u,n)*pow(c2_inv,abs(v),n)),1,n)
    
    return long_to_bytes(m)







def egcd(a,b) :
    ro=max(a,b)
    r=min(a,b)
    so=1
    s=0
    to=0
    t=1
    while r!=0 :
        q=ro/r
        ro,r = r , ro%r
        so,s = s,so - q*s
        to,t = t,to - q*t
    
    return ro,so,to

def _test_() :
    M="This is the sample test case"
    p=getPrime(512)
    q=getPrime(512)
    phi=(p-1)*(q-1)
    n=p*q
    m=(M)
    e1=pow(2,random.randint(15,17))+1
    e2=pow(2,random.randint(15,17))+1
    while(e1!=e2) :
        e2=pow(2,random.randint(15,17))+1
    
    c1=pow(m,e1,n)
    c2=pow(m,e2,n)

    print(attack(c1,e1,c2,e2,n))

if __name__ == "__main__" :
    _test_()
