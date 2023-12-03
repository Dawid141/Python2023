from point import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, file_path): #metoda czyta dane z pliku i tworzy prostokąt
        with open(file_path, "r") as file:
            lines = file.readlines()
            point1_data = list(map(int, lines[0].split()))
            point2_data = list(map(int, lines[1].split()))

        point1 = Point(*point1_data)
        point2 = Point(*point2_data)
        return cls(point1.x, point1.y, point2.x, point2.y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y) #górna krawędz prostokata

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y) #dolna krawędz prostokąta

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x) #lewa krawędz prostokąta

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x) #prawa krawędz prostokąta

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x) #szerokosc prostokata

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y) #wysokosc prostokata

    @property
    def topleft(self):
        return Point(self.left, self.top) #wierzcholek gorny lewy

    @property
    def topright(self):
        return Point(self.right, self.top) #wierzcholek gorny prawy

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom) #wierzcholek dolny lewy

    @property
    def bottomright(self):
        return Point(self.right, self.bottom) #wierzcholek dolny prawy

    def __eq__(self, other): #eq z poprzedniego programu
        return self.pt1 == other.pt1 and self.pt2 == other.pt2
