from tkinter import *
from tkinter import ttk

class PrestamoDeRecursos(Frame):

    def __init__(self, root):
        super().__init__(root, height=70,width=500,bg="#7c9933")
        self.root = root 
        palabraLibro = StringVar(value="Libro")
        def busquedaBasica():
            def buscar(event):
                if opciones.get() == "Libro":
                    consulta.config(text="Ingrese el titulo del libro a consultar: ")
                else:
                    consulta.config(text="Ingrese el modelo del computador a consultar: ")

                    
            frame4 = Frame(self)
            frame4.grid(row=3,column=0)

            Label(frame4, text="Seleccione el material que desea consultar: ", fg="black").grid(row=0,column=0)
            opciones = ttk.Combobox(frame4, values=["Libro", "Computador"], textvariable=palabraLibro, foreground="black", state="readonly")
            opciones.grid(row=0,column=1)
            opciones.bind("<<ComboboxSelected>>", buscar)
            consulta = Label(frame4,text="Ingrese el titulo del libro a consultar: ")
            consulta.grid(row=1,column=0)
            entrada = Entry(frame4)
            entrada.grid(row=1,column=1)
            
            """
            criterio = Label(frame4, text="CRITERIO")
            criterio.grid(row=1,column=0, padx=10, pady=10)
            valor = Label(frame4, text="VALOR")
            valor.grid(row=1,column=1, padx=10, pady=10)
            """

        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Consulta de disponibilidad para prestamo", fg="white", bg="#7c9933")
        titulo.pack()
        frame2 = Frame(self)
        frame2.grid(row=1,column=0)
        desc =  """
                En esta opcion podras consultar la disponibilidad para prestamo de los diferentes recursos de la biblioteca, 
                usando criterios como Sede, Titulo, Autor, Fecha. Para de esta manera generar un prestamo a nombre del usuario.
                """
        
        descripcion = Label(frame1, text=desc, fg="white", bg="#7c9933")
        descripcion.pack(anchor="center")

        frame3 = Frame(self, bg="#7c9933")
        frame3.grid(row=2,column=0)
        basica = Button(frame3, text="Busqueda básica", command=busquedaBasica)
        porCriterio = Button(frame3, text= "Busqueda por criterios")
        basica.grid(row=0,column=0, padx=100, pady=15)
        porCriterio.grid(row=0,column=1,padx=100, pady=15)
