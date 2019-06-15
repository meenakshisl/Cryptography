
#----------functions to pad , unpad and check_padding---------

def unpad(cipher_text,block_size) :

#---------unpads parameter string after checking for padding---------

    assert check_pad(cipher_text,block_size)=="Ok",check_pad(cipher_text,block_size)
    ch=ord(cipher_text[-1])    
    plain_text=cipher_text[:-ch]
    return plain_text

def pad(plain_text,block_size) :

#---------pads the string given as parameter------------------

    tmp=block_size-(len(plain_text)%block_size)                           return plain_text+chr(tmp)*tmp


def check_pad(cipher_text,block_size) :

#----------checks for padding of the string-----------------
    ch=ord(cipher_text[-1])
    if ch > 16 :    # if padding character is within the block range
        r="Padding incorrect 1"
        return r
    else :
        for i in range(ch) : #checks if all padded characters are same
            if(cipher_text[(-i-1)]!=chr(ch)) :
                r= "Padding incorrect 2"
            else :
                r="Ok"
    return r





