import math

class Complex(object):
    #Metodo Acessor
    def getR(self):
        return math.sqrt(self._real * self._real +
                         self._imag * self._imag)

    #Metodo Modificador
    def setR(self, valor):
        theta = self.theta
        self._real = valor * math.cos(theta)
        self._imag = valor * math.sin(theta)

    r = property(fget=getR,
                 fset=setR)

    #Metodo Acessor
    def getTheta(self):
        return math.atan2(self._imag, self._real)

    #Metodo Modificador
    def setTheta(self, valor):
        r = self.r
        self._real = r * math.cos(valor)
        self._imag = r * math.sin(valor)

    theta = property(fget=getTheta,
                     fset=setTheta)

c = Complex()
c._real = 2
print(c._real)