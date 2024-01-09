from .config import *


from config import ScConfig
from . import config


from config import gameplay, is_jump, jump_count_start, jump_count, blasters_left, blast, blasts, blast_speed



def bg_animation():
    """
    Background animation.
    Used as a base background screen throughout the game.
    Contains grass, mountains and sky.
    """
    screen.blit(config.Background.BG_SKY, (config.Background.BG_SKY_X, config.Background.BG_WIDTH_START))
    screen.blit(config.Background.BG_SKY, (config.Background.BG_SKY_X + config.Background.BG_WIDTH_END, config.Background.BG_WIDTH_START))
    screen.blit(config.Background.BG_MOUNTAIN_BACK, (config.Background.BG_MOUNTAIN_BACK_X, config.Background.BG_WIDTH_START))
    screen.blit(config.Background.BG_MOUNTAIN_BACK, (config.Background.BG_MOUNTAIN_BACK_X + config.Background.BG_WIDTH_END, config.Background.BG_WIDTH_START))
    screen.blit(config.Background.BG_MOUNTAIN_FRONT, (config.Background.BG_MOUNTAIN_FRONT_X, config.Background.BG_WIDTH_START))
    screen.blit(config.Background.BG_MOUNTAIN_FRONT, (config.Background.BG_MOUNTAIN_FRONT_X + config.Background.BG_WIDTH_END, config.Background.BG_WIDTH_START))
    screen.blit(config.Background.BG_GRASS, (config.Background.BG_GRASS_X, config.Background.BG_WIDTH_START))
    screen.blit(config.Background.BG_GRASS, (config.Background.BG_GRASS_X + config.Background.BG_WIDTH_END, config.Background.BG_WIDTH_START))


running = True
while running:

    #рух фону
    bg_animation()

    if gameplay:
        player_hitbox = walk_left[0].get_rect(topleft=(config.Player.X, config.Player.Y))

        #пацюк в яких випадках зникає або закінчує гру
        # Rat logic and conditions:
        # If rat is in the game - remove it,
        # otherwise put 3 on top.
        # We expect player to be ready for this.
        if rat_list_in_game:
            for (i, el) in enumerate (rat_list_in_game):
                screen.blit(rat, el)
                el.x -= rat_speed

                if el.x < config.ScConfig.HIDDEN_SIZE[0]:
                    rat_list_in_game.pop(i)

                if player_hitbox.colliderect(el):
                    gameplay = False

        #кнопки
        keys = pygame.key.get_pressed()

        #button: dict[str, Any] = {"jump", keys[pygame.K_SPACE],
        #                          "go_left", keys[pygame.K_a],
        #                          "go_right", keys[pygame.K_d]}

        if keys[pygame.K_a]:
            screen.blit(walk_left[config.Player.ANIMATION_COUNT], (config.Player.X, config.Player.Y))
        else:
            screen.blit(stay[config.Player.ANIMATION_COUNT], (config.Player.X, config.Player.Y))

        if keys[pygame.K_d]:
            screen.blit(walk_right[config.Player.ANIMATION_COUNT], (config.Player.X, config.Player.Y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and config.Player.X > config.Player.X_MIN:
            config.Player.X -= player_speed
        elif keys[pygame.K_d] and config.Player.X < config.Player.X_MAX:
            config.Player.X += player_speed



            # прижок
        if not is_jump:
            #if button["jump"]:
            if keys[pygame.K_SPACE]:
                is_jump = True

        else:
            if jump_count >= -jump_count_start:
                if jump_count > 0:
                    config.Player.Y -= (jump_count ** 2) / 3
                else:
                    config.Player.X += (jump_count ** 2) / 3
                jump_count -= 1
            else:
                is_jump = False
                jump_count = jump_high = jump_count_start


#анімація гравця
        if config.Player.ANIMATION_COUNT == 3:
            config.Player.ANIMATION_COUNT = 0
        else:
            config.Player.ANIMATION_COUNT += 1


# задній фон рух
        config.Background.BG_SKY_X -= config.Background.BG_SKY_SPEED
        if config.Background.BG_SKY_X == -config.Background.BG_WIDTH_END:
            config.Background.BG_SKY_X = config.Background.BG_WIDTH_START

        config.Background.BG_MOUNTAIN_BACK_X -= config.Background.BG_MOUNTAIN_BACK_SPEED
        if config.Background.BG_MOUNTAIN_BACK_X == -config.Background.BG_WIDTH_END:
            config.Background.BG_MOUNTAIN_BACK_X = config.Background.BG_WIDTH_START

        config.Background.BG_MOUNTAIN_FRONT_X -= config.Background.BG_MOUNTAIN_FRONT_SPEED
        if config.Background.BG_MOUNTAIN_FRONT_X == -config.Background.BG_WIDTH_END:
            config.Background.BG_MOUNTAIN_FRONT_X = config.Background.BG_WIDTH_START

        config.Background.BG_GRASS_X -= config.Background.BG_GRASS_SPEED
        if config.Background.BG_GRASS_X == -config.Background.BG_WIDTH_END:
            config.Background.BG_GRASS_X = config.Background.BG_WIDTH_START



        #бластери/постріли
        blasts_to_remove = []

        if blasts:
            for i, el in enumerate(blasts):
                screen.blit(blast, (el.x, el.y))
                el.x += blast_speed

                if el.x > config.ScConfig.HIDDEN_SIZE[1]:
                    blasts_to_remove.append(i)
                    blasters_left += 1

        # Удаление элементов после завершения итерации
        for i in blasts_to_remove:
            blasts.pop(i)




        #screen.blit(square, (230, 380))

        #фпс гри
        clock.tick(game_speed)


    #екран програшу
    else:

        screen.blit(restart_screen, ScConfig.START_SIZE)
        screen.blit(lose_label,lose_label_location)
        screen.blit(restart_label,restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            config.Player.X = 10
            rat_list_in_game.clear()
            blasts.clear()
            blasters_left = 5


    pygame.display.update()

    # вимнення гри (хрестик)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        #де з'являються пацюки
        if event.type == rat_timer:
            rat_list_in_game.append(rat.get_rect(topleft=(rat_width_hitbox, rat_heigh_hitbox)))

        #обмеження кікості бластерів/пострілів і де вони з'являються
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and blasters_left > 0:
            blasts.append(blast.get_rect(topleft=(config.Player.X + 100, config.Player.Y + 127)))
            blasters_left -= 1