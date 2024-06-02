import pygame
import sys
from .config import *
from . import config
from . import background
from . import enemies
from . import screen_start
from . import functions
import random

# Стан гри
START = 0
PLAYING = 1
GAME_OVER = 2


# Ініціалізація Pygame
pygame.init()

# Глобальна змінна стану гри
game_state = START

#enemies.rat.set_random_timer(self)
#enemies.lake.set_random_timer(self)
#config.logger.info(1111)
#config.logger.info(f'game_state {game_state}')


def run_game():
    global game_state

    gameplay = False
    running = True
    attacking_animation_playing = False
    attacking_animation_frame = 0

    rat_instance = enemies.rat()
    lake_instance = enemies.lake()
    frog_instance = enemies.frog()

    frog_jump_up = True

    #івекнти гри
    while running:
        functions.listen_game_mode(screen_start.restart_button_rect, game_state)


        # Логіка гри
        # Головний екран
        if game_state == START:
            screen.blit(screen_start.main_pictures.main_bg, ScConfig.START_SIZE)
            functions.main_menu_movement(screen, screen_start)

            # Виклик функції з вказанням аргументу
            # Main menu buttons
            screen_start.draw_main_menu_buttons(screen)

            for event in pygame.event.get():
                event_game_state = screen_start.listen_main_menu_buttons(event)
                if event_game_state:
                    game_state = event_game_state

        # Екран гри
        elif game_state == PLAYING:
            # Рух фону
            background.bg_animation()


            gameplay = True

            # анімації на кнопках
            keys = pygame.key.get_pressed()

            # Хітбокс для повзання
            if keys[pygame.K_s]:
                player_hitbox = walk_crawls_on_ground[0].get_rect(topleft=(config.Player.X, config.Player.Y + 170))
            else:
                player_hitbox = walk_left[0].get_rect(topleft=(config.Player.X, config.Player.Y))



            # Запуск анамації атаки
            if keys[pygame.K_f] and config.blasters.BLASTERS_LEFT > 0:
                if not attacking_animation_playing:
                    attacking_animation_playing = True



            # Логіка для анімації атаки
            if attacking_animation_playing and attacking_animation_frame < 7:
                # Відображення поточного кадру анімації атаки
                screen.blit(
                    walk_attacking[
                        min(
                        attacking_animation_frame,
                        config.ANIMATION_COUNT.ANIMATION_COUNT_ATTACKING
                        )
                    ],
                    (config.Player.X, config.Player.Y))
                attacking_animation_frame += 1
                # Перевірка, чи пройшов кінець анімації атаки
                if attacking_animation_frame >= config.ANIMATION_COUNT.ANIMATION_COUNT_ATTACKING:
                    attacking_animation_playing = False
                    attacking_animation_frame = 0



            # Логіка для інших дій гравця
            else:
                #рух гравця вліво
                if keys[pygame.K_a] and not keys[pygame.K_SPACE] and not keys[pygame.K_f] and not keys[pygame.K_s] and Player.Y >= 300:
                    screen.blit(walk_left[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_LEFT)],
                                (config.Player.X, config.Player.Y))
                #рух гравця вправо
                elif keys[pygame.K_d] and not keys[pygame.K_SPACE] and not keys[pygame.K_f] and not keys[pygame.K_s] and Player.Y >= 300:
                    screen.blit(walk_right[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_RIGHT)],
                                (config.Player.X, config.Player.Y))
                #рух гравця повзе
                elif keys[pygame.K_s] and Player.Y >= 300 or keys[pygame.K_s] and keys[pygame.K_d] or keys[pygame.K_s] and keys[pygame.K_a]:
                    screen.blit(walk_crawls_on_ground[
                                    min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.PLAYER_CRAWLS_ON_GROUND_WALK)],
                                (config.Player.X, config.Player.Y + 170))
                #рух гравця ходьба
                else:
                    if Player.Y >= 400:
                        screen.blit(walk_stay[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_STAY)],
                                    (config.Player.X, config.Player.Y))
                #рух гравця стрибок
                    else:
                        screen.blit(walk_jump[min(config.Player.ANIMATION_COUNT, ANIMATION_COUNT.ANIMATION_COUNT_JUMP)],
                                    (config.Player.X, config.Player.Y))



            #рух гравця вліво і вправо
            if keys[pygame.K_a] and config.Player.X > config.Player.X_MIN:
                config.Player.X -= player_speed
            elif keys[pygame.K_d] and config.Player.X < config.Player.X_MAX:
                config.Player.X += player_speed

            # Перевірка, чи може гравець стрибнути
            if config.Player.Y >= config.Player.PLAYER_OM_THE_GROUND:
                config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                config.jump.IS_JUMP = False

            # Умови для IS_JUMP = True
            if keys[pygame.K_SPACE] and not config.jump.IS_JUMP:
                config.jump.IS_JUMP = True
                config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                config.jump.jump_press_time = 0
                config.Player.start_Y = config.Player.Y

            if keys[pygame.K_s]:
                IS_JUMP = False




            # При натисканні на "S" телепортація на землю
            if keys[pygame.K_s]:
                config.Player.Y = config.Player.PLAYER_OM_THE_GROUND
                config.jump.IS_JUMP = False
                config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                config.jump.jump_press_time = 0


            # ініціація прижка
            if config.jump.IS_JUMP:
                if config.jump.JUMP_COUNT >= -config.jump.JUMP_COUNT_START:
                    if keys[pygame.K_SPACE] and config.jump.JUMP_COUNT > 0:
                        config.jump.jump_press_time += 1
                        if config.jump.jump_press_time > config.jump.max_jump_time:
                            config.jump.jump_press_time = config.jump.max_jump_time

                        # вплив тривалісті натискання на прижок
                        jump_strength = config.jump.base_jump_strength + (config.jump.jump_press_time / config.jump.max_jump_time) * (
                                    config.jump.base_jump_strength - 1)
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
                            config.Player.Y = config.Player.PLAYER_OM_THE_GROUND
                            config.jump.jump_press_time = 0

                else:
                    # Завершення стрибка
                    config.jump.IS_JUMP = False
                    config.jump.JUMP_COUNT = config.jump.JUMP_COUNT_START
                    config.jump.jump_press_time = 0



            # Оновлення лічильника анімації
            if config.Player.ANIMATION_COUNT >= max(ANIMATION_COUNT.ANIMATION_COUNT_LEFT,
                                                ANIMATION_COUNT.ANIMATION_COUNT_RIGHT,
                                                ANIMATION_COUNT.ANIMATION_COUNT_JUMP,
                                                ANIMATION_COUNT.ANIMATION_COUNT_STAY,
                                                ANIMATION_COUNT.PLAYER_CRAWLS_ON_GROUND_WALK):
                config.Player.ANIMATION_COUNT = 0
            else:
                config.Player.ANIMATION_COUNT += 1

            functions.bg_animation(background)

            #додавання ворогів
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                #додавання крис
                if event.type == rat_instance.RAT_TIMER:
                    enemies.rat.add_rat()

                #додавання озера
                if event.type == lake_instance.LAKE_TIMER:
                    enemies.lake.LAKE_LIST_IN_GAME.append(
                        lake_instance.LAKE.get_rect(
                            topleft=(lake_instance.LAKE_WIDTH_SPAWN, lake_instance.LAKE_HEIGHT_SPAWN)))
                    lake_instance.set_random_timer()

                #додавання жаби
                if event.type == frog_instance.FROG_TIMER:
                    enemies.frog.add_frog()

                for frog_instance in enemies.frog.FROG_LIST_IN_GAME:
                    frog_instance.jump()

            #Якщо криска додана у гру
            if enemies.rat.RAT_LIST_IN_GAME:
                for (i, el) in enumerate(enemies.rat.RAT_LIST_IN_GAME):
                    screen.blit(enemies.rat.RAT, el)
                    el.x -= enemies.rat.RAT_SPEED

                    # Видалення крис поза межею екрана
                    if el.x < config.ScConfig.HIDDEN_SIZE[0]:
                        enemies.rat.RAT_LIST_IN_GAME.pop(i)

                    # Програш гри при доторканні гравця до хітбоксу
                    if player_hitbox.colliderect(el):
                        game_state = GAME_OVER

            #якщо жабка додана у гру
            if enemies.frog.FROG_LIST_IN_GAME:
                for frog_instance in enemies.frog.FROG_LIST_IN_GAME:
                    frog_instance.jump()  # Виклик методу прижка
                    frog_instance.draw(screen)  # Виклик методу малювання

                for (i, el) in enumerate(enemies.frog.FROG_LIST_IN_GAME):
                    #screen.blit(enemies.frog.FROG, el.frog_rect)
                    el.frog_rect.x -= enemies.frog.FROG_SPEED

                    #чи це прижок вверх
                    if el.frog_rect.y <= 100:
                        el.jump_up = False
                    elif el.frog_rect.y >= 600:
                        el.jump_up = True

                    #як відбувається прижок
                    if el.jump_up:
                        el.frog_rect.y -= 10  # jump up
                    else:
                        el.frog_rect.y += 10  # fall down

                    #Знищення при виходженні за рамки
                    if el.frog_rect.x < config.ScConfig.HIDDEN_SIZE[0]:
                        enemies.frog.FROG_LIST_IN_GAME.pop(i)

                    #кінець гри при дотику до жабки
                    if player_hitbox.colliderect(el.frog_rect):
                        game_state = GAME_OVER

            # Якщо озеро було додано до гемплею
            if enemies.lake.LAKE_LIST_IN_GAME:
                for (i, el) in enumerate(enemies.lake.LAKE_LIST_IN_GAME):
                    screen.blit(enemies.lake.LAKE, el)
                    el.x -= enemies.lake.LAKE_SPEED

                    # Видалення озер поза межею екрана
                    if el.x < config.ScConfig.HIDDEN_SIZE[0]:
                        enemies.lake.LAKE_LIST_IN_GAME.pop(i)

                    # Програш гри при доторканні гравця до хітбоксу
                    if player_hitbox.colliderect(el):
                        game_state = GAME_OVER


            # фпс гри
            clock.tick(GAME_SPEED)





        # екран програшу
        elif game_state == GAME_OVER:
            screen.blit(restart_screen, ScConfig.START_SIZE)
            screen.blit(lose_label, lose_label_location)
            screen.blit(restart_label, restart_label_rect)


            mouse = pygame.mouse.get_pos()
            #if restart button clik
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                #reset lists
                game_state = START
                config.blasters.BLASTERS_LEFT = 3
                config.Player.X = 10
                enemies.rat.RAT_LIST_IN_GAME.clear()
                enemies.lake.LAKE_LIST_IN_GAME.clear()
                enemies.frog.FROG_LIST_IN_GAME.clear()
                config.blasters.BLASTS.clear()
                gameplay = False

        pygame.display.update()

        # вимкнення гри (хрестик)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # обмеження кількості бластерів/пострілів і де вони з'являються
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and config.blasters.BLASTERS_LEFT > 0:
                config.blasters.BLASTS.append(
                    config.blasters.BLAST.get_rect(topleft=(config.Player.X + 100, config.Player.Y + 127)))
                config.blasters.BLASTERS_LEFT -= 1


        #pygame.display.flip()
        clock.tick(60)

