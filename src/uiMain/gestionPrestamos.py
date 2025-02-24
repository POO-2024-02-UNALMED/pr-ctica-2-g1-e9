from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.clasesDeAdministracion.Prestamo import Prestamo
from gestorAplicacion.clasesDeBiblioteca.Copia import Copia
from gestorAplicacion.clasesDeBiblioteca.PC import PC
from datetime import date
from uiMain.FieldFrame import FieldFrame
from tkcalendar import Calendar
from gestorExcepciones.erroresPython import *
from gestorExcepciones.erroresDeUsuario import *

class GestionPrestamo(Frame):

    def _init_(self, root, sistema):
        super()._init_(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]


        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Gestion de prestamos", fg="black", bg="white", font=("Arial", 11))
        titulo.pack()


        frame2 = Frame(self)
        frame2.grid(row=1,column=0)
        descripcion = """En esta opcion podras gestionar tus prestamos actuales, puediendo consultar detalles como
        el material prestado, la fecha de devolucion o realizar acciones como devolver antes de la fecha estipulada"""
        
        Label(frame2, text=descripcion, bg="white", fg="black",font=("Arial", 11)).grid(row=0,column=0)

        self.frame3 = Frame(self, bg="white")
        self.frame3.grid(row=2,column=0)
        self.gestionar = Button(self.frame3, text="Gestionar prestamos", command=self.mostrarPrestamos, font=("Arial", 11))
        self.gestionar.grid(row=0,column=0, padx=50, pady=15)
        self.frame4 = Frame(self, bg="white")
        self.frame4.grid(row=3, column=0)

    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()


    def mostrarPrestamos(self):
        try:
            if not self.sistema.get_user().get_prestamos():
                raise NoHayPrestamos
            self.kill(self.frame4)
            prestamos = self.sistema.get_user().get_prestamos()
            lista = ""
            for i, prestamo in enumerate(prestamos):
                lista += f"{i}. Prestamo de: {prestamo.get_materialPrestado().get_nombre()} con fecha de vencimiento: {prestamo.get_fecha_fin()} \n"
            listaPrestamos = Text(self.frame4, border=False, font=("Arial", 11), borderwidth=2, highlightthickness=3, highlightbackground="gray")
            listaPrestamos.grid(row=0, column=0, columnspan=2, pady=5)
            listaPrestamos.delete("1.0", "end")
            listaPrestamos.config(height=5)
            listaPrestamos.insert(INSERT, lista)

            self.seleccion = FieldFrame(self.frame4, "Criterio", ["ID: "], "Valor")
            self.seleccion.grid(row=1, column =0, columnspan=2, pady=5)
            self.seleccion.crearBoton("Enviar", self.confirmar, 0)
        except NoHayPrestamos:
            messagebox.showerror("Error", NoHayPrestamos().getError())


    def confirmar(self):
        try:
            if self.seleccion.getValue("ID: ") == "":
                raise CampoVacio
        except CampoVacio:
            return messagebox.showerror("Error", CampoVacio().getError())
        try:
            if int(self.seleccion.getValue("ID: ")) < 0:
                raise IndexFuera
            self.prestamo = self.sistema.get_user().get_prestamos()[int(self.seleccion.getValue("ID: "))]
            self.kill(self.frame4)
            Label(self.frame4, text="Detalles del prestamo: ", bg="white", fg="black",font=("Arial", 11)).grid(row=0,column=0, columnspan=2)
            fieldframe = FieldFrame(self.frame4, "Detalle", ["Material prestado: ", "Tipo: ", "Fecha de inicio: ", "Fecha de vencimiento: ", "Sede del prestamo: "], "", [self.prestamo.get_materialPrestado().get_nombre(), self.prestamo.get_tipo(), self.prestamo.get_fecha_inicio(), self.prestamo.get_fecha_fin(), self.prestamo.get_sede().get_sede()], False)
            fieldframe.grid(row=1, column=0, columnspan=2)
            devolver = Button(self.frame4, text="Devolver prestamo", command= self.devolver)
            devolver.grid(row=2, column= 0)
            extender = Button(self.frame4, text="Extender prestamo", command= self.extender)
            extender.grid(row=2, column=1)
        except (IndexError, IndexFuera):
            messagebox.showerror("Error", IndexFuera().getError())
        except ValueError:
            messagebox.showerror("Error", DatoIncorrecto("Numero").getError())

    def extender(self):
        self.kill(self.frame4)
        Label(self.frame4, text= "Escoge la fecha hasta la cual deseas extender tu prestamo: ", bg="white", fg="black",font=("Arial", 11)).grid(row=0,column=0, columnspan=2, pady=5)
        self.cal = Calendar(self.frame4, mindate= self.prestamo.get_fecha_fin())
        self.cal.grid(row=1, column = 0, columnspan = 2, pady=5)
        self.cal.bind("<<CalendarSelected>>", self.seleccionarFecha)

    def seleccionarFecha(self, event):
        fechaSeleccionada = self.cal.get_date()
        self.prestamo.set_fecha_fin(fechaSeleccionada)
        messagebox.askokcancel(title="Prestamo extendido", message="Â¡Su prestamo ha sido extendido con exito!, No olvide devolver su recurso :)")
        self.kill(self.frame4)

    def devolver(self):
        if isinstance(self.prestamo.get_materialPrestado, Copia):
            self.prestamo.get_sede().get_copias().append(self.prestamo.get_materialPrestado)
            self.sistema.get_user().get_prestamos().remove(self.prestamo)
        else:
            self.prestamo.get_sede().get_PCs().append(self.prestamo.get_materialPrestado)
            self.sistema.get_user().get_prestamos().remove(self.prestamo)
        messagebox.askokcancel(title="Prestamo devuelto", message="Â¡Su prestamo ha sido devuelto con exito!, Gracias por su puntualidad :)")
        self.kill(self.frame4)