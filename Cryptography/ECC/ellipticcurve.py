

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

        if other

