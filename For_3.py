def div4_7(N):
	tot = 0
	
	for i in range(N):
		tot += (N%4 == 0 and N%7 == 0)
	print(tot)
	# rychlejsie by bolo vyprintovat floor(N/28)

print(div4_7(int(input("Zadajte N: "))))
