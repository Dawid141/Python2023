import pygame
import sys
import random

pygame.init()

# Proste ustawienai okna gry oraz nazwa
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Topienie Śniegu")

# kolory które będą używane podczas gry
white = (255, 255, 255)
black = (0, 0, 0)

# ustawienia płatka sniegu
snowflake_size = 40
snowflake_color = (255, 255, 255)
snowflakes = []

# ustawienie gry na stan poczatkowy
clock = pygame.time.Clock()
game_over = False
score = 0

while not game_over: # prosta petla ktora dziala do czasu aż nie zostanie spełniony warunek quit. W ifie sprawdzamy po prostu czy klikniecie
    for event in pygame.event.get(): # uzytkownika zawiera sie w rozmiarze naszego platka sniegu, jesli tak score idzie w gore
        if event.type == pygame.QUIT: # a platek jest kasowany, jesli nie to warunek quit jest spelniony i game_over ustawia sie na true co konczy rozgrywke
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for snowflake in snowflakes:
                if (
                    snowflake[0] < mouse_x < snowflake[0] + snowflake_size
                    and snowflake[1] < mouse_y < snowflake[1] + snowflake_size
                ):
                    score += 1
                    snowflakes.remove(snowflake)

    # dodawanie platkow sniegu, czestotliwosc generowania oraz losowe rozmieszczanie u gory ekranu
    if random.randint(0, 100) < 7:
        snowflakes.append([random.randint(0, width - snowflake_size), 0])

    # aktualizowanie pozycji platkow sniegu - innymi slowy proces ich spadku
    for snowflake in snowflakes:
        snowflake[1] += 2
        if snowflake[1] > height: # jesli platek spadnie "poza" ekran gra sie konczy
            game_over = True

    # rysowanie tla gry
    screen.fill(black)

    # samo w sobie rysowanie platkow sniegu
    for snowflake in snowflakes:
        pygame.draw.rect(screen, snowflake_color, (snowflake[0], int(snowflake[1]), snowflake_size, snowflake_size))

    # scoreboard w lewym gornym rogu rozgrywki
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(24) # ilosc klatek

# Zakończenie gry
pygame.quit()
sys.exit()
