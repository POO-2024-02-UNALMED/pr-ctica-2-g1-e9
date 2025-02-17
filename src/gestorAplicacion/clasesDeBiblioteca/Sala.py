class Sala:
    def __init__(self, biblioteca, nombre, capacidad):
        self.biblioteca = biblioteca
        self.nombre = nombre
        self.capacidad = capacidad

    def get_nombre(self):
        return self.nombre

    def get_capacidad(self):
        return self.capacidad

    def get_biblioteca(self):
        return self.biblioteca

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def set_biblioteca(self, biblioteca):
        self.biblioteca = biblioteca

    def __str__(self):
        return self.nombre
