#Inheritance testing

class Animals:
	def eat(self):
		print("I can eat")
	def talk(self):
		print("I can talk")

class Cat(Animals):
	def talk(self):
		print("I can meow")
	def move(self):
		print("I can move")

#Putting 'pass' at a class simply passes all the functions of the parent 
#class and because it has no functions inside the childd class 
#it only have the parents class.
class Dog(Animals):
	pass

lilo = Cat()
#Printing cat function of talking
lilo.talk()

class Asiento:
	def __init__(self,material, color, textura):
		self.material = material
		self.color = color
		self.textura = textura

	def setMaterial(self,material):
		self.material = material

	def getMaterial(self,material):
		return self.material

	def setColor(self,color):
		self.color = color

	def getColor(self,color):
		return self.color

	def setTextura(self,textura):
		self.textura = textura

	def getTextura(self,textura):
		return self.textura

class Llanta:
	def __init__(self,material, tamano, agarre):
		self.agarre = agarre 
		self.tamano = tamano
		self.material = material

	def setAgarre(self,agarre):
		self.agarre = agarre

	def getAgarre(self,agarre):
		return self.agarre

	def setTamano(self,tamano):
		self.tamano = tamano

	def getTamano(self,tamano):
		return tamano

	def setMaterial(self,material):
		self.material = material

	def getMaterial(self,material):
		return self.material
		
class Carro(Asiento, Llanta):
	def __init__(self, marca, color, modelo, ano):
		self.marca = marca 
		self.color = color
		self.modelo = modelo
		self.ano = ano

	def setMarca(self,marca):
		self.marca = marca	

	def getMarca(self,marca):
		return self.marca

bmw = Carro("bmw","rojo","i5",2017)

bmw.