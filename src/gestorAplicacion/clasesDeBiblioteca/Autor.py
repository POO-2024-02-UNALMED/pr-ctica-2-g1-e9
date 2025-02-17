class Autor:
    def __init__(self, nombre, nacionalidad, corriente):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.corriente = corriente
        self.obras = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nacionalidad(self):
        return self.nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def get_corriente(self):
        return self.corriente

    def set_corriente(self, corriente):
        self.corriente = corriente

    def get_obras(self):
        return self.obras

    def set_obras(self, obras):
        self.obras = obras

    def __str__(self):
        return self.nombre
