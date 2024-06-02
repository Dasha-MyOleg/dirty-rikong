import pygame
import random

pygame.init()

# пацюк
class rat:
    # все для налаштування крис
    RAT_WIDTH_SPAWN = 1265
    RAT_HEIGHT_SPAWN = 350
    RAT_TIMER = pygame.USEREVENT + 1
    RAT = pygame.image.load('images/enemies/rat/rat.png').convert_alpha()
    RAT_LIST_IN_GAME = []
    RAT_SPEED = 25

    def __init__(self):
        self.RAT_PER_MILLISECOND = random.randint(50, 100)
        pygame.time.set_timer(self.RAT_TIMER, self.RAT_PER_MILLISECOND)

    @staticmethod
    def add_rat():
        rat_height_spawn = random.randint(200, 420)
        rat.RAT_LIST_IN_GAME.append(rat.RAT.get_rect(topleft=(rat.RAT_WIDTH_SPAWN, rat_height_spawn)))

# озеро
class lake:
    # все для налаштування озер
    LAKE_WIDTH_SPAWN = 1450
    LAKE_HEIGHT_SPAWN = 610
    LAKE_TIMER = pygame.USEREVENT + 2
    LAKE = pygame.image.load('images/enemies/lake/lake.png').convert_alpha()
    LAKE_LIST_IN_GAME = []
    LAKE_SPEED = 20

    def __init__(self):
        self.set_random_timer()

    def set_random_timer(self):
        self.LAKE_PER_MILLISECOND = random.randint(110, 500)
        pygame.time.set_timer(self.LAKE_TIMER, self.LAKE_PER_MILLISECOND)

# жаба
class frog:
    #все для налаштування жаб
    FROG_WIDTH_SPAWN = 1265
    FROG_HEIGHT_SPAWN = 350  # Фіксована висота появи
    FROG_TIMER = pygame.USEREVENT + 3
    FROG = pygame.image.load('images/enemies/frog/frog_1.png').convert_alpha()
    FROG_LIST_IN_GAME = []
    FROG_SPEED = 20
    FROG_JUMP_FRAMES = [pygame.image.load(f'images/enemies/frog/frog_{i}.png').convert_alpha() for i in range(1, 6)]

    def __init__(self):
        #рандомна поява жаб
        self.frog_rect = frog.FROG.get_rect(topleft=(frog.FROG_WIDTH_SPAWN, frog.FROG_HEIGHT_SPAWN))
        self.FROG_PER_MILLISECOND = random.randint(30, 400)
        pygame.time.set_timer(self.FROG_TIMER, self.FROG_PER_MILLISECOND)
        self.jump_up = True  # Початковий стан прижка жаби
        # Останній кадр анімації
        self.animation_index = 0
        self.animation_timer = pygame.time.get_ticks()

    @staticmethod
    #додавання жаб
    def add_frog():
        frog_instance = frog()
        frog.FROG_LIST_IN_GAME.append(frog_instance)

    def animate_jump(self):
        # Визначення кадру анімації в залежності від положення жабки
        if self.frog_rect.y <= 400:
            self.animation_index = 0  # frog_1
        elif self.frog_rect.y <= 500:
            if self.jump_up:
                self.animation_index = 1  # frog_2 (жабка летить вверх)
            else:
                self.animation_index = 3  # frog_4 (жабка летить вниз)
        elif self.frog_rect.y < 600:
            if self.jump_up:
                self.animation_index = 2  # frog_3 (жабка летить вверх)
            else:
                self.animation_index = 4  # frog_5 (жабка летить вниз)

    def draw(self, screen):
        self.animate_jump()
        screen.blit(frog.FROG_JUMP_FRAMES[self.animation_index], self.frog_rect)

    def jump(self):
        #механіка прижка
        if self.frog_rect.y <= 100:
            self.jump_up = False
            self.animation_index = 3
        elif self.frog_rect.y >= 600:
            self.jump_up = True

        if self.jump_up:
            self.frog_rect.y -= 10  # підйом
            self.animation_index = 2
        else:
            self.frog_rect.y += 10  # падіння
            self.animation_index = 4

