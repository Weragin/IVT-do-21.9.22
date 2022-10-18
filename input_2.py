def line(n: int, text=""):
    if text == "":
        print(n * "*")
    else:
        stars = (n - len(text) - 2)
        assert stars >=0, "Given text is longer than the length of a line"
        print((stars + 1) // 2 * "*" + " " + text + " " + stars // 2 * "*")
        # stars + 1 // 2 will be h/2 for evens and stars/2 + 1 for odd


while True:
    line(int(input("Gimme numba: ")), input("Gimme texta: "))
