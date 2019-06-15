from itertools import izip

def xor(a,b) :
    return (''.join(chr(ord(i)^ord(j)) for i,j in izip(a,b))).encode('hex')


if __name__ == "__main__" :
    m1="1c0111001f010100061a024b53535009181c".decode('hex')
    m2="686974207468652062756c6c277320657965".decode('hex')

    print xor(m1,m2)
