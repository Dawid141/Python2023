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

def kratka(wiersze, kolumny):
    prostokat = ""
    for i in range(wiersze * 2):
        if i % 2 == 0:
            prostokat += "+" + "---+" * kolumny + "\n"
        else:
            prostokat += "|" + "   |" * kolumny + "\n"

    prostokat += "+" + "---+" * kolumny
    return prostokat

linijka = rysuj(7)
print(linijka)

prostokat = kratka(4, 3)
print(prostokat)
