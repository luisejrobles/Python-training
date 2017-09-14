gender = 0
boolean = 0
while (boolean == 0):
	print("Ingresa m/M f/F para elegir tu sexo")
	gender = input()
	gender = gender.upper()
	print("el genero ingresado es {}" .format(gender) )
	if gender == 'M' or gender == 'F':
		print("El sexo seleccionado es: {}" .format(gender))
		boolean = 1