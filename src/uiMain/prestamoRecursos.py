from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import date
from gestorAplicacion.clasesDeAdministracion.Prestamo import Prestamo
from uiMain.FieldFrame import FieldFrame
from gestorExcepciones.erroresDeUsuario import *
from gestorExcepciones.erroresPython import *

class PrestamoRecursos(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#2b6fb8")
        self.root = root
        self.sistema = sistema
        

        self.frame1 = Frame(self, bg="white", borderwidth = 1, highlightbackground = "#2b6fb8", highlightcolor= "#2b6fb8")
        self.frame1.grid(row=0, column=0, padx=0)
        self.titulo = Label(self.frame1, text="Consulta de disponibilidad para prestamo", fg="black", bg="white", font=("Arial", 11))
        self.titulo.pack()
        self.frame2 = Frame(self, highlightbackground = "#2b6fb8")
        self.frame2.grid(row=1,column=0)
        self.desc =  """En esta opcion podras consultar la disponibilidad para prestamo de los diferentes recursos de la biblioteca, usando \ncriterios como Sede, Titulo, Autor, Fecha. Para de esta manera generar un prestamo en la biblioteca. """

        self.descripcion = Label(self.frame1, text=self.desc, fg="black", bg="white", font=("Arial", 11))
        self.descripcion.pack(side="left", fill="x", padx=100)

        self.frame3 = Frame(self, bg="white")
        self.frame3.grid(row=2,column=0)


        self.basica = Button(self.frame3, text="Busqueda básica", command=self.funcBusquedaBasica, font=("Arial", 11))
        self.porCriterio = Button(self.frame3, text= "Busqueda por criterios", command=self.funcBusquedaPorCriterio, font=("Arial", 11))
        self.porLista = Button(self.frame3, text= "Busqueda por lista", command=self.funcBusquedaPorLista, font=("Arial", 11))
        self.basica.grid(row=0,column=0, padx=50, pady=15)
        self.porCriterio.grid(row=0,column=1,padx=50, pady=15)
        self.porLista.grid(row=0, column=2, padx=50, pady=15)
        self.frame4 = busquedaBasica(self, self.sistema)
        self.frame4.grid(row = 3, column=0)
    def funcBusquedaBasica(self):
        self.kill(self.frame4)
        self.frame4 = busquedaBasica(self, self.sistema)
        self.frame4.grid(row = 3, column=0)

    def funcBusquedaPorCriterio(self):
        self.palabraLibro = StringVar(value="Libro")
        self.kill(self.frame4)
        self.opciones = ttk.Combobox(self.frame4, values=["Libro", "Computador"], textvariable=self.palabraLibro, foreground="white", state="readonly", font=("Arial", 11))
        self.opciones.grid(row=0,column=1)
        self.seleccione = Label(self.frame4, text="Seleccione el material que desea consultar: ", bg="white", fg="black", font=("Arial", 11))
        self.seleccione.grid(row=0,column=0, pady=5)
        
        def computadorOLibro(evento):
            if self.opciones.get() == "Libro":
                self.kill(self.frame4)
                self.frame4 = busquedaPorCriterio(self, "Criterios", ["Nombre", "ID", "ISBN", "Autor", "Año"], "Valor", self.sistema, "Libro")
                self.frame4.grid(row=3, column=0)
            else:
                self.kill(self.frame4)
                self.frame4 = busquedaPorCriterio(self, "Criterios", ["Modelo", "ID", "Marca", "Gama"], "Valor", self.sistema, "Computador")
                self.frame4.grid(row=3, column=0)
        self.opciones.bind("<<ComboboxSelected>>", computadorOLibro)

        
    def funcBusquedaPorLista(self):
        self.kill(self.frame4)
        self.frame4 = busquedaPorLista(self, self.sistema)
        self.frame4.grid(row = 3, column=0)

        def computadorOLibro(evento):
            if self.opciones.get() == "Libro":
                self.kill(self.frame4)
                self.frame4 = busquedaPorCriterio(self, "Criterios", ["Nombre", "ID", "ISBN", "Autor", "Año"], "Valor", self.sistema, "Libro")
                self.frame4.grid(row=3, column=0)
            else:
                self.kill(self.frame4)
                self.frame4 = busquedaPorCriterio(self, "Criterios", ["Modelo", "ID", "Marca", "Gama"], "Valor", self.sistema, "Computador")
                self.frame4.grid(row=3, column=0)

    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()


class busquedaBasica(Frame):
    def __init__(self, root, sistema):
        super().__init__(root, width=1100, height=700, bg="white", highlightbackground = "#2b6fb8", highlightcolor= "#2b6fb8")
        self.root = root
        self.sistema = sistema
        self.palabraLibro = StringVar(value="Libro")
        self.seleccione = Label(self, text="Seleccione el material que desea consultar: ", bg="white", fg="black", font=("Arial", 11))
        self.seleccione.grid(row=0,column=0, pady=5, sticky="w")
        def computadorOLibro(evento):
            if self.opciones.get() == "Libro":
                self.consulta.config(text="Ingrese el titulo del libro a consultar: ")
            else:
                self.consulta.config(text="Ingrese el modelo del computador a consultar: ")
        self.opciones = ttk.Combobox(self, values=["Libro", "Computador"], textvariable=self.palabraLibro, foreground="white", state="readonly")
        self.opciones.grid(row=0,column=1)
        self.opciones.bind("<<ComboboxSelected>>", computadorOLibro)
        self.consulta = Label(self,text="Ingrese el material a consultar: ", bg="white", fg="black", font=("Arial", 11), justify="left")
        self.consulta.grid(row=1,column=0, sticky="w")
        self.entrada = Entry(self, border=1, highlightthickness= 0, width=23)
        self.entrada.grid(row=1,column=1, pady=5)

        self.botonBuscar = Button(self, text="Buscar", command= self.confirmarExistencia, font=("Arial", 11))
        self.botonBuscar.grid(row=2,column=0, columnspan=1, padx=25, pady=5)
        self.botonLimpiar = Button(self, text="Limpiar campos", command= lambda: self.entrada.delete(0, 'end'), font=("Arial", 11))
        self.botonLimpiar.grid(row=2,column=1, columnspan=1, padx=5, pady=5)

    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

    def confirmarExistencia(self):
        nombre = str(self.entrada.get())
        if self.opciones.get() == "Libro":
            try:
                for libro in self.sistema.get_libros():
                    if str(nombre) == libro.get_nombre():
                        respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{libro.get_nombre()}'?")
                        if not respuesta: 
                            return 
                        else:
                            self.reservarLibro(libro)
                            return
                    elif nombre == "":
                        raise CampoVacio 
                raise libroNoEncontrado(nombre)
            except CampoVacio:
                    return messagebox.showerror("Error",CampoVacio().getError())
            except libroNoEncontrado:
                    return messagebox.showerror("Error",libroNoEncontrado(nombre).getError())
        else:      
            try:
                for computador in self.sistema.get_computadores():
                    if nombre == computador.get_nombre():
                        respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{computador.get_nombre()}'?")
                        if not respuesta: 
                            return 
                        else:
                            self.reservarComputador(computador)
                            return
                    elif nombre == "":
                        raise Exception
                raise ComputadorNoEncontrado(nombre)
            except CampoVacio:
                return messagebox.showerror("Error",CampoVacio().getError())
            except ComputadorNoEncontrado:
                return messagebox.showerror("Error",ComputadorNoEncontrado(nombre).getError())
        

    def reservarLibro(self, recurso):
            try:
                sedes = []
                self.entrada.config(state="disabled")
                self.opciones.config(state="disabled")
                for biblioteca in self.sistema.get_bibliotecas():
                    for copia in biblioteca.get_copias():
                        if recurso.get_nombre() == copia.get_nombre() and biblioteca.get_nombre() not in sedes:
                            sedes.append(biblioteca.get_nombre())
                if not sedes:
                    raise NoHayCopia(recurso)
                Label(self, text="Reserva de recurso", font=("Arial", 15), bg="white", fg="black").grid(row=3, column=0, columnspan=2, pady= (7,1))
                Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=4,column=0, columnspan=2, pady=5)
                opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly", font=("Arial", 11))
                opcionSede.grid(row=5, column=0, columnspan=2) 
                sedeSeleccionada = date.today()                            
                hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
                hur.grid(row=6,column=0, columnspan=2)
                cal = Calendar(self, mindate=date.today())
                cal.grid(row=7,column=0, columnspan=2)

                fechaSeleccionada = date.today()    
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
                            copiaSel = copia 
                    self.sistema.get_user().get_prestamos().append(Prestamo(self.sistema.get_user(), copiaSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                    sedeSel.get_copias().remove(copiaSel)
                    messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                    self.kill(self)
                botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
                botonReservar.grid(row=8, column=0, columnspan=2, pady=5)
            except NoHayCopia: 
                return messagebox.showerror("Error",NoHayCopia(recurso).getError())

    def reservarComputador(self, recurso):
        try:
            sedes = []
            self.entrada.config(state="readonly")
            for biblioteca in self.sistema.get_bibliotecas():
                for pc in biblioteca.get_PCs():
                    if recurso.get_nombre() == pc.get_nombre() and biblioteca.get_nombre() not in sedes:
                        sedes.append(biblioteca.get_nombre())
            if not sedes:
                    raise NoHayPC(recurso)
            Label(self, text="Reserva de recurso", font=("Arial", 15), bg="white", fg="black").grid(row=3, column=0, columnspan=2, pady= (7,1))
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black").grid(row=4,column=0, columnspan=2, pady=5)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
            opcionSede.grid(row=5, column=0, columnspan=2) 
            sedeSeleccionada = date.today()                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black")
            hur.grid(row=6,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=7,column=0, columnspan=2)

            self.fechaSeleccionada = date.today()    
            def seleccionarFecha(event):
                self.fechaSeleccionada = cal.get_date()
            cal.bind("<<CalendarSelected>>", seleccionarFecha)

            def realizarReserva():
                sedeSel = opcionSede.get()
                for sede in self.sistema.get_bibliotecas():
                    if sede.get_nombre() == sedeSel:
                        sedeSel = sede
                for pc in sedeSel.get_PCs():
                    if pc.get_nombre() == recurso.get_nombre():
                        copiaSel = pc 
                self.sistema.get_user().get_prestamos().append(Prestamo(self.sistema.get_user(), copiaSel, "Particular", date.today(), self.fechaSeleccionada, sedeSel))
                sedeSel.get_PCs().remove(copiaSel)
                messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                self.kill(self)
                    
            botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
            botonReservar.grid(row=8, column=0, columnspan=2, pady=5)

        except NoHayPC:
            return messagebox.showerror("Error", NoHayPC(recurso).getError())


class busquedaPorCriterio(FieldFrame):
    
    def __init__(self, root, criteriosTitulo, lista, valorTitulo, sistema, recurso):
        super().__init__(root, criteriosTitulo, lista, valorTitulo)
        self.sistema = sistema
        self.recurso = recurso
        self.crearBoton("Guardar", self.comprobar, 0)

    def comprobar(self):
        libroSel = None
        computadorSel = None
        if (len(self.valores) < len(self.criterios)):
            for i in range(len(self.criterios)):
                self.valores.append(self.entradas[i].get())
        if self.recurso == "Libro":
            try:
                if "" in self.valores:
                    raise CampoVacio
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
                self.reservarLibro(libroSel)
            except CampoVacio:
                self.valores = []
                return messagebox.showerror("Error", CampoVacio().getError())
            except NingunRecurso:
                return messagebox.showerror("Error", NingunRecurso().getError())
        else: 
            try:
                if "" in self.valores:
                    raise CampoVacio
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
                self.reservarComputador(computadorSel)
            except CampoVacio:
                self.valores = []
                return messagebox.showerror("Error", CampoVacio().getError())
            except NingunRecurso:
                return messagebox.showerror("Error", NingunRecurso().getError())
    
    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()
        

    def reservarLibro(self, recurso):
            try: 
                sedes = []
                for biblioteca in self.sistema.get_bibliotecas():
                    for copia in biblioteca.get_copias():
                        if recurso.get_nombre() == copia.get_nombre() and biblioteca.get_nombre() not in sedes:
                            sedes.append(biblioteca.get_nombre())
                if not sedes: 
                    raise NoHayCopia(recurso)
                Label(self, text="Reserva de recurso", font=("Arial", 11), bg="white", fg="black").grid(row=3, column=0, columnspan=2)
                Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=4,column=0, columnspan=2, pady=5)
                opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
                opcionSede.grid(row=5, column=0, columnspan=2) 
                sedeSeleccionada = date.today()                            
                hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
                hur.grid(row=6,column=0, columnspan=2)
                cal = Calendar(self, mindate=date.today())
                cal.grid(row=7,column=0, columnspan=2)

                fechaSeleccionada = date.today()    
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
                            copiaSel = copia 
                    self.sistema.get_user().get_prestamos().append(Prestamo(self.sistema.get_user(), copiaSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                    sedeSel.get_copias().remove(copiaSel)
                    messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                    self.kill(self)

                botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
                botonReservar.grid(row=8, column=0, columnspan=2, pady=5)
            except NoHayCopia:
                messagebox.showerror("Error", NoHayCopia(recurso).getError)

    def reservarComputador(self, recurso):
        try:
            sedes = []
            for biblioteca in self.sistema.get_bibliotecas():
                for pc in biblioteca.get_PCs():
                    if recurso.get_nombre() == pc.get_nombre() and biblioteca.get_nombre() not in sedes:
                        sedes.append(biblioteca.get_nombre())
            if not sedes:
                raise NoHayPC(recurso)
            Label(self, text="Reserva de recurso", font=("Arial", 11), bg="white", fg="black").grid(row=3, column=0, columnspan=2)
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=4,column=0, columnspan=2, pady=5)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
            opcionSede.grid(row=5, column=0, columnspan=2) 
            sedeSeleccionada = date.today()                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
            hur.grid(row=6,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=7,column=0, columnspan=2)

            fechaSeleccionada = date.today()    
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
                        copiaSel = pc 
                self.sistema.get_user().get_prestamos().append(Prestamo(self.sistema.get_user(), copiaSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                sedeSel.get_PCs().remove(copiaSel)
                messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                self.kill(self)
                    
            botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
            botonReservar.grid(row=8, column=0, columnspan=2, pady=5)
        except NoHayPC:
            messagebox.showerror("Error", NoHayPC(recurso).getError())
class busquedaPorLista(Frame):
    def __init__(self, root, sistema):
        super().__init__(root, width=1100, height=700, bg="white", highlightbackground = "#2b6fb8", highlightcolor= "#2b6fb8")
        self.root = root
        self.sistema = sistema
        self.palabraLibro = StringVar(value="Libro")
        self.seleccione = Label(self, text="Seleccione el material que desea consultar: ", bg="white", fg="black", font=("Arial", 11))
        self.seleccione.grid(row=0,column=0, pady=5)
        self.opciones = ttk.Combobox(self, values=["Libro", "Computador"], textvariable=self.palabraLibro, foreground="white", state="readonly", font=("Arial", 11))
        self.opciones.grid(row=0,column=1)
        self.opciones.bind("<<ComboboxSelected>>", self.computadorOLibro)
    
    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()


    def computadorOLibro(self, evento):
        if self.opciones.get() == "Libro":
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
            Label(self, text="Reserva de recurso", font=("Arial", 20), bg="white", fg="black").grid(row=0, column=0, columnspan=2, pady= (7,1))
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=1,column=0, columnspan=2, pady=5)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly", font=("Arial", 11))
            opcionSede.grid(row=2, column=0, columnspan=2) 
            sedeSeleccionada = date.today()                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black")
            hur.grid(row=3,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=4,column=0, columnspan=2)

            fechaSeleccionada = date.today()    
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
                        copiaSel = copia 
                self.sistema.get_user().get_prestamos().append(Prestamo(self.sistema.get_user(), copiaSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                sedeSel.get_copias().remove(copiaSel)
                messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                self.kill(self)
                
            botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
            botonReservar.grid(row=5, column=0, columnspan=2, pady=5)

        except (IndexError, IndexFuera):
            messagebox.showerror("Error", IndexFuera().getError())
        except ValueError:
            messagebox.showerror("Error", DatoIncorrecto("Numero").getError())
        except NoHayCopia:
            messagebox.showerror("Error", NoHayCopia(NoHayCopia(self.libroSel.get_nombre())).getError())

    
    
    
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
            Label(self, text="Reserva de recurso", font=("Arial", 20), bg="white", fg="black").grid(row=0, column=0, columnspan=2, pady= (7,1))
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11)).grid(row=1,column=0, columnspan=2, pady=5)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
            opcionSede.grid(row=2, column=0, columnspan=2) 
            sedeSeleccionada = date.today()                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black", font=("Arial", 11))
            hur.grid(row=3,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=4,column=0, columnspan=2)

            fechaSeleccionada = date.today()    
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
                self.sistema.get_user().get_prestamos().append(Prestamo(self.sistema.get_user(), pcSel, "Particular", date.today(), fechaSeleccionada, sedeSel))
                sedeSel.get_PCs().remove(pcSel)
                messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                self.kill(self)
                            
            botonReservar = Button(self, text="Reservar", command=realizarReserva, font=("Arial", 11))
            botonReservar.grid(row=5, column=0, columnspan=2, pady=5)
            

        except (IndexError, IndexFuera):
            messagebox.showerror("Error", IndexFuera().getError())
        except ValueError:
            messagebox.showerror("Error", DatoIncorrecto("Numero").getError())
        except NoHayPC:
            messagebox.showerror("Error", NoHayPC(self.computadorSel.get_nombre()).getError())