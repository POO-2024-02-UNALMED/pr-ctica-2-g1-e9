import pickle
from gestorExcepciones.erroresPython import *
class Serializador:
    @classmethod
    def serializar(cls, sistema):
        cls.serializarBibliotecas(sistema,"baseDatos\\temp\\Bibliotecas.pkl")
        cls.serializarLibros(sistema,"baseDatos\\temp\\Libros.pkl")
        cls.serializarComputadores(sistema,"baseDatos\\temp\\Computadores.pkl")
        cls.serializarAutores(sistema,"baseDatos\\temp\\Autores.pkl")
        cls.serializarUsuario(sistema,"baseDatos\\temp\\Usuario.pkl")
    
    @classmethod
    def serializarBibliotecas(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "wb")
            pickle.dump(sistema.get_bibliotecas(), picklefile)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())
        

    @classmethod
    def serializarLibros(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "wb")
            pickle.dump(sistema.get_libros(), picklefile)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())

    @classmethod
    def serializarComputadores(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "wb")
            pickle.dump(sistema.get_computadores(), picklefile)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())

    @classmethod
    def serializarAutores(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "wb")
            pickle.dump(sistema.get_autores(), picklefile)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())

    @classmethod
    def serializarUsuario(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "wb")
            pickle.dump(sistema.get_user(), picklefile)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())