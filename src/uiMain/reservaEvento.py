from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.clasesDeAdministracion.Prestamo import Prestamo
from datetime import date
from uiMain.FieldFrame import FieldFrame
from tkcalendar import Calendar
from gestorExcepciones.erroresDeUsuario import *
from gestorExcepciones.erroresPython import * 

class ReservaEvento(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]


        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Reserva de sala para evento", fg="black", bg="white", font=("Arial", 11))
        titulo.pack()


        frame2 = Frame(self)
        frame2.grid(row=1,column=0)
        descripcion = """En esta opcion podras realizar una reserva de evento en una de las salas de nuestras bibliotecas, ademas 
        de esto, podras reservar material que pueda ser de utilidad en tu evento"""
        
        Label(frame2, text=descripcion, bg="white", fg="black", font=("Arial", 11)).grid(row=0,column=0)

        self.frame3 = Frame(self, bg="white")
        self.frame3.grid(row=2,column=0)
        self.basica = Button(self.frame3, text="Busqueda básica", command=self.funcBusquedaBasica, font=("Arial", 11))
        self.porCriterio = Button(self.frame3, text= "Busqueda por criterios", command=self.funcBusquedaPorCriterio, font=("Arial", 11))
        self.porLista = Button(self.frame3, text= "Busqueda por lista", command=self.funcBusquedaPorLista, font=("Arial", 11))
        self.basica.grid(row=0,column=0, padx=50, pady=15)
        self.porCriterio.grid(row=0,column=1,padx=50, pady=15)
        self.porLista.grid(row=0, column=2, padx=50, pady=15)
        self.frame4 = Frame(self)


    def funcBusquedaBasica(self):
        self.kill(self.frame4)
        self.frame4 = BusquedaBasica(self, self.sistema)
        self.frame4.grid(row=3, column=0)

    def funcBusquedaPorCriterio(self):
        self.kill(self.frame4)
        self.frame4 = BusquedaPorCriterio(self, self.sistema)
        self.frame4.grid(row=3, column=0)

    def funcBusquedaPorLista(self):
        self.kill(self.frame4)
        self.frame4 = BusquedaPorLista(self, self.sistema)
        self.frame4.grid(row=3, column=0)


    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

