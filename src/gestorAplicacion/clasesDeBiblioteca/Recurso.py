from abc import ABC, abstractmethod

class Recurso(ABC):
    def __init__(self, nombre, id_recurso, tipo_de_recurso):
        self.nombre = nombre
        self.id_recurso = id_recurso
        self.tipo_de_recurso = tipo_de_recurso
      
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id_recurso(self):
        return self.id_recurso

    def set_id_recurso(self, id_recurso):
        self.id_recurso = id_recurso

    def get_tipo_de_recurso(self):
        return self.tipo_de_recurso

    @abstractmethod
    def tipo_recurso(self):
        pass

    def __str__(self):
        return self.nombre
