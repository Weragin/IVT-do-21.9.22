def pal(string):

    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False

    return True
