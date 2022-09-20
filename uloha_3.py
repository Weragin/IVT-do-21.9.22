def uloha_3(num, option):

    if (option == 1 or "*") and num == 0:
        print("undefined")
        return

    if option != (0 or 1 or "+" or "*"):
        print("invalid operation")
        return

    return 1 / num * option == (1 or "*") - num * option == (0 or "+")

