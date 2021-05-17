from abc import abstractmethod
import ponto


class ObjetoGrafico(object):
    def __init__(self, centro):
        super(ObjetoGrafico, self).__init__()
        self._centro = centro

    @abstractmethod
    def desenha(self):
        pass

    def apaga(self):
        self.setPenColor(self.BACKGROUND_COLOR)
        self.desenha()
        self.setPenColor(self.FOREGROUND_COLOR)

    def move_para(self, p):
        self.apaga()
        self._centro = p
        self.desenha()


class Circulo(ObjetoGrafico):
    def __init__(self, centro, raio):
        super(Circulo, self).__init__(centro)
        self._raio = raio

    def desenha(self):
        pass


class Retangulo(ObjetoGrafico):
    def __init__(self, centro, altura, largura):
        super(Retangulo, self).__init__(centro)
        self._altura = altura
        self._largura = largura

    def desenha(self):
        pass


class Quardrado(Retangulo):
    def __init__(self, centro, altura, largura):
        super(Quardrado, self).__init__(centro, altura, largura)


g1 = Circulo(ponto(0,0), 5)
g2 = Quardrado(ponto(0,0), 5)
g1.desenha()
g2.desenha()

