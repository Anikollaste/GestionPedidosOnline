import sqlite3

class CrearBdd():

	def crearInsertar(self):

		miConexion = sqlite3.connect("BdFerretería")
		miCursor = miConexion.cursor()

		try:
			miCursor.execute("""
					CREATE TABLE PRODUCTOS(
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					NOMBRE_ARTICULO VARCHAR(50),
					METRICA VARCHAR(3),
					LARGO VARCHAR(20),
					PRECIO INTEGER(4))
			""")

		except sqlite3.OperationalError:
			print('La tabla ya existe')

		finally: #Insertar Campos en Bdd
				productos = [
				("tornillo","M8","22mm",0.20),
				("tornillo","M6","22mm",0.15),
				("tuerca","M8","10mm",0.10),
				("tuerca","M6","10mm",0.08)
				]

				miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?,?)", productos)

				miConexion.commit()
				miConexion.close()
