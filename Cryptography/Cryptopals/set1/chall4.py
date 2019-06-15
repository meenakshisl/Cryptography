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
            print n,chr(i)


if __name__ =="__main__" :
    f=open("xored.txt","r")
    lines=f.readlines()
    for i in lines :
        brute(i)



