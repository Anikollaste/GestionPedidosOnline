import sqlite3
from pathlib import Path
from bdFerreteria import CrearBdd as bdd
import csv

class Funciones():
	#----------------- Crea el archivo Datos cliente.csv ---------------------------------
	@staticmethod
	def datosCliente(self):
		datos_cliente=[
		['Dni:',self.obDni.get()],
		['Télefono:',self.obTelefono.get()],
		['Apellidos:',self.obApellido.get()],
		['Nombre:',self.obNombre.get()],
		['Dirección:',self.obDireccion.get()]
		]

		with open('Datos_Cliente.csv','w',newline='') as f:
			w=csv.writer(f)
			w.writerows(datos_cliente)

	# Crea un archivo de texto con los campos Nombre,Dni,Tel,Dirección, Apellidos y Datos del pedido.
	def verAlbaran(self):
		Funciones.datosCliente(self)
	
		tituloCliente=' Datos del cliente '
		tituloDatos=' Datos del pedido '

		with open('Prueba.txt','w') as p:
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

				total=[]
				for row in wArticulos:
					p.writelines('{:<14}{:^14}{:^14}{:^14}{:^14}\n'.format(row[0],row[1],row[2],row[3],row[4]))
					total.append(row[4])
				
				'''
				1)-Elimina primer elemento de la lista total 'Subtotal'
				2)-Convierte la lista a float 'result'
				3)-Suma los elementos de la lista
				
				***FALTA convertir a string para poder escribir el resultado en el TXT(sólo acepta string)

					'''
				total.pop(0)
				result = list(map(lambda x: float(x.replace(",", "")), total))
				suma=(sum(result))
				print(suma)
				#p.write(total)

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

			Funciones.insertArti(insertar)
			break

	#----------------- Si no existe crea el archivo Articulos.csv e inserta fila encabezados ------
	def articulos():
		infoArticulos=Path('Articulos.csv').is_file()

		if infoArticulos==False:
			with open('Articulos.csv','w',newline='') as f:
				w=csv.writer(f)
				w.writerow(['Descripción','Métrica','Cantidad','Precio unidad','Subtotal','Total'])
		else:
			None

		
	#--------------- Inserta nuevos artículos ----------------------
	def insertArti(datos):
		with open('Articulos.csv','a',newline='') as f:
			w = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
			w.writerow(datos)


	#--------------- Consulta de productos en el almacen BDD -------------------------------------
	def consultaAlmacen(self):
		conexion=sqlite3.connect("BdFerretería")
		cursor=conexion.cursor()
		cursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_ARTICULO = '{}'".format(self.vBus.get().lower()))

		articulos = cursor.fetchall()
		conexion.commit()
		conexion.close()

		for nomArt in articulos:
			iD=nomArt[0]
			mT=nomArt[2]
			largo=nomArt[3]
			precio=nomArt[4]
			self.cuadroTexto.insert('1.0','iD\t  {}\nMétrica  {}\nLargo  {}\nPrecio  {}\n'.format(iD,mT,largo,precio))
			
	#--------------- Evalua si existe el archivo BdFerretería -------------------------------------
	def bdd_existe():
		archivo=Path('BdFerretería').is_file()

		if archivo==False:
			bdd.crearInsertar()
		else:
			None
