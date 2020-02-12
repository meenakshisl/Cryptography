from sage.all import *
import random
import os
from hashlib import sha256

class ECC :
    def __init__(self,p,a,b) :
        self.E = EllipticCurve(GF(p),[a,b])
        self.N = self.E.order()
        self.G = self.E.gen(0)

    def keygen(self) :
        private_key = random.randrange(1,self.N)
        public_key = private_key*self.G
        return private_key,public_key
        
    def sign_message(self,dA,message) :
        z = int(sha256(message).hexdigest(),16)
        r=0
        s=0
        while r==0 or s==0 :
            k = random.randrange(1,self.N)
            x,y = (k*self.G).xy()
            r = int(x)
            s = ((((int(z) + int(r)*int(dA))%self.N)*inverse_mod(int(k),self.N)))%self.N

        return (r,s)

    def verify_signature(self,H,message,signature) :
        z = int(sha256(message).hexdigest(),16)
        r,s = signature
        w = inverse_mod(int(s),self.N)
        u1 = (int(w)*z)%self.N
        u2 = (int(w)*r)%self.N
        x,y = (u1*self.G + u2*H).xy()
        if x == r :
            return 'Signature matches'
        else :
            return 'Invalid Signature'


def test() :
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    a=0
    b=7
    E = ECC(p,a,b)
    message = os.urandom(16)
    Alice = E.keygen()
    Bob = E.keygen()
    if E.verify_signature(Alice[1],message,E.sign_message(Alice[0],message)) == 'Signature matches' :
        return 'Test passed'

if __name__ == "__main__" :
    print test()
