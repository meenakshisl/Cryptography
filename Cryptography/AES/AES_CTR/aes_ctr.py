import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

nonce=get_random_bytes(8)
key=os.urandom(16)


def pad(m) :
    tmp=16-len(m)%16
    return m + chr(tmp)*tmp



def unpad(m) :
        return m[:-ord(m[-1])]


def encrypt_CTR(m) :

    ctr=Counter.new(64,prefix=nonce)

    cipher=AES.new(key,AES.MODE_CTR,counter=ctr)
    ct=cipher.encrypt(pad(m)).encode('hex')
    
    return ct



def decrypt_CTR(ct) :

    ctr=Counter.new(64,prefix=nonce)
    
    cipher=AES.new(key,AES.MODE_CTR,counter=ctr)
    pt=cipher.decrypt(ct.decode('hex'))

    return pt



