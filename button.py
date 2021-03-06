import pygame
import random
import os
import game

nextLabelFlag = True

currentLableButton = ["1", "2", "3", "4"] #список для вариантов ответов на кнопки
labelButtons = [] #Список со всеми возможными вариантами ответов
ball = 0    #перемменная, считает правильные ответы
answer = "" #Переменная, которая содержит правильный ответ


class Button:

    def __init__(self, width, height):      #Создание кнопки(длина, ширина)
        self.width = width
        self.height = height
        self.unactive_color = (255, 255, 255) #Цвет когда кнопка не активная(т.е курсор не на ней)
        self.active_color = (23, 204, 58)   #Цвет когда кнопка активная(т.е курсор на ней)

    def labelButtons(self): #Метод(функция) смены вариантов ответа
        global nextLabelFlag, currentLableButton, labelButtons, namePict, answer

        #Создание списка. со всеми возможными вариантами ответа, по названию деталей из папки
        path = "picturies"
        labelButtons = [i for i in os.listdir(path)]#создаем список файлов из полных имен картинки с расширенниями
        labelButtons = ''.join(labelButtons)   #Преобразование списка в строчку
        labelButtons = labelButtons.split(".png") #разделяем строку на элементы, относительно .jpg, т.е убираем .jpg
        labelButtons.pop()  #Удаляем последний элемент, иак как он пустой

        a = labelButtons.copy() #Переносим копию нашего списка в новый список a
        answer = game.namePict  #Ответ равен имени картинки
        while answer not in currentLableButton: #наполняем список для кнопок, пока не будет в нем правильного ответа
            for i in range(4):
                currentLableButton[i] = a.pop(random.randint(0, len(a) - 1))#Наполнение списка надписей на кнопки аозможными вариантами

    def proverka(self, labBut):#Функция проверки на правильность ответа
        global ball, answer
        if labBut == answer: #если нажата кнопка у которой надпись совбадает с именем картинки, то верно и + балл
            ball += 1

    #функция вывода текста на  текста на кнопку, и не только, куда угодно
    def print_text(self, window, message, x, y, font_color=(0, 0, 0), font_type="impact.ttf", font_size=20):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        window.blit(text, (x, y - 5))

    #функция прорисовки кнопки
    def drawButton(self, window, message, x, y, action1=None, action2=None, action3=None, font_size=30):
        global currentLableButton, nextLabelFlag, ball, answer
        mouse = pygame.mouse.get_pos()  # позиция мышки
        click = pygame.mouse.get_pressed()#Щелчок ЛКМ
        # self.imgBut=pygame.image.load("butimg.png")
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:  # Проверка находится ли укзатель в поределах кнопкиесли находится, то прорисовываем новый прямоугольник, только другим цвето
            pygame.draw.rect(window, self.active_color, (x, y, self.width, self.height))#Отрисовкапрямоугольника, в качестве кнопки
            # если н1ажать на кнопку, когда указатель мыши входит в кнопку, то проверится на правильность и перегрузит картинки и варианты
            if click[0] == 1:#Если ЛКМ нажата в пределах кнопки, то выполнить дефствия
                action3(message)#Проверка на верность
                action1()   #Смена катринки
                action2()   #Смена текста на кнопках
                pygame.time.delay(200)# 200мс ожидание
        else:
            pygame.draw.rect(window, self.unactive_color, (x, y, self.width, self.height))#Отрисовкапрямоугольника, в качестве кнопки
        self.print_text(window=window, message=message,x=x + 10, y=y + 10, font_size=font_size)#Вывод текста на кнопку
