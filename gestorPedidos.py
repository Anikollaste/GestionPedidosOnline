import tkinter as tk
from funcionalidad import Funciones as fun

class Gestor():


    def __init__(self, root):
        root.title('Generador de pedidos')
        root.config(bg='#3F3C3C')
        self.miFrame=tk.Frame(root,bg='#3F3C3C')
        self.miFrame.pack()
        self.miFrame2=tk.Frame(root,bg='#3F3C3C')
        self.miFrame2.pack()
        self.miFrame1=tk.Frame(root,bg='#3F3C3C')
        self.miFrame1.pack()
        self.miFrame3=tk.Frame(root,bg='#3F3C3C')
        self.miFrame3.pack()

        #-------------------------------- Crear la GUI ---------------------------------------------
        self.graficos=self.dni(),self.apellido(),self.nombre(),self.direccion(),self.telefono(),self.busqueda(),
        self.codidoProductos(),self.descripcion(),self.metrica(),self.cantidad(),self.precio(),self.subtotal(),
        self.mensajes()

        #----------- Obtener valores Código producto y autocompletar Descripción, unidad, precio-------
        self.consulta=tk.Button(self.miFrame3,text='Añadir artículo',fg='#2192AC',bg='#3F3C3C',
            command=lambda:fun.consultaBdd(self)).grid(row=0,column=0,pady=5,padx=5)
        
        #--------------- Listar árticulos en el pedido ------------------------------------------------
        self.listaArticulos=tk.Button(self.miFrame3,text='Lista de artículos',fg='#2192AC'
            ,bg='#3F3C3C',command=lambda:self.verArticulos()).grid(row=0,column=1,pady=5,padx=5)
        
        #--------------- Obtener valores de los Entry para generar Pedido.txt--------------------------
        self.guardar=tk.Button(self.miFrame3,text='Generar pedido',fg='#2192AC',bg='#3F3C3C',
            command=lambda:fun.verAlbaran(self)).grid(row=0,column=2,pady=5,padx=5)
        
        #----------- Si la base de datos no existe la crea e inserta productos--------------------------
        fun.bdd_existe()

        #----------- Si el archivo Articulos.csv no exite lo crea ------------------------------
        fun.articulos()

    def dni(self):
        self.obDni=tk.StringVar()
        lDni=tk.Label(self.miFrame, text='DNI:',bg='#3F3C3C',fg='#04B486')
        lDni.grid(row=0, column=0, sticky='e', pady=5, padx=5)
        tDni=tk.Entry(self.miFrame,textvariable=self.obDni,fg='#A34B0C')
        tDni.grid(row=0, column=1, pady=5, padx=5)


    def telefono(self):
        self.obTelefono=tk.StringVar()
        lTel=tk.Label(self.miFrame, text='Teléfono:',bg='#3F3C3C',fg='#04B486')
        lTel.grid(row=0, column=2, sticky='e', pady=5, padx=5)
        tTel=tk.Entry(self.miFrame,textvariable=self.obTelefono,fg='#A34B0C')
        tTel.grid(row=0, column=3,pady=5, padx=5)

    def apellido(self):
        self.obApellido=tk.StringVar()
        lApellido=tk.Label(self.miFrame, text='Apellido:',bg='#3F3C3C',fg='#04B486')
        lApellido.grid(row=1, column=0, sticky='e', pady=5, padx=5)
        tApellido=tk.Entry(self.miFrame,textvariable=self.obApellido,fg='#A34B0C')
        tApellido.grid(row=1, column=1, pady=5, padx=5)

    def nombre(self):
        self.obNombre=tk.StringVar()
        lNombre=tk.Label(self.miFrame, text='Nombre:',bg='#3F3C3C',fg='#04B486')
        lNombre.grid(row=1, column=2, sticky='e', pady=5, padx=5)
        tNombre=tk.Entry(self.miFrame,textvariable=self.obNombre,fg='#A34B0C')
        tNombre.grid(row=1, column=3, pady=5, padx=5)

    def direccion(self):
        self.obDireccion=tk.StringVar()
        lDireccion=tk.Label(self.miFrame, text='Dirección:',bg='#3F3C3C',fg='#04B486')
        lDireccion.grid(row=2, column=0, sticky='e', pady=5, padx=5)
        tDireccion=tk.Entry(self.miFrame,textvariable=self.obDireccion,fg='#A34B0C')
        tDireccion.grid(row=2, column=1, columnspan=3, sticky='we',pady=5, padx=5)


    def busqueda(self):
        self.vBus=tk.StringVar()
        lBusqueda=tk.Label(self.miFrame2,text='Búsqueda de productos',fg='#04B486',bg='#3F3C3C')
        lBusqueda.grid(row=4, column=0,sticky='w', pady=10, padx=10,columnspan=2)
        lProductos=tk.Label(self.miFrame2, text='Artículos en el almacen',fg='#04B486',bg='#3F3C3C')
        lProductos.grid(row=4, column=3,sticky='w', pady=10, padx=10)
        lDescripcion=tk.Label(self.miFrame2, text='Descripción:',fg='#04B486',bg='#3F3C3C')
        lDescripcion.grid(row=5, column=0,sticky='w', pady=10, padx=10)
        tBusqueda=tk.Entry(self.miFrame2,textvariable=self.vBus,width=10,fg='#A34B0C')
        tBusqueda.grid(row=5, column=1,sticky='w', pady=5, padx=5)
        bBusqueda=tk.Button(self.miFrame2,text='Buscar',fg='#2192AC',bg='#3F3C3C',command=lambda:fun.consultaAlmacen(self))
        bBusqueda.grid(row=5,column=2,sticky='w',pady=5,padx=5)
        self.cuadroTexto=tk.Text(self.miFrame2, width='40', height='5',fg='#A34B0C')
        self.cuadroTexto.grid(row=5, column=3, padx=10, pady=10)

    def mensajes(self):
        self.obMensaje=tk.StringVar()
        tMensajes=tk.Entry(self.miFrame2,textvariable=self.obMensaje,state="readonly",justify='center',fg='#F12269')
        tMensajes.grid(row=6, column=0,columnspan=4,sticky='we', pady=5, padx=5)
        tMensajes.delete('0',tk.END)

    def codidoProductos(self):
        self.obC1=tk.StringVar()
        lCodigo=tk.Label(self.miFrame1, text='ID',bg='#3F3C3C',fg='#04B486')
        lCodigo.grid(row=4, column=0,sticky='ew', pady=10, padx=10)
        tCodigo1=tk.Entry(self.miFrame1,textvariable=self.obC1,width=9,fg='#F12269')
        tCodigo1.grid(row=5, column=0, pady=10, padx=10)

    def descripcion(self):
        self.obDe1=tk.StringVar()
        lDes=tk.Label(self.miFrame1, text='Descripción',bg='#3F3C3C',fg='#04B486')
        lDes.grid(row=4, column=1,sticky='ew', pady=10, padx=10)
        self.tDes1=tk.Entry(self.miFrame1,textvariable=self.obDe1, width=9,fg='#A34B0C',state="readonly")
        self.tDes1.grid(row=5, column=1, pady=10, padx=10)
        self.tDes1.delete('0',tk.END)

    def metrica(self):
        self.obM1=tk.StringVar()
        lM=tk.Label(self.miFrame1, text='Métrica',bg='#3F3C3C',fg='#04B486')
        lM.grid(row=4, column=2,sticky='ew', pady=10, padx=10)
        tM1=tk.Entry(self.miFrame1,textvariable=self.obM1,width=9,fg='#A34B0C',state="readonly")
        tM1.grid(row=5, column=2, pady=10, padx=10)

    def cantidad(self):
        self.obCa1=tk.IntVar(value='')
        lCantidad=tk.Label(self.miFrame1, text='Cantidad',bg='#3F3C3C',fg='#04B486')
        lCantidad.grid(row=4, column=3,sticky='ew', pady=10, padx=10)
        tCantidad1=tk.Entry(self.miFrame1,textvariable=self.obCa1,width=9,fg='#F12269')
        tCantidad1.grid(row=5, column=3, pady=10, padx=10)

    def precio(self):
        self.obP1=tk.IntVar(value='')
        lPrecio=tk.Label(self.miFrame1, text='Precio',bg='#3F3C3C',fg='#04B486')
        lPrecio.grid(row=4, column=4,sticky='ew', pady=10, padx=10)
        tPrecio1=tk.Entry(self.miFrame1,textvariable=self.obP1,width=9,fg='#A34B0C',state="readonly")
        tPrecio1.grid(row=5, column=4, pady=10, padx=10)

    def subtotal(self):
        self.obSb1=tk.IntVar(value='')
        lSubtotal=tk.Label(self.miFrame1, text='Subtotal',bg='#3F3C3C',fg='#04B486')
        lSubtotal.grid(row=4, column=5,sticky='ew', pady=10, padx=10)
        tSubtotal1=tk.Entry(self.miFrame1,textvariable=self.obSb1,width=9,fg='#A34B0C',state="readonly")
        tSubtotal1.grid(row=5, column=5, pady=10, padx=10)

    def total(self):
        self.obTo=tk.IntVar(value='')
        lTotal=tk.Label(self.miFrame1, text='Total',bg='#3F3C3C',fg='#04B486')
        lTotal.grid(row=7, column=6,sticky='ew', pady=5, padx=5)
        tTotal=tk.Entry(self.miFrame1,textvariable=self.obTo,width=7, state="readonly")
        tTotal.grid(row=7, column=7, pady=5, padx=5)
        pass

    def verArticulos(self):
        texto=open('Articulos.csv').readlines()
        articuloTexto=tk.Text(self.miFrame3, width='70', height='10',fg='#A34B0C')
        articuloTexto.grid(row=1, column=0, columnspan=3, sticky='ew', padx=10, pady=10)
        articuloTexto.insert(tk.INSERT, texto)


    def limpiarCampos(self):
        self.tDes1.delete('0',tk.END)


myApp=tk.Tk()
gui=Gestor(myApp)
myApp.mainloop()
