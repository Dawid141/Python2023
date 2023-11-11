from math import gcd


def add_frac(frac1, frac2):
    mian = frac1[1] * frac2[1]
    licz = frac1[0] * frac2[1] + frac2[0] * frac1[
        1]  # mnożymy przez siebie mianowniki a nastepnie każdy z liczników mnożymy przez ten "drugi" mianownik
    return simplify_frac([licz, mian])


def sub_frac(frac1, frac2):
    return add_frac(frac1, [-frac2[0], frac2[1]])  # dodawanie na minusie


def mul_frac(frac1, frac2):
    return simplify_frac([frac1[0] * frac2[0], frac1[1] * frac2[1]])  # góra z górą, dół z dołem


def div_frac(frac1, frac2):
    return mul_frac(frac1, invert_frac(frac2))  # jak wiadomo dzielenie to mnożenie przez odwrotność


def is_positive(frac):  # sprawdzenie czy ułamek jest większy niż 0
    return frac[0] * frac[1] > 0


def is_zero(frac):  # sprawdzenie czy nie jest zerem
    return frac[0] == 0


def cmp_frac(frac1,
             frac2):  # generalnie chodzi o porównanie dwóch ułamków ze sobą i zwrócenie wartości 1 gdy pierwszy z
    # nich jest większy, -1 gdy dugi i 0 gdy są równe
    diff = sub_frac(frac1, frac2)
    if diff[0] > 0:
        return 1
    elif diff[0] < 0:
        return -1
    else:
        return 0


def frac2float(frac):  # zwykłe dzielenie zwracające nam postać float
    return frac[0] / frac[1]


def simplify_frac(
        frac):  # funkcja pomocnicza do upraszczania ulamkow.W innym wypadku np. w dodawaniu otrzymywalibysmy bardzo
    # malo optymalne wyniki
    common_div = gcd(frac[0], frac[
        1])  # używamy funkcji gdc do znalezienia największego wspólnego dzielnika i następnie dzielimy licznik i
    # mianownik przez ten dzielnik
    return [frac[0] // common_div, frac[1] // common_div]


def invert_frac(frac):  # funkcja pomocnicza służąca do inwersji ułamka w przypadku dzielenia
    return [frac[1], frac[0]]
