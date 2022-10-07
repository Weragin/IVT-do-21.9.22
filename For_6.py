def div8(low, upp):
	"""Pomalé:
	s = 0
	for i in range(low, upp):
		s+= i%8 == 0
	return s
	
	Rýchle:
	"""
	
	if low > upp:
		raise Exception("The upper bound has to be higher than the lower bound. ")
	else:
		return (upp - low)//8 + (upp%8 < (upp - low)%8)
			# Druhá časť zistí, či sa pre velkosť zoznamu nedeliteľnú 8
			# zmestí dalšie číslo deliteľné 8
			# napr. veľkosť 9 môže mať 1 alebo 2 také čísla

print(div8(int(input("Lower bound: ")), int(input("Upper bound: "))))
