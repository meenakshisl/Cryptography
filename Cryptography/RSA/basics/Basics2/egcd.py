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
    print str(max(a,b))+ "x+" + str(min(a,b)) + "y = " + " GCD("+str(a)+","+str(b) + ") = " + str(ro) 
    print "where (x,y) :: ("+str(so)+","+str(to) +")"




if __name__ == "__main__" :

    a=input()
    b=input()
    egcd(a,b)


