N = int(input("Zadaj cislo: "))
s = 0

for i in range(N//2): 
	s += i*2


print(s)
# Rýchlejšie s použitím matiky (for is slow):

N = int(input("Zadaj cislo (rychly algorytmus): "))
s = (N//2 + 1)N//2	# vzorček pre súčet od 1 do N//2 vynásobený dvomi
