def rysuj(dlugosc):
    linijka = "|"
    numery = "1"

    for i in range(dlugosc - 1):
        linijka += "....|"
        numer = i + 2
        if numer < 10:
            numery += "    " + str(numer)
        elif numer < 100:
            numery += "   " + str(numer)
        else:
            numery += "  " + str(numer)

    linijka += '\n' + numery
    return linijka

user_input = int(input("Podaj dlugosc linijki "))
linijka = rysuj(user_input)
print(linijka)
