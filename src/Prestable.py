from abc import ABC, abstractmethod

#Corroborar con precision
#Recordar que se debe implementar junto a
#Copia

class Prestable(ABC):
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def is_prestado(self):
        pass

    @abstractmethod
    def is_disponible_evento(self):
        pass

    @abstractmethod
    def is_disponible_particular(self):
        pass