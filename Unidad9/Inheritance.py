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
