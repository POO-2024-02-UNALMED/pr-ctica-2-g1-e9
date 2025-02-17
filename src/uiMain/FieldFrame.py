from tkinter import *

class FieldFrame(Frame):

    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores = None, habilitado = None):
        super().__init__(root, width=200, height=200, bg="white")
        self.root = root
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        if valores is None:
            self.valores = []
        else: 
            self.valores = valores
        self.entradas = []
        self.estado = "normal"
        self.habilitado = habilitado



        self.criteriosLabel = Label(self, text= self.tituloCriterios, bg="white", font= ("Arial", 11))
        self.criteriosLabel.grid(row=0, column=0, padx= 50, pady= 10)

        self.valoresLabel = Label(self, text = self.tituloValores, bg="white", font= ("Arial", 11))
        self.valoresLabel.grid(row=0, column=1, padx= 50, pady= 10)

        for i in range(len(self.criterios)):
            Label(self, text=self.criterios[i], bg="white", font= ("Arial", 11)).grid(row=(i+1), column = 0)
            valor = Entry(self, width=60)
            valor.grid(row=(i+1), column=1, padx= 50, pady= 10)
            if self.valores:
                valor.insert(0, valores[i])
            self.entradas.append(valor)
            if habilitado is not None:
                    valor.configure(state = "disabled")
            
        if habilitado is None:
            self.crearBoton("Limpiar campos", self.limpiarEntradas, 1)
        

    def crearBoton(self, texto, comando, col):
        Button(self, text=texto, command= comando, font= ("Arial", 11)).grid(row=(len(self.criterios)+1), column= col, padx= 50, pady= 10)
    
    def añadirBoton(self, boton, col):
        boton.grid(row=(len(self.criterios)+1), column= col, padx= 50, pady= 10)
    
    def limpiarEntradas(self):
        for entrada in self.entradas:
            entrada.delete(0, last=END)

    def getValores(self):
        self.valores = [valor.get() for valor in self.entradas]

    def getValue(self, criterio):
        i = self.criterios.index(criterio)
        return self.entradas[i].get()
    
