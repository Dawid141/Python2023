from point import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]" #wypisuje kolejno wspolrzędne prostokata

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})" #podobnie jak wyżej ale z dodaniem słowa Rectangle

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2  #operator równości między prostokątami

    def __ne__(self, other):    #negacja równości między prostokątami
        return not self == other

    def center(self):       #zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)

    def area(self):     #zwraca pole prostokąta
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height

    def move(self, x, y): #przesuwa prostokąt o chciane wartości
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

    def intersection(self, other): #zwraca część wspólną dwóch prostokątów
        x_min = max(self.pt1.x, other.pt1.x)
        y_min = max(self.pt1.y, other.pt1.y)
        x_max = min(self.pt2.x, other.pt2.x)
        y_max = min(self.pt2.y, other.pt2.y)

        if x_min < x_max and y_min < y_max:
            return Rectangle(x_min, y_min, x_max, y_max)
        else:
            return None

    def cover(self, other): #zwraca prostokąt zakrywający obydwa prostokąty
        x_min = min(self.pt1.x, other.pt1.x)
        y_min = min(self.pt1.y, other.pt1.y)
        x_max = max(self.pt2.x, other.pt2.x)
        y_max = max(self.pt2.y, other.pt2.y)

        return Rectangle(x_min, y_min, x_max, y_max)

    def make4(self): #zwraca punkty związane z 4 prostokątami na które dzielony jest duży prostokąt
        center = self.center()

        rect1 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        rect2 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        rect3 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        rect4 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)

        return rect1, rect2, rect3, rect4


