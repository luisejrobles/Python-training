#Using db from python
import sqlite3

db = sqlite3.connect('database.db')
#Row factory allows to treat the rows with all their keys and attributes
db.row_factory = sqlite3.Row

db.execute('drop table if exists person')
db.execute('create table person (firstname text, secondname text, age int)')
db.execute('insert into person(firstname,secondname,age) values("Luis", "Eduardo","24")')

#Commit is used to make the changes
db.commit()

#Updating rows in db with command where
db.execute('update person set firstname ="Alex" where secondname="Eduardo"')
db.execute('insert into person(firstname,secondname,age) values("Saul", "Hernandez", "23")')
db.commit()

#Retrieve data from db
# * is used to select all the entries from the db
table = db.execute('select * from person')
for each in table:
	print(dict(each))