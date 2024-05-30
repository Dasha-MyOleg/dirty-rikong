
import pygame
from .config import *
from . import config
from . import background
from . import enemies


def run_game():
    running = True
    gameplay = True
    attacking_animation_playing = False

    while running:

        #рух фону
        background.bg_animation()

        if gameplay:


            #анімації на кнопках
            keys = pygame.key.get_pressed()



            if keys[pygame.K_s]:
                player_hitbox = walk_crawls_on_ground[0].get_rect(topleft=(config.Player.X, config.Player.Y + 170))
            else:
                player_hitbox = walk_left[0].get_rect(topleft=(config.Player.X, config.Player.Y))


            if keys[pygame.K_f] and config.blasters.BLASTERS_LEFT > 0:
                # Запустіть анімацію атаки, якщо вона ще не програвається
                if not attacking_animation_playing:
                    attacking_animation_playing = True
                    attacking_animation_frame = 0

            # Логіка для анімації атаки
            if attacking_animation_playing:
                # Відобразіть поточний кадр анімації атаки
                screen.blit(
                    walk_attacking[min(attacking_animation_frame, config.ANIMATION_COUNT.ANIMATION_COUNT_ATTACKING)],
                    (config.Player.X, config.Player.Y))
                attacking_animation_frame += 1
                # Перевірте, чи пройшов кінець анімації атаки
                if attacking_animation_frame >= config.ANIMATION_COUNT.ANIMATION_COUNT_ATTACKING:
                    attacking_animation_playing = False  # Зупиніть анімацію атаки
                    attacking_animation_frame = 0  # Скинути кадр анімації атаки

            # Логіка для інших дій гравця
            else:
                if keys[pygame.K_a] and not keys[pygame.K_SPACE] and not keys[pygame.K_f] and not keys[pygame.K_s] and Player.Y >= 300:
                    screen.blit(walk_left[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_LEFT)],
                                (config.Player.X, config.Player.Y))
                elif keys[pygame.K_d] and not keys[pygame.K_SPACE] and not keys[pygame.K_f] and not keys[pygame.K_s] and Player.Y >= 300:
                    screen.blit(walk_right[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_RIGHT)],
                                (config.Player.X, config.Player.Y))
                elif keys[pygame.K_s] and Player.Y >= 300 or keys[pygame.K_s] and keys[pygame.K_d] or keys[pygame.K_s] and keys[pygame.K_a]:
                    screen.blit(walk_crawls_on_ground[
                                    min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.PLAYER_CRAWLS_ON_GROUND_WALK)],
                                (config.Player.X, config.Player.Y + 170))
                else:
                    if Player.Y >= 400:
                        screen.blit(walk_stay[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_STAY)],
                                    (config.Player.X, config.Player.Y))
                    else:
                        screen.blit(walk_jump[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_JUMP)],
                                    (config.Player.X, config.Player.Y))



            # якщо гравець виконує будь-яку дію окрім атаки.
            if not keys[pygame.K_f] and not attacking_animation_playing:
                attacking_animation_playing = False



            if keys[pygame.K_a] and config.Player.X > config.Player.X_MIN:
                config.Player.X -= player_speed
            elif keys[pygame.K_d] and config.Player.X < config.Player.X_MAX:
                config.Player.X += player_speed



            # Check if the player is on the ground to reset jump count
            if config.Player.Y >= 420:
                config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                config.jump.IS_JUMP = False


            # Перевірка, чи може гравець стрибнути
            if keys[pygame.K_SPACE] and not config.jump.IS_JUMP:
                config.jump.IS_JUMP = True
                config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                jump_press_time = 0
                config.Player.start_Y = config.Player.Y

            if keys[pygame.K_s]:
                IS_JUMP = False

            jump_press_time = 0
            max_jump_time = 4
            base_jump_strength = 1.8


            #при натисканні на 'S'  персонаж опускається на землю
            if keys[pygame.K_s]:
                config.Player.Y = 420
                config.jump.IS_JUMP = False
                config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                jump_press_time = 0  # Скидаємо час натискання

            if config.jump.IS_JUMP:
                if config.jump.JUMP_COUNT >= -config.jump.JUMP_COUNT_START:
                    if keys[pygame.K_SPACE] and config.jump.JUMP_COUNT > 0:
                        jump_press_time += 1
                        if jump_press_time > max_jump_time:
                            jump_press_time = max_jump_time

                        # вплив тривалісті натискання на прижок
                        jump_strength = base_jump_strength + (jump_press_time / max_jump_time) * (
                                    base_jump_strength - 1)
                        config.Player.Y -= (config.jump.JUMP_COUNT ** 2) / (6 / jump_strength)
                        config.jump.JUMP_COUNT -= 1

                    else:
                        # Якщо клавішу відпущено або JUMP_COUNT <= 0, персонаж починає падати
                        if config.jump.JUMP_COUNT > 0:
                            config.Player.Y += (config.jump.JUMP_COUNT ** 2) / (6 / jump_strength)
                        else:
                            config.Player.Y += (config.jump.JUMP_COUNT ** 2) / (6 / jump_strength)
                        config.jump.JUMP_COUNT -= 1

                        # Завершення стрибка, коли персонаж приземлився
                        if config.jump.JUMP_COUNT < -config.jump.JUMP_COUNT_START:
                            config.jump.IS_JUMP = False
                            config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                            config.Player.Y = 420
                            jump_press_time = 0

                else:
                    # Завершення стрибка
                    config.jump.IS_JUMP = False
                    config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                    jump_press_time = 0



              # Оновлення лічильника анімації
            if config.Player.ANIMATION_COUNT >= max(ANIMATION_COUNT.ANIMATION_COUNT_LEFT,
                                                ANIMATION_COUNT.ANIMATION_COUNT_RIGHT,
                                                ANIMATION_COUNT.ANIMATION_COUNT_JUMP,
                                                ANIMATION_COUNT.ANIMATION_COUNT_STAY,
                                                ANIMATION_COUNT.PLAYER_CRAWLS_ON_GROUND_WALK):
                config.Player.ANIMATION_COUNT = 0
            else:
                config.Player.ANIMATION_COUNT += 1


            # задній фон рух
            background.Background.BG_SKY_X -= background.Background.BG_SKY_SPEED
            if background.Background.BG_SKY_X == -background.Background.BG_WIDTH_END:
                background.Background.BG_SKY_X = background.Background.BG_WIDTH_START

            background.Background.BG_MOUNTAIN_BACK_X -= background.Background.BG_MOUNTAIN_BACK_SPEED
            if background.Background.BG_MOUNTAIN_BACK_X == -background.Background.BG_WIDTH_END:
                background.Background.BG_MOUNTAIN_BACK_X = background.Background.BG_WIDTH_START

            background.Background.BG_MOUNTAIN_FRONT_X -= background.Background.BG_MOUNTAIN_FRONT_SPEED
            if background.Background.BG_MOUNTAIN_FRONT_X == -background.Background.BG_WIDTH_END:
                background.Background.BG_MOUNTAIN_FRONT_X = background.Background.BG_WIDTH_START

            background.Background.BG_GRASS_X -= background.Background.BG_GRASS_SPEED
            if background.Background.BG_GRASS_X == -background.Background.BG_WIDTH_END:
                background.Background.BG_GRASS_X = background.Background.BG_WIDTH_START



            # пацюк в яких випадках зникає або закінчує гру
            if enemies.rat.RAT_LIST_IN_GAME:
                for (i, el) in enumerate(enemies.rat.RAT_LIST_IN_GAME):
                    screen.blit(enemies.rat.RAT, el)
                    el.x -= enemies.rat.RAT_SPEED

                    if el.x < config.ScConfig.HIDDEN_SIZE[0]:
                        enemies.rat.RAT_LIST_IN_GAME.pop(i)

                    if player_hitbox.colliderect(el):
                        gameplay = False




            # озеро в яких випадках зникає або закінчує гру
            if enemies.lake.LAKE_LIST_IN_GAME:
                for (i, el) in enumerate(enemies.lake.LAKE_LIST_IN_GAME):
                    screen.blit(enemies.lake.LAKE, el)
                    el.x -= enemies.lake.LAKE_SPEED

                    if el.x < config.ScConfig.HIDDEN_SIZE[0]:
                        enemies.lake.LAKE_LIST_IN_GAME.pop(i)

                    if player_hitbox.colliderect(el):
                        gameplay = False




            #бластери/постріли

            blasts_copy = config.blasters.BLASTS.copy()

            for el in blasts_copy:
                screen.blit(config.blasters.BLAST, (el.x, el.y))
                el.x += config.blasters.BLAST_SPEED


                if el.x > config.ScConfig.HIDDEN_SIZE[1]:
                # Видаляємо елемент з оригінального списку
                   config.blasters.BLASTS.remove(el)
                   config.blasters.BLASTERS_LEFT += 1

                if enemies.rat.RAT_LIST_IN_GAME:
                    for (idex, rat_el) in enumerate(enemies.rat.RAT_LIST_IN_GAME):
                       if el.colliderect(rat_el):
                           enemies.rat.RAT_LIST_IN_GAME.pop(idex)
                           config.blasters.BLASTS.remove(el)
                           config.blasters.BLASTERS_LEFT += 1





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
                config.blasters.BLASTERS_LEFT = 3
                config.Player.X = 10
                enemies.rat.RAT_LIST_IN_GAME.clear()
                enemies.lake.LAKE_LIST_IN_GAME.clear()
                config.blasters.BLASTS.clear()



        pygame.display.update()

        # вимнення гри (хрестик)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


            #де з'являються пацюки
            if event.type == enemies.rat.RAT_TIMER:
                enemies.rat.RAT_LIST_IN_GAME.append(enemies.rat.RAT.get_rect(topleft=(enemies.rat.RAT_WIDTH_SPAWN, enemies.rat.RAT_HEIGHT_SPAWN)))

            # де з'являютється озера
            if event.type == enemies.lake.LAKE_TIMER:
                enemies.lake.LAKE_LIST_IN_GAME.append(
                    enemies.lake.LAKE.get_rect(topleft=(enemies.lake.LAKE_WIDTH_SPAWN, enemies.lake.LAKE_HEIGHT_SPAWN)))



            #обмеження кікості бластерів/пострілів і де вони з'являються
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and config.blasters.BLASTERS_LEFT > 0:
                config.blasters.BLASTS.append(config.blasters.BLAST.get_rect(topleft=(config.Player.X + 100, config.Player.Y + 127)))
                config.blasters.BLASTERS_LEFT -= 1