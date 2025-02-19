from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.clasesDeBiblioteca.Copia import Copia
from gestorAplicacion.clasesDeBiblioteca.PC import PC
from datetime import date
from uiMain.FieldFrame import FieldFrame
from gestorExcepciones.erroresPython import *
from gestorExcepciones.erroresDeUsuario import *

class GestionMultas(Frame):


    def _init_(self, root, sistema):
        super()._init_(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]


        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Gestion de multas", fg="black", bg="white", font=("Arial", 11))
        titulo.pack()


        frame2 = Frame(self)
        frame2.grid(row=1,column=0)
        descripcion = """En esta opcion podras gestionar tus multas actuales ademas de pagarlas, en las siguientes opciones
        podras acceder a los detalles de cada multa asociada y realizar acciones sobre ellas"""
        
        Label(frame2, text=descripcion, bg="white", fg="black",font=("Arial", 11)).grid(row=0,column=0)

        self.frame3 = Frame(self, bg="white")
        self.frame3.grid(row=2,column=0)
        self.gestionar = Button(self.frame3, text="Gestionar multas", command=self.mostrarMultas, font=("Arial", 11))
        self.gestionar.grid(row=0,column=0, padx=50, pady=15)
        self.frame4 = Frame(self, bg="white")
        self.frame4.grid(row=3, column=0)

    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()


    def mostrarMultas(self):
        try: 
            if not self.sistema.get_user().get_multas():
                raise NoHayMultas
            self.kill(self.frame4)
            multas = self.sistema.get_user().get_multas()
            lista = ""
            for i, multa in enumerate(multas):
                lista += f"{i}. Multa de costo: {multa.get_costo()} con fecha impuesta de pago: {multa.get_fecha_impuesta()} \n"
            listaMultas = Text(self.frame4, border=False, font=("Arial", 11), borderwidth=2, highlightthickness=3, highlightbackground="gray")
            listaMultas.grid(row=0, column=0, columnspan=2, pady=5)
            listaMultas.delete("1.0", "end")
            listaMultas.config(height=5)
            listaMultas.insert(INSERT, lista)

            self.seleccion = FieldFrame(self.frame4, "Criterio", ["ID: "], "Valor")
            self.seleccion.grid(row=1, column =0, columnspan=2, pady=5)
            self.seleccion.crearBoton("Enviar", self.confirmar, 0)
            
        except NoHayMultas:
            messagebox.showerror("Error", NoHayMultas().getError())

        

    def confirmar(self):
        try:
            if self.seleccion.getValue("ID: ") == "":
                raise CampoVacio
        except CampoVacio:
            return messagebox.showerror("Error", CampoVacio().getError())
        try:
            if int(self.seleccion.getValue("ID: ")) < 0:
                raise IndexFuera
            self.multa = self.sistema.get_user().get_multas()[int(self.seleccion.getValue("ID: "))]
            self.kill(self.frame4)
            Label(self.frame4, text="Detalles de la multa: ", bg="white", fg="black",font=("Arial", 11)).grid(row=0,column=0, columnspan=2)
            fieldframe = FieldFrame(self.frame4, "Detalle", ["Tipo: ", "Fecha: ", "Costo:"], "", [self.multa.get_tipo(), self.multa.get_fecha_impuesta(), self.multa.get_costo()], False)
            fieldframe.grid(row=1, column=0, columnspan=2)
            pagar = Button(self.frame4, text="Pagar", command= self.pagar)
            pagar.grid(row=2, column= 0, columnspan = 2)
        except (IndexError, IndexFuera):
            messagebox.showerror("Error", IndexFuera().getError())
        except ValueError:
            messagebox.showerror("Error", DatoIncorrecto("Numero").getError())
    
    def pagar(self):
        self.multa.pagar_multa()
        messagebox.askokcancel("Multa pagada", "Su multa ha sido pagada con exito.")
        self.kill(self.frame4)