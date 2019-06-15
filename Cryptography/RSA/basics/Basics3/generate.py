
#!/usr/bin/env python3


from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import fractions

def generate(e=65537) :
    p=getPrime(512)
    q=getPrime(512)
    phi=(p-1)*(q-1)
    while fractions.gcd(e,phi)!=1 :
        p=getPrime(512)
        q=getPrime(512)
        phi=(p-1)*(q-1)
    n=p*q
    d=inverse(e,phi)
    return n,d,p,q,e


