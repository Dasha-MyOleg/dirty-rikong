#background.py

import pygame
pygame.init()

class ScConfig:
    SIZE        = (1280, 720)
    START_SIZE  = (0, 0)
    HIDDEN_SIZE = (-200, 1360)



screen = pygame.display.set_mode(ScConfig.SIZE)



#картинки заднього фону
class Background:
    BG_WIDTH_START = 0
    BG_WIDTH_END = 2500

    BG_SKY = pygame.image.load('images/bg/bg_sky.png').convert_alpha()
    BG_SKY_X = 0
    BG_MOUNTAIN_BACK = pygame.image.load('images/bg/bg_mountain_back.png').convert_alpha()
    BG_MOUNTAIN_BACK_X = 0
    BG_MOUNTAIN_FRONT = pygame.image.load('images/bg/bg_mountain_front.png').convert_alpha()
    BG_MOUNTAIN_FRONT_X = 0
    BG_GRASS = pygame.image.load('images/bg/bg_grass.png').convert_alpha()
    BG_GRASS_X = 0

    BG_SKY_SPEED = 2
    BG_MOUNTAIN_BACK_SPEED = 4
    BG_MOUNTAIN_FRONT_SPEED = 10
    BG_GRASS_SPEED = 20



def bg_animation():

    width = Background.BG_WIDTH_START

    screen.blit(Background.BG_SKY, (Background.BG_SKY_X, width))
    screen.blit(Background.BG_SKY, (Background.BG_SKY_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_BACK, (Background.BG_MOUNTAIN_BACK_X, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_BACK,  (Background.BG_MOUNTAIN_BACK_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_FRONT, (Background.BG_MOUNTAIN_FRONT_X, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_FRONT,(Background.BG_MOUNTAIN_FRONT_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))
    screen.blit(Background.BG_GRASS, (Background.BG_GRASS_X, Background.BG_WIDTH_START))
    screen.blit(Background.BG_GRASS, (Background.BG_GRASS_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))