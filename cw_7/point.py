# point.py

class Point:

    def __init__(self, x, y):  #konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})" #wyświetlenie punktów jako stringa

    def __repr__(self):
        return f"Point({self.x}, {self.y})" #wyswietlanie punktu jako Point(,)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y #operator równosci miedzy punktami

    def __ne__(self, other):
        return not self == other #negacja rowności między punktami

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y) #dodawanie wektorow [a,b] + [c,d] = [a+c,b+d]

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y) #odejmowanie wektorow [a,b] - [c,d] = [a-c,b-d]

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  #iloczyn skalarny

    def cross(self, other):
        return self.x * other.y - self.y * other.x  #iloczyn wektorowy 2D

    def length(self):
        return (self.x**2 + self.y**2)**0.5  #długość wektora jako suma kwadratow która na sam koniec jest pierwiastkowana

    def __hash__(self):
        return hash((self.x, self.y))
