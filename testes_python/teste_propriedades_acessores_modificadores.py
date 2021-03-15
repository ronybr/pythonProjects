class Complex(object):
    #Metodo Acessor
    def getReal(self):
        return self._real

    #Metodo Modificador
    def setReal(self, valor):
        self._real = valor

    real = property(fget=getReal,
                    fset=setReal)

    #Metodo acessor
    def getImag(self):
        return self._imag

    #Metodo Modificador
    def setImag(self, valor):
        self._imag = valor

    imag = property(fget=getImag,
                    fset=setImag)

c = Complex()
c.setReal(2)
print(c.getReal())

c.imag = 3
print(c.imag)