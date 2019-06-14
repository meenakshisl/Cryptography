from itertools import izip,cycle
import string

def xor(a,b) :
    return ''.join(chr(ord(i)^ord(j)) for i,j in izip(a,cycle(b)))

def brute(m) :
    ch="ETAOIN SHRDLUetaoin shrdlu"
    for i in range(256) :
        n=xor(m,chr(i))
        maxim=0
        for j in n :
            if n.count(j) > maxim :
                most=j
        if most in ch and all(k in string.printable for k in n) :
            print n


if __name__ =="__main__" :
    m="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode('hex')
    brute(m)



