def triangle(rows: int):
	for i in range(rows):
		print((((rows - i - 1) * " ") + ( i + 1)*"* "))


a = 1
while a!=0:
	a = int(input())
	triangle(a)
