
from .config import *
from . import config


def run_game():
    running = True
    gameplay = True

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
            if config.rat.RAT_LIST_IN_GAME:
                for (i, el) in enumerate(config.rat.RAT_LIST_IN_GAME):
                    screen.blit(config.rat.RAT, el)
                    el.x -= config.rat.RAT_SPEED

                    if el.x < config.ScConfig.HIDDEN_SIZE[0]:
                        config.rat.RAT_LIST_IN_GAME.pop(i)

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
                screen.blit(walk_right [config.Player.ANIMATION_COUNT], (config.Player.X, config.Player.Y))

            if keys[pygame.K_d]:
                screen.blit(walk_right[config.Player.ANIMATION_COUNT], (config.Player.X, config.Player.Y))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and config.Player.X > config.Player.X_MIN:
                config.Player.X -= player_speed
            elif keys[pygame.K_d] and config.Player.X < config.Player.X_MAX:
                config.Player.X += player_speed



                # прижок
            if not config.jump.IS_JUMP:
                if keys[pygame.K_SPACE]:
                    config.jump.IS_JUMP = True

            else:
                if config.jump.JUMP_COUNT >= -config.jump.JUMP_COUNT_START:
                    if config.jump.JUMP_COUNT > 0:
                        config.Player.Y -= (config.jump.JUMP_COUNT ** 2) / 3
                    else:
                        config.Player.Y += (config.jump.JUMP_COUNT ** 2) / 3
                    config.jump.JUMP_COUNT -= 1
                else:
                    config.jump.IS_JUMP = False
                    config.jump.JUMP_COUNT = jump_high = config.jump.JUMP_COUNT_START



                #else:
                 #   config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                  #  config.jump.IS_JUMP = False



    #анімація гравця
            if Player.ANIMATION_COUNT == 3:
                Player.ANIMATION_COUNT = 0
            else:
                Player.ANIMATION_COUNT += 1


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


            if config.blasters.BLASTS:
                for el in config.blasters.BLASTS:
                    screen.blit(config.blasters.BLAST, (el.x, el.y))
                    el.x += config.blasters.BLAST_SPEED

                    if el.x > config.ScConfig.HIDDEN_SIZE[1]:
                        config.blasters.BLASTS.pop()
                        config.blasters.BLASTERS_LEFT += 1


                    if config.rat.RAT_LIST_IN_GAME:
                        for (idex, rat_el) in enumerate(config.rat.RAT_LIST_IN_GAME):
                            if el.colliderect(rat_el):
                                config.rat.RAT_LIST_IN_GAME.pop(idex)
                                config.blasters.BLASTS.pop(idex)
                                config.blasters.BLASTERS_LEFT += 1


            #screen.blit(square, (230, 380))

            #фпс гри
            clock.tick(GAME_SPEED)


        #екран програшу
        else:

            screen.blit(restart_screen, ScConfig.START_SIZE)
            screen.blit(lose_label,lose_label_location)
            screen.blit(restart_label,restart_label_rect)

            mouse = pygame.mouse.get_pos()

            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                config.Player.X = 10
                config.rat.RAT_LIST_IN_GAME.clear()
                config.blasters.BLASTS.clear()



        pygame.display.update()

        # вимнення гри (хрестик)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


            #де з'являються пацюки
            if event.type == config.rat.RAT_TIMER:
                config.rat.RAT_LIST_IN_GAME.append(config.rat.RAT.get_rect(topleft=(config.rat.RAT_WIDTH_HITBOX, config.rat.RAT_HEIGHT_HITBOX)))

            #обмеження кікості бластерів/пострілів і де вони з'являються
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and config.blasters.BLASTERS_LEFT > 0:
                config.blasters.BLASTS.append(config.blasters.BLAST.get_rect(topleft=(config.Player.X + 100, config.Player.Y + 127)))
                config.blasters.BLASTERS_LEFT -= 1