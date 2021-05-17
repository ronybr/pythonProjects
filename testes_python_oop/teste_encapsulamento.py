class Livro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.autor = autor

    #Metodo acessor (GETTER)
    @property
    def titulo(self):
        return self.__titulo

    #Metodo modificador SETTER)
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

livro1 = Livro("Curso Python", "Rony Brito")
print(livro1.titulo) #Consulta o atributo privado
livro1.titulo = "Novo curso" #Altera o atributo privado
print(livro1.titulo)#Consulta o atributo privado