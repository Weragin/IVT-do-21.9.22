import math


# print("    1   2   3   4   5   6   7   8   9")
# for i in range(1, 10):
#
#     for j in range(1, 10):
#         print()
#

# funguje len z 10 na To, zatiaľ
def conversion(x, From = 10, To):
    res = str(To)+"/"
    if To ** math.floor(math.log(x, To)) == x:
        return res + "1" + x * "0"

    for i in range(math.floor(math.log(x, To)), -1, -1):
        res += str(1 * (To**i <= x))
        x -= To**i*(To**i <= x)
    return res
print(conversion(156, To = 2))


def to_dec(x,From):
    res = 0
    been = 0
    for i in x:
        been += 1*(i=="/")
        i *= been
    x[0] = ""
    for i in range(len.x, -1, -1):
        res += x[i]
