from datetime import date
from .Usuario import Usuario

class Prestamo:
    numero_prestamos = 0  # Variable de clase para llevar un registro del número de préstamos

    def __init__(self, usuario, materialPrestado, tipo, fecha_inicio, fecha_fin, sede):
        self.tipo = tipo
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.sede = sede
        self.materialPrestado = materialPrestado
        # Generar un identificador único para el préstamo (puedes implementar esta lógica)
        self.id_prestamo = self.generar_identificador_unico()
        self.copias_prestadas = []
        self.pcs_prestados = []
        """
        sede.eliminar_salas(sede.get_salas())
        sede.eliminar_copias(sede.get_copias())
        sede.eliminar_pcs(sede.get_pcs())
        """
        
    def get_sede(self):
        return self.sede

    def get_id_prestamo(self):
        return self.id_prestamo

    def set_sala(self, sala):
        self.sala = sala

    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin
    
    def get_materialPrestado(self):
        return self.materialPrestado

    def get_tipo(self):
        return self.tipo

    def get_usuario(self):
        return self.usuario

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_fecha_fin(self):
        return self.fecha_fin

    def get_sala(self):
        return self.sala

    def get_copias_prestadas(self):
        return self.copias_prestadas

    def get_pcs_prestados(self):
        return self.pcs_prestados

    def contiene_recursos(self, copias, pcs):
        return all(copia in self.copias_prestadas for copia in copias) and all(pc in self.pcs_prestados for pc in pcs)

    def finalizar_prestamo(self):
        pass

    def generar_identificador_unico(self):
        return 0  