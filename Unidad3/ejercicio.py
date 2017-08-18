varA, varB = 1,0
varQ = 5

#AND table
if varA == 1 and varB == 1:
	varQ = 1
elif varA == 1 and varB == 0:
	varQ = 0
elif varA == 0 and varB == 1:
	varQ = 0
else:
	varQ = 0
print(varQ)

#OR table
if varA == 1 and varB == 1:
	varQ = 1
elif varA == 1 and varB == 0:
	varQ = 1
elif varA == 0 and varB == 1:
	varQ = 1
else:
	varQ = 0
print(varQ)

#NOT table
if varA:
	varA = 0
else:
	varA = 1
print(varA)

#Hard table
varA, varB, varC, varQ = 1, 0, 0, 5
if varB:
	varB = 0
else:
	varB = 1

if (varA and varB) or varC:
	varQ = 1
else:
	varQ = 0
print(varQ)