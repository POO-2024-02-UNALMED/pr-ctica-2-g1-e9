class Sistema:
    def __init__(self):
        self.user = None
        self.bibliotecas = []
        self.libros = []
        self.computadores = []
        self.autores = []
        # Deserializador.deserializar(self)

    def get_bibliotecas(self):
        return self.bibliotecas

    def get_autores(self):
        return self.autores

    def get_computadores(self):
        return self.computadores

    def get_libros(self):
        return self.libros

    def set_autores(self, autores):
        self.autores = autores

    def set_bibliotecas(self, bibliotecas):
        self.bibliotecas = bibliotecas

    def set_computadores(self, computadores):
        self.computadores = computadores

    def set_libros(self, libros):
        self.libros = libros

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user