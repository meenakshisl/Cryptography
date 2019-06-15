from Crypto.Cipher import AES
import os
key=os.urandom(16)

#-------------function to pad the string passed as argument-------
def pad(m):
        tmp=16-len(m)%16
        return m+chr(tmp)*tmp
#------------function to unpad the string passed as argument--------
def unpad(c):
    assert check_pad(c)==0
    return c[:-ord(c[-1])]

#-----------function to decrypt in aes cbc mode---------
def decrypt_CBC(c):
    iv=c[:16]
    obj=AES.new(key,AES.MODE_CBC,iv)
    return unpad(obj.decrypt(c[17:]))

#----------function to encrypt in aes cbc mode------------
def encrypt_CBC(m):
    iv=os.urandom(16)
    obj=AES.new(key,AES.MODE_CBC,iv)
    
    return iv+":"+obj.encrypt(pad(m))

def check_pad(m) :
    if (ord(m[-1])<0) or (ord(m[-1])>=16):
        print "Padding incorrect"
        return -1
    for i in range(ord(m[-1])) :
        if m[-i-1]!=m[-1] :
            return -1
    return 0


