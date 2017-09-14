#Functions!
#All functions manage parameters by reference not by value!

num1, num2 = 5,6
myArray = [1,2,3,4,5,6]
myArray2 = [4,5,6,7,8]

def func_sum(num1, num2):
	"It sums two values!"
	return num1+num2

result = func_sum(num1,num2)
print(result)


def func_sumArray(array):
	sum = 0
	for num in array:
		sum += num

	return sum

resultado = func_sumArray(myArray)
#print("La suma de los digitos en el arreglo es: {}" .format(func_sumArray(myArray)))
print("La suma de los digitos en el arreglo es: {}" .format(resultado))


#Concanetate two arrays
def func_conca2Arrays(array, array2):
	array.extend(array2)

func_conca2Arrays(myArray,myArray2)
print(myArray)