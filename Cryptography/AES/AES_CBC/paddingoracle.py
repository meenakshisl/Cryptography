from Crypto.Cipher import AES
from itertools import *
import os,sys
import random


l=["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
"MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
"MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
"MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
"MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
"MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
"MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
"MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
"MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
"MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]

key=os.urandom(16)

def xor(a,b) :
#---------xors a and b------------------------------------------------------------------------
    return ''.join(chr(ord(i)^ord(j)) for i,j in izip(a,cycle(b)))

def pad(m) :
#---------pads the string passed as parameter with pkcs7 standards
    tmp=16-len(m)%16
    return m+chr(tmp)*tmp

def unpad(m) :
#------unpads the message passed as parameter after checking for the padding first------------
    r=checkpad(m)
    try :
        assert r==0
        ch=ord(m[-1])
    #    print ch
        return m[:-ch]
    except :
        return r

def checkpad(m) :
#------checks padding ; returns 0 for correct padding and -1 in all other cases---------------
    ch=ord(m[-1])
    if ch<1 or ch>16 :
        #print "Incorrect padding"
        return -1
    for i in range(ch) :
        if m[(-i-1)]!=chr(ch) :
            return -1
    return 0


def Encrypt() :
#----------selects a random string from l and encrypts it in  AES-CBC mode-----------------------    
    c=random.randint(0,9)
    s=l[c].decode('base64')
    iv=os.urandom(16)
    obj=AES.new(key,AES.MODE_CBC,iv)
    return iv+obj.encrypt(pad(s))


def Decrypt(m) :
#---------decrypts the string passed as argument and returns the decrypted string---------------
    iv,cipher=m[:16],m[16:]
    obj=AES.new(key,AES.MODE_CBC,iv)
    return unpad(obj.decrypt(cipher))

if __name__ == "__main__" :

    c=Encrypt()
    
    b=len(c)/16
    Df=""
    #------loop to decrypt the entire block----------------
    for k in range((b-2)*16,-1,-16) :
        D=""
    #----loop to decrypt each block------------------------
        for i in range(16) :
    #----loop to decrypt each character---------------------
            for j in range(256) :
                mc='\x00'*(16-i-1) + chr(j) + xor(D,chr(i+1))  #---------mc is the crafter cipher text---------------
                print("xor.. : " ,xor(D,chr(i+1))
                #assert len(mc) == 16

                C=c[:k]+mc+c[k+16:k+32]   
#---------mc is being passed as the second last block-
                if Decrypt(C) != -1 :                      
#---------enters the if condition only if padding is correct
                    
                    D=xor(chr(j),chr(i+1)) + D
                    break
        Df=D+Df

    print xor(Df,c[:-16])    


