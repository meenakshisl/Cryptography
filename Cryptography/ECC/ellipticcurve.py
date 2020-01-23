from Crypto.Util.number import inverse

class Curve :

    def __init__(self,p,a,b) :
        self._a = a
        self._b = b
        self._p = p

    def get_a(self) :
        return self._a

    def get_b(self) :
        return self._b

    def get_p(self) :
        return self._p

    def check_exist(self,x,y) :
        return ( y*y - (x*x*x + _a*x + _b)) % _p == 0

class Point : 

    def __init__(self,curve,x,y) :
        self._curve = curve
        self._x = x
        self._y = y
        if self._curve :
            assert _curve.check_exist(x,y)

    def add(self,other) :
        if other == INFINITY : return self
        if self == INFINITY : return other

        assert other._curve == other._self

        if other._x == self._x :
            if (other._y + self._y) % self._curve.get_p() == 0 :
                return INFINITY
            else
                return self.double()
        p = self._curve.get_p()
        m = ((other._y - self._y)*inverse(other._x - self._x , p )) % p
        xR = (m*m - other._x - self._x) % p
        yR = (self._y - m*(other._x - self._x)) % p
        return Point(self,xR,yR)

    #def mult(self,curve,n) :
        
    def double(self) :
        if self == INFINITY :
            return INFINITY

        p = self._curve.get_p()
        a = self._curve.get_a()
        m = ((3*(self._x**2) + a)*inverse(self._y,p)) % p

        xR = (m**2 - 2*self_x)%p
        yR = (m*(self_x - xR) - self._y) % p
        return Point(self._curve,x3,y3)
    
    def x(self) :
        return self._x

    def y(self) :
        return self._y

    def curve(self) :
        return self._curve

    def order(self) :
        return self._order

INFINITY = Point(None,None,None)



