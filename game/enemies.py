import pygame
pygame.init()

#пацюк
class rat:
    RAT_WIDTH_SPAWN = 1265
    RAT_HEIGHT_SPAWN = 350
    RAT_TIMER = pygame.USEREVENT + 1
    RAT = pygame.image.load('images/enemies/rat/rat.png').convert_alpha()
    RAT_LIST_IN_GAME = []
    RAT_SPEED = 25
    RAT_PER_MILLISECOND = 5000
    pygame.time.set_timer(RAT_TIMER, RAT_PER_MILLISECOND)

class lake:
    LAKE_WIDTH_SPAWN = 1450
    LAKE_HEIGHT_SPAWN = 610
    LAKE_TIMER = pygame.USEREVENT + 1
    LAKE = pygame.image.load('images/enemies/lake/lake.png').convert_alpha()
    LAKE_LIST_IN_GAME = []
    LAKE_SPEED = 20
    LAKE_PER_MILLISECOND = 5000
    pygame.time.set_timer(LAKE_TIMER, LAKE_PER_MILLISECOND)