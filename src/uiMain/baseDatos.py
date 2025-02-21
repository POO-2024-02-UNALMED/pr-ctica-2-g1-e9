import tkinter as tk
from tkinter import Frame, Label, messagebox
from gestorExcepciones.erroresDeUsuario import CampoVacio
from uiMain.FieldFrame import FieldFrame
from gestorAplicacion.clasesDeBiblioteca.Autor import Autor
from gestorAplicacion.clasesDeAdministracion.Sistema import *
from gestorAplicacion.clasesDeBiblioteca.Biblioteca import *
from gestorAplicacion.clasesDeBiblioteca.Recurso import *
from gestorAplicacion.clasesDeBiblioteca.Libro import *
from gestorAplicacion.clasesDeBiblioteca.Computador import *
from gestorAplicacion.clasesDeBiblioteca.Copia import *
from gestorAplicacion.clasesDeBiblioteca.PC import *

class BaseDeDatos(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema

        self.sede_var = tk.StringVar()
        self.accion_var = tk.StringVar()
        self.recurso_var = tk.StringVar()
        self.ejemplar_var = tk.StringVar()

        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Gestión de Base de Datos", fg="black", bg="white", font=("Arial", 11))
        titulo.pack()


        frame2 = Frame(self, bg="white")
        frame2.grid(row=1,column=0)
        descripcion = "En este apartado podrás realizar cambios en la Base de Datos \nde la biblioteca, añadiendo o eliminando recursos."
        
        Label(frame2, text=descripcion, bg="white", fg="black", font=("Arial", 11)).grid(row=0,column=0, pady=15)

        frame3 = Frame(self, bg="white")
        frame3.grid(row=2, column=0)
        tk.Label(frame3, text="Sede:", bg="white", font=("Arial", 11)).pack()
        optn = tk.OptionMenu(frame3, self.sede_var, *['Medellín', 'Bogotá'])
        optn.configure(font=("Arial", 11), width=10)
        optn.pack(pady=7)

        lbl = tk.Label(frame3, text="Acción:")
        lbl.configure(font=("Arial", 11))
        lbl.pack(pady=7)
        tk.Radiobutton(frame3, text='Agregar', variable=self.accion_var, value='Agregar', font=("Arial", 11)).pack()
        tk.Radiobutton(frame3, text='Eliminar', variable=self.accion_var, value='Eliminar',font=("Arial", 11)).pack()

        lbl2 = tk.Label(frame3, text="Recurso:",font=("Arial", 11))
        lbl2.configure(pady=7)
        lbl2.pack()
        optn2 = tk.OptionMenu(frame3, self.recurso_var, *['Libro', 'Copia', 'Computador', 'PC'])
        optn2.configure(font=("Arial", 11), width=10)
        optn2.pack(pady=10)

        self.campos = []  # Esta lista almacenará los campos de entrada actuales

        self.sede_var.trace('w', lambda *args: self.actualizar_campos(frame3))
        self.ejemplar_var.trace('w', lambda *args: self.actualizar_campos(frame3))
        self.accion_var.trace('w', lambda *args: self.actualizar_campos(frame3))
        self.recurso_var.trace('w', lambda *args: self.actualizar_campos(frame3))

        frame4 = Frame(self, bg="white")
        frame4.grid(row=3, column=0)

    def actualizar_campos(self, frame):
        # Elimina los campos de entrada actuales
        for campo in self.campos:
            campo.destroy()
        self.campos = []

        accion = self.accion_var.get()
        recurso = self.recurso_var.get()
        sede = self.sede_var.get()

        if accion == 'Agregar':
            if recurso == 'Libro':
                # Crea y empaqueta los campos de entrada para agregar un libro
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]

                frameInputs = Agregar(frame, "Criterios", ["Nombre", "ISBN", "Autor", "Año"], "Valor", self.sistema, "Libro")
                self.campos.append(frameInputs)
                self.campos[-1].pack(pady=7)
                frameInputs.añadirBoton(tk.Button(frameInputs, command= lambda: self.agregar(frameInputs,biblioteca,frame),text="Aceptar", font=("Arial", 11)), 0)
        

            elif recurso == 'Copia':
                # Crea y empaqueta los campos de entrada para agregar una copia
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]
                
                frameInputs = Agregar(frame, "Criterios", ["Libro"], "Valor", self.sistema, "Copia")
                self.campos.append(frameInputs)
                self.campos[-1].pack(pady=7)
                frameInputs.añadirBoton(tk.Button(frameInputs, command= lambda: self.agregar(frameInputs,biblioteca,frame),text="Aceptar"), 0)
                

            elif recurso == 'Computador':
                # Crea y empaqueta los campos de entrada para agregar un computador
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]
                
                frameInputs = Agregar(frame, "Criterios", ["Nombre", "Marca", "Gama"], "Valor", self.sistema, "Computador")
                self.campos.append(frameInputs)
                self.campos[-1].pack(pady=7)
                frameInputs.añadirBoton(tk.Button(frameInputs, command= lambda: self.agregar(frameInputs,biblioteca,frame),text="Aceptar"), 0)
             

            elif recurso == 'PC':
                # Crea y empaqueta los campos de entrada para agregar un PC
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]
                
                frameInputs = Agregar(frame, "Criterios", ["Modelo"], "Valor", self.sistema, "PC")
                self.campos.append(frameInputs)
                self.campos[-1].pack(pady=7)
                frameInputs.añadirBoton(tk.Button(frameInputs, command= lambda: self.agregar(frameInputs,biblioteca,frame),text="Aceptar"), 0)


        
        elif accion == "Eliminar":
            if recurso == "Libro":
                self.campos.append(tk.Label(frame, text="Seleccione Libro a Eliminar, Esto Eliminará Todas Sus Copias",font=("Arial", 11)))
                self.campos[-1].pack(pady=7)
                libro_var = tk.StringVar(frame)  # Crea una nueva variable de control
                lista = tk.OptionMenu(frame, libro_var, "Seleccione aquí")  # Usa la nueva variable de control
                lista.configure(font=("Arial", 11), width=10)
                lista.pack(pady=7)
                self.campos.append(lista)
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]

                for libro in biblioteca.get_libros():
                    lista["menu"].add_command(label=f"{libro.get_nombre()}", command=tk._setit(libro_var, libro.get_nombre()))  # Usa la nueva variable de control
                lista["menu"].configure(font=("Arial", 11))
                self.campos.append(tk.Button(frame, command=lambda: self.eliminar(biblioteca, libro_var.get(), frame), text = "Eliminar", font=("Arial", 11)))
                self.campos[-1].pack(pady=7)
            
            elif recurso == "Copia":
                self.campos.append(tk.Label(frame, text="Seleccione la Copia a Eliminar", font=("Arial", 11)))
                self.campos[-1].pack(pady=7)
                copia_var = tk.StringVar(frame)
                lista = tk.OptionMenu(frame, copia_var, "Seleccione aquí")
                lista.configure(font=("Arial", 11), width=10)
                lista.pack(pady=7)
                self.campos.append(lista)
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]

                for copia in biblioteca.get_copias():
                    coso = f"{copia.get_nombre()} ID: {copia.get_id()}"
                    lista["menu"].add_command(label=coso, command=tk._setit(copia_var, coso))
                lista["menu"].configure(font=("Arial", 11))
                self.campos.append(tk.Button(frame, command=lambda: self.eliminar(biblioteca, copia_var.get(), frame), text="Eliminar",font=("Arial", 11)))
                self.campos[-1].pack(pady=7)

            elif recurso == "Computador":
                self.campos.append(tk.Label(frame, text="Seleccione Computador a Eliminar, Esto Eliminará Todos Sus PC", font=("Arial", 11)))
                self.campos[-1].pack(pady=7)
                computador_var = tk.StringVar(frame)
                lista = tk.OptionMenu(frame, computador_var, "Seleccione aquí")
                lista.configure(font=("Arial", 11), width=10)
                lista.pack(pady=7)
                self.campos.append(lista)
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]

                for computador in biblioteca.get_computadores():
                    lista["menu"].add_command(label=f"{computador.get_nombre()}", command=tk._setit(computador_var, computador.get_nombre()))
                lista["menu"].configure(font=("Arial", 11))
                self.campos.append(tk.Button(frame, command=lambda: self.eliminar(biblioteca, computador_var.get(), frame), text = "Eliminar",font=("Arial", 11)))
                self.campos[-1].pack(pady=7)

            elif recurso == "PC":
                self.campos.append(tk.Label(frame, text="Seleccione el PC a Eliminar",font=("Arial", 11)))
                self.campos[-1].pack(pady=7)
                PC_var = tk.StringVar(frame)
                lista = tk.OptionMenu(frame, PC_var, "Seleccione aquí")
                lista.configure(font=("Arial", 11), width=10)
                lista.pack()
                self.campos.append(lista)
                if sede == "Medellín":
                    biblioteca = self.sistema.get_bibliotecas()[0]
                elif sede == "Bogotá":
                    biblioteca = self.sistema.get_bibliotecas()[1]

                for PC in biblioteca.get_PCs():
                    coso = f"{PC.get_nombre()} ID: {PC.get_id()}"
                    lista["menu"].add_command(label=coso, command=tk._setit(PC_var, coso))      
                lista["menu"].configure(font=("Arial", 11))          
                self.campos.append(tk.Button(frame, command=lambda: self.eliminar(biblioteca, PC_var.get(), frame), text = "Eliminar", font=("Arial", 11)))
                self.campos[-1].pack(pady=7)
        # tk.Button(frame3, text='Ejecutar', command=self.ejecutar).pack()
    
    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

    def agregar(self, frameInputs, biblioteca,frame):
        recurso = self.recurso_var.get()
        frameInputs.getValores()
        valores = frameInputs.valores
        try:
            for valor in valores:
                if valor == "":
                    raise CampoVacio
            if biblioteca == "":
                raise CampoVacio
            if recurso == "Libro":
                autor = False
                autorobj = ""
                for libro in biblioteca.get_libros():
                    if libro.get_isbn() == valores[1]:
                        messagebox.showerror("Error","Este libro ya se encuentra en la base de datos (o uno con el mismo ISBN)")
                        return
                    if libro.get_autor().get_nombre() == valores[2]:
                        autor = True
                        autorobj = libro.get_autor()
                if autor == True:
                    biblioteca.get_libros().append(Libro(valores[0],0,valores[1],autorobj,valores[3]))
                else:
                    biblioteca.get_libros().append(Libro(valores[0],0,valores[1],Autor(valores[2],"Desconocida","Desconocida"),valores[3]))
                messagebox.showinfo("Éxito","Se ha agregado el Libro a la base de datos con éxito.")
                self.actualizar_campos(frame)
                
            elif recurso == "Copia":
                copiaDe = ""
                for libro in biblioteca.get_libros():
                    if libro.get_nombre() == valores[0]:
                        copiaDe = libro
                        break
                if copiaDe == "":
                    messagebox.showerror("ERROR","Ese Libro no se encuentra en la Biblioteca, añada el Libro primero o intente con otro.")
                    return
                biblioteca.get_copias().append(Copia(0,copiaDe,biblioteca.get_sede()))
                messagebox.showinfo("Éxito","Se ha agregado la Copia a la base de datos con éxito.")
                self.actualizar_campos(frame)
            elif recurso == "Computador":
                for computador in biblioteca.get_computadores():
                    if computador.get_nombre() == valores[0] and computador.get_marca() ==  valores[1]:
                        messagebox.showerror("Error","Este computador ya se encuentra en la base de datos.")
                        return
                biblioteca.get_computadores().append(Computador(valores[0],0,valores[1],valores[2]))
                messagebox.showinfo("Éxito","Se ha agregado el Computador a la base de datos con éxito.")
                self.actualizar_campos(frame)
            elif recurso == "PC":
                modelo = ""
                for computador in self.sistema.get_computadores():
                    if computador.get_nombre() == valores[0]:
                        modelo = computador
                        break
                if modelo == "":
                    messagebox.showerror("ERROR","Ese modelo de PC no se encuentra en la Biblioteca, añada el Computador primero o intente con otro.")
                    return
                    biblioteca.get_PCs().append(PC(modelo.get_nombre(),True,biblioteca.get_sede()))
                messagebox.showinfo("Éxito","Se ha agregado el PC a la base de datos con éxito.")
                self.actualizar_campos(frame)
        except CampoVacio:
            return messagebox.showerror("Error", CampoVacio().getError())

    def eliminar(self, biblioteca, re_var, frame):
        recurso = self.recurso_var.get()
        try:
            if re_var == "":
                raise CampoVacio
            
            if biblioteca == "":
                raise CampoVacio
            
            if recurso == "Libro":
                for prestamos in biblioteca.get_prestamos():
                    for copia in prestamos.get_copias_prestadas():
                        if(copia.get_nombre() == re_var):
                            messagebox.showerror("Error","Hay una o más copias en préstamo de este libro.")
                            return
                
                for i in range(len(biblioteca.get_libros())):
                    if biblioteca.get_libros()[i].get_nombre() == re_var:
                        del biblioteca.get_libros()[i]
                        messagebox.showinfo("Éxito","Se ha eliminado el libro de la base de datos con éxito.")
                        self.actualizar_campos(frame)
                        return

            elif recurso == "Copia":

                for prestamos in biblioteca.get_prestamos():
                    for copia in prestamos.get_copias_prestadas():
                        if(f"{copia.get_nombre()} ID: {copia.get_nombre()}" == re_var):
                            messagebox.showerror("Error","La Copia Se Encuentra Prestada.")
                            return
                
                for i in range(len(biblioteca.get_copias())):
                    if f"{biblioteca.get_copias()[i].get_nombre()} ID: {biblioteca.get_copias()[i].get_id()}" == re_var:
                        del biblioteca.get_copias()[i]
                        messagebox.showinfo("Éxito","Se ha eliminado la copia de la base de datos con éxito.")
                        self.actualizar_campos(frame)
                        return   

            elif recurso == "Computador":
                for prestamos in biblioteca.get_prestamos():
                    for PC in prestamos.get_pcs_prestados():
                        if(PC.get_modelo() == re_var):
                            messagebox.showerror("Error","Hay una o más ejemplares en préstamo de este computador.")
                            return
                
                for i in range(len(biblioteca.get_computadores())):
                    if biblioteca.get_computadores()[i].get_nombre() == re_var:
                        del biblioteca.get_computadores()[i]
                        messagebox.showinfo("Éxito","Se ha eliminado el computador de la base de datos con éxito.")
                        self.actualizar_campos(frame)
                        return
            elif recurso == "PC":
                for prestamos in biblioteca.get_prestamos():
                    for PC in prestamos.get_pcs_prestados():
                        if(f"{PC.get_modelo()} ID: {PC.get_id()}" == re_var):
                            messagebox.showerror("Error","El PC Se Encuentra Prestado.")
                            return
                
                for i in range(len(biblioteca.get_PCs())):
                    if f"{biblioteca.get_PCs()[i].get_modelo()} ID: {biblioteca.get_PCs()[i].get_id()}" == re_var:
                        del biblioteca.get_PCs()[i]
                        messagebox.showinfo("Éxito","Se ha eliminado el PC de la base de datos con éxito.")
                        self.actualizar_campos(frame)
                        return
        except CampoVacio:
            return messagebox.showerror("Error", CampoVacio().getError())


class Agregar(FieldFrame):
    def __init__(self, root, criteriosTitulo, lista, valorTitulo, sistema, recurso):
        super().__init__(root, criteriosTitulo, lista, valorTitulo)
        self.sistema = sistema
        self.recurso = recurso
        
