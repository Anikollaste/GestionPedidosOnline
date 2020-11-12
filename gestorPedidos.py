import tkinter as tk
from funcionalidad import Funciones
import pandas as pd
import time

class Gestor(Funciones):


    def __init__(self):
        self.root=tk.Tk()
        self.root.title('Generador de pedidos')
        self.bMenu=tk.Menu(self.root)
        self.root.config(bg='#3F3C3C',menu=self.bMenu)
        self.miFrame=tk.Frame(self.root,bg='#3F3C3C')
        self.miFrame.pack()
        self.miFrame2=tk.Frame(self.root,bg='#3F3C3C')
        self.miFrame2.pack()
        self.miFrame1=tk.Frame(self.root,bg='#3F3C3C')
        self.miFrame1.pack()
        self.miFrame3=tk.Frame(self.root,bg='#3F3C3C')
        self.miFrame3.pack()
        self.suma=0
        self.graficos()
       

        #----------- Obtener valores Código producto y autocompletar Descripción, unidad, precio-------
        self.consulta=tk.Button(self.miFrame3,text='Añadir artículo',fg='#2192AC',bg='#3F3C3C',
            command=lambda:self.consultaBdd()).grid(row=0,column=0,pady=5,padx=5)
        
        #--------------- Listar árticulos en el pedido ------------------------------------------------
        self.listaArticulos=tk.Button(self.miFrame3,text='Lista de artículos',fg='#2192AC'
            ,bg='#3F3C3C',command=lambda:self.verArticulos()).grid(row=0,column=1,pady=5,padx=5)
                
        #----------- Si la Bdd no existe la crea -------------------------------------------------------
        self.bdd_existe()

        #----------- Variable del método total ---------------------------------------------------------
        self.obTotal=tk.IntVar(value='')

    def barraMenu(self):
        archivoArchi=tk.Menu(self.bMenu, tearoff=0)
        self.bMenu.add_cascade(label='Archivo', menu=archivoArchi)
        #archivoArchi.add_command(label='Nuevo',command=lambda:self.eliminarArchivos())
        #archivoArchi.add_command(label='Guardar',command=lambda:self.generarAlbaran())
        archivoArchi.add_command(label='Guardar como',command=lambda:self.guardar_archivo())

    def barraApli(self):
        archivoAplica=tk.Menu(self.bMenu, tearoff=0)
        self.bMenu.add_cascade(label='Aplicación', menu=archivoAplica)
        archivoAplica.add_command(label='Borrar campos',command=lambda:self.limpiarAllCampos())
        archivoAplica.add_command(label='Salir',command=lambda:self.eliminarArchivos())

    def graficos(self):
        self.barraMenu(),self.barraApli(),self.dni(),self.apellido(),self.nombre(),self.direccion(),self.telefono(),
        self.busqueda(),self.codidoProductos(),self.descripcion(),self.metrica(),self.cantidad(),self.precio(),
        self.subtotal(),self.mensajes()

    def dni(self):
        self.obDni=tk.StringVar()
        lDni=tk.Label(self.miFrame, text='DNI:',bg='#3F3C3C',fg='#04B486')
        lDni.grid(row=0, column=0, sticky='e', pady=5, padx=5)
        self.tDni=tk.Entry(self.miFrame,textvariable=self.obDni,fg='#A34B0C')
        self.tDni.grid(row=0, column=1, pady=5, padx=5)


    def telefono(self):
        self.obTelefono=tk.StringVar()
        lTel=tk.Label(self.miFrame, text='Teléfono:',bg='#3F3C3C',fg='#04B486')
        lTel.grid(row=0, column=2, sticky='e', pady=5, padx=5)
        self.tTel=tk.Entry(self.miFrame,textvariable=self.obTelefono,fg='#A34B0C')
        self.tTel.grid(row=0, column=3,pady=5, padx=5)

    def apellido(self):
        self.obApellido=tk.StringVar()
        lApellido=tk.Label(self.miFrame, text='Apellido:',bg='#3F3C3C',fg='#04B486')
        lApellido.grid(row=1, column=0, sticky='e', pady=5, padx=5)
        self.tApellido=tk.Entry(self.miFrame,textvariable=self.obApellido,fg='#A34B0C')
        self.tApellido.grid(row=1, column=1, pady=5, padx=5)

    def nombre(self):
        self.obNombre=tk.StringVar()
        lNombre=tk.Label(self.miFrame, text='Nombre:',bg='#3F3C3C',fg='#04B486')
        lNombre.grid(row=1, column=2, sticky='e', pady=5, padx=5)
        self.tNombre=tk.Entry(self.miFrame,textvariable=self.obNombre,fg='#A34B0C')
        self.tNombre.grid(row=1, column=3, pady=5, padx=5)

    def direccion(self):
        self.obDireccion=tk.StringVar()
        lDireccion=tk.Label(self.miFrame, text='Dirección:',bg='#3F3C3C',fg='#04B486')
        lDireccion.grid(row=2, column=0, sticky='e', pady=5, padx=5)
        self.tDireccion=tk.Entry(self.miFrame,textvariable=self.obDireccion,fg='#A34B0C')
        self.tDireccion.grid(row=2, column=1, columnspan=3, sticky='we',pady=5, padx=5)


    def busqueda(self):
        self.vBus=tk.StringVar()
        lBusqueda=tk.Label(self.miFrame2,text='Búsqueda de productos',fg='#04B486',bg='#3F3C3C')
        lBusqueda.grid(row=4, column=0,sticky='w', pady=10, padx=10,columnspan=2)
        lProductos=tk.Label(self.miFrame2, text='Artículos en el almacen',fg='#04B486',bg='#3F3C3C')
        lProductos.grid(row=4, column=3,sticky='w', pady=10, padx=10)
        lDescripcion=tk.Label(self.miFrame2, text='Descripción:',fg='#04B486',bg='#3F3C3C')
        lDescripcion.grid(row=5, column=0,sticky='w', pady=10, padx=10)
        self.tBusqueda=tk.Entry(self.miFrame2,textvariable=self.vBus,width=10,fg='#A34B0C')
        self.tBusqueda.grid(row=5, column=1,sticky='w', pady=5, padx=5)
        bBusqueda=tk.Button(self.miFrame2,text='Buscar',fg='#2192AC',bg='#3F3C3C',command=lambda:self.consultaAlmacen())
        bBusqueda.grid(row=5,column=2,sticky='w',pady=5,padx=5)
        self.cuadroTexto=tk.Text(self.miFrame2, width='40', height='5',fg='#A34B0C')
        self.cuadroTexto.grid(row=5, column=3, padx=10, pady=10)

    def mensajes(self):
        self.obMensaje=tk.StringVar()
        self.tMensajes=tk.Entry(self.miFrame2,textvariable=self.obMensaje,state="readonly",justify='center',fg='#F12269')
        self.tMensajes.grid(row=6, column=0,columnspan=4,sticky='we', pady=5, padx=5)
        self.tMensajes.delete('0',tk.END)

    def codidoProductos(self):
        self.obC1=tk.StringVar()
        lCodigo=tk.Label(self.miFrame1, text='ID',bg='#3F3C3C',fg='#04B486')
        lCodigo.grid(row=4, column=0,sticky='ew', pady=10, padx=10)
        self.tCodigo1=tk.Entry(self.miFrame1,textvariable=self.obC1,width=9,fg='#F12269')
        self.tCodigo1.grid(row=5, column=0, pady=10, padx=10)

    def descripcion(self):
        self.obDe1=tk.StringVar()
        lDes=tk.Label(self.miFrame1, text='Descripción',bg='#3F3C3C',fg='#04B486')
        lDes.grid(row=4, column=1,sticky='ew', pady=10, padx=10)
        self.tDes1=tk.Entry(self.miFrame1,textvariable=self.obDe1, width=9,fg='#A34B0C',state='readonly')
        self.tDes1.grid(row=5, column=1, pady=10, padx=10)
        self.tDes1.delete('0',tk.END)

    def metrica(self):
        self.obM1=tk.StringVar()
        lM=tk.Label(self.miFrame1, text='Métrica',bg='#3F3C3C',fg='#04B486')
        lM.grid(row=4, column=2,sticky='ew', pady=10, padx=10)
        self.tM1=tk.Entry(self.miFrame1,textvariable=self.obM1,width=9,fg='#A34B0C',state='readonly')
        self.tM1.grid(row=5, column=2, pady=10, padx=10)

    def cantidad(self):
        self.obCa1=tk.IntVar(value='')
        lCantidad=tk.Label(self.miFrame1, text='Cantidad',bg='#3F3C3C',fg='#04B486')
        lCantidad.grid(row=4, column=3,sticky='ew', pady=10, padx=10)
        self.tCantidad1=tk.Entry(self.miFrame1,textvariable=self.obCa1,width=9,fg='#F12269')
        self.tCantidad1.grid(row=5, column=3, pady=10, padx=10)

    def precio(self):
        self.obP1=tk.IntVar(value='')
        lPrecio=tk.Label(self.miFrame1, text='Precio',bg='#3F3C3C',fg='#04B486')
        lPrecio.grid(row=4, column=4,sticky='ew', pady=10, padx=10)
        self.tPrecio1=tk.Entry(self.miFrame1,textvariable=self.obP1,width=9,fg='#A34B0C',state='readonly')
        self.tPrecio1.grid(row=5, column=4, pady=10, padx=10)

    def subtotal(self):
        self.obSb1=tk.IntVar(value='')
        lSubtotal=tk.Label(self.miFrame1, text='Subtotal',bg='#3F3C3C',fg='#04B486')
        lSubtotal.grid(row=4, column=5,sticky='ew', pady=10, padx=10)
        self.tSubtotal1=tk.Entry(self.miFrame1,textvariable=self.obSb1,width=9,fg='#A34B0C',state='readonly')
        self.tSubtotal1.grid(row=5, column=5, pady=10, padx=10)

    def total(self):
        self.lTotal=tk.Label(self.miFrame3, text='Total',bg='#3F3C3C',fg='#04B486')
        self.lTotal.grid(row=2, column=1,sticky='e', pady=5, padx=5)
        self.tTotal=tk.Entry(self.miFrame3,textvariable=self.obTotal,width=12)#state="readonly"
        self.tTotal.grid(row=2, column=2, sticky='w',pady=10, padx=10)


    def verArticulos(self):
        df=pd.read_csv('Articulos.csv')
        self.articuloTexto=tk.Text(self.miFrame3, width='70', height='10',fg='#A34B0C')
        self.articuloTexto.grid(row=1, column=0, columnspan=3, sticky='ew', padx=10, pady=10)
        self.articuloTexto.insert(tk.INSERT, df)
        self.total()

    def limpiarAllCampos(self):
        self.tDni.delete('0',tk.END)
        self.tTel.delete('0',tk.END)
        self.tApellido.delete('0',tk.END)
        self.tNombre.delete('0',tk.END)
        self.tDireccion.delete('0',tk.END)
        self.tBusqueda.delete('0',tk.END)
        self.cuadroTexto.delete('1.0',tk.END)
        self.tMensajes.delete('0',tk.END)
        self.limpiarEntrys()

    def limpiarEntrys(self):
        self.tDes1.config(state=tk.NORMAL)
        self.tM1.config(state=tk.NORMAL)
        self.tPrecio1.config(state=tk.NORMAL)
        self.tSubtotal1.config(state=tk.NORMAL)

        self.tDes1.delete('0',tk.END)
        self.tM1.delete('0',tk.END)
        self.tPrecio1.delete('0',tk.END)
        self.tSubtotal1.delete('0',tk.END)
        self.tCodigo1.delete('0',tk.END)
        self.tCantidad1.delete('0',tk.END)

        self.tDes1.config(state='readonly')
        self.tM1.config(state='readonly')
        self.tPrecio1.config(state='readonly')
        self.tSubtotal1.config(state='readonly')


gui=Gestor()
gui.root.mainloop()