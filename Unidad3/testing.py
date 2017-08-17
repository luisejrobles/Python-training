#Unidad 3 Python
#Condicionales

#if statement
var1, var2 = 2, 1
if var1 == var2:
	print("Si lo es")
else:
	print("No lo es")

if not var1 > var2:
	print("No lo es")
else:
	print("Si lo es")

if var1 == var2 or var2 < var1:
	print("Entró");

if var1 > var2 and var2 == 1:
	print("var2 si es uno")

if var1 < var2 or var2 == 1:
	print("Test con or")

#else if 
#elif statement
var1, var2 = 55, 21
if var1 < var2:
	print("Var1 es menor")
elif var1 > var2:
	print("Var1 es mayor")
else:
	print("Son iguales")

#switch statement