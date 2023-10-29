def rzymskie_na_arabskie(liczba_rzymska):
    rzymskie = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    } #slownik zawierajacy odpowiadajace liczby arabskie dla znakow w rzymskiej numeracji

    liczba_arabska = 0 #zmienna przechowujaca wartosc koncowa deszyfrowanej liczby
    poprzednia_wartosc = 0 #wartosc do sytuacji liczb takich jak IV lub XI

    for znak in reversed(liczba_rzymska): #petla przechodzi przez caly zapis rzymski od konca (jako ze tak zapisywane sa liczby rzymskie)
        aktualna_wartosc = rzymskie[znak]  #dla kazdego znaku odczytywana jest jego wartosc arabska a nastepne sprawdzane jest (przy pomocy zmiennej poprzednia_wartosc)
        #czy nie mamy do czynienia z sytuacja szczegolna VI lub IV. Jesli wartosc aktualna jest mniejsza niz poprzednia odejmujemy ta wartosc od liczba_arabska,
        #a jesli jest wieksza to dodajemy ja, na koniec wystepuje uaktualnienie warosci poprzednia_wartosc

        if aktualna_wartosc < poprzednia_wartosc:
            liczba_arabska -= aktualna_wartosc
        else:
            liczba_arabska += aktualna_wartosc

        poprzednia_wartosc = aktualna_wartosc

    return liczba_arabska

liczba_rzymska = "MCMXCIX"
liczba_arabska = rzymskie_na_arabskie(liczba_rzymska)
print(liczba_arabska)
