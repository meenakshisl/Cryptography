
def checkp1(a) :
    ct=0
    for i in range(2,int(a**0.5)+1,) :
        if(a%i==0) :
            ct=1
            break
    if ct==0 :
        return "Prime"
    else :
        return "Composite"

def checkp2(a) :
    for i in range(2,a,) :
        if(a%i==0) :
            break
    if i<a :
        return "Composite"
    else :
        return "Prime"
    

def sieve(a) :
    l=[x for x in xrange(1,int(a**0.5)+1,)]
    for i in l :
        for j in l :
            if j%i==0 :
                try :
                    l.remove(i)
                except :
                    pass
    for i in l :
        ct=0
        if a%i==0 :
            ct=1
            break
    if(ct==0) :
        return "Prime"
    else :
        return "Composite"

