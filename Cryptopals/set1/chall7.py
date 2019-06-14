from Crypto.Cipher import AES


key="YELLOW SUBMARINE"

def _decrypt(m) :
    obj=AES.new(key,AES.MODE_ECB)
    return obj.decrypt(m)

if __name__ =="__main__" :
    f=open("ch7.txt","r")
    lines=f.read()
    lines=lines.decode('base64')
    print _decrypt(lines)
