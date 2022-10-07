s = 0
count = 0
i = int(input("Zadaj cislo: "))
step =int(input("Zadaj krok: "))

while s < 100:
	s += i
	i += step
	count += 1


print(f"Suma: {s}, pocet cisel: {count}")
