from tkinter import *
from tkinter import messagebox
#from baseDatos import Aplicacion
from uiMain.prestamoRecursos import PrestamoRecursos
from uiMain.reservaEvento import ReservaEvento
from uiMain.baseDatos import BaseDeDatos
from uiMain.gestionPrestamos import GestionPrestamo
from uiMain.gestionMultas import GestionMultas
from gestorAplicacion.clasesDeBiblioteca.Libro import Libro
from gestorAplicacion.clasesDeBiblioteca.Computador import Computador
from gestorAplicacion.clasesDeBiblioteca.BibliotecaDos import BibliotecaDos
from gestorAplicacion.clasesDeBiblioteca.Copia import Copia
from gestorAplicacion.clasesDeBiblioteca.PC import PC
from gestorAplicacion.clasesDeBiblioteca.Autor import Autor
from gestorAplicacion.clasesDeBiblioteca.Sala import Sala
from gestorAplicacion.clasesDeAdministracion.Sistema import Sistema
from gestorAplicacion.clasesDeAdministracion.Usuario import Usuario
from gestorAplicacion.clasesDeAdministracion.Prestamo import Prestamo
from gestorAplicacion.clasesDeAdministracion.Multa import Multa
from datetime import date
from baseDatos.Serializador import Serializador
from baseDatos.Deserializador import Deserializador

#Color de bordes = #2b6fb8
#Color de fondo = #72b2f4

