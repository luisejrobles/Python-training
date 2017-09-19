#Abriendo archivos en python
file = open("archi.txt")

for line in file:
	print(line,end = '')

#Escribiendo en archivo de texto

input = open("archi.txt",'r')
output = open('text.txt','w')




#Escribir y leer archivos binarios