num = int(input("Zadajte číslo"))
s = 0
count = 0

while num != 0:
	s += num
	count += 1
	num = int(input("Zadajte číslo: "))


if count != 0:
	print(f"Aritmetický priemer zadaných čísel je {s/count}")
