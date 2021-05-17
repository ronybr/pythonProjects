class Complex(object):
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

c = Complex(1,0)
d = Complex(2,0)
e = Complex(3,0)
print(
c._real,
d._real,
e._real)