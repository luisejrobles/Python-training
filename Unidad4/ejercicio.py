#Fibonacci numbers
num0, num1,Fn = 0,1,0

while Fn <= 100:
	Fn = num0+num1
	print("F0: ", num0)
	print("F1: ", num1)
	num0 = num1
	num1 = Fn 
	print("Fn: ", Fn)

