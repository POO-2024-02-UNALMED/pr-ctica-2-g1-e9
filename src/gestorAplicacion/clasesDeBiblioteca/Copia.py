from .Libro import Libro
from .Prestable import Prestable

class Copia(Libro, Prestable):
    contadorCopia = 0
    def __init__(self, idCopia, libro, ubicacion):
        super().__init__(libro.get_nombre(), 1, libro.get_isbn(), libro.get_autor(), libro.get_año())
        self.disponibleEvento = True  # Por defecto, disponible para eventos
        self.disponibleParticular = True  # Por defecto, disponible para préstamos particulares
        self.ubicacion = ubicacion
        Copia.contadorCopia += 1
        self.idCopia = Copia.contadorCopia

    @staticmethod
    def get_contadorCopia():
        return Copia.contadorCopia
    
    def get_id(self):
        return self.idCopia

    def get_copia_de(self):
        return self.copiaDe

    def is_disponible_evento(self):
        return self.disponibleEvento

    def set_disponible_evento(self, disponibleEvento):
        self.disponibleEvento = disponibleEvento

    def is_disponible_particular(self):
        return self.disponibleParticular

    def set_disponible_particular(self, disponibleParticular):
        self.disponibleParticular = disponibleParticular

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def is_prestado(self):
        return not (self.disponibleEvento and self.disponibleParticular)

    def __str__(self):
        return self.get_nombre()

    def tipo_recurso(self):
        return "Copia"
