
def egcd(a,b) :
    ro=max(a,b)
    r=min(a,b)
    so=1
    s=0
    to=0
    t=1
    while r!=0 :
        q=ro/r
        ro,r = r , ro%r
        so,s = s,so - q*s
        to,t = t,to - q*t
    return [ro,so,to]


def inv(a,b) :
    ans=egcd(a,b)
    if ans[0]!=1 :
        print "Inverse does not exist"
        return
    else :
        if a>b :
            if ans[1]<0 :
                return b+ans[1]
            else :
                return ans[1]
        else :
            if ans[2]<0 :
                return b+ans[2]
            else :
                return ans[2]

if __name__ == "__main__" :
    
    a=input()
    b=input()
    print inv(a,b)

