#!/usr/bin/python3

def calc(n,d) :
    """calc(n,d) - given function when passed the numerator and denominator of a fraction calculates the continuous fraction form
       n         - numerator
       d         - denominator"""
    f=[-1,0]
    r=[n,d]
    c=[]
    while(f[0]!=0) :
        i=r[0]//r[1]
        f=[(r[0]-(i*r[1])),r[1]]
        c.append(i)
        finv=[f[1],f[0]]
        r=finv
    
    return c

def _test_() :
    print(calc(649,200))
    
if __name__ =="__main__" :
    _test_()

    

        

