import sys
import pygame
from . import config


def listen_game_mode(restart_button_rect, game_state):
    for event in pygame.event.get():

        # game quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # game start
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button_rect.collidepoint(event.pos):
                game_state = config.GameState.PLAYING.value

        # пояснення при  яких випадках буде START PLAYING GAME_OVER
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if game_state == config.GameState.START .value:
                    game_state = config.GameState.PLAYING.value
                elif game_state == config.GameState.PLAYING.value:
                    if config.blasters.BLASTERS_LEFT > 0:
                        config.blasters.BLASTS.append(
                            config.blasters.BLAST.get_rect(topleft=(config.Player.X + 100, config.Player.Y + 127)))
                        config.blasters.BLASTERS_LEFT -= 1
                elif game_state == config.GameState.GAME_OVER.value:
                    game_state = config.GameState.START.value


def main_menu_movement(screen, screen_start):
    """

    Args:
        screen: Rokgs
        screen_start: dytfugihuoj

    Returns:

    """
    # Рух змії, головний екран
    if screen_start.Pictures_Y.SNAKE_Y >= 0:
        if screen_start.Pictures_Y.SNAKE_Y >= 10:
            # Звичайна швидкість для Х кадрів
            screen_start.Pictures_Y.SNAKE_Y -= 1.9
        else:
            # Сповільнена швидкість для останніх Х кадрів
            screen_start.Pictures_Y.SNAKE_Y -= 0.3

    screen.blit(screen_start.main_pictures.Snake, (0, screen_start.Pictures_Y.SNAKE_Y))


    # Рух жаби, головний екран
    if screen_start.Pictures_Y.FROG_Y >= 0:
        if screen_start.Pictures_Y.FROG_Y >= 14:
            # Звичайна швидкість для Х кадрів
            screen_start.Pictures_Y.FROG_Y -= 1.3
        else:
            # Сповільнена швидкість для останніх Х кадрів
            screen_start.Pictures_Y.FROG_Y -= 0.3

    screen.blit(screen_start.main_pictures.Frog, (0, screen_start.Pictures_Y.FROG_Y))


    # Рух криси, головний екран
    if screen_start.Pictures_Y.RAT_Y >= 0:
        if screen_start.Pictures_Y.RAT_Y >= 30:
            # Звичайна швидкість для Х кадрів
            screen_start.Pictures_Y.RAT_Y -= 1
        else:
            # Сповільнена швидкість для останніх Х кадрів
            screen_start.Pictures_Y.RAT_Y -= 0.3

    screen.blit(screen_start.main_pictures.Rat, (0, screen_start.Pictures_Y.RAT_Y))


    # Рух гравця, головний екран
    if screen_start.Pictures_Y.RAT_Y >= 0:
        if screen_start.Pictures_Y.RAT_Y >= 50:
            # Звичайна швидкість для Х кадрів
            screen_start.Pictures_Y.RAT_Y -= 3
        else:
            # Сповільнена швидкість для останніх Х кадрів
            screen_start.Pictures_Y.RAT_Y -= 0.3

    screen.blit(screen_start.main_pictures.Player1, (0, screen_start.Pictures_Y.RAT_Y))


def bg_animation(background):
    # задній фон рух
    background.Background.BG_SKY_X -= background.Background.BG_SKY_SPEED
    if background.Background.BG_SKY_X == -background.Background.BG_WIDTH_END:
        background.Background.BG_SKY_X = background.Background.BG_WIDTH_START

    background.Background.BG_MOUNTAIN_BACK_X -= background.Background.BG_MOUNTAIN_BACK_SPEED
    if background.Background.BG_MOUNTAIN_BACK_X == -background.Background.BG_WIDTH_END:
        background.Background.BG_MOUNTAIN_BACK_X = background.Background.BG_WIDTH_START

    background.Background.BG_MOUNTAIN_FRONT_X -= background.Background.BG_MOUNTAIN_FRONT_SPEED
    if background.Background.BG_MOUNTAIN_FRONT_X == -background.Background.BG_WIDTH_END:
        background.Background.BG_MOUNTAIN_FRONT_X = background.Background.BG_WIDTH_START

    background.Background.BG_GRASS_X -= background.Background.BG_GRASS_SPEED
    if background.Background.BG_GRASS_X == -background.Background.BG_WIDTH_END:
        background.Background.BG_GRASS_X = background.Background.BG_WIDTH_START
