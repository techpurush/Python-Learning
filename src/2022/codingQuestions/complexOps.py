import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        z = x + y
        return Complex(z.real, z.imag)

    def __sub__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        z = x - y
        return Complex(z.real, z.imag)

    def __mul__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        z = x * y
        return Complex(z.real, z.imag)

    def __truediv__(self, no):
        x = complex(self.real, self.imaginary)
        y = complex(no.real, no.imaginary)
        z = x / y
        return Complex(z.real, z.imag)

    def mod(self):
        x = self.real
        y = self.imaginary
        import math
        z = math.sqrt(x ** 2 + y ** 2)
        return Complex(z, 0)

    def __str__(self):

        if self.imaginary >= 0:
            result = "%.2f+%.2fi" % (self.real, abs(self.imaginary))
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')