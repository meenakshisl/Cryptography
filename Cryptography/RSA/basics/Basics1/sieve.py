def sieve(a) :
    l=[x for x in xrange(1,int(a**0.5)+1,)]
    for i in l :
        for j in l :
            if j%i==0 :
                try :
                    l.remove(i)
                except :
                    pass
    ct=0
    for i in l :
        ct=0
        if a%i==0 :
            ct=1
            break
    if(ct==0) :
        return "Prime"
    else :
        return "Composite"


if __name__ =="__main__" :
    a=input()
    print sieve(a)
