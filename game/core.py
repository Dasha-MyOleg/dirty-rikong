
from config import ScConfig
config_instance = ScConfig()
def bg_animation():
    """
    Background animation.
    Used as a base background screen throughout the game.
    Contains grass, mountains and sky.
    """
    screen.blit(bg_sky, (bg_sky_x, bg_width_start))
    screen.blit(bg_sky, (bg_sky_x + bg_width_end, bg_width_start))
    screen.blit(bg_mountain_back, (bg_mountain_back_x, bg_width_start))
    screen.blit(bg_mountain_back, (bg_mountain_back_x + bg_width_end, bg_width_start))
    screen.blit(bg_mountain_front, (bg_mountain_front_x, bg_width_start))
    screen.blit(bg_mountain_front, (bg_mountain_front_x + bg_width_end, bg_width_start))
    screen.blit(bg_grass, (bg_grass_x, bg_width_start))
    screen.blit(bg_grass, (bg_grass_x + bg_width_end, bg_width_start))


running = True
while running:

    #рух фону
    bg_animation()

    if gameplay:
        player_hitbox = walk_left[0].get_rect(topleft=(player_x, player_y))

        #пацюк - в яких випадках зникає або закінчує гру
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
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(stay[player_anim_count], (player_x, player_y))

        if keys[pygame.K_d]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > player_x_min:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < player_x_max:
            player_x += player_speed



        #прижок

        if not is_jump:
            #if button["jump"]:
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

        #анімація гравця
        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1


        #задній фон - рух
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



        #бластери/постріли
        if blasts:
            for el in blasts:
                screen.blit(blast,(el.x,el.y))
                el.x += blast_speed

                if el.x > config_instance.HIDDEN_SIZE[0]:
                    blasts.pop(i)
                    blasters_left += 1

                #якщо постріл попаде в пацюка
                if rat_list_in_game:
                    for (idex, rat_el) in enumerate(rat_list_in_game):
                        if el.colliderect(rat_el):
                            rat_list_in_game.pop(idex)
                            blasts.pop(idex)
                            blasters_left += 1

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


        #де з'являються пацюки
        if event.type == rat_timer:
            rat_list_in_game.append(rat.get_rect(topleft=(rat_width_hitbox, rat_heigh_hitbox)))

        #обмеження кікості бластерів/пострілів і де вони з'являються
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and blasters_left > 0:
            blasts.append(blast.get_rect(topleft=(player_x + 100, player_y + 127)))
            blasters_left -= 1