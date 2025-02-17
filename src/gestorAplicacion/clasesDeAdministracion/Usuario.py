class Usuario:
    prestamos_maximos = 3  # Número máximo de préstamos permitidos

    def __init__(self):
        self.prestamos = []  # Lista de préstamos realizados por el usuario
        self.multas = []  # Lista de multas impuestas al usuario

    def get_prestamos(self):
        return self.prestamos

    def set_prestamos(self, prestamos):
        self.prestamos = prestamos

    def get_multas(self):
        return self.multas

    def set_multas(self, multas):
        self.multas = multas

    def eliminar_multa(self, multa):
        # Lógica para eliminar una multa del registro del usuario
        self.multas.remove(multa)
