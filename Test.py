#Classes and Objects
class Person:
	"""docstring for Person"""
	def __init__(self,gender,name):
		self.gender = gender 
		self.name = name
	def display(self):
		print("You're a ", self.gender ,"and your name is: ",self.name)


people = Person("Male","Luis Eduardo Jimenez Robles")
people2 = Person("Female","Brenda Herrera")

people.display()
people2.display()

	