class ErrorAplicacion(Exception):
    def _init_(self, error):
        self.error = "Error en la aplicacion: " + error
    
    def getError(self):
        return self.error