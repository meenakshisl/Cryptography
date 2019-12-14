#!/usr/bin/python3

from Crypto.Util.number import *
import random
import os

class PublicKey :

    def __init__(self,g,p,q,h) :
        self.g = g
        self.p = p
        self.h = h
        self.q = q
class PrivateKey :

    def __init__(self,x,g,p,q) :
        self.x = x
        self.g = g
        self.p = p
        self.q = q


def genkey(bitlength) :
    p = getPrime(bitlength)
    q = p-1
    g = 5
    x = random.randint(2,p-2)
    h = pow(g,x,p)
    return (PrivateKey(x,g,p,q),PublicKey(g,p,q,h))


def encrypt(message,pub) :
    h = pub.h
    g = pub.g
    p = pub.p
    y  =random.randint(2,p-2)
    m = bytes_to_long(message)
    c1 = pow(g,y,p)
    s = pow(h,y,p)
    c2 = pow(m*s,1,p)
    return (c1,c2)

def decrypt(cipher,priv) :
    c1,c2 = cipher
    x = priv.x
    p = priv.p
    g = priv.g
    s = pow(c1,x,p)
    sinv = inverse(s,p)
    m = pow(sinv*c2,1,p)
    return long_to_bytes(m)

if __name__ == "__main__" :
    priv,pub = genkey(140)
    message = os.urandom(16)
    try : 
        assert decrypt(encrypt(message,pub),priv) == message
        print("All check")
    except :
        print("Error in code")

