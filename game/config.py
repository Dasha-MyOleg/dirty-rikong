
#from typing import Dict, Any

import pygame
pygame.init()


clock = pygame.time.Clock()
GAME_SPEED = 9


def load_image(path, alpha=True):
    """Load pygame icon."""
    if alpha:
        return pygame.image.load(path).convert_alpha()
    else:
        return pygame.image.load(path)


class ScConfig:
    SIZE        = (1280, 720)
    START_SIZE  = (0, 0)
    HIDDEN_SIZE = (-200, 1360)


class PgDisplay:
    CAPTION = "Dirty Rikong Game"


screen = pygame.display.set_mode(ScConfig.SIZE)
pygame.display.set_caption(PgDisplay.CAPTION)

icon = load_image('images/icon.png')
pygame.display.set_icon(icon)


class Player:
    ANIMATION_COUNT = 0
    SPEED = 15
    X = 10
    Y = 420
    X_MIN = 0
    X_MAX = 600


class Images:
    # base folder
    BASE_DIR = 'images/'
    # background folder
    BG_DIR = BASE_DIR + 'bg/'

    # game
    PYGAME_ICON = BASE_DIR + 'icon.png'

    # player folder
    PLAYER_STAY_DIR = BASE_DIR + 'player_stay/'
    PLAYER_L_DIR = BASE_DIR + 'player_left/'
    PLAYER_R_DIR = BASE_DIR + 'player_right/'

    PLAYER_BASE      = PLAYER_R_DIR + 'right_1.png'

    PLAYER_STAY = [
        'stay_1.png',
    ]

    PLAYER_L = [
        'left_1.png',
        'left_2.png',
        'left_3.png',
        'left_4.png',
    ]

    PLAYER_R = [
        'right_1.png',
        'right_2.png',
        'right_3.png',
        'right_4.png',
    ]


PLAYER_STAY = [Images.PLAYER_STAY_DIR + x for x in Images.PLAYER_STAY]
PLAYER_L_WALK = [Images.PLAYER_L_DIR + x for x in Images.PLAYER_L]
PLAYER_R_WALK = [Images.PLAYER_R_DIR + x for x in Images.PLAYER_R]


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


#гравець
player = load_image(Images.PLAYER_BASE, alpha=False)
player_speed = 15


#пересування гравця
stay  = [load_image(x) for x in PLAYER_STAY]
#walk_left  = [load_image(x) for x in PLAYER_L_WALK]
walk_right = [load_image(x) for x in PLAYER_R_WALK]


walk_left = []
for x in PLAYER_L_WALK:
    img = load_image(x)
    walk_left.append(img)


class jump:
    IS_JUMP = False
    JUMP_COUNT_START = 15
    JUMP_COUNT = JUMP_COUNT_START



#картинки заднього фону



#музика
bg_sound = pygame.mixer.Sound('sounds/soundtrack.mp3')
bg_sound.play()

#пацюк
class rat:
    RAT_WIDTH_HITBOX = 1265
    RAT_HEIGHT_HITBOX = 450
    RAT_TIMER = pygame.USEREVENT + 1
    RAT = pygame.image.load('images/rat.png').convert_alpha()
    RAT_LIST_IN_GAME = []
    RAT_SPEED = 20
    RAT_PER_MILLISECOND = 5000
    pygame.time.set_timer(RAT_TIMER, RAT_PER_MILLISECOND)



#бластер
class blasters:
    BLASTERS_LEFT = 3
    BLAST = pygame.image.load('images/blast.png').convert_alpha()
    BLASTS = []
    BLAST_SPEED = 11
    BLAST_WIDTH_HITBOX = Player.X + 100
    BLAST_HEIGHT_HITBOX= Player.Y + 127




#текст - налаштування і місцезнаходження
label_text_size = 200
label          = pygame.font.Font('FontsText/VT323-Regular.ttf',label_text_size)
lose_label     = label.render('You lose!',False,"Black")
restart_label  = label.render('restart',False,"Black")
restart_screen = pygame.image.load('images/lose_screen.png')

lose_label_location = (30,40)
restart_label_location = (30,200)
restart_label_rect = restart_label.get_rect(topleft=(restart_label_location))

def bg_animation():
    """
    Background animation.
    Used as a base background screen throughout the game.
    Contains grass, mountains and sky.
    """
    width = Background.BG_WIDTH_START

    screen.blit(Background.BG_SKY, (Background.BG_SKY_X, width))
    screen.blit(Background.BG_SKY, (Background.BG_SKY_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_BACK, (Background.BG_MOUNTAIN_BACK_X, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_BACK, (Background.BG_MOUNTAIN_BACK_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_FRONT, (Background.BG_MOUNTAIN_FRONT_X, Background.BG_WIDTH_START))
    screen.blit(Background.BG_MOUNTAIN_FRONT, (Background.BG_MOUNTAIN_FRONT_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))
    screen.blit(Background.BG_GRASS, (Background.BG_GRASS_X, Background.BG_WIDTH_START))
    screen.blit(Background.BG_GRASS, (Background.BG_GRASS_X + Background.BG_WIDTH_END, Background.BG_WIDTH_START))

