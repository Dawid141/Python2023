def wspolne_elementy(sek1, sek2):
    wspolne = []

    for element in sek1:
        if element in sek2:
            wspolne.append(element)

    return wspolne

def unikalne_elementy(sek1, sek2):
    unikalne = list(set(sek1 + sek2))
    return unikalne


lista1 = ["dad", "ab", "dasdas", "wdawdaw", "dwa", 5]
lista2 = ["dad", 4, 5, 6, "ab","dwa"]

wspolne = wspolne_elementy(lista1, lista2)
unikalne = unikalne_elementy(lista1, lista2)

print("Wspólne elementy:", wspolne)
print("Unikalne elementy z obu sekwencji:", unikalne)