# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem


class Complex(object):
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        c = complex.__mul__(complex(self.r, self.i), complex(other.r, other.i))
        return Complex(c.real, c.imag)

    def __truediv__(self, other):
        c = complex.__truediv__(complex(self.r, self.i), complex(other.r, other.i))
        return Complex(c.real, c.imag)

    def mod(self):
        return Complex(math.sqrt(pow(self.r, 2) + pow(self.i, 2)), 0)

    def __str__(self):
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result