class BusquedaBasica(Frame):
    def __init__(self, root, sistema):
        super().__init__(root, width=1100, height=700, bg="white")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]
        self.palabraLibro = StringVar(value="Libro")
        Label(self, text= "Seleccione la sede en la que desea realizar su evento: ", bg="white", font=("Arial", 11)).grid(row=0, column=0, pady=5)
        self.sedeSel = None 
        self.sedeSelObj = None
        self.salaSelObj = None
        self.salas = ttk.Combobox(self, values=self.nombreSedes, foreground="black", state="readonly", font=("Arial", 11))
        self.salas.grid(row=0,column=1)
        self.salas.bind("<<ComboboxSelected>>", func= self.sede)

    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

    def sede(self, event):
        self.sedeSel = self.salas.get()
        for biblioteca in self.sistema.get_bibliotecas():
                if biblioteca.get_nombre() == self.sedeSel:
                  self.sedeSelObj = biblioteca     
        Label(self, text="Las salas disponibles para evento en esta biblioteca son:", bg= "white", font=("Arial", 11)).grid(row=1, column=0, pady=5)
        self.opciones = ttk.Combobox(self, values=self.sedeSelObj.get_salas(), font=("Arial", 11), state="readonly")
        self.opciones.grid(row=1, column=1)
        self.opciones.bind("<<ComboboxSelected>>", func= self.sala)

    def sala(self, evento):
        self.salaSel = self.opciones.get()
        for sala in self.sedeSelObj.get_salas():
                if sala.get_nombre() == self.salaSel:
                  self.salaSelObj = sala
        confirmacion = messagebox.askyesno(title= "Confirmación", message=f"Deseas Reservar el {self.salaSelObj.get_nombre()} con capacidad para {int(self.salaSelObj.get_capacidad())} personas?")
        if not confirmacion:
            return
        Label(self, text="Seleccione el material que desea reservar para el evento: ", font=("Arial", 11), bg= "white").grid(row=2, column=0, pady=5)
        self.opcionMaterial = ttk.Combobox(self, values=["Libro", "Computador"], font=("Arial", 11), state="readonly")
        self.opcionMaterial.grid(row=2, column=1)
        self.opcionMaterial.bind("<<ComboboxSelected>>", func= self.buscar)

    def buscar(self, evento):
        opcionEscogida = self.opcionMaterial.get()
        self.lab = Label(self, text="", font=("Arial", 11), bg= "white", width=50)
        self.lab.grid(row=3, column=0, pady=5)
        self.computador = Entry(self, font=("Arial", 11), width=22)
        self.libro = Entry(self, font=("Arial", 11), width=22)
        if opcionEscogida == "Libro":
            self.lab.config(text="Ingrese el titulo del libro que desea reservar: ")
            self.libro = Entry(self, font=("Arial", 11), width=22)
            self.libro.grid(row=3,column=1)
            Button(self, text= "Buscar", command= self.reservarLibro, font=("Arial", 11)).grid(row=4, column=0, pady=5)
        else:
            self.lab.config(text="Ingrese el modelo del computador que desea reservar: ")
            self.computador = Entry(self, font=("Arial", 11), width=22)
            self.computador.grid(row=3,column=1)
            Button(self, text= "Buscar", command= self.reservarComputador, font=("Arial", 11)).grid(row=4, column=0, pady=5)
            

    def reservarLibro(self):
        self.computador.destroy()
        libroSel = None 
        try:
            if self.libro.get() == "":
                raise CampoVacio
            for lib in self.sistema.get_libros():
                    if lib.get_nombre() == self.libro.get():
                        confirmacion = messagebox.askyesno(title= "Confirmación", message=f"¿Deseas reservar el libro {self.libro.get()} en tu evento?")
                        if not confirmacion:
                            return
                        else:
                            libroSel = lib
            if not libroSel:
                raise libroNoEncontrado(self.libro.get())
                #messagebox.showerror(title="Error", message="El libro no existe")
            for copia in self.sedeSelObj.get_copias():
                if copia.get_nombre() == libroSel.get_nombre():
                    self.copiaSel = copia
            if not self.copiaSel:
                raise NoHayCopia(libroSel.get_nombre())
            prestamo = Prestamo(self.sistema.get_user(), self.copiaSel, "Evento", date.today(), date.today(), self.sedeSelObj)
            self.sistema.get_user().get_prestamos().append(prestamo)
            self.sedeSelObj.get_copias().remove(self.copiaSel)
            messagebox.askokcancel(title="Reserva realizada", message="¡Reserva realizada con exito! Mucha suerte en tu evento :)")
            self.kill(self)

        except CampoVacio:
            messagebox.showerror("Error", CampoVacio().getError())
        except libroNoEncontrado:
            messagebox.showerror("Error", libroNoEncontrado(self.libro.get()).getError())
        except NoHayCopia:
            messagebox.showerror("Error", NoHayCopia(libroSel.get_nombre()).getError())
        except AttributeError:
            messagebox.showerror("Error", NoHayCopia(libroSel.get_nombre()).getError())


    def reservarComputador(self):
        self.libro.destroy()
        computadorSel = None 
        try:
            if self.computador.get() == "":
                raise CampoVacio
            for pc in self.sistema.get_computadores():
                    if pc.get_nombre() == self.computador.get():
                        confirmacion = messagebox.askyesno(title= "Confirmación", message=f"¿Deseas reservar el computador {self.computador.get()} en tu evento?")
                        if not confirmacion:
                            return
                        else:
                            computadorSel = pc
            if not computadorSel:
                raise ComputadorNoEncontrado(self.computador.get())
            for pc in self.sedeSelObj.get_PCs():
                if pc.get_nombre() == computadorSel.get_nombre():
                    pcSel = pc
            if not pcSel:
                raise NoHayPC(computadorSel.get_nombre())
            prestamo = Prestamo(self.sistema.get_user(), pcSel, "Evento", date.today(), date.today(), self.sedeSelObj)
            self.sistema.get_user().get_prestamos().append(prestamo)
            self.sedeSelObj.get_PCs().remove(pcSel)
            messagebox.askokcancel(title="Reserva realizada", message="¡Reserva realizada con exito! Mucha suerte en tu evento :)")
            self.kill(self)
        except CampoVacio:
            messagebox.showerror("Error", CampoVacio().getError())
        except ComputadorNoEncontrado:
            messagebox.showerror("Error", ComputadorNoEncontrado(self.computador.get()).getError())
        except NoHayCopia:
            messagebox.showerror("Error", NoHayPC(computadorSel.get_nombre()).getError())
        except AttributeError:
            messagebox.showerror("Error", NoHayPC(self.computador.get()).getError())

