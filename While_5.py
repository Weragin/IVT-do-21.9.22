word = input("Zadajte slovo: ")
count = 0

while word[0] != "x":
	count += len(word)
	word = input("Zadajte slovo: ")


print(f"Dokopy symbolov: {count}")
