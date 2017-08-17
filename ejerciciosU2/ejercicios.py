# Using the knowledge that:
#	When under constant movement, we can work out the acceleration of a vehicle, assuming no friction
#	using the following equation:
#		V = u + at
#		
#	Where v is final velocity (25m/s), u is initial velocity (0 m/s) and t is time taken (10 seconds)
#	Work out acceleration (a) and print it to the screen
#	
#	Despejando:
#		V-U = at
#		a = (V-U)/t

velocidad = 25
velInicial = 0
tiempo = 10
aceleracion = (velocidad - velInicial) / tiempo
print(aceleracion)
