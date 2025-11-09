import math

class Vector:    
    '''
    Run some tests
    >>> Vector(4,5) + Vector(5,6)
    Vector(9,11)
    >>> abs(Vector(3,4))
    5.0
    >>> bool(Vector(0,0))
    False
    >>> Vector(4,5) * 2
    Vector(8,10)

    Notice that right multiplication will fail!!
    '''

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vector({self._x!r},{self._y!r})'
    
    def __abs__(self):
        return math.hypot(self._x, self._y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(
            self._x + other._x,
            self._y + other._y,
        )
    
    def __mul__(self, scalar):
        return Vector(
            self._x * scalar,
            self._y * scalar,
        )

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(Vector(3,4))
