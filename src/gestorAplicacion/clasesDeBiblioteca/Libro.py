from .Recurso import Recurso

class Libro(Recurso):
    totalLibros = 0

    def __init__(self, nombre, idRecurso, isbn, autor, año):
        super().__init__(nombre, idRecurso, "Libro")
        self.isbn = isbn
        self.autor = autor
        self.año = año
        autor.get_obras().append(self)
        Libro.totalLibros += 1
        self.idRecurso = Libro.totalLibros
    
    def get_nombre(self):
        return self.nombre
    
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_año(self):
        return self.año

    def set_año(self, año):
        self.año = año

    def tipo_recurso(self):
        return "Libro"

    def __str__(self):
        return self.get_nombre()

    @staticmethod
    def get_total_libros():
        return Libro.totalLibros