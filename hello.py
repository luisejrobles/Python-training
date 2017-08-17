#variables
miNombre = "Luis Eduardo"
miApellido = "Jimenez Robles"
misAnos = 22
miPeso = 105.5
todoJunto = "Hola mi nombre es {} tengo {} y peso {}"
lista = (1, 2, 3, 4)
miArreglo = [11, 22, 33, 44, 55]
misPalabras = {'nombre': 'Luis', 'Apellido': 'Jimenez'}
encendido = False

#prints
print("Hola Mundo!")
print(miNombre + " " + miApellido)
print(type(miNombre))
print(type(misAnos), misAnos)
print(type(miPeso), miPeso)

#format concatena variables a una cadena
print(todoJunto.format(miNombre, miApellido, misAnos, miPeso))
print("Imprimiendo lista:", lista)

#agregando valor a mi arreglo
miArreglo.append(99)
print("Imprimiendo mi arreglo con nuevo valor: ", miArreglo)

#imprimiendo algo del arreglo
print(miArreglo[0:2])
print(misPalabras)

#cambiando boolean
if encendido:
	print("hola")
else:
	print("no")
encendido = True
print(encendido)
print(miArreglo[0] + miArreglo[1])

#al cuadrado
print(5 ** 2)
