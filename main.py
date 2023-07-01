
import pygame

clock = pygame.time.Clock()
game_speed = 9

pygame.init()

screen_width_start = 0
screen_heigh_start = 0
screen_width = 1280
screen_heigh = 720
screen_width_not_seen_end = -200
screen = pygame.display.set_mode((screen_width, screen_heigh))
#screen = pygame.display.set_mode((screen_width, screen_heigh). flags=pygame.NOFRAME) - без рамки

pygame.display.set_caption("Dirty Rikong Game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)


#square = pygame.Surface((75,55))
#square.fill('Blue')

#myfont = pygame.font.Font('FontsText/SpaceMono-Regular.ttf',40)
#text_surfase = myfont.render('Rikong love you',False,'Red','Blue')


player = pygame.image.load('images/player_right/right_1.png')
player_anim_count = 0
player_speed = 15
player_x = 10
player_y = 420
player_x_min = 0
player_x_max = 600

walk_left = [
    pygame.image.load('images/player_left/left_1.png').convert_alpha(),
    pygame.image.load('images/player_left/left_2.png').convert_alpha(),
    pygame.image.load('images/player_left/left_3.png').convert_alpha(),
    pygame.image.load('images/player_left/left_4.png').convert_alpha(),
]

walk_right = [
    pygame.image.load('images/player_right/right_1.png').convert_alpha(),
    pygame.image.load('images/player_right/right_2.png').convert_alpha(),
    pygame.image.load('images/player_right/right_3.png').convert_alpha(),
    pygame.image.load('images/player_right/right_4.png').convert_alpha(),
]

is_jump = False
jump_count_start = 15
jump_count = jump_count_start



bg_width_start = 0
bg_width_end = 2500

bg_sky = pygame.image.load('images/bg/bg_sky.png').convert_alpha()
bg_sky_x=0
bg_mountain_back = pygame.image.load('images/bg/bg_mountain_back.png').convert_alpha()
bg_mountain_back_x=0
bg_mountain_front = pygame.image.load('images/bg/bg_mountain_front.png').convert_alpha()
bg_mountain_front_x=0
bg_grass = pygame.image.load('images/bg/bg_grass.png').convert_alpha()
bg_grass_x=0

bg_sky_speed = 2
bg_mountain_back_speed = 4
bg_mountain_front_speed = 10
bg_grass_speed = 20


bg_sound = pygame.mixer.Sound('sounds/soundtrack.mp3')
bg_sound.play()

rat_width_hitbox = 1265
rat_heigh_hitbox = 450
rat_timer = pygame.USEREVENT + 1
rat_per_millisecond = 10000
pygame.time.set_timer(rat_timer,rat_per_millisecond)
rat = pygame.image.load('images/rat.png').convert_alpha()
#rat x and y = 1290,450
rat_list_in_game =[]
rat_speed = 20


blasters_left = 5
blast = pygame.image.load('images/blast.png').convert_alpha()
blasts = []
blast_speed = 11
blast_width_hitbox = player_x + 100
blast_heigh_hitbox = player_y + 127


gameplay = True

label_text_size = 200
label = pygame.font.Font('FontsText/VT323-Regular.ttf',label_text_size)
lose_label = label.render('You lose!',False,"Black")
restart_label = label.render('Restart',False,"Black")
restart_screen = pygame.image.load('images/lose_screen.png')

lose_label_location = (30,40)
restart_label_location = (30,200)
restart_label_rect = restart_label.get_rect(topleft=(restart_label_location))




running = True
while running:

    #рух фону
    screen.blit(bg_sky, (bg_sky_x, bg_width_start))
    screen.blit(bg_sky, (bg_sky_x + bg_width_end, bg_width_start))
    screen.blit(bg_mountain_back, (bg_mountain_back_x, bg_width_start))
    screen.blit(bg_mountain_back, (bg_mountain_back_x + bg_width_end, bg_width_start))
    screen.blit(bg_mountain_front, (bg_mountain_front_x, bg_width_start))
    screen.blit(bg_mountain_front, (bg_mountain_front_x + bg_width_end, bg_width_start))
    screen.blit(bg_grass, (bg_grass_x, bg_width_start))
    screen.blit(bg_grass, (bg_grass_x + bg_width_end, bg_width_start))

    if gameplay:

        player_hitbox = walk_left[0].get_rect(topleft=(player_x, player_y))
        if rat_list_in_game:
            for (i, rat_hitbox) in enumerate (rat_list_in_game):
                screen.blit(rat, rat_hitbox)
                rat_hitbox.x -= rat_speed

                if rat_hitbox.x < screen_width_not_seen_end:
                    rat_list_in_game.pop()

                if player_hitbox.colliderect(rat_hitbox):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # left
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > player_x_min:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < player_x_max:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True

        else:
            if jump_count >= -jump_count_start:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 3
                else:
                    player_y += (jump_count ** 2) / 3
                jump_count -= 1
            else:
                is_jump = False
                jump_count = jump_high = jump_count_start

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_sky_x -= bg_sky_speed
        if bg_sky_x == -bg_width_end:
           bg_sky_x = bg_width_start

        bg_mountain_back_x -= bg_mountain_back_speed
        if bg_mountain_back_x == -bg_width_end:
           bg_mountain_back_x = bg_width_start

        bg_mountain_front_x -= bg_mountain_front_speed
        if bg_mountain_front_x == -bg_width_end:
            bg_mountain_front_x = bg_width_start

        bg_grass_x -= bg_grass_speed
        if bg_grass_x == -bg_width_end:
           bg_grass_x = bg_width_start


        #screen.blit(blast_label, "blasters_left", (400, 100))



        #if keys[pygame.K_f]:
        #    blasts.append(blast.get_rect(topleft=(player_x+100,player_y+110)))

        if blasts:
            for blast_hitbox in blasts:
                screen.blit(blast,(blast_hitbox.x,blast_hitbox.y))
                blast_hitbox.x += blast_speed

                if blast_hitbox.x > screen_width_not_seen_end:
                    blasts.pop(i)
                    blasters_left += 1


                if rat_list_in_game:
                    for (index, rat_rat_hitbox) in enumerate(rat_list_in_game):
                        if blast_hitbox.colliderect(rat_rat_hitbox):
                            rat_list_in_game.pop(index)
                            blasts.pop(i)
                            blasters_left += 1

        # rat_x -= 17

        #screen.blit(square, (230, 380))

        clock.tick(game_speed)

    else:

        screen.blit(restart_screen, (screen_width_start,screen_heigh_start))
        screen.blit(lose_label,lose_label_location)
        screen.blit(restart_label,restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 10
            rat_list_in_game.clear()
            blasts.clear()
            blasters_left = 5


    pygame.display.update()

    # вимнення гри (хрестик)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == rat_timer:
           rat_list_in_game.append(rat.get_rect(topleft=(rat_width_hitbox,screen_heigh)))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and blasters_left > 0:
            blasts.append(blast.get_rect(topleft=(blast_width_hitbox, blast_heigh_hitbox)))
            blasters_left -= 1