class ventanaInicial(Tk):

    def __init__(self, sistema):
        super().__init__()
        self.title("Inicio")
        self.geometry("1250x800")
        self.configure(background="#72b2f4")
        self.iconbitmap("img\\R.ico")
        self.resizable(False, False)

        self.sistema = sistema

        """

        frameP1 = frame que contiene los frames de saludo y el de ingreso
        frameP2 = frame que contiene los frames de biografia y fotos
        frameP3 = frame contenido en frameP1, que contiene el saludo de bienvenida
        frameP4 = frame contenido en frameP1 que contiene el boton de ingreso
        frameP5 = frame contenido en frameP2 que contiene la biografia de desarrolladores
        frameP6 = frame contenido en frameP2 que contiene las fotos de los desarrolladores

        """


        frameP1 = Frame(self)
        frameP1.grid(row=0,column=0,padx=25,pady=5, sticky="n")
        frameP1['borderwidth'] = 5
        frameP1.configure(background="#72b2f4")

        frameP2 = Frame(self)
        frameP2.grid(row=0,column=1,padx=25,pady=5, sticky="n")
        frameP2['borderwidth'] = 5
        frameP2.configure(background="#72b2f4")

        frameP3=Frame(frameP1,height=70,width=500,bg="#72b2f4")
        frameP3.grid(row=0,column=0)

        frameP4 = Frame(frameP1, bg = "#72b2f4", width=400, height=400)
        frameP4.grid(row = 1, column = 0, pady=45)

        frameP5 = Frame(frameP2,height=70,width=500,bg="#2b6fb8")
        frameP5.grid(row=0,column=0) 


        frameP6 = Frame(frameP2, width=450, height=450, bg ="#2b6fb8")
        frameP6.grid(row = 1, column = 0, pady=40)


        saludo = Label(frameP3,text="Bienvenido al sistema de bibliotecas de la Universidad Nacional de Colombia",font=("arial", 17, "bold"),bg="#2b6fb8",wraplength=500,fg="#cedae0")
        saludo.pack(expand = True)

        imagenes = [PhotoImage(file = "img\\Sis1.png"),
                    PhotoImage(file = "img\\Sis2.png"),
                    PhotoImage(file = "img\\Sis3.png"),
                    PhotoImage(file = "img\\Sis4.png"),
                    PhotoImage(file = "img\\Sis5.png")]

        ImagenSistema = Label(frameP4, image= imagenes[0],width=420,height=420,wraplength=160,highlightbackground="#2b6fb8",highlightthickness=4, bg = "#72b2f4")
        ImagenSistema.pack(side="top",pady=0)

        def Ingresar(self):
            self.destroy()
            ventPrincipal(sistema)

        botonIngreso=Button(frameP4,text="Ingresar",bg="#2b6fb8",font=("arial", 12, "bold"),fg="#cedae0", command=lambda: Ingresar(self))
        botonIngreso.pack(side="top",pady=(10,20))

        biografias = [
                        "Me llamo Paulina Gómez Hincapié, tengo 21 años y soy estudiante de traslado a Ingeniería de Sistemas",
                        "Soy Daniel Hincapié Cardona, soy parte del programa de Ciencias de la Computacion y soy integrante del grupo cultural Coro UNAL. Entre mis hobbies está todo lo relacionado con computadores, videojuegos, música y astronomía.",
                        "Mi nombre es Valentina Sierra soy estudiante del pregrado de estadística me apasiona conocer pueblos y paisajes vivo con mis padres y dos hermosos cachorros entre mis personajes favoritos está Stitch que me gusta mucho su historia y sus películas incluso tengo un tatuaje sobre él y lo que representa.",
                        "Me llamo Alejandro Avendaño Serna, estudio ingeniería de sistemas e informática, me apasionan muchas cosas como el automovilismo, la tecnología y los videojuegos.",
                        "Mi nombre es Juan Leonardo Medina Reyes, estudio Ingeniería de Sistemas e informática y me gusta experimentar con Machine Learning"]

        presentacion = Label(frameP5, text = biografias[0], font=("arial", 13, "bold"), bg="#2b6fb8", wraplength = 500, fg="#cedae0", width= 50)
        presentacion.pack(expand = True)

        fotosCat1 = [PhotoImage(file = "img\\devSam1.png"),
                    PhotoImage(file = "img\\devSam2.png"),
                    PhotoImage(file = "img\\devSam3.png"),
                    PhotoImage(file = "img\\devSam4.png")]

        fotosDog1 = [PhotoImage(file = "img\\devPab1.png"),
                    PhotoImage(file = "img\\devPab2.png"),
                    PhotoImage(file = "img\\devPab3.png"),
                    PhotoImage(file = "img\\devPab4.png")]
        
        fotosFox1 = [PhotoImage(file = "img\\devFox1.png"),
                    PhotoImage(file = "img\\devFox2.png"),
                    PhotoImage(file = "img\\devFox3.png"),
                    PhotoImage(file = "img\\devFox4.png")]
        
        fotosFerret1 = [PhotoImage(file = "img\\devFerret1.png"),
                    PhotoImage(file = "img\\devFerret2.png"),
                    PhotoImage(file = "img\\devFerret3.png"),
                    PhotoImage(file = "img\\devFerret4.png")]
        
        fotosBunny1 = [PhotoImage(file = "img\\devBunny1.png"),
                    PhotoImage(file = "img\\devBunny2.png"),
                    PhotoImage(file = "img\\devBunny3.png"),
                    PhotoImage(file = "img\\devBunny4.png")]
        
        listimagenes = [fotosCat1, fotosDog1, fotosFox1, fotosFerret1, fotosBunny1]
        self.dev_animal = 0 
        label_imagenes = []

        for i in range(4):
            label_imagenes2 = Label(frameP6, image=listimagenes[0][i], width=220, height=220, wraplength=500, highlightbackground="#2b6fb8", highlightthickness=2, bg="#72b2f4")
            label_imagenes2.grid(column=i % 2, row=i // 2)  # Coloca las imágenes en un grid
            label_imagenes.append(label_imagenes2)  # Agrega la etiqueta a la lista

        def cambiarImagenes(evento):
            self.dev_animal = (self.dev_animal + 1) % len(listimagenes)

            for i in range(4):
                label_imagenes[i].config(image=listimagenes[self.dev_animal][i])
                presentacion.config(text=biografias[self.dev_animal])

        presentacion.bind("<Button-1>", cambiarImagenes)

        descripTexto = Label(frameP4,text="",font=("arial", 9, "bold"),bg="#72b2f4",wraplength=500)
        descripTexto.pack(side="left")
        menuBar = Menu(self)
        self.option_add("*tearOff",  False)
        self.config(menu=menuBar)
        menu1= Menu(menuBar)
        menuBar.add_cascade(label="Inicio",menu=menu1)

        textDescrip="Este sistema permite el control y administracion de la base de datos del sistema de bibliotecas de la Universidad Nacional. En este sistema encontraras funcionalidades para el prestamo de material de la biblioteca, para agregar/eliminar material y para gestionar tus reservas/multas."
        menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))

        def salirSerializar():
            Serializador.serializar(sistema)
            self.destroy()

        menu1.add_command(label="Salir",command=salirSerializar)

        self.mainloop()
