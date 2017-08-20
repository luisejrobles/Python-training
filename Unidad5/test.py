lista = [1,2,3,4,5,6,7,8,9,9]
lista2 = [11,12,13]

#print solo un numero
print(lista[2])

print("El tamano de la lista es: ",len(lista))


#uno por uno
for int in lista:
	print(int)

#imprimir algunos
print(lista[1:4])

#imprimir con salto
print(lista[::2])

#append agrega al final de la lista
lista.append(12)

#extend extiende la lista con otra lista
lista.extend(lista2)

#insert(posicion, item)
lista.insert(2,11)

#editando un valor de la lista
lista[2] = 3

#eliminando de la lista
del lista[2]

#eliminando de la lista buscando el valor
lista.remove(9)

#reverse invierte la cadena
lista.reverse()

#sort ordena lista
lista.sort()
lista.reverse()
lista3 = sorted(lista)
print(lista)
print(lista3)


