from .Recurso import Recurso

class Computador(Recurso):
    # Atributo de clase que lleva el conteo total de objetos Computador creados
    totalPCs = 0

    def __init__(self, nombre, idRecurso, marca, gama):
        # Llama al constructor de la clase base Recurso, asignando tipo "Computador"
        super().__init__(nombre, idRecurso, "Computador")
        self.marca = marca  # Marca del computador (ejemplo: Dell, HP)
        self.gama = gama  # Gama del computador (ejemplo: alta, media, baja)
        
        # Incrementa el contador total de computadoras y asigna un ID único
        Computador.totalPCs += 1
        self.idRecurso = Computador.totalPCs

    def tipo_recurso(self):
        """Devuelve el tipo de recurso como 'Computador'."""
        return "Computador"

    def get_nombre(self):
        """Obtiene el nombre del recurso desde la clase base."""
        return super().get_nombre()
    
    def __str__(self):
        """Devuelve el nombre del computador como su representación en cadena."""
        return self.get_nombre()

    def get_marca(self):
        """Devuelve la marca del computador."""
        return self.marca

    def set_marca(self, marca):
        """Establece la marca del computador."""
        self.marca = marca

    def get_gama(self):
        """Devuelve la gama del computador."""
        return self.gama

    def set_gama(self, gama):
        """Establece la gama del computador."""
        self.gama = gama

    @staticmethod
    def get_total_pcs():
        """Devuelve la cantidad total de objetos Computador creados."""
        return Computador.totalPCs
