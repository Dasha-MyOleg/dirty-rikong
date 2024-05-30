import pygame
pygame.init()

#пацюк
class rat:
    RAT_WIDTH_SPAWN = 1265
    RAT_HEIGHT_SPAWN = 350
    RAT_TIMER = pygame.USEREVENT + 1
    RAT = pygame.image.load('images/rat.png').convert_alpha()
    RAT_LIST_IN_GAME = []
    RAT_SPEED = 20
    RAT_PER_MILLISECOND = 5000
    pygame.time.set_timer(RAT_TIMER, RAT_PER_MILLISECOND)