#Object Data Testing

class Example:
	def __init__(self, **kwargs):
		self.variables = kwargs

	def set_vars(self,k,v):
		self.variables[k] = v
	
	def get_vars(self,k):
		return self.variables.get(k,None)

var = Example(Nombre='Luis Eduardo', Location='Tijuana')
print(var.get_vars('Nombre'))