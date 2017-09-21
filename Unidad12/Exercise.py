from classes import LogMessageDB
from classes import LogMessageFile

#Read/Write to file
file = LogMessageFile('archivo.txt')
file.write()
file.read()

#Read/Write to DB

dataBase = LogMessageDB('db')
dataBase.read()