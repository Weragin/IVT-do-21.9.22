def oneToN(N): # pomalé
	s = 0
	
	for i in range(N):	# pripocita aj nulu, ale to nema efekt
		s+= N
	print(s)


def oneToNfast(N): # rýchle
	print((N+1)*N/2)


1toN(int(input("Zadajte N: ")))
