import pygame
import pygame_menu
from robot_hum import robot_hum
from robot_wall_NN import robot_wall
def start_the_game():
    robot_wall(dis)
    mainmenu._open(datamenu)
        
def project_data():
    mainmenu._open(datamenu)
def help():
    mainmenu._open(helpmenu)
def select_map():
    pass
def select_photo():
    pass
def help_button_click():
    mainmenu._open(helpmenufaq)
def about_program():
    mainmenu._open(aboutprogrammenu)
pygame.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = 750
dis = pygame.display.set_mode((WIDTH, HEIGHT))

mainmenu = pygame_menu.Menu('Система управления роботом-пылесосом', 1000, 150,
                        columns=4,
                        rows=1,
                        position=[0,0],
                        theme=pygame_menu.themes.THEME_BLUE)
# menu.add.button('Играть за Даниса', start_the_game)
# menu.add.button('Играть за Рушана', start_the_game)
mainmenu.add.button('Запуск робота', start_the_game)
mainmenu.add.button('Загрузка карты', project_data)
mainmenu.add.button('Справка', help)
mainmenu.add.button('Выход', pygame_menu.events.EXIT)

datamenu = pygame_menu.Menu('Выбор Карты', 1000, 150,
                        columns=1,
                        rows=4,
                        position=[0,0],
                        theme=pygame_menu.themes.THEME_BLUE)
datamenu.add.text_input('URL:', default='/')
datamenu.add.button('Добавить', select_map)
#datamenu.add.button('Загрузка фотографий окружения', select_photo)

helpmenu = pygame_menu.Menu('Справка', 1000, 150,
                        columns=4,
                        rows=1,
                        position=[0,0],
                        theme=pygame_menu.themes.THEME_BLUE)
helpmenu.add.button('Помощь', help_button_click)
helpmenu.add.button('О программе', about_program)

helpmenufaq = pygame_menu.Menu('Помощь', 1000, 750,
                        columns=1,
                        rows=4,
                        position=[0,0],
                        theme=pygame_menu.themes.THEME_BLUE)
HELP1 = "1.Для загрузки карты необходимо указать её абсолютный путь в системе."
HELP2 = "2.После этого можно нажать кнопку добавить или Enter"
HELP3 = "3.Карта принимается в оцифрованном виде с указанием границ помещения"
HELP4 = "и стен внутри него"
helpmenufaq.add.label(HELP1, max_char=-1, font_size=20, font_color='black')
helpmenufaq.add.label(HELP2, max_char=-1, font_size=20, font_color='black')
helpmenufaq.add.label(HELP3, max_char=-1, font_size=20, font_color='black')
helpmenufaq.add.label(HELP4, max_char=-1, font_size=20, font_color='black')

aboutprogrammenu = pygame_menu.Menu('О программе', 1000, 750,
                        columns=1,
                        rows=6,
                        position=[0,0],
                        theme=pygame_menu.themes.THEME_BLUE)
ABOUT_PROGRAM1 = "Данная программа выполнена в качестве программной реализации к"
ABOUT_PROGRAM2 = "дипломной работе по теме:"
ABOUT_PROGRAM3 = "Разработка интеллектуальной системы управления роботом-пылесосом"
ABOUT_PROGRAM4 = "Автор программы: Батыршин Данис"
ABOUT_PROGRAM5 = "Группа 4413"
ABOUT_PROGRAM6 = "Дата защиты 9 июля 2023 года"
aboutprogrammenu.add.label(ABOUT_PROGRAM1, max_char=-1, font_size=20, font_color='black')
aboutprogrammenu.add.label(ABOUT_PROGRAM2, max_char=-1, font_size=20, font_color='black')
aboutprogrammenu.add.label(ABOUT_PROGRAM3, max_char=-1, font_size=20, font_color='black')
aboutprogrammenu.add.label(ABOUT_PROGRAM4, max_char=-1, font_size=20, font_color='black')
aboutprogrammenu.add.label(ABOUT_PROGRAM5, max_char=-1, font_size=20, font_color='black')
aboutprogrammenu.add.label(ABOUT_PROGRAM6, max_char=-1, font_size=20, font_color='black')

mainmenu.mainloop(dis)