class BusquedaPorCriterio(Frame):
    def __init__(self, root, sistema):
        super().__init__(root, width=1100, height=700, bg="white")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]
        self.palabraLibro = StringVar(value="Libro")
        Label(self, text= "Seleccione la sede en la que desea realizar su evento: ", bg="white", font=("Arial", 11)).grid(row=0, column=0, pady=5)
        self.sedeSel = None 
        self.sedeSelObj = None
        self.salaSelObj = None
        self.salas = ttk.Combobox(self, values=self.nombreSedes, foreground="black", state="readonly", font=("Arial", 11))
        self.salas.grid(row=0,column=1)
        self.salas.bind("<<ComboboxSelected>>", func= self.sede)
    

    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()


    def sede(self, event):
        self.sedeSel = self.salas.get()
        for biblioteca in self.sistema.get_bibliotecas():
                if biblioteca.get_nombre() == self.sedeSel:
                  self.sedeSelObj = biblioteca     
        Label(self, text="Las salas disponibles para evento en esta biblioteca son:", font=("Arial", 11), bg= "white").grid(row=1, column=0, pady=5)
        self.opciones = ttk.Combobox(self, values=self.sedeSelObj.get_salas(), font=("Arial", 11), state="readonly")
        self.opciones.grid(row=1, column=1)
        self.opciones.bind("<<ComboboxSelected>>", func= self.sala)

    def sala(self, evento):
        self.salaSel = self.opciones.get()
        for sala in self.sedeSelObj.get_salas():
                if sala.get_nombre() == self.salaSel:
                  self.salaSelObj = sala
        confirmacion = messagebox.askyesno(title= "Confirmación", message=f"Deseas Reservar el {self.salaSelObj.get_nombre()} con capacidad para {int(self.salaSelObj.get_capacidad())} personas?")
        if not confirmacion:
            return
        Label(self, text="Seleccione el material que desea reservar para el evento: ", font=("Arial", 11), bg= "white").grid(row=2, column=0, pady=5)
        self.opcionMaterial = ttk.Combobox(self, values=["Libro", "Computador"], font=("Arial", 11), state="readonly")
        self.opcionMaterial.grid(row=2, column=1)
        self.opcionMaterial.bind("<<ComboboxSelected>>", func= self.crearFields)
        self.frameCriterios = Frame()

    def crearFields(self, evento):
        self.kill(self.frameCriterios)
        if self.opcionMaterial.get() == "Libro":
            self.frameCriterios = FieldFrame(self, "Criterios", ["Nombre", "ID", "ISBN", "Autor", "Año"], "Valor")
            self.frameCriterios.grid(row=3, column=0, columnspan=2)
            self.frameCriterios.crearBoton("Buscar", self.buscar, 0)  
        else:
            self.frameCriterios = FieldFrame(self, "Criterios", ["Modelo", "ID", "Marca", "Gama"], "Valor")
            self.frameCriterios.grid(row=3, column=0, columnspan=2)
            self.frameCriterios.crearBoton("Buscar", self.buscar, 0)
            

    def buscar(self):
        libroSel = None
        computadorSel = None
        self.frameCriterios.getValores()
        self.valores = self.frameCriterios.valores
        try: 
            if "" in self.valores:
                raise CampoVacio
            if self.opcionMaterial.get() == "Libro":
                self.valores = self.frameCriterios.valores
                for libro in self.sistema.get_libros():
                    if (libro.get_nombre() == self.valores[0]) and (str(libro.get_id_recurso()) == self.valores[1]) and (libro.get_isbn() == self.valores[2]) and (libro.get_autor().get_nombre() == self.valores[3]) and (str(libro.get_año()) == self.valores[4]):
                        libroSel = libro
                        respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{libroSel.get_nombre()}'?")
                        if not respuesta: 
                            self.valores = []
                            return
                if not libroSel:
                    self.valores = []
                    raise NingunRecurso
                self.kill(self)
                self.reservarRecurso(libroSel)
            else:
                self.frameCriterios.getValores()
                self.valores = self.frameCriterios.valores
                for computador in self.sistema.get_computadores():
                    if (computador.get_nombre() == self.valores[0]) and (str(computador.get_id_recurso()) == self.valores[1]) and (computador.get_marca() == self.valores[2]) and (computador.get_gama() == self.valores[3]):
                        computadorSel = computador
                        respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{computadorSel.get_nombre()}'?")
                        if not respuesta: 
                            self.valores = []
                            return
                if not computadorSel:
                    self.valores = []
                    raise NingunRecurso
                self.kill(self)
                self.reservarRecurso(computadorSel)
        except CampoVacio:
            self.valores = []
            messagebox.showerror("Error", CampoVacio().getError())
        except NingunRecurso:
            self.valores = []
            messagebox.showerror("Error", NingunRecurso().getError())
        except TypeError:
            self.valores = []
            messagebox.showerror("Error", CampoVacio().getError())


    def reservarRecurso(self, recurso):
        try:
            sedes = []
            if recurso.tipo_recurso() == "Libro":
                for biblioteca in self.sistema.get_bibliotecas():
                    for copia in biblioteca.get_copias():
                        if recurso.get_nombre() == copia.get_nombre() and biblioteca.get_nombre() not in sedes:
                            sedes.append(biblioteca.get_nombre())
                if not sedes:
                    raise NoHayCopia(recurso)
                Label(self, text="Reserva de recurso", font=("Arial", 15), bg="white", fg="black").grid(row=3, column=0, columnspan=2)
                Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=4,column=0, columnspan=2, pady=5)
                opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
                opcionSede.grid(row=5, column=0, columnspan=2) 
                sedeSeleccionada = None                            
                hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
                hur.grid(row=6,column=0, columnspan=2)
                cal = Calendar(self, mindate=date.today())
                cal.grid(row=7,column=0, columnspan=2)
                self.copiaSel = None
                fechaSeleccionada = None
                def seleccionarFecha(event):
                    global fechaSeleccionada
                    fechaSeleccionada = cal.get_date()
                cal.bind("<<CalendarSelected>>", seleccionarFecha)

                def realizarReserva():
                    sedeSel = opcionSede.get()
                    for sede in self.sistema.get_bibliotecas():
                        if sede.get_nombre() == sedeSel:
                            sedeSel = sede
                    for copia in sedeSel.get_copias():
                        if copia.get_nombre() == recurso.get_nombre():
                            self.copiaSel = copia 
                    self.sistema.get_user().get_multas().append(Prestamo(self.sistema.get_user(), self.copiaSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                    sedeSel.get_copias().remove(self.copiaSel)
                    messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                    self.kill(self)
                        
                botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
                botonReservar.grid(row=8, column=0, columnspan=2)
            else:
                for biblioteca in self.sistema.get_bibliotecas():
                    for pc in biblioteca.get_PCs():
                        if recurso.get_nombre() == pc.get_nombre() and biblioteca.get_nombre() not in sedes:
                            sedes.append(biblioteca.get_nombre())
                if not sedes:
                    raise NoHayPC(recurso)
                Label(self, text="Reserva de recurso", font=("Arial", 15), bg="white", fg="black").grid(row=3, column=0, columnspan=2)
                Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=4,column=0, columnspan=2, pady=5)
                opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
                opcionSede.grid(row=5, column=0, columnspan=2) 
                sedeSeleccionada = None                            
                hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
                hur.grid(row=6,column=0, columnspan=2)
                cal = Calendar(self, mindate=date.today())
                cal.grid(row=7,column=0, columnspan=2)
                self.pcSel = None
                fechaSeleccionada = None
                def seleccionarFecha(event):
                    global fechaSeleccionada
                    fechaSeleccionada = cal.get_date()
                cal.bind("<<CalendarSelected>>", seleccionarFecha)

                def realizarReserva():
                    sedeSel = opcionSede.get()
                    for sede in self.sistema.get_bibliotecas():
                        if sede.get_nombre() == sedeSel:
                            sedeSel = sede
                    for pc in sedeSel.get_PCs():
                        if pc.get_nombre() == recurso.get_nombre():
                            self.pcSel = pc 
                    self.sistema.get_user().get_multas().append(Prestamo(self.sistema.get_user(), self.pcSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                    sedeSel.get_PCs().remove(self.pcSel)
                    messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                    self.kill(self)
                botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
                botonReservar.grid(row=8, column=0, columnspan=2)
        except NoHayPC:
            messagebox.showerror("Error", NoHayPC(recurso).getError())

class BusquedaPorLista(Frame):
    def __init__(self, root, sistema):
        super().__init__(root, width=1100, height=700, bg="white")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]
        self.palabraLibro = StringVar(value="Libro")
        Label(self, text= "Seleccione la sede en la que desea realizar su evento: ", bg="white", font=("Arial", 11)).grid(row=0, column=0, pady=5)
        self.sedeSel = None 
        self.sedeSelObj = None
        self.salaSelObj = None
        self.salas = ttk.Combobox(self, values=self.nombreSedes, foreground="black", state="readonly", font=("Arial", 11))
        self.salas.grid(row=0,column=1)
        self.salas.bind("<<ComboboxSelected>>", func= self.sede)
    
    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

    def sede(self, event):
        self.sedeSel = self.salas.get()
        for biblioteca in self.sistema.get_bibliotecas():
                if biblioteca.get_nombre() == self.sedeSel:
                  self.sedeSelObj = biblioteca     
        Label(self, text="Las salas disponibles para evento en esta biblioteca son:", font=("Arial", 11), bg= "white").grid(row=1, column=0, pady=5)
        self.opciones = ttk.Combobox(self, values=self.sedeSelObj.get_salas(), font=("Arial", 11), state="readonly")
        self.opciones.grid(row=1, column=1)
        self.opciones.bind("<<ComboboxSelected>>", func= self.sala)

    def sala(self, evento):
        self.salaSel = self.opciones.get()
        for sala in self.sedeSelObj.get_salas():
                if sala.get_nombre() == self.salaSel:
                  self.salaSelObj = sala
        confirmacion = messagebox.askyesno(title= "Confirmación", message=f"Deseas Reservar el {self.salaSelObj.get_nombre()} con capacidad para {int(self.salaSelObj.get_capacidad())} personas?")
        if not confirmacion:
            return
        Label(self, text="Seleccione el material que desea reservar para el evento: ", font=("Arial", 11), bg= "white").grid(row=2, column=0, pady=5)
        self.opcionMaterial = ttk.Combobox(self, values=["Libro", "Computador"], font=("Arial", 11), state="readonly")
        self.opcionMaterial.grid(row=2, column=1)
        self.opcionMaterial.bind("<<ComboboxSelected>>", func= self.computadorOLibro)

    def computadorOLibro(self, evento):
        if self.opcionMaterial.get() == "Libro":
            self.kill(self)
            Label(self, text="Seleccione un libro de la siguiente lista: ", font=("Arial", 11), bg="white").grid(row=1,column=0, columnspan=2, pady=5)
            lista = Text(self, border=False, font=("Arial", 11), borderwidth=2, highlightthickness=3, highlightbackground="gray")
            lista.grid(row=2, column=0, columnspan=2, pady=5)
            lista.delete("1.0", "end")
            listaLibros = [libro.get_nombre() for libro in self.sistema.get_libros()]
            lista.config(height=10)
            listaLibrosString = ""
            for i, titulo in enumerate(listaLibros):
                listaLibrosString += f"{i}. {titulo} \n"
            lista.insert(INSERT, listaLibrosString)
            self.seleccion = FieldFrame(self, "Criterio", ["ID: "], "Valor")
            self.seleccion.grid(row=3, column =0, columnspan=2, pady=5)
            self.seleccion.crearBoton("Enviar", self.reservarLibro, 0)
        else:
            self.kill(self)
            Label(self, text="Seleccione un computador de la siguiente lista: ", font=("Arial", 11), bg="white").grid(row=1,column=0, columnspan=2, pady=5)
            lista = Text(self, border=False, font=("Arial", 11), borderwidth=2, highlightthickness=3, highlightbackground="gray")
            lista.grid(row=2, column=0, columnspan=2, pady=5)
            lista.delete("1.0", "end")
            listaComputadores = [computador.get_nombre() for computador in self.sistema.get_computadores()]
            lista.config(height=10)
            listaComputadoresString = ""
            for i, titulo in enumerate(listaComputadores):
                listaComputadoresString += f"{i}. {titulo} \n"
            lista.insert(INSERT, listaComputadoresString)
            self.seleccion = FieldFrame(self, "Criterio", ["ID: "], "Valor")
            self.seleccion.grid(row=3, column =0, columnspan=2, pady=5)
            self.seleccion.crearBoton("Enviar", self.reservarComputador, 0)
    
    def reservarLibro(self):
        self.LibroSel = None
        try: 
            if self.seleccion.getValue("ID: ") == "":
                raise CampoVacio
        except CampoVacio:
            return messagebox.showerror("Error", CampoVacio().getError())
        try:
            if int(self.seleccion.getValue("ID: ")) < 0:
                raise IndexFuera
            self.libroSel = self.sistema.get_libros()[int(self.seleccion.getValue("ID: "))]
            sedes = []
            self.kill(self)
            for biblioteca in self.sistema.get_bibliotecas():
                for copia in biblioteca.get_copias():
                    if self.libroSel.get_nombre() == copia.get_nombre() and biblioteca.get_nombre() not in sedes:
                        sedes.append(biblioteca.get_nombre())
            if not sedes: 
                raise NoHayCopia(self.libroSel.get_nombre())
            Label(self, text="Reserva de recurso", font=("Arial", 15), bg="white", fg="black").grid(row=0, column=0, columnspan=2)
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=1,column=0, columnspan=2, pady=5)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly", font=("Arial", 11))
            opcionSede.grid(row=2, column=0, columnspan=2) 
            sedeSeleccionada = None                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
            hur.grid(row=3,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=4,column=0, columnspan=2)

            fechaSeleccionada = None
            def seleccionarFecha(event):
                global fechaSeleccionada
                fechaSeleccionada = cal.get_date()
            cal.bind("<<CalendarSelected>>", seleccionarFecha)

            def realizarReserva():
                sedeSel = opcionSede.get()
                for sede in self.sistema.get_bibliotecas():
                    if sede.get_nombre() == sedeSel:
                        sedeSel = sede
                for copia in sedeSel.get_copias():
                    if copia.get_nombre() == self.libroSel.get_nombre():
                        self.copiaSel = copia 
                self.sistema.get_user().get_multas().append(Prestamo(self.sistema.get_user(), self.copiaSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                sedeSel.get_copias().remove(self.copiaSel)
                messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                self.kill(self)
            botonReservar = Button(self, text="Reservar", command=realizarReserva)
            botonReservar.grid(row=5, column=0, columnspan=2)

        except (IndexError, IndexFuera):
            messagebox.showerror("Error", IndexFuera().getError())
        except ValueError:
            messagebox.showerror("Error", DatoIncorrecto("Numero").getError())
        except NoHayCopia:
            messagebox.showerror("Error", NoHayPC(self.libroSel.get_nombre()).getError())


            

    
    
    
    def reservarComputador(self):
        self.computadorSel = None
        try: 
            if self.seleccion.getValue("ID: ") == "":
                raise CampoVacio
        except CampoVacio:
            return messagebox.showerror("Error", CampoVacio().getError())
        try:
            if int(self.seleccion.getValue("ID: ")) < 0:
                raise IndexFuera
            self.computadorSel = self.sistema.get_computadores()[int(self.seleccion.getValue("ID: "))]
            sedes = []
            self.kill(self)
            for biblioteca in self.sistema.get_bibliotecas():
                for pc in biblioteca.get_PCs():
                    if self.computadorSel.get_nombre() == pc.get_nombre() and biblioteca.get_nombre() not in sedes:
                        sedes.append(biblioteca.get_nombre())
            if not sedes:
                raise NoHayPC(self.computadorSel.get_nombre())
            Label(self, text="Reserva de recurso", font=("Arial", 15), bg="white", fg="black").grid(row=0, column=0, columnspan=2)
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=1,column=0, columnspan=2, pady=5)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly", font=("Arial", 11))
            opcionSede.grid(row=2, column=0, columnspan=2) 
            sedeSeleccionada = None                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
            hur.grid(row=3,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=4,column=0, columnspan=2)

            fechaSeleccionada = None
            def seleccionarFecha(event):
                global fechaSeleccionada
                fechaSeleccionada = cal.get_date()
            cal.bind("<<CalendarSelected>>", seleccionarFecha)

            def realizarReserva():
                sedeSel = opcionSede.get()
                for sede in self.sistema.get_bibliotecas():
                    if sede.get_nombre() == sedeSel:
                        sedeSel = sede
                for pc in sedeSel.get_PCs():
                    if pc.get_nombre() == self.computadorSel.get_nombre():
                        pcSel = pc
                self.sistema.get_user().get_multas().append(Prestamo(self.sistema.get_user(), pcSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                sedeSel.get_PCs().remove(pcSel)
                messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                self.kill(self)
            botonReservar = Button(self, text="Reservar", command=realizarReserva)
            botonReservar.grid(row=5, column=0, columnspan=2)
            
        except (IndexError, IndexFuera):
            messagebox.showerror("Error", IndexFuera().getError())
        except ValueError:
            messagebox.showerror("Error", DatoIncorrecto("Numero").getError())
        except NoHayPC:
            messagebox.showerror("Error", NoHayPC(self.computadorSel.get_nombre()).getError())




        





