
import pygame
import time
import random
import pandas as pd
# from neural_network import *
# from wall import *
import numpy as np

def robot_hum(display):
    # features_train, target_train = create_train()
    features_train=[]
    target_train=[]
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    dis_width = 1000
    dis_height = 750
    dis = display
    # dis = pygame.display.set_mode((dis_width, dis_height))
    # pygame.display.set_caption('Robot with NN')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 5

    font_style = pygame.font.SysFont(None, 30)

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 2, dis_height / 2])

    def gameLoop():  # creating a function
        batary = 1000
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2 + 5

        x1_change = 0
        y1_change = 0
        wallx = round(random.randrange(0, dis_width - snake_block*40) / 10.0) * 10.0
        wally = round(random.randrange(300, dis_width - snake_block - 300) / 10.0) * 10.0
        print(wallx, wallx + snake_block*40)
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(300, dis_height - snake_block) / 10.0) * 10.0
        while foodx == wallx:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        while foody == wally:
            foody = round(random.randrange(300, dis_height - snake_block) / 10.0) * 10.0
        print(foodx)
        print(foody)
        # food2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        # food2y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0


        while not game_over:
            print(batary)

            while game_close == True:
                dis.fill(white)
                message("You Lost! Press Q-Quit or C-Play Again", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True # Для выхода
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
            if y1_change == 0 and x1_change == 0:
                target_train.append(1)
            elif y1_change == 0 and x1_change == -snake_block:
                target_train.append(1)
            elif y1_change == 0 and x1_change == snake_block:
                target_train.append(2)
            elif x1_change == 0 and y1_change == -snake_block:
                target_train.append(3)
            elif x1_change == 0 and y1_change == snake_block:
                target_train.append(4)

            # Создаем признаки для обучения
            features = []
            # Feature 1
            if foodx > x1:
                features.append(1)
            elif foodx == x1:
                features.append(0.5)
            else:
                features.append(0)
            # Feature 2
            if foody > y1:
                features.append(1)
            elif foody == y1:
                features.append(0.5)
            else:
                features.append(0)
            # Feature 3
            if (foody > wally > y1 or foody < wally < y1) and (wallx + snake_block * 40 > x1 > wallx):
                features.append(1)
            else:
                features.append(0)
            # if foodx - x1 == 0:
            # features.append(abs(foodx - x1))
            # # Feature 4
            # features.append(abs(foody - y1))
            #
            features_train.append(features)

            # Заканчиваем подбирать признаки и возвращаемся к игре
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            if batary == 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(white)

            camera_surf = pygame.image.load(f'VID_20230525_095425_out000{batary // 150}.jpg')
            camera_scale = pygame.transform.scale(
                camera_surf, (camera_surf.get_width() // 4,
                        camera_surf.get_height() // 3))
            camera_rect = camera_scale.get_rect(
                bottomright=(320, 240))
            dis.blit(camera_scale, camera_rect)

            pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
            # pygame.draw.rect(dis, blue, [food2x, food2y, snake_block, snake_block])
            pygame.draw.rect(dis, black, [wallx, wally, snake_block * 40, snake_block])

            pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(300, dis_height - snake_block) / 10.0) * 10.0
                while foodx == wallx:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                while foody == wally:
                    foody = round(random.randrange(300, dis_height - snake_block) / 10.0) * 10.0
            # if x1 == food2x and y1 == food2y:
            #     food2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            #     food2y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            batary -= 10
            clock.tick(snake_speed)
        # print(len(features_train), 'features_train:',features_train)
        # print(len(target_train), 'target_train:', target_train)
        df = pd.DataFrame(features_train, columns=['f1', 'f2', 'f3'])
        df["target"] = target_train
        # print(df)
        df.to_excel("output.xlsx")
        pygame.quit()
        quit()
    gameLoop()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     robot_hum()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
