from itertools import izip,cycle

def xor(a,b) :
    return (''.join(chr(ord(i)^ord(j)) for i,j in izip(a,cycle(b)))).encode('hex')


if __name__ == "__main__" :
    m1="""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    key="ICE"
    print xor(m1,key)

