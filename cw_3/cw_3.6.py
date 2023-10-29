def kratka(wiersze, kolumny):
    prostokat = ""
    for i in range(wiersze * 2):
        if i % 2 == 0:
            prostokat += "+" + "---+" * kolumny + "\n"
        else:
            prostokat += "|" + "   |" * kolumny + "\n"

    prostokat += "+" + "---+" * kolumny

    return prostokat


wiersze = 10
kolumny = 20

prostokat = kratka(wiersze, kolumny)
print(prostokat)
