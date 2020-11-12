import sqlite3
from pathlib import Path
from bdFerreteria import CrearBdd
import csv
from os import remove
import time
import tkinter as tk
from tkinter import filedialog
import pandas as pd

class Funciones(CrearBdd):


	#----------------- Dado un nombre guarda el archivo con los datos del pedido ------------------
	def guardar_archivo(self):
		archivo_guardado=filedialog.asksaveasfilename(initialdir="/home",title="Selecciona archivo",
			defaultextension=".txt",filetypes = (("txt files","*.txt"),("all files","*.*")))

		self.generarAlbaran()
		archivo=open(archivo_guardado,"w")
		with open('Albaran.txt','r') as p:
			l=p.readlines()
			p.close()
		archivo.writelines(l)
		archivo.close()


 	#----------------- Crea el archivo Datos cliente.csv ---------------------------------
	def datosCliente(self):
		datos_cliente=[
		['Dni:',self.obDni.get()],
		['Télefono:',self.obTelefono.get()],
		['Apellidos:',self.obApellido.get()],
		['Nombre:',self.obNombre.get()],
		['Dirección:',self.obDireccion.get()]
		]
		infoCliente=Path('Datos_Cliente.csv').is_file()

		if infoCliente==False:
			with open('Datos_Cliente.csv','w',newline='') as f:
				w=csv.writer(f)
				w.writerows(datos_cliente)


	# Crea un archivo de texto con los campos Nombre,Dni,Tel,Dirección, Apellidos y Datos del pedido.
	def generarAlbaran(self):
		self.datosCliente()
	
		tituloCliente=' Datos del cliente '
		tituloDatos=' Datos del pedido '

		with open('Albaran.txt','w') as p:
			p.write(tituloCliente.center(70,'_'))
			p.write('\n')

			with open('Datos_Cliente.csv') as c:
				wCliente=csv.reader(c)
				for row in wCliente:
					p.writelines('{:<14}{:<14}\n'.format(row[0],row[1]))
			p.write('\n')

			with open('Articulos.csv') as f:
				wArticulos=csv.reader(f)
				p.write(tituloDatos.center(70,'_'))
				p.write('\n')

				for row in wArticulos:
					p.writelines('{:<14}{:^14}{:^14}{:^14}{:^14}\n'.format(row[0],row[1],row[2],row[3],row[4]))
			p.write('\n*Importe total: {}$'.format(str(self.suma)))


	# Consulta campo ID y autocompleta los campos; Descripción,Métrica y Precio
	def consultaBdd(self):

		conexion=sqlite3.connect("BdFerretería")
		cursor=conexion.cursor()

		while True:
			try:
				cursor.execute("SELECT * FROM PRODUCTOS WHERE ID = {}".format(self.obC1.get()))
				productos = cursor.fetchall()

			except sqlite3.OperationalError:
				self.obMensaje.set('Los campos ID y Cantidad no pueden estar en blanco')
				conexion.commit()
				conexion.close()
				break
	
			for campoID in productos:
				descripcion=campoID[1]
				metrica=campoID[2]
				valorPrecio=campoID[4]

			cantidad=self.obCa1.get()
			subTotal=round(cantidad*valorPrecio,2)
			self.obDe1.set(descripcion)
			self.obM1.set(metrica)
			self.obP1.set(valorPrecio)
			self.obSb1.set(subTotal)
			
			insertar=[descripcion,metrica,cantidad,valorPrecio,subTotal]
			self.insertArti(insertar)
			break

	#----------------- Si no existe crea el archivo Articulos.csv e inserta fila encabezados ------
	def articulos(self):
		infoArticulos=Path('Articulos.csv').is_file()

		if infoArticulos==False:
			with open('Articulos.csv','w',newline='') as f:
				w=csv.writer(f)
				w.writerow(['Descripción','Métrica','Cantidad','Precio unidad','Subtotal'])
		else:
			None

		
	#--------------- Inserta nuevos artículos y obtiene Total----------------------
	def insertArti(self,datos):
		self.articulos()

		with open('Articulos.csv','a',newline='') as f:
			w = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
			w.writerow(datos)

		df=pd.read_csv('Articulos.csv')
		self.suma=round(df['Subtotal'].sum(),2)
		self.obTotal.set(self.suma)


	#--------------- Consulta de productos en el almacen BDD -------------------------------------
	def consultaAlmacen(self):
		conexion=sqlite3.connect("BdFerretería")
		cursor=conexion.cursor()
		cursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_ARTICULO = '{}'".format(self.vBus.get().lower()))

		articulos = cursor.fetchall()
		conexion.commit()
		conexion.close()
		#################################################################################
		#						Por revisar		

		# with open('BusquedaBdd.csv','w') as b:
		# 	w=csv.writer(b)
		# 	w.writerows(articulos)
		# df=pd.read_csv('BusquedaBdd.csv',columns=['ID','Métrica','Largo','Precio'])
		#################################################################################

		for nomArt in articulos:
			iD=nomArt[0]
			mT=nomArt[2]
			largo=nomArt[3]
			precio=nomArt[4]
			self.cuadroTexto.insert('1.0','iD\t  {}\nMétrica  {}\nLargo  {}\nPrecio  {}\n'.format(iD,mT,largo,precio))

			
	#--------------- Evalua si existe el archivo BdFerretería -------------------------------------
	def bdd_existe(self):
		archivo=Path('BdFerretería').is_file()

		if archivo==False:
			self.crearInsertar()
		else:
			None


	#--------------- Elimina archivos al salir de la aplicación
	def eliminarArchivos(self):
		datosAlbaran=['Datos_Cliente.csv','Articulos.csv','Albaran.txt']

		for arch in datosAlbaran:
			try:
				remove(arch)
			except FileNotFoundError:
				None
		self.root.destroy()


	