##1 kod
L = [3, 5, 4] ; L = L.sort()

##mamy do czynienia z redundancją poniewaz sort soruje liste w miejscu wiec powinno sie to zapisac w ten sposob
L = [3, 5, 4]
L.sort()


##2 kod
x, y = 1, 2, 3 ##proba przypiisania dwom zmiennym trzech wartosci wiec blad

##3 kod
X = 1, 2, 3 ; X[1] = 4 ##blad braku możliwości zmiany X powinno sie zapisac
X = (1, 4, 3)


##4 kod
X = [1, 2, 3] ; X[3] = 4 ##proba odwolanai sie do elementu poza zakresem listy

##5 kod
X = "abc" ; X.append("d") ##metoda append jest dostepna dla list a nie lancuchow znakow

##6 kod
L = list(map(pow, range(8))) ##brak ostatniego nawiasu zamyykajacego