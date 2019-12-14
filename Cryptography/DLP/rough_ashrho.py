from Crypto.Util.number import *

def func_f(x_i, base, y, p):
    """
    x_(i+1) = func_f(x_i)
    """
    if x_i % 3 == 2:
        return (y*x_i) % p
    elif x_i % 3 == 0:
        return pow(x_i, 2, p)
    elif x_i % 3 == 1:
        return base*x_i % p
    else:
        print "[-] Something's wrong!"
        return -1

def func_g(a, n, p, x_i):
    """
    a_(i+1) = func_g(a_i, x_i)
    """
    if x_i % 3 == 2:
        return a
    elif x_i % 3 == 0:
        return 2*a % n
    elif x_i % 3 == 1:
        return (a + 1) % n
    else:
        print "[-] Something's wrong!"
        return -1

def func_h(b, n, p, x_i):
    """
    b_(i+1) = func_g(b_i, x_i)
    """
    if x_i % 3 == 2:
        return (b + 1) % n
    elif x_i % 3 == 0:
        return 2*b % n
    elif x_i % 3 == 1:
        return b
    else:
        print "[-] Something's wrong!"
        return -1

def pollardrho(base, y, p, n):
    """
    Refer to section 3.6.3 of Handbook of Applied Cryptography
    Computes `x` = a mod n for the DLP base**x % p == y
    in the Group G = {0, 1, 2, ..., n}
    given that order `n` is a prime number.
    :parameters:
        base : int/long
                Generator of the group
        y : int/long
                Result of base**x % p
        p : int/long
                Group over which DLP is generated.
        n : int/long
                Order of the group generated by `base`.
                Should be prime for this implementation
    """

    if not isPrime(n):
        print "[-] Order of group must be prime for Pollard Rho"
        return -1

    x_i = 1
    x_2i = 1

    a_i = 0
    b_i = 0
    a_2i = 0
    b_2i = 0

    i = 1
    while i <= n:
        # Single Step calculations
        a_i = func_g(a_i, n, p, x_i)
        b_i = func_h(b_i, n, p, x_i)
        x_i = func_f(x_i, base, y, p)

        # Double Step calculations
        a_2i = func_g(func_g(a_2i, n, p, x_2i), n, p, func_f(x_2i, base, y, p))
        b_2i = func_h(func_h(b_2i, n, p, x_2i), n, p, func_f(x_2i, base, y, p))
        x_2i = func_f(func_f(x_2i, base, y, p), base, y, p)

        if x_i == x_2i:
            """
            If x_i == x_2i is True
            ==> (base^(a_i))*(y^(b_i)) = (base^(a_2i))*(y^(b_2i)) (mod p)
            ==> y^(b_i - b_2i) = base^(a_2i - a_i)                (mod p)
            ==> base^((b_i - b_2i)*x) = base^(a_2i - a_i)         (mod p)
            ==> (b_i - b_2i)*x = (a_2i - a_i)                     (mod n)
            r = (b_i - b_2i) % n
            if GCD(r, n) == 1 then,
            ==> x = (r^(-1))*(a_2i - a_i)                         (mod n)
            """
            r = (b_i - b_2i) % n
            if r == 0:
                print "[-] b_i = b_2i, returning -1"
                return -1
            else:
                assert GCD(r, n) == 1
                """
                If `n` is not a prime number this algorithm will not be able to
                solve the DLP, because GCD(r, n) != 1 then and one will have to
                write an implementation to solve the equation:
                    (b_i - b_2i)*x = (a_2i - a_i) (mod n)
                This equation will have multiple solutions out of which only one
                will be the actual solution
                """
                return (inverse(r, n)*(a_2i - a_i)) % n
        else:
            i += 1
            continue
