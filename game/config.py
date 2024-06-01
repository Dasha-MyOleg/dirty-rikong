import enum

import pygame
pygame.init()

import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

clock = pygame.time.Clock()


# Швидкість анімацій
GAME_SPEED = 16


def load_image(path, alpha=True):
    """Load pygame icon."""
    if alpha:
        return pygame.image.load(path).convert_alpha()
    else:
        return pygame.image.load(path)



class GameState(enum.Enum):
    # Стан гри
    START     = 0
    PLAYING   = 1
    GAME_OVER = 2


class ScConfig:
    # розмір екрану
    SIZE        = (1280, 720)
    # початковий координати
    START_SIZE  = (0, 0)
    # координати знищення
    HIDDEN_SIZE = (-400, 1360)


class PgDisplay:
    # назва гри
    CAPTION = "Dirty Rikong Game"


screen = pygame.display.set_mode(ScConfig.SIZE)
pygame.display.set_caption(PgDisplay.CAPTION)

# іконка гри
icon = load_image('images/icon.png')
pygame.display.set_icon(icon)


class Player:
    # налаштування гравця
    ANIMATION_COUNT = 0
    SPEED = 4
    X = 10
    Y = 420
    PLAYER_OM_THE_GROUND = 420
    X_MIN = 0
    X_MAX = 1100


class Images:
    # base folder
    BASE_DIR = 'images/'
    # background folder
    BG_DIR = BASE_DIR + 'bg/'

    # game
    PYGAME_ICON = BASE_DIR + 'icon.png'

    # player folder
    PLAYER_STAY_DIR = BASE_DIR + 'player_stay/'
    PLAYER_JUMP_DIR = BASE_DIR + 'player_jump/'
    PLAYER_L_DIR = BASE_DIR + 'player_left/'
    PLAYER_R_DIR = BASE_DIR + 'player_right/'
    PLAYER_ATTACKING_DIR = BASE_DIR + 'player_attacking/'
    PLAYER_CRAWLS_ON_GROUND_DIR = BASE_DIR + 'player_povze/'

    PLAYER_BASE      = PLAYER_R_DIR + 'right_1.png'

    PLAYER_STAY = [
        'stay_1.png',
        'stay_2.png',
        'stay_3.png',
        'stay_4.png',
        'stay_5.png',
        'stay_6.png',
    ]

    PLAYER_JUMP = [
        'jump_1.png',
        'jump_2.png',
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

    PLAYER_ATTACKING = [
        'PlayerAttacking_1.png',
        'PlayerAttacking_2.png',
        'PlayerAttacking_3.png',
        'PlayerAttacking_4.png',
        'PlayerAttacking_5.png',
        'PlayerAttacking_6.png',
        'PlayerAttacking_7.png',
    ]

    PLAYER_CRAWLS_ON_GROUND = [
        'Povze_1.png',
        'Povze_2.png',
        'Povze_3.png',
        'Povze_4.png',
        'Povze_5.png',
        'Povze_6.png',
    ]

# перелік картинок руху
PLAYER_STAY_WALK = [Images.PLAYER_STAY_DIR + x for x in Images.PLAYER_STAY]
PLAYER_JUMP_WALK = [Images.PLAYER_JUMP_DIR + x for x in Images.PLAYER_JUMP]
PLAYER_L_WALK = [Images.PLAYER_L_DIR + x for x in Images.PLAYER_L]
PLAYER_R_WALK = [Images.PLAYER_R_DIR + x for x in Images.PLAYER_R]
PLAYER_ATTACKING_WALK = [Images.PLAYER_ATTACKING_DIR + x for x in Images.PLAYER_ATTACKING]
PLAYER_CRAWLS_ON_GROUND_WALK = [Images.PLAYER_CRAWLS_ON_GROUND_DIR + x for x in Images.PLAYER_CRAWLS_ON_GROUND]


#гравець
player = load_image(Images.PLAYER_BASE, alpha=False)

#Швидкість гравця по Х
player_speed = 23


#пересування гравця
walk_stay = [load_image(x) for x in PLAYER_STAY_WALK]
walk_jump = [load_image(x) for x in PLAYER_JUMP_WALK]
walk_left = [load_image(x) for x in PLAYER_L_WALK]
walk_right = [load_image(x) for x in PLAYER_R_WALK]
walk_attacking = [load_image(x) for x in PLAYER_ATTACKING_WALK]
walk_crawls_on_ground = [load_image(x) for x in PLAYER_CRAWLS_ON_GROUND_WALK]


class jump:
    # Прижки
    IS_JUMP = False
    JUMP_COUNT_START = 15
    JUMP_COUNT = JUMP_COUNT_START
    jump_press_time = 0
    max_jump_time = 4
    base_jump_strength = 1.8

class player_hit_box:
    # хітбокс гравця
    walking_hit_box = walk_left[0]
    walk_crawls_on_ground_hit_box = walk_crawls_on_ground[0]

#музика
bg_sound = pygame.mixer.Sound('sounds/soundtrack.mp3')
bg_sound.play()


#бластер
class blasters:
    BLASTERS_LEFT = 3
    BLAST = pygame.image.load('images/blast.png').convert_alpha()
    BLASTS = []
    BLAST_SPEED = 27
    BLAST_WIDTH_HITBOX = Player.X + 100
    BLAST_HEIGHT_HITBOX= Player.Y + 127



class ANIMATION_COUNT:
    # обща кількість картинок (- 1 кадр)
    ANIMATION_COUNT_JUMP = 1
    ANIMATION_COUNT_LEFT = 3
    ANIMATION_COUNT_RIGHT = 3
    ANIMATION_COUNT_STAY = 5
    ANIMATION_COUNT_ATTACKING = 7
    PLAYER_CRAWLS_ON_GROUND_WALK = 5



#текст програшу налаштування і місцезнаходження
label_text_size = 200
label          = pygame.font.Font('FontsText/VT323-Regular.ttf',label_text_size)
lose_label     = label.render('You lose!',False,"Black")
restart_label  = label.render('restart',False,"Black")
restart_screen = pygame.image.load('images/lose_screen.png')

lose_label_location = (30,40)
restart_label_location = (30,200)
restart_label_rect = restart_label.get_rect(topleft=(restart_label_location))


