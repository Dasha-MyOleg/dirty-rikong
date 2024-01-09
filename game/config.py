
#from typing import Dict, Any

import pygame
pygame.init()


clock = pygame.time.Clock()
game_speed = 9


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

    # game
    PYGAME_ICON = BASE_DIR + 'icon.png'

    # player folder
    PLAYER_STAY_DIR = BASE_DIR + 'player_stay/'
    PLAYER_L_DIR = BASE_DIR + 'player_left/'
    PLAYER_R_DIR = BASE_DIR + 'player_right/'

    PLAYER_BASE      = PLAYER_R_DIR + 'right_1.png'

    PLAYER_STAY = [
        'stay_1.png',]

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

    # full paths
    PLAYER_STAY = [PLAYER_STAY_DIR + x for x in PLAYER_STAY]
    PLAYER_L_WALK = [PLAYER_L_DIR + x for x in PLAYER_L]
    PLAYER_R_WALK = [PLAYER_R_DIR + x for x in PLAYER_R]

    # background folder
    BG_DIR = BASE_DIR + 'bg/'


#гравець
player = load_image(Images.PLAYER_BASE, alpha=False)
player_speed = 15


#пересування гравця
stay  = [load_image(x) for x in Images.PLAYER_STAY]
#walk_left  = [load_image(x) for x in Images.PLAYER_L_WALK]
walk_right = [load_image(x) for x in Images.PLAYER_R_WALK]


walk_left = []
for x in Images.PLAYER_L_WALK:
    img = load_image(x)
    walk_left.append(img)



is_jump = False
jump_count_start = 15
jump_count = jump_count_start


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


#музика
bg_sound = pygame.mixer.Sound('sounds/soundtrack.mp3')
bg_sound.play()

#пацюк
rat_width_hitbox = 1265
rat_heigh_hitbox = 450
rat_timer = pygame.USEREVENT + 1
rat = pygame.image.load('images/rat.png').convert_alpha()
rat_list_in_game =[]
rat_speed = 20
rat_per_millisecond = 5000
pygame.time.set_timer(rat_timer,rat_per_millisecond)


#бластер
blasters_left = 3
blast = pygame.image.load('images/blast.png').convert_alpha()
blasts = []
blast_speed = 11
blast_width_hitbox = Player.X + 100
blast_heigh_hitbox = Player.Y + 127


gameplay = True

#текст - налаштування і місцезнаходження
label_text_size = 200
label = pygame.font.Font('FontsText/VT323-Regular.ttf',label_text_size)
lose_label = label.render('You lose!',False,"Black")
restart_label = label.render('restart',False,"Black")
restart_screen = pygame.image.load('images/lose_screen.png')

lose_label_location = (30,40)
restart_label_location = (30,200)
restart_label_rect = restart_label.get_rect(topleft=(restart_label_location))