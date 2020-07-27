import pygame as p
import random
x = p.init()

#Color
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

#Creating Window

screenwidth = 1500
screenheight = 900
gameWindow = p.display.set_mode((screenwidth,screenheight))
p.display.set_caption("My Snake Game using Python")
font = p.font.SysFont(None,55)
clock = p.time.Clock()
p.display.update()



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow_, color_, snk_list_, Snake_size_):
    for x, y in snk_list_:
        p.draw.rect(gameWindow_, color_ , [x, y, Snake_size_, Snake_size_])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome To Snake Game ", black, 300, 275)
        text_screen("Press Space Bar For Continue  ", black, 300, 320)
        for event in p.event.get():
            # print(event)
            if event.type == p.QUIT:
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    selectgame()
        p.display.update()

def level1():
    global speed1
    # global speed2
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Press 1 for EASY LEVEL   ", black, 300, 320)
        text_screen("Press 2 for MEDIUM LEVEL   ", black, 300, 360)
        text_screen("Press 3 for HARD LEVEL   ", black, 300, 400)
        text_screen("Press 4 for INSANE LEVEL   ", black, 300, 440)
        for event in p.event.get():
            # print(event)
            if event.type == p.QUIT:
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    speed1 = 4
                    # speed2 = 4
                    colour()

                if event.key == p.K_2:
                    speed1 = 10
                    # speed2 = 10
                    colour()

                if event.key == p.K_3:
                    speed1 = 15
                    # speed2 = 15
                    colour()

                if event.key == p.K_4:
                    speed1 = 20
                    # speed2 = 20
                    colour()

        p.display.update()

def level2():
    global speed1
    global speed2
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Press 1 for EASY LEVEL   ", black, 300, 320)
        text_screen("Press 2 for MEDIUM LEVEL   ", black, 300, 360)
        text_screen("Press 3 for HARD LEVEL   ", black, 300, 400)
        text_screen("Press 4 for INSANE LEVEL   ", black, 300, 440)
        for event in p.event.get():
            # print(event)
            if event.type == p.QUIT:
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    speed1 = 4
                    speed2 = 4
                    colour1()

                if event.key == p.K_2:
                    speed1 = 10
                    speed2 = 10
                    colour1()
                if event.key == p.K_3:
                    speed1 = 15
                    speed2 = 15
                    colour1()
                if event.key == p.K_4:
                    speed1 = 20
                    speed2 = 20
                    colour1()
        p.display.update()


def colour():
    global color
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen(" PRESS B FOR BLACK ... G FOR GREEN ... R FOR RED ", black, 300, 320)
        text_screen(" PLAYER1 SNAKE COLOR  ", red , 300, 370)
        for event in p.event.get():
            # print(event)
            if event.type == p.QUIT:
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_b:
                    color = black
                    gameloop1()

                if event.key == p.K_g:
                    color = green
                    gameloop1()

                if event.key == p.K_r:
                    color = red
                    gameloop1()
        p.display.update()


def colour1():
    global color1
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen(" PRESS B FOR BLACK ... G FOR GREEN ... R FOR RED ", black, 300, 320)
        text_screen(" PLAYER1 SNAKE COLOR  ", red , 300, 370)
        for event in p.event.get():
            # print(event)
            if event.type == p.QUIT:
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_b:
                    color1 = black
                    colour2()

                if event.key == p.K_g:
                    color1 = green
                    colour2()

                if event.key == p.K_r:
                    color1 = red
                    colour2()


        p.display.update()

def colour2():
    global color2
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen(" PRESS B FOR BLACK ... G FOR GREEN ... R FOR RED ", black, 300, 320)
        text_screen(" PLAYER2 SNAKE COLOR  ", red, 300, 370)
        for event in p.event.get():
            # print(event)
            if event.type == p.QUIT:
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_b:
                    color2 = black
                    gameloop2()

                if event.key == p.K_g:
                    color2 = green
                    gameloop2()

                if event.key == p.K_r:
                    color2 = red
                    gameloop2()

        p.display.update()

