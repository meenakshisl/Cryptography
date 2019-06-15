def GCD(a,b) :
    if a%b==0 :
        return b
    elif b%a==0 :
        return a
    else :
        p=1
        i=2
        m=min(a,b)
        while(a,b not in [0,1])and i<=m :
            
            if a%i==0 and b%i==0 :
                p*=i
                a=a/i
                b=b/i
            else :
                i=i+1
        return p

