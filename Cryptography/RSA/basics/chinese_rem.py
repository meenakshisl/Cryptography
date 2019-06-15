]#for python3

from Crypto.Util.number import *

def chinese_remainder(r,n) :

    """ Function to solve a set of congruenies using chinese remaindertheorum.
    Parameters (r,n) : r - list of remainders
                       n - list of modulus """
    import gmpy2

    for i in n :
        for j in n :
            if i!=j and GCD(i,j)!=1 :
                print("Chinese remainder theorum cannot be applied")
                return
    
    N = eval('*'.join(str(i) for i in n))
    y=[int(N/n[i]) for i in range(len(n))]
    z=[inverse(y[i],n[i]) for i in range(len(y))]
    x=0
    for i in range(len(r)) :
        x+=r[i]*y[i]*z[i]
    
    return x%N


def _test_chinese() :
    import gmpy2,secrets
    #large number
    x=secrets.randbits(124)
    n=[getPrime(120) for i in range(3)]
    r=[x%n[i] for i in range(len(n))]
    res = chinese_remainder(r,n)
    if res == x :
        print(res ,"Successful")
    else :
        print("Error in code")
    #small numbers
    if (chinese_remainder([1,4,6],[3,5,7])) == 34 :
        print("Successful for small")
    else :
        print("Error in code")

if __name__== "__main__" :
    _test_chinese()

