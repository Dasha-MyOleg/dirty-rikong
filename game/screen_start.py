import pygame
from . import config

pygame.init()

class ScConfig:
    SIZE        = (1280, 720)
    START_SIZE  = (0, 0)
    HIDDEN_SIZE = (-400, 1360)


class main_pictures:
    Player1    = pygame.image.load('images/screen_start/main_start/Player1.png')
    Frog       = pygame.image.load('images/screen_start/main_start/Frog.png')
    Snake      = pygame.image.load('images/screen_start/main_start/Snake.png')
    Rat        = pygame.image.load('images/screen_start/main_start/Rat.png')
    main_bg    = pygame.image.load('images/screen_start/main_start/main_bg.png')


class main_buttons:
    play_button = pygame.image.load('images/screen_start/main_start/play_button.png')
    choose_player_button = pygame.image.load('images/screen_start/main_start/Choose_Player_button.png')
    function_button = pygame.image.load('images/screen_start/main_start/Function_button.png')


class Pictures_Y:
    SNAKE_Y = 100
    FROG_Y = 40
    RAT_Y = 50
    PLAYER1_Y = 100

# Кнопки оловного меню (треба перенести)
#кнопка запуску гри  , початковий екран
restart_button_image  = main_buttons.play_button
restart_button_rect   = restart_button_image.get_rect(topleft  = (399, 90))

#кнопка вибору гравця, початковий екран
choose_player_image   = main_buttons.choose_player_button
choose_player_rect    = choose_player_image.get_rect(topleft   = (409, 320))

#кнопка функцій      , початковий екран
function_button_image = main_buttons.function_button
function_button_rect  = function_button_image.get_rect(topleft = (449, 440))


def draw_main_menu_buttons(screen):
    screen.blit(restart_button_image, restart_button_rect)
    screen.blit(choose_player_image, choose_player_rect)
    screen.blit(function_button_image, function_button_rect)


def listen_main_menu_buttons(event):
    # що роблять кноки
    game_state = None
    if event.type == pygame.MOUSEBUTTONDOWN:
        if restart_button_rect.collidepoint(event.pos):
            game_state = config.GameState.PLAYING.value

        elif choose_player_rect.collidepoint(event.pos):
            game_state = config.GameState.PLAYING.value

        elif function_button_rect.collidepoint(event.pos):
            game_state = config.GameState.PLAYING.value

    return game_state
