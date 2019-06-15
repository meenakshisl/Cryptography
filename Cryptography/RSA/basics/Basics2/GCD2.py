def GCD(a,b) :
    l=max(a,b)
    s=min(a,b)
    if l%s==0 :
        return s
    else :
        return GCD(l%s,s)


if __name__ =="__main__" :
    a=input()
    b=input()
    GCD(a,b)
