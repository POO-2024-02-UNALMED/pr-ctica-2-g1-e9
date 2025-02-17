import pickle
from gestorExcepciones.erroresPython import *
class Deserializador:
    @classmethod
    def deserializar(cls, sistema):
        cls.deserializarBibliotecas(sistema,"baseDatos\\temp\\Bibliotecas.pkl")
        cls.deserializarLibros(sistema,"baseDatos\\temp\\Libros.pkl")
        cls.deserializarComputadores(sistema,"baseDatos\\temp\\Computadores.pkl")
        cls.deserializarAutores(sistema,"baseDatos\\temp\\Autores.pkl")
        cls.deserializarUsuario(sistema,"baseDatos\\temp\\Usuario.pkl")

    @classmethod
    def deserializarBibliotecas(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "rb")
            bibliotecas = pickle.load(picklefile)
            sistema.set_bibliotecas(bibliotecas)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())

    @classmethod
    def deserializarLibros(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "rb")
            libros = pickle.load(picklefile)
            sistema.set_libros(libros)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())

    @classmethod
    def deserializarComputadores(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "rb")
            computadores = pickle.load(picklefile)
            sistema.set_computadores(computadores)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())

    @classmethod
    def deserializarAutores(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "rb")
            autores = pickle.load(picklefile)
            sistema.set_autores(autores)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())

    @classmethod
    def deserializarUsuario(cls, sistema, ruta):
        try:
            picklefile = open(ruta, "rb")
            user = pickle.load(picklefile)
            sistema.set_user(user)
            picklefile.close()
        except:
            print(ErrorSerializacion().getError())