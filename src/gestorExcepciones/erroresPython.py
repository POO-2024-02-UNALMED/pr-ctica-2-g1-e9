from gestorExcepciones.ErrorAplicacion import ErrorAplicacion

class ErrorDePython(ErrorAplicacion):
    def __init__(self, error):
        super().__init__(error)

class IndexFuera(ErrorAplicacion):
    def __init__(self):
        super().__init__(f"Seleccione un numero en la lista")

class DatoIncorrecto(ErrorAplicacion):
    def __init__(self, valor):
        super().__init__(f"Por favor, ingrese un dato de tipo: {valor}")

class VariableNone(ErrorAplicacion):
    def __init__(self, valor):
        super().__init__(f"'{valor}' no está asociada a ningún valor")

class RutaIncorrecta(ErrorAplicacion):
    def __init__(self, valor):
        super().__init__(f"No se ha podido encontrar la ruta {valor}")

class ErrorSerializacion(ErrorAplicacion):
    def __init__(self):
        super().__init__(f"Ha ocurrido un error con la serialización")