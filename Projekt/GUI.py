import pygame
import sys
from button import Button
from projekt import MazeDrawer
import time

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def display_info(messages): # Wyswietlanie informacji przed rozpoczeciem gry
    info = True
    while info:
        SCREEN.blit(BG, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        y_position = 260
        for message in messages:
            WIN_TEXT = get_font(20).render(message, True, "White")
            WIN_RECT = WIN_TEXT.get_rect(center=(640, y_position))
            SCREEN.blit(WIN_TEXT, WIN_RECT)
            y_position += 40

        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="OK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    info = False
                    break

        pygame.display.update()


def play():
    messages = [
        "1. Press S and click on the maze to set the start point",
        "2. Distance between both cells must be 1 >=",
        "3. Press E and click on the maze to set the end point",
        "4. Draw walls by holding the left mouse button",
        "5. Remove walls by holding the right mouse button",
        "6. Press Space and click on the maze to start the algorithm"
    ]

    display_info(messages) # Wyswietlanie tych wiadomosci

    maze_drawer = MazeDrawer()
    game_status = maze_drawer.run()
    SCREEN.blit(BG, (0, 0))

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        if game_status:
            message = "Path found!"
        else:
            message = "No Path!"

        WIN_TEXT = get_font(75).render(message, True, "White")
        WIN_RECT = WIN_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(WIN_TEXT, WIN_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_AGAIN = Button(image=None, pos=(640, 560),
                            text_input="PLAY AGAIN", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        PLAY_AGAIN.changeColor(OPTIONS_MOUSE_POS)
        PLAY_AGAIN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if PLAY_AGAIN.checkForInput(OPTIONS_MOUSE_POS):
                    play()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 500),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
# Inspired by https://www.youtube.com/watch?v=GMBqjxcKogA User baraltech