def gameloop2():
    #game specific variables
    i1=0
    i2=0
    exit_game = False
    game_over = False
    Snake_x1 = 45
    Snake_y1 = 30
    Snake_size1 = 20
    Snake_x2 = 45
    Snake_y2 = 30
    Snake_size2 = 20
    fps = 60
    # speed1 = 10
    # speed2 = 10
    score1 = 0
    score2 = 0
    velocity_x1=0
    velocity_y1=0
    velocity_x2 = 0
    velocity_y2 = 0
    food_x = random.randint(0, screenwidth-10)
    food_y = random.randint(0, screenheight-10)

    snk_length1=1
    snk_list1=[]
    snk_length2 = 1
    snk_list2 = []

    with open("Highscore_Double_1_1.txt", 'r') as f1:
        highscore1=f1.read()
    with open("Highscore_Double_1_2.txt", 'r') as f2:
        highscore2=f2.read()


    #Creating game loop
    while not exit_game:

        if game_over:

            with open("Highscore_Double_1_1.txt", 'w') as f:
                f.write(str(highscore1))
            gameWindow.fill(white)
            with open("Highscore_Double_1_2.txt", 'w') as f:
                f.write(str(highscore2))
            gameWindow.fill(white)

            text_screen("Game Over ... Plz Press Enter to Continue",red,100,200)


            text_screen(" PLAYER 1 SCORE " + str(score1), black, 300, 320)
            text_screen(" PLAYER 2 SCORE " + str(score2), black, 300, 370)
            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game=True
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        gameloop2()

        else:

            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game = True
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RIGHT:
                        velocity_x1 = speed1
                        velocity_y1 = 0
                    if event.key == p.K_LEFT:
                        velocity_x1 = -speed1
                        velocity_y1 = 0
                    if event.key == p.K_UP:
                        velocity_x1 = 0
                        velocity_y1 = -speed1
                    if event.key == p.K_DOWN:
                        velocity_x1 = 0
                        velocity_y1 = speed1

                    if event.key == p.K_d:
                        velocity_x2 = speed2
                        velocity_y2 = 0
                    if event.key == p.K_a:
                        velocity_x2 = -speed2
                        velocity_y2 = 0
                    if event.key == p.K_w:
                        velocity_x2 = 0
                        velocity_y2 = -speed2
                    if event.key == p.K_s:
                        velocity_x2 = 0
                        velocity_y2 = speed2

            Snake_x1 += velocity_x1
            Snake_y1 += velocity_y1

            Snake_x2 += velocity_x2
            Snake_y2 += velocity_y2

            if abs(Snake_x1-food_x)<15 and abs(Snake_y1-food_y)<15:
                score1 += 1
                food_x = random.randrange(0, (screenwidth-30)/2)
                food_y = random.randrange(0, (screenheight-30)/2)
                snk_length1 += 5

                if score1 > int(highscore1):
                    highscore1 = score1

            if abs(Snake_x2 - food_x) < 15 and abs(Snake_y2 - food_y) < 15:
                score2 += 1
                food_x = random.randrange(0, (screenwidth-30)/2)
                food_y = random.randrange(0, (screenheight-30)/2)
                snk_length2 += 5

                if score2 > int(highscore2):
                    highscore2 = score2


            gameWindow.fill(white)
            text_screen("Score1: " + str(score1)  +"\t Score2: " + str(score2)   +"\t High Score1:" + str(highscore1)   +"\tHigh Score2:" + str(highscore2)  ,red,5,5)
            # text_screen("Score: " + str(score2) + " High Score:" + str(highscore2), red, 5, 5)
            # p.draw.rect(gameWindow,black,[Snake_x,Snake_y,Snake_size,Snake_size])
            p.draw.rect(gameWindow,red,[food_x,food_y,Snake_size1,Snake_size1])


            head1 = []
            head1.append(Snake_x1)
            head1.append(Snake_y1)
            snk_list1.append(head1)

            if len(snk_list1)>snk_length1:
                del snk_list1[0]

            if head1 in snk_list1[ :-1]:
                game_over = True


            if (Snake_x1>screenwidth):
                Snake_x1 = 0

            if (Snake_y1 > screenheight):
                Snake_y1 = 0

            if (Snake_x1 < 0):
                Snake_x1 = screenwidth

            if (Snake_y1<0):
                Snake_y1 = screenheight

            plot_snake(gameWindow, color1 ,snk_list1,Snake_size1)

            head2 = []
            head2.append(Snake_x2)
            head2.append(Snake_y2)
            snk_list2.append(head2)

            if len(snk_list2)>snk_length2:
                del snk_list2[0]

            if head2 in snk_list2[ :-1]:
                game_over = True



            if (Snake_x2>screenwidth):
                Snake_x2 = 0

            if (Snake_y2 > screenheight):
                Snake_y2 = 0

            if (Snake_x2 < 0):
                Snake_x2 = screenwidth

            if (Snake_y2<0):
                Snake_y2 = screenheight

            plot_snake(gameWindow , color2 , snk_list2 , Snake_size2)

        p.display.update()
        clock.tick(fps)
    p.quit()
    quit()

