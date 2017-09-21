import sqlite3

class LogMessageFile:
	def __init__(self,name):
		self.file = open(name,'r+')
	
	def write(self):
		self.file.write('We in!')
		#self.file.close()

	def read(self):
		#self.file.open()
		print (self.file.readline())


class LogMessageDB:
	def __init__(self,name):
		self.db = sqlite3.connect(name)
		self.db.execute('drop table if exists logginMessage')
		self.db.execute('create table logginMessage(message text)')
		self.db.execute('insert into logginMessage(message) values("We in!")')
		self.db.commit()

	def read(self):
		message = self.db.execute('select * from logginMessage')
		for msg in message:
			print(msg)