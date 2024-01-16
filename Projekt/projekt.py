import pygame
from collections import deque
import time

class MazeDrawer:
    def __init__(self):
        pygame.init()
        self.setup_display()  # Inicjalizacja ekranu Pygame
        self.setup_maze()  # Inicjalizacja punktu startowego i końcowego
        self.setup_game()  # Inicjalizacja zmiennych gry

    def setup_display(self):
        # Rozmiar ekranu
        self.WIDTH, self.HEIGHT = 1280, 720
        self.FPS = 50
        self.CELL_SIZE = 60
        # Kolory
        self.WHITE, self.BLACK, self.RED, self.BLUE, self.GREEN, self.GRAY, self.PURPLE = \
            (227, 218, 201), (0, 0, 0), (255, 0, 0), (0, 0, 255), (0, 255, 0), (211, 211, 211), (128, 0, 128)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Maze Drawing")

    def setup_maze(self):
        # Punkt poczatkowy i koncowy
        self.entry_point = None
        self.exit_point = None

    def setup_game(self):
        # Ustawienia początkowe gry
        self.drawing = False
        self.draw_path = False
        self.search_complete = False
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_status = True

    def draw_cell(self, row, col, color):
        # Rysowanie komórki
        pygame.draw.rect(self.screen, color,(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        # Rysowanie kratki
        pygame.draw.line(self.screen, self.GRAY, (col * self.CELL_SIZE, row * self.CELL_SIZE),(col * self.CELL_SIZE + self.CELL_SIZE, row * self.CELL_SIZE), 2)
        pygame.draw.line(self.screen, self.GRAY, (col * self.CELL_SIZE, row * self.CELL_SIZE),(col * self.CELL_SIZE, row * self.CELL_SIZE + self.CELL_SIZE), 2)

    def draw_grid(self, grid):
        # Rysowanie kwadratow w zaleznosci od wartosci
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 3:
                    self.draw_cell(row, column, self.GREEN)  # PATH
                elif grid[row][column] == 1:
                    self.draw_cell(row, column, self.BLACK)  # WALL
                elif grid[row][column] == 0:
                    self.draw_cell(row, column, self.WHITE)  # EMPTY
                elif grid[row][column] == 4:
                    self.draw_cell(row, column, self.BLUE)  # START
                elif grid[row][column] == 5:
                    self.draw_cell(row, column, self.RED)  # EXIT

    def animate_search(self, grid, start, end):
        # Animacja przeszukiwania labiryntu
        visited = set() # Set do przechowania odwiedzonych komorek
        q = deque([(start, [])])
        path_found = True

        while q:
            current, path = q.popleft()
            if current not in visited: # Sprawdzenie czy komorka nie zostala juz wczesniej odwiedzona
                visited.add(current)
                row, col = current
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 0:
                        q.append(((new_row, new_col), path + [(new_row, new_col)]))
                        grid[new_row][new_col] = 3  # Jesli komorka znajduje sie w obrebie labiryntu, nie zostala odwiedzona  i ma wartosc 0 to zmieniamy jej wartosc na 3 (komorka odwiedzona w BFS)
                        self.draw_grid(grid)  # Rysowanie aktualnego stanu labiryntu
                        pygame.time.delay(150) # Opoznienie dla "plynnosci" animacji
                        pygame.display.flip()
                    elif 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 5: # Sprawdzenie czy punkt nie jest punktem wyjsciowym, dodane bo wczesniej program nie zapisywal tej
                        q.append(((new_row, new_col), path + [(new_row, new_col)]))                                # tej wartosci i konczyl sie bez wyswietlenia sciezki
                        if (new_row, new_col) == end: # Sprawdzenie, czy bieżąca pozycja to punkt wyjścia
                            return path_found, path

        path_found = False
        return path_found, path

    def run(self):
        grid = [[0] * (self.WIDTH // self.CELL_SIZE) for _ in range(self.HEIGHT // self.CELL_SIZE)] # Inicjalizacja jako macierz z samymi zerami

        while not self.entry_point or not self.exit_point: # Pierwsza petla sluzaca do ustawienia punktu startowego i wyjsciowego
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s and not self.entry_point: # Klawisz S został wciśnięty i punkt startowy nie został jeszcze ustawiony
                        row, col = pygame.mouse.get_pos()[1] // self.CELL_SIZE, pygame.mouse.get_pos()[0] // self.CELL_SIZE
                        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                            grid[row][col] = 4
                            self.entry_point = (row, col) # Ustawienie punktu wejsciowego
                    elif event.key == pygame.K_e and not self.exit_point and self.entry_point: # Klawisz E został wciśnięty i punkt końcowy nie został jeszcze ustawiony
                        row, col = pygame.mouse.get_pos()[1] // self.CELL_SIZE, pygame.mouse.get_pos()[0] // self.CELL_SIZE
                        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 4 :
                            grid[row][col] = 5
                            self.exit_point = (row, col) # Ustawienie punktu wyjsciowego

            # Rysowanie na ekranie
            self.screen.fill(self.WHITE)
            self.draw_grid(grid)
            pygame.display.flip()

        while self.running: # Glowna petla gry po otrzymaniu wszystkich potrzebnych informacji
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.drawing = True
                elif event.type == pygame.MOUSEMOTION and self.drawing:
                    row, col = event.pos[1] // self.CELL_SIZE, event.pos[0] // self.CELL_SIZE
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 4 and grid[row][col] != 5: # Sprawdzenie, czy obszar nie zawiera punktu startowego lub końcowego
                            # Sprawdzenie, który przycisk myszy został wciśnięty
                            if event.buttons[0]:  # Lewy przycisk wiec program "rysuje" czarny labirynt
                                grid[row][col] = 1
                            elif event.buttons[2]:  # Prawy przycisk wiec program uznaje to jako "kasowanie" sciezki
                                grid[row][col] = 0
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.drawing = False
                elif event.type == pygame.KEYDOWN: # Jesli wykryte zostanie uzycie spacji to rysowanie zostaje wylaczone
                    if event.key == pygame.K_SPACE:
                        path_found, path = self.animate_search(grid, self.entry_point, self.exit_point) # Rozpoczecie szukania sciezki
                        self.draw_path = True

                        if path[-1] == self.exit_point or path_found: # Jesli sciezka znaleziona to program zaczyna rysowac ja na fioletowo
                            if self.draw_path:
                                for step in path:
                                    pygame.draw.rect(self.screen, self.PURPLE,(step[1] * self.CELL_SIZE, step[0] * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                                    pygame.display.flip()
                                    time.sleep(0.2) # Opoznienie dla plynnosci animacji
                            return True
                        else:
                            return False

            # Rysowanie na ekranie
            self.screen.fill(self.WHITE)
            self.draw_grid(grid)
            pygame.display.flip()
            self.clock.tick(self.FPS)

