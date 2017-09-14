
#Type(var) return the type of the variable ek:
#bool
#int
#string
#float

string = "123asdf"
num = 1234
bol = True

def checkString(string):

		return type(string)

print(checkString(string))
print(checkString(num))
print(checkString(bol))