def gameloop1():

    i=0
    exit_game = False
    game_over = False
    Snake_x = 45
    Snake_y = 30
    Snake_size = 20
    fps = 60
    score = 0
    velocity_x=0
    velocity_y=0
    food_x = random.randint(0, screenwidth-10)
    food_y = random.randint(0, screenheight-10)

    snk_length=1
    snk_list=[]
    with open("Highscore_Single.txt", 'r') as f:
        highscore=f.read()



    while not exit_game:

        if game_over:

            with open("Highscore_Single.txt", 'w') as f:
                f.write(str(highscore))
            gameWindow.fill(white)

            text_screen(" PLAYER 1 SCORE " + str(score), black, 300, 320)

            text_screen("Game Over ... Plz Press Enter to Continue",red,100,200)
            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game=True
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        gameloop1()

        else:

            for event in p.event.get():

                if event.type == p.QUIT:
                    exit_game = True
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RIGHT:
                        velocity_x = speed1
                        velocity_y = 0
                    if event.key == p.K_LEFT:
                        velocity_x = -speed1
                        velocity_y = 0
                    if event.key == p.K_UP:
                        velocity_x = 0
                        velocity_y = -speed1
                    if event.key == p.K_DOWN:
                        velocity_x = 0
                        velocity_y = speed1

            Snake_x += velocity_x
            Snake_y += velocity_y

            if abs(Snake_x-food_x)<20 and abs(Snake_y-food_y)<20:
                score += 5
                food_x = random.randrange(0, (screenwidth-30)/2)
                food_y = random.randrange(0, (screenheight-30)/2)
                snk_length += 5

                if score > int(highscore):
                    highscore = score




            gameWindow.fill(white)
            text_screen("Score: " + str(score) + " High Score:"+ str(highscore),red,5,5)

            p.draw.rect(gameWindow,red,[food_x,food_y,Snake_size,Snake_size])

            head = []
            head.append(Snake_x)
            head.append(Snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[ :-1]:
                game_over = True


            if (Snake_x>screenwidth):
                Snake_x = 0

            if (Snake_y > screenheight):
                Snake_y = 0

            if (Snake_x < 0):
                Snake_x = screenwidth

            if (Snake_y<0):
                Snake_y = screenheight

            plot_snake(gameWindow,color,snk_list,Snake_size)

        p.display.update()
        clock.tick(fps)
    p.quit()                    #quits pygame
    quit()                      #quits code

def selectgame():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen(" PRESS 1 FOR SINGLE PLAYER ", black, 300, 320)
        text_screen(" PRESS 2 FOR DOUBLE PLAYER  ", black, 300, 370)
        for event in p.event.get():
            if event.type == p.QUIT:
                exit_game = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    level1()

                if event.key == p.K_2:
                    level2()
                   
        p.display.update()


welcome()


