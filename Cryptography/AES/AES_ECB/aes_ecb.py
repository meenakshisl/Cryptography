#______________program to encrypt and decrypt in aes-ecb mode ______
import os
from Crypto.Cipher import AES
key=os.urandom(16)

#---------unpads the string passes as argument after checking if padding is correct making use of assert-----
def unpad(ct) :
    assert check_pad(ct,16)=="Ok",check_pad(ct,16)
    ch=ord(ct[-1])
    pt=ct[:-ch]
    return pt

#----------pads the string passed as argument-------------
def pad(pt) :
    tmp=16-(len(pt)%16)
    return pt+chr(tmp)*tmp
    
#---------------------function checks if padding is correct---------------------
def check_pad(ct,bs) :
    ch=ord(ct[-1])

    print ch
    if ch > 16 :
        
        r="Padding incorrect 1"
        return r
    else :
        for i in range(ch) :
            if(ct[(-i-1)]!=chr(ch)) :
                r= "Padding incorrect 2"
            else :
                r="Ok"
    return r

#----------encrypts the string in ecb mode------------------
    
def encrypt_ecb(pt) :

    
    aes=AES.new(key,AES.MODE_ECB)
    ct=pad(pt)
    assert check_pad(ct,16)=="Ok",check_pad(ct,16)
    ct=aes.encrypt(ct)
    print "Encrypted text is : " + ct.encode('hex')
    return ct.encode('hex')

#---------decrypts the string in ecb mode-----------
def decrypt_ecb(ct) :

    aes=AES.new(key,AES.MODE_ECB)
    pt=unpad(aes.decrypt(ct.decode('hex')))
    print "Decrypted cipher text is : " + pt

    return pt

    


