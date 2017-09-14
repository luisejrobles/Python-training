class Person:
	"""docstring for Person"""
	def __init__(self, name, earning, hours):
		self.name = name
		self.earning = earning
		self.hours = hours

	def overtimeCalc(self, extraHours):
		extraMoney = extraHours * self.earning
		extraMoney += extraMoney/2
		print('You have worked overtime', extraHours,'hours')
		print('You have earned', extraMoney,'extra money')
		return extraMoney

	def totalEarning(self):
		extraHours = 0
		total = 0
		if (self.hours > 8):
			extraHours = self.hours - 8
			self.hours = 8
			total = self.overtimeCalc(extraHours)
		total += self.hours*self.earning
		print('You have worked',self.hours, 'hours at a rate of',self.earning)
		print('So your total earnings are:', total)
		return total


luis = Person('Luis Eduardo', 3, 10)
luis.totalEarning()
