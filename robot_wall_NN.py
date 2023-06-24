import math

import pygame
import random
from neural_network import *
from keras.models import load_model
import numpy as np
from sklearn import preprocessing

# def main():
def robot_wall(display):
    model = load_model('model3.h5')
    features_train, target_train = create_train()

    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    YELLOW = (225, 225, 0)

    # dis_width = 800
    # dis_height = 600
    dis_width = 1000
    dis_height = 750
    dis = display

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Робот-пылесос')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 2

    font_style = pygame.font.SysFont(None, 30)

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 2, dis_height / 2])

    def gameLoop():  # creating a function
        batary =  63
        game_over = False
        game_close = False
        test = False
        # x1 = dis_width / 2
        # y1 = dis_height / 2 + 5
        x1 = 700
        y1 = 500
        x1_change = 0
        y1_change = 0

        # foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        # foody = round(random.randrange(300, dis_height - snake_block) / 10.0) * 10.0

        foodx = 390
        foody = 500
        print(foodx)
        print(foody)
        # food2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        # food2y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

        # wallx = round(random.randrange(0, dis_width - snake_block*40) / 10.0) * 10.0
        # wally = round(random.randrange(300, dis_width - snake_block - 300) / 10.0) * 10.0

        wallx = 400
        wally = 600

        radius = 350
        while not game_over:
            print(batary)
            while game_close == True:
                dis.fill(white)
                message("Работа окончена(Q для выхода), C(Заново)", red)
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
            if (foody > wally > y1 or foody < wally < y1) and (wallx + snake_block * 40 >= x1 >= wallx):
                features.append(1)
            else:
                features.append(0)
            # # Feature 3
            # features.append(abs(foodx - x1))
            # # Feature 4
            # features.append(abs(foody - y1))

            features_train.append(features)

            # features = pd.DataFrame(features)
            # print(features)
            # scaler = preprocessing.StandardScaler()
            # features = np.array(features)
            # features = scaler.fit_transform(features)
            # features = np.array([[x[0] for x in features]])
            print(features)
            sqx = (x1 + snake_block / 2 - foodx) ** 2
            sqy = (y1 + snake_block / 2 - foody) ** 2
            if math.sqrt(sqx + sqy) < radius:
                predict_x = model.predict([features])

                classes_x = np.argmax(predict_x, axis=1)
                print(classes_x)
                if classes_x[0] == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif classes_x[0] == 1:
                    x1_change = snake_block
                    y1_change = 0
                elif classes_x[0] == 2:
                    y1_change = -snake_block
                    x1_change = 0
                elif classes_x[0] == 3:
                    y1_change = snake_block
                    x1_change = 0
            else:
                direction_class = random.randrange(1, 5)
                if direction_class == 1:
                    x1_change = -snake_block
                    y1_change = 0
                elif direction_class == 2:
                    x1_change = snake_block
                    y1_change = 0
                elif direction_class == 3:
                    y1_change = -snake_block
                    x1_change = 0
                elif direction_class == 4:
                    y1_change = snake_block
                    x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            if x1 >= wallx and x1 <= wallx + snake_block * 40 and wally == y1:
                game_close = True
            if batary == 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(white)

            camera_surf = pygame.image.load(f'VID_20230525_095425_out000{batary // 8}.jpg')
            camera_scale = pygame.transform.scale(
                camera_surf, (camera_surf.get_width() // 4,
                        camera_surf.get_height() // 3))
            camera_rect = camera_scale.get_rect(
                bottomright=(320, 240))
            dis.blit(camera_scale, camera_rect)

            pygame.draw.circle(dis, blue,(x1 + snake_block / 2, y1 + snake_block / 2), radius, 5)
            pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
            # pygame.draw.rect(dis, blue, [food2x, food2y, snake_block, snake_block])
            pygame.draw.rect(dis, black, [wallx, wally, snake_block * 40, snake_block])

            pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                if test == True:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(300, dis_height - snake_block) / 10.0) * 10.0
                    while foodx == wallx:
                        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    while foody == wally:
                        foody = round(random.randrange(300, dis_height - snake_block) / 10.0) * 10.0
                else:
                    foodx = 390
                    foody = 700
                    test = True
            # if x1 == food2x and y1 == food2y:
            #     food2x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            #     food2y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            batary -= 1
            clock.tick(snake_speed)

        pygame.quit()
        quit()
    gameLoop()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main()