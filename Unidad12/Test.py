#using date time library
import datetime
import sys
import os

time = datetime.datetime.today()
print(time)

start = datetime.datetime.now()
i = 0
while i < 1000000:
	i+=1

end = datetime.datetime.now()
print(end-start)


print(os.name)