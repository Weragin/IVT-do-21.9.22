def rectangle(w, symbol = "*"):
	print(w * symbol)
	print(symbol + (w - 2) * " " * len(symbol) + symbol)
	print(w * symbol)


rectangle(7, "©©©")
