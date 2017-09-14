APIkey = '82914656273523:a4edFea2786DGex'
APIdata = APIkey.split(':')
ID = APIdata[0]
key = APIdata[1]
print(ID)
print(key)
if ID.isdigit() == True and len(ID) == 14:
	if key.isalnum() == True and (len(key) > 10 or len(key) < 20):
		print("All is good")
else:
	print("The ID or the key are incorect, please contact the appropiate person to fix it.")