
import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
#screen = pygame.display.set_mode((600, 300). flags=pygame.NOFRAME) - без рамки
pygame.display.set_caption("Dirty Rikong Game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)


#square = pygame.Surface((75,55))
#square.fill('Blue')


#myfont = pygame.font.Font('FontsText/SpaceMono-Regular.ttf',40)
#text_surfase = myfont.render('Rikong love you',False,'Red','Blue')

bg = pygame.image.load('images/bg.png').convert()
player = pygame.image.load('images/player_right/right_1.png')

rat = pygame.image.load('images/rat.png').convert_alpha()
#rat_x = 1290
rat_list_in_game =[]

player_anim_count = 0
bg_x=0

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

player_speed = 10
player_x = 10
player_y = 380

is_jump = False
jump_count = 15

bg_sound = pygame.mixer.Sound('sounds/soundtrack.mp3')
bg_sound.play()

rat_timer = pygame.USEREVENT + 1
pygame.time.set_timer(rat_timer,10000)

blasters_left = 5
blast = pygame.image.load('images/blast.png').convert_alpha()
blasts = []

gameplay = True
label = pygame.font.Font('FontsText/SpaceMono-Regular.ttf',70)
label_2 = pygame.font.Font('FontsText/Foldit-VariableFont_wght.ttf', 60)
lose_label = label.render('You lose!',False,(0,0,0))
restart_label = label.render('Restart?',False,(0,0,0))
restart_label_rect = restart_label.get_rect(topleft=(420, 300))
blast_label = label_2.render('Blasts left:',True,(230, 240, 255))

running = True
while running:

    #персонаж
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x+1280, 0))
    #screen.blit(rat, (rat_x, 450))

    if gameplay:

        player_hitbox = walk_left[0].get_rect(topleft=(player_x, player_y))
        if rat_list_in_game:
            for (i, el) in enumerate (rat_list_in_game):
                screen.blit(rat, el)
                el.x -= 16

                if el.x < -200:
                    rat_list_in_game.pop()

                if player_hitbox.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # left
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 0:  # left
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < 400:  # right
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True

        else:
            if jump_count >= -15:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 3
                else:
                    player_y += (jump_count ** 2) / 3
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 15

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 5
        if bg_x == -1280:
            bg_x = 0

        #screen.blit(blast_label, "blasters_left", (400, 100))



        #if keys[pygame.K_f]:
        #    blasts.append(blast.get_rect(topleft=(player_x+100,player_y+110)))

        if blasts:
            for el in blasts:
                screen.blit(blast,(el.x,el.y))
                el.x += 7

                if el.x > 1360:
                    blasts.pop(i)
                    blasters_left += 1


                if rat_list_in_game:
                    for (index, rat_el) in enumerate(rat_list_in_game):
                        if el.colliderect(rat_el):
                            rat_list_in_game.pop(index)
                            blasts.pop(i)
                            blasters_left += 1

        # rat_x -= 17

        #screen.blit(square, (230, 380))

        clock.tick(9)
    else:
        screen.fill((87,88,89))
        screen.blit(lose_label,(400,100))
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
           rat_list_in_game.append(rat.get_rect(topleft=(1270,450)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and blasters_left > 0:
            blasts.append(blast.get_rect(topleft=(player_x+100,player_y+110)))
            blasters_left -= 1



