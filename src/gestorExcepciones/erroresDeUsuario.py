from gestorExcepciones.ErrorAplicacion import ErrorAplicacion

class ErrorDeUsuario(ErrorAplicacion):
    def __init__(self, error):
        super().__init__(error)

class libroNoEncontrado(ErrorDeUsuario):
    def __init__(self, valor):
        super().__init__(f"El libro '{valor}' no ha sido encontrado")

class ComputadorNoEncontrado(ErrorDeUsuario):
    def __init__(self, valor):
        super().__init__(f"El computador '{valor}' no ha sido encontrado")

class CampoVacio(ErrorDeUsuario):
    def __init__(self):
        super().__init__(f"Hay un campo vacío")

class NingunRecurso(ErrorDeUsuario):
    def __init__(self):
        super().__init__(f"No existe ningun recurso con estos criterios")

class NoHayCopia(ErrorDeUsuario):
    def __init__(self, valor):
        super().__init__(f"No hay copias del libro '{valor}'")

class NoHayPC(ErrorDeUsuario):
    def __init__(self, valor):
        super().__init__(f"No hay computadores disponibles del modelo '{valor}'")

class NoHayPrestamos(ErrorDeUsuario):
    def __init__(self):
        super().__init__(f"No hay prestamos que mostrar")

class NoHayMultas(ErrorDeUsuario):
    def __init__(self):
        super().__init__(f"No hay multas que mostrar")