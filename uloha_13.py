def uloha_13(a, b, c):

    sides = sorted([a,b,c])
    type_1 = ""
    type_2 = ""

    if sides[0] < sides[1] + sides[2]:

        if sides[0] == sides[2]:
            print("Vytvorí rovnostranný trojuholník.")
            return

        if sides[0] == sides[1]:
            type_1 = " rovnostranný"

        if sides[0]**2 == sides[1]**2 + sides[2]**2:
            type_2 = "pravouhlý"

        elif sides[0]**2 > sides[1]**2 + sides[2]**2:
            type_2 = "tupouhlý"

        elif sides[0]**2 < sides[1]**2 + sides[2]**2:
            type_2 = "ostrouhlý"

        print("Vytvorí {0}{1} trojuholník.".format(type_1, type_2))

    else:
        print("Nevytvorí trojuholník.")

uloha_13(3,4,5)