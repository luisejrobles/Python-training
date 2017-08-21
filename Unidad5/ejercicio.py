lista = [8, 7, 12, 4, 9, 6, 5]
#i,j = 0, 0
aux = 0

largo = len(lista)
print(largo)

for i in range(len(lista)):
	for j in range(len(lista)-1):
		if lista[j] > lista[j+1]:
			aux = lista[j+1]
			lista[j+1] = lista[j]
			lista[j] = aux
		j+=1
	i+=1
print(lista)
