from Crypto.Cipher import AES
import re
import os
key=os.urandom(16)
m=""

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
        c=c[17:]
        ct_list=[c[i:i+16] for i in range(0,len(c),16)]
        tmp=ct_list[1]
        #....performing the attack by xoring the previous encrypted block in order to get required output...
        tmp2=list(tmp)
        tmp2[32%16]=chr(ord(tmp[32%16])^ord(';')^ord('?'))
        tmp2[38%16]=chr(ord(tmp[38%16])^ord('=')^ord('?'))    
        tmp2[43%16]=chr(ord(tmp[43%16])^ord(';')^ord('?'))
        ct_list[1]=''.join(tmp2)
        c=''.join(ct_list)
        print c
        obj=AES.new(key,AES.MODE_CBC,iv)
        m=unpad(obj.decrypt(c))
        print m
        #-------checks if the word ';admin=true; is present in the decrypted text------------
        if ';admin=true;' in m :
            print "Wow!You won"
        else:
            print "Sorry !You lose !Better luck next time "

#----------function to encrypt in aes cbc mode------------
def encrypt_CBC(inp):
    
        iv=os.urandom(16)
        obj=AES.new(key,AES.MODE_CBC,iv)
        
        str1="comment1=cooking%20MCs;userdata="
        str2=";comment2=%20like%20a%20pound%20of%20bacon"
        m="???"+re.sub(";|=","",(str1+inp+str2)) #.....three characters are added in order to shift the bits to be flipped to a single block
        m=obj.encrypt(pad(m))

        return iv+":"+m

#-----------function to check if the given string is properly padded or not-------------------------------
def check_pad(m) :
        if (ord(m[-1])<0) or (ord(m[-1])>=16):
             print "Padding incorrect"
             return -1
        for i in range(ord(m[-1])) :
             if m[-i-1]!=m[-1] :
                 return -1
        return 0

if __name__ =="__main__" :
        
        inp=raw_input("Enter the pass")
        decrypt_CBC(encrypt_CBC(inp))
        
