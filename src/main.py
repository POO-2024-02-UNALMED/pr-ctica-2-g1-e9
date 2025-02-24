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

class ventPrincipal(Tk):
      def __init__(self,sistema):
            super().__init__()
            self.title("Sistema de Gestión de Bibliotecas")
            self.geometry("1250x800")
            self.configure(background="#72b2f4")
            self.iconbitmap("img\\R.ico")

            def Volver():
                self.destroy()
                ventanaInicial(sistema)

            def kill(root):
                for widget in root.winfo_children():
                        if isinstance(widget, Frame):
                            widget.destroy()

            def prestamoDeRecursos():
                kill(self)
                p = PrestamoRecursos(self, sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def ReservaDeEvento():
                kill(self)
                p = ReservaEvento(self,sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def BaseDatos():
                kill(self)
                p = BaseDeDatos(self,sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def gestionPrestamos():
                kill(self)
                p = GestionPrestamo(self, sistema)
                p.grid(row=0, column=0,rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def gestionarMultas():
                kill(self)
                p = GestionMultas(self, sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def Funny():
                respuesta = False
                while(respuesta != True):
                    respuesta = messagebox.askyesno("Profesores Jaime y David", "¿Paulina, Daniel, Valentina, Alejandro y Leonardo se merecen un 5.0 por este trabajo?")
                messagebox.showwarning("Cuidado!","Lo tendremos en cuenta!")

            frame = Frame(self, bg="#72b2f4")
            frame.pack(padx=10,pady=10)

            bienvenida = Label(frame, text="¡Bienvenido al sistema de bibliotecas de la Universidad Nacional de Colombia!", bg= "#2b6fb8", fg= "white", font=("arial", 15, "bold"))
            bienvenida.pack(anchor="center")
            img = PhotoImage(file="img\\logo.png")
            contenedorImg = Label(frame, image = img, bg = "#72b2f4")
            contenedorImg.pack(anchor="center", pady=(27,20))
            texto = "El sistema de bibliotecas de la universidad ofrece las siguientes cinco funcionalidades: \n1. Reserva de Recurso: Esta función permite a los usuarios reservar recursos disponibles \nen la biblioteca, como libros, revistas y documentos electrónicos. \n\n2. Reserva para Evento: Los usuarios pueden reservar espacios dentro de la biblioteca para \neventos como reuniones de estudio, presentaciones y conferencias. \n\n3. Gestión de Base de Datos: Esta funcionalidad permite a los administradores de la \nbiblioteca gestionar la base de datos de la biblioteca, incluyendo la adición, eliminación \ny modificación de registros de recursos. \n\n4. Gestión de Préstamos: Esta función permite a los usuarios solicitar préstamos de recursos \nde la biblioteca y a los administradores gestionar estos préstamos, incluyendo la emisión, \nrenovación y devolución de recursos. \n\n5. Gestión de Multas: Esta funcionalidad permite a los administradores de la biblioteca emitir \ny gestionar multas por retrasos en la devolución de recursos prestados. Estas funcionalidades \nhacen que el sistema de bibliotecas de la universidad sea eficiente y fácil de usar para todos \nlos usuarios."

            descripcion = Label(frame, text=texto, bg="#2b6fb8", fg = "white", font=("arial", 11, "bold"),justify="left", padx= 20, pady=20)
            descripcion.pack(padx=25,pady=10, expand=False)

            menuBar2 = Menu(self)
            self.option_add("*tearOff",  False)
            self.config(menu=menuBar2)
            menu2= Menu(menuBar2)

            menuBar2.add_cascade(label="Archivo",menu=menu2)
            menu2.add_command(label="Aplicacion",command=lambda: messagebox.showinfo("Aplicacion","Este sistema permite el control y administracion de la base de datos del sistema de bibliotecas de la Universidad Nacional. En este sistema encontraras funcionalidades para el prestamo de material de la biblioteca, para agregar/eliminar material y para gestionar tus reservas/multas."))
            menu2.add_command(label="Salir",command=lambda:Volver())

            menu3 = Menu(menuBar2)
            menuBar2.add_cascade(label="Procesos y Consultas",menu=menu3)
            menu3.add_command(label="Préstamo de Recursos",command= prestamoDeRecursos)
            menu3.add_command(label="Reserva de Recursos para Eventos",command= ReservaDeEvento)
            menu3.add_command(label="Gestión Base de Datos",command= BaseDatos)
            menu3.add_command(label="Gestión de Prestamos y Reservas",command= gestionPrestamos)
            menu3.add_command(label="Gestión de Multas",command=gestionarMultas)
            
            menu4 = Menu(menuBar2)
            menuBar2.add_cascade(label="Ayuda",menu=menu4)
            menu4.add_command(label="Acerca de",command=lambda: Funny())

            self.mainloop()
  
if __name__ == "__main__":
    sistema = Sistema()
    Deserializador.deserializar(sistema)
    #app = Aplicacion(sistema)
    """
    autor1 = Autor("Yuval Noah Harari", "Israel", "Historia")
    autor2 = Autor("J.K. Rowling", "Reino Unido", "Fantasía")
    autor3 = Autor("Harper Lee", "Estados Unidos", "Ficción")
    autor4 = Autor("José Saramago", "Portugal", "Realismo mágico")
    autor5 = Autor("Rebecca Solnit", "Estados Unidos", "Ensayo")
    autor6 = Autor("Miguel de Cervantes", "España", "Ficción")
    autor7 = Autor("Orson Scott Card", "Estados Unidos", "Ciencia ficción")
    autor8 = Autor("Julio Cortázar", "Argentina", "Ficción")
    autor9 = Autor("F. Scott Fitzgerald", "Estados Unidos", "Ficción")
    autor10 = Autor("Yuval Noah Harari", "Israel", "Ensayo")
    autor11 = Autor("Gabriel García Márquez", "Colombia", "Realismo mágico")
    autor12 = Autor("George Orwell", "Reino Unido", "Distopía")

    autores = [autor1, autor2, autor3, autor4, autor5, autor6, autor7, autor8, autor9, autor10, autor11, autor12]

    libros = [
        Libro("Sapiens: De animales a dioses", 1, "978-0-307-58973-2", autor1, 2014),
        Libro("Harry Potter y la piedra filosofal", 2, "978-0-7475-3269-6", autor2, 1997),
        Libro("Cien años de soledad", 3, "978-84-204-3471-6", autor11, 1967),
        Libro("1984", 4, "978-3-16-148410-0", autor12, 1949),
        Libro("Matar a un ruiseñor", 5, "978-0-553-21311-6", autor3, 1960),
        Libro("Ensayo sobre la ceguera", 6, "978-1-84749-593-7", autor4, 1995),
        Libro("Los hombres me explican cosas", 7, "978-1-933633-92-9", autor5, 2014),
        Libro("Don Quijote de la Mancha", 8, "978-84-204-9184-8", autor6, 1605),
        Libro("El juego de ender", 9, "978-0-06-112008-4", autor7, 1985),
        Libro("Crónica de una muerte anunciada", 10, "978-84-339-7049-4", autor11, 1981),
        Libro("Rayuela", 11, "978-84-3760494-7", autor8, 1963),
        Libro("El gran Gatsby", 12, "978-0-8129-7449-8", autor9, 1925),
        Libro("El amor en los tiempos del cólera", 13, "978-84-204-5298-7", autor11, 1985),
        Libro("To Kill a Mockingbird", 14, "978-0-525-43396-9", autor3, 1960),
    ]

    computadores = [
        Computador("Samsung JX", 0, "Samsung", "Alta"),
        Computador("HP Pavilion", 1, "HP", "Media"),
        Computador("Dell Inspiron", 2, "Dell", "Baja"),
        Computador("Lenovo ThinkPad", 3, "Lenovo", "Alta"),
        Computador("Asus VivoBook", 4, "Asus", "Media"),
        Computador("Acer Aspire", 5, "Acer", "Baja"),
    ]

    bibliotecas = [
        BibliotecaDos("Efe Gomez", "Medellín"),
        BibliotecaDos("Gabriel Garcia Marquez", "Bogota")
    ]

    librosSedeMedellin = [libros[0],libros[1],libros[2],libros[3],libros[4],libros[7],libros[10],libros[13]]
    bibliotecas[0].set_libros(librosSedeMedellin)

    librosSedeBogota = [libros[0],libros[1],libros[2],libros[5],libros[6],libros[7],libros[10],libros[11], libros[12], libros[13]]
    bibliotecas[1].set_libros(librosSedeBogota)

    computadoresSedeMedellin = [computadores[0], computadores[1], computadores[2], computadores[3]]
    bibliotecas[0].set_computadores(computadoresSedeMedellin)

    computadoresSedeBogota = [computadores[0], computadores[1], computadores[2], computadores[3], computadores[5]]
    bibliotecas[1].set_computadores(computadoresSedeBogota)


    bibliotecas[0].añadir_sala(Sala(bibliotecas[0], "Auditorio 1", 30))
    bibliotecas[0].añadir_sala(Sala(bibliotecas[0], "Auditorio 2", 50))
    bibliotecas[0].añadir_sala(Sala(bibliotecas[0], "Auditorio 3", 10))
    bibliotecas[1].añadir_sala(Sala(bibliotecas[1], "Auditorio 4", 150))
    bibliotecas[1].añadir_sala(Sala(bibliotecas[1], "Auditorio 5", 30))
    bibliotecas[1].añadir_sala(Sala(bibliotecas[1], "Auditorio 6", 60))


    # Copias sede Medellin
    bibliotecas[0].añadir_copia(Copia(0, libros[0], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(1, libros[0], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(2, libros[1], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(3, libros[2], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(4, libros[3], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(5, libros[3], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(6, libros[4], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(7, libros[7], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(8, libros[10], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(9, libros[13], bibliotecas[0]))

    #Copias sede Bogota
    bibliotecas[1].añadir_copia(Copia(0, libros[0], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(1, libros[1], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(2, libros[2], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(3, libros[5], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(4, libros[6], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(5, libros[7], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(6, libros[7], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(7, libros[10], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(8, libros[11], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(9, libros[11], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(10, libros[12], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(11, libros[13], bibliotecas[1]))

    #PCs a sede Medellin
    bibliotecas[0].añadir_pc(PC(computadores[0], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[0], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[0], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[1], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[1], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[1], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[2], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[2], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))

    #Pcs a sede Bogota

    bibliotecas[1].añadir_pc(PC(computadores[0], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[1], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[2], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[2], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[3], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[3], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[5], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[5], True, bibliotecas[1]))

    user = Usuario()
    user.get_prestamos().append(Prestamo(user, Copia(12, libros[2], bibliotecas[1]), "Particular", date.today(), date(2023, 12, 31), bibliotecas[1]))
    user.get_prestamos().append(Prestamo(user, PC(computadores[2], True, bibliotecas[1]), "Particular", date.today(), date(2023, 12, 31), bibliotecas[0]))

    user.get_multas().append(Multa("Retraso", date.today(), user, 3000))
    user.get_multas().append(Multa("Uso indebido", date.today(), user, 10000))

    sistema.set_autores(autores)
    sistema.set_bibliotecas(bibliotecas)
    sistema.set_computadores(computadores)
    sistema.set_libros(libros)
    sistema.set_user(user)

    
    Serializador.serializar(sistema)
    """
    ventanaInicial(sistema)