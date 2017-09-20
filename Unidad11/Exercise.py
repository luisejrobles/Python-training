import sqlite3

class Excercise:
	def __init__(self, nombre):
		self.db = sqlite3.connect(nombre)
		self.db.execute('DROP TABLE IF EXISTS  mensajes')
		self.db.execute('create table mensajes(nombre text, mensaje text)')

	def readDB(self):
		entradas = self.db.execute('SELECT * from mensajes')
		for entries in entradas:
			print(entries)

	def writeDB(self,mensaje, nombre):
		self.db.execute('INSERT INTO mensajes(nombre, mensaje) VALUES (?, ?)',(mensaje, nombre))
		self.db.commit()


prueba = Excercise('DB')
prueba.writeDB('Hola como estan','Luis Eduardo Jimenez')
prueba.writeDB('Esta es una prueba','Yessica Jimenez Robles')
prueba.readDB()
