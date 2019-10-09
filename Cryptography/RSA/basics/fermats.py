import gmpy2


def Ncheck(n,i=1) :
    if(n%2!=0) :
        return (n,i)
    else :
        return Ncheck(n//2,i*2)


def factorise(n) :
    #n,k=Ncheck(n)
    a=gmpy2.iroot(n,2)[0]
    b=gmpy2.square(a)-n
    while((a+b)<=n) :
        if(gmpy2.is_square(b) == True) :
            print(a,b)
        a=a+1
        b=gmpy2.iroot(gmpy2.square(a)-n,2)[0]
    

if __name__ == "__main__" :
    
    n=input()
    factorise(n)
