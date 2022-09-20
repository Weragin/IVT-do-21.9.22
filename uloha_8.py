def uloha_8(num):  # true if sum of last to digits divisible by 2

    return (num % 10 + num % 100 // 10) % 2 == 0

