
from .config import *
from . import config


def run_game():
    running = True
    gameplay = True
    attacking_animation_playing = False

    while running:

        #рух фону
        bg_animation()

        if gameplay:
            player_hitbox = walk_left[0].get_rect(topleft=(config.Player.X, config.Player.Y))


            #пацюк в яких випадках зникає або закінчує гру

            if config.rat.RAT_LIST_IN_GAME:
                for (i, el) in enumerate(config.rat.RAT_LIST_IN_GAME):
                    screen.blit(config.rat.RAT, el)
                    el.x -= config.rat.RAT_SPEED

                    if el.x < config.ScConfig.HIDDEN_SIZE[0]:
                        config.rat.RAT_LIST_IN_GAME.pop(i)

                    if player_hitbox.colliderect(el):
                        gameplay = False

            #анімації на кнопках
            keys = pygame.key.get_pressed()



            if keys[pygame.K_a] and not keys[pygame.K_SPACE] and not keys[pygame.K_f] and Player.Y >= 300 and not attacking_animation_playing:
                screen.blit(walk_left[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_LEFT)],
                            (config.Player.X, config.Player.Y))
            elif keys[pygame.K_d] and not keys[pygame.K_SPACE] and not keys[pygame.K_f] and Player.Y >= 300 and not attacking_animation_playing:
                screen.blit(walk_right[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_RIGHT)],
                            (config.Player.X, config.Player.Y))
            elif keys[pygame.K_SPACE] or Player.Y >= 520 and not attacking_animation_playing:
                screen.blit(walk_jump[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_JUMP)],
                            (config.Player.X, config.Player.Y))
            elif keys[pygame.K_f] and config.blasters.BLASTERS_LEFT > 0:
                 # Запустіть анімацію атаки, якщо вона ще не програвається
                    if not attacking_animation_playing:
                        attacking_animation_playing = True
                        attacking_animation_frame = 0
            else:
                if Player.Y >= 301 and not attacking_animation_playing:
                    screen.blit(walk_stay[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_STAY)],
                            (config.Player.X, config.Player.Y))
                else:
                    if not attacking_animation_playing:
                        screen.blit(walk_jump[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_JUMP)],
                                 (config.Player.X, config.Player.Y))



                # Якщо анімація атаки програється, відображайте кадр анімації
                if attacking_animation_playing:
                    # Перевірте, чи пройшов кінець анімації атаки
                    if attacking_animation_frame >= config.ANIMATION_COUNT.ANIMATION_COUNT_ATTACKING:
                        attacking_animation_playing = False  # Зупиніть анімацію атаки
                        attacking_animation_frame = 0  # Скинути кадр анімації атаки
                    else:
                        # Відобразіть поточний кадр анімації атаки
                        screen.blit(
                            walk_attacking[min(attacking_animation_frame, config.ANIMATION_COUNT.ANIMATION_COUNT_ATTACKING)],
                            (config.Player.X, config.Player.Y))
                        attacking_animation_frame += 1



                # Check if the player is on the ground to reset jump count
            if config.Player.Y >= 420:
                config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                config.jump.IS_JUMP = False


            if keys[pygame.K_a] and config.Player.X > config.Player.X_MIN:
                config.Player.X -= player_speed
            elif keys[pygame.K_d] and config.Player.X < config.Player.X_MAX:
                config.Player.X += player_speed


            # Перевірка, чи може гравець стрибнути
            if not config.jump.IS_JUMP and keys[pygame.K_SPACE]:
                config.jump.IS_JUMP = True


            # Логіка прижку
            if config.jump.IS_JUMP:
                if config.jump.JUMP_COUNT >= -config.jump.JUMP_COUNT_START:
                    if config.jump.JUMP_COUNT > 0:
                        config.Player.Y -= (config.jump.JUMP_COUNT ** 2) / 3
                        # Перевірка, чи досягнуто максимальної висоти
                        if config.jump.JUMP_COUNT == 1:
                            # Встановлення анімації прижку до максимальної висоти
                            config.Player.ANIMATION_COUNT = ANIMATION_COUNT.ANIMATION_COUNT_JUMP
                    else:
                        config.Player.Y += (config.jump.JUMP_COUNT ** 2) / 3
                    config.jump.JUMP_COUNT -= 1
                else:
                    config.jump.IS_JUMP = False
                    config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START





    #перебирання кадрів гравця


            # Оновлення лічильника анімації
            if config.Player.ANIMATION_COUNT >= max(ANIMATION_COUNT.ANIMATION_COUNT_LEFT,
                                                    ANIMATION_COUNT.ANIMATION_COUNT_RIGHT,
                                                    ANIMATION_COUNT.ANIMATION_COUNT_JUMP,
                                                    ANIMATION_COUNT.ANIMATION_COUNT_STAY):
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

            blasts_copy = config.blasters.BLASTS.copy()

            for el in blasts_copy:
                screen.blit(config.blasters.BLAST, (el.x, el.y))
                el.x += config.blasters.BLAST_SPEED

                if el.x > config.ScConfig.HIDDEN_SIZE[1]:
                    # Видаляємо елемент з оригінального списку
                    config.blasters.BLASTS.remove(el)
                    config.blasters.BLASTERS_LEFT += 1

                if config.rat.RAT_LIST_IN_GAME:
                    for (idex, rat_el) in enumerate(config.rat.RAT_LIST_IN_GAME):
                        if el.colliderect(rat_el):
                            config.rat.RAT_LIST_IN_GAME.pop(idex)
                            config.blasters.BLASTS.remove(el)
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