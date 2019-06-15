#Cryptopals set 2 challenge 12


import base64
from Crypto.Cipher import AES
import os
key=os.urandom(16)
import string

unknown="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
out=""

def pad(m):
        tmp=16-len(m)%16
        return m+chr(tmp)*tmp

def unpad(c):
    assert check_pad(c)==0
    return c[:-ord(c[-1])]

def check_pad(m) :
    if (ord(m[-1])<0) or (ord(m[-1])>=16):
        print "Padding incorrect"
        return -1
    for i in range(ord(m[-1])) :
        if m[-i-1]!=m[-1] :
            return -1
    return 0


def blocksize() :
    i=0
    m="A"*i
    flag=0
    l=0
    l0=len(encrypt_ECB("A"))
    while(flag==0) :
        i=i+1
        m="A"*i
        l=len(encrypt_ECB(m))
        if(l==l0+len(m)):
            flag=flag+1

    return len(m)

def encrypt_ECB(m) :
    aes=AES.new(key,AES.MODE_ECB)
    return aes.encrypt(pad(m+unknown.decode('base64')))

def modedetect() :

    l=blocksize()
    print l
    m="A"*l
    if encrypt_ECB(m) in encrypt_ECB(m*2) :
        return "ECB"
    else :
        return "CBC"


def byte_at_a_time() :

    l=blocksize()
    out=""
    s=""
    #for block-0
    for i in range(l) :
        m="A"*(l-i-1)
        for j in range(256) :
            s=chr(j)
            if(encrypt_ECB(m)[:l]==encrypt_ECB(m + out+s)[:l]) :
                out=out+s
                break

    nb=(len(encrypt_ECB("A"))-l)/l

    #for block-1 to block-nb

    for k in range(1,nb+1,1) :
        
        for i in range(l) :
            
            m="A"*(l-i-1)
            for j in range(256):
                s=chr(j)
                if(encrypt_ECB(m)[((k*l)):(k+1)*l]==encrypt_ECB(out[(k-1)*l+i+1 :]+s)[:l]) :
                    
                    out=out+s
                    break
    print len(out)
    return out

if __name__ =="__main__" :

    print modedetect()
    print byte_at_a_time()



