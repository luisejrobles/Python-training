#WHILE loops
var1 = 5

while var1 != 0:
	print("HEY")
	var1 -= 1


#FOR loops
for data in ['hola','como','estas']:
	print(data)

#sacando letras pares
for key,letra in enumerate('holamiasd'):
	if key % 2 == 0:
		print('La letra {} está en una posicion par'.format(letra)) 


#Try, Except, Finally
array = (1,2,3,4,5)
try:
	array.append(6)
except AttributeError as e:
	print("Error: ",e)
else:
	for each in array:
		print(each)


#Break, Continue, else
lista = [1,2,3,4,5,6,7]
for num in lista:
	print(num)
	if num == 5:
		break
print("terminó")

#Testint continue
for int in lista:
	if (int == 5) or (int == 4):
		continue
	else:
		print(int)
print("terminó")