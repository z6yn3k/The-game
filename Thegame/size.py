import pygame_widgets,pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

def Ex(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2):
    f=open('playerData.txt','w')
    TexT=[]
    TexT.append('complete='+str(complete2)+'\n')
    TexT.append('completecust='+str(completecust2)+'\n')
    TexT.append('easycomplete=' + str(easycomplete2) + '\n')
    TexT.append('hardcomplete=' + str(hardcomplete2) + '\n')
    TexT.append('soundloud='+str(soundloud2)+'\n')
    TexT.append('diffuc='+str(diffuc2))
    f.writelines(TexT)
    f.close()
    pygame.quit()
    exit()

def screenfill(screen,tag):
    LGRAY = (196, 196, 196)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    if tag==0:
        screen.fill(LGRAY)
        for i in range(0,640,18):
            pygame.draw.rect(screen, GRAY, [i, 0, 1, 620], 1)
        for i in range(0,640,18):
            pygame.draw.rect(screen, GRAY, [0, i, 620, 1], 1)
        for i in range(0,640,36):
            pygame.draw.rect(screen, BLACK, [i, 0, 1, 620], 1)
        for i in range(0,640,36):
            pygame.draw.rect(screen, BLACK, [0, i, 620, 1], 1)
    if tag==1:
        pygame.draw.rect(screen, GRAY, [10, 50, 200, 40])
    if tag==2:
        pygame.draw.rect(screen, GRAY, [180, 55, 200, 40])
    if tag==3:
        pygame.draw.rect(screen, GRAY, [10, 50, 360, 40])
    if tag==4:
        pygame.draw.rect(screen, GRAY, [10, 90, 360, 40])
    if tag==5:
        pygame.draw.rect(screen, GRAY, [10, 130, 360, 40])
    if tag==6:
        pygame.draw.rect(screen, GRAY, [10, 170, 360, 40])

def number(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2):
    BUTTON = (96, 96, 96)
    DARKBUTTON = (64, 64, 64)
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    hig=85
    weg=5
    pygame.init()
    win = pygame.display.set_mode((320, 180))
    output2=output1=0

    smallfont = pygame.font.SysFont('Corbel', 35)
    Back = smallfont.render('Next', True, WHITE)
    Next = smallfont.render('Back', True, WHITE)
    select = smallfont.render('Select size', True, WHITE)
    select1 = smallfont.render('Select size', True, BLACK)

    slider = Slider(win, 30, 60, 160, 20, min=3, max=32, step=1)
    output=TextBox(win,230, 55, 30, 30,fontSize=22,borderColour=BUTTON,colour=DARKBUTTON,textColour=WHITE,
                   borderThickness=5)
    output.disable()  # Act as label instead of textbox
    screenfill(win,0)
    clock = pygame.time.Clock()
    FPS=15
    run = True
    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:

            mouse = pygame.mouse.get_pos()

            win.blit(select1, (50, 1))
            win.blit(select, (52, 3))

            if weg + 10 <= mouse[0] <= weg + 10 + 140 and hig + 20 <= mouse[1] <= hig + 20+40:
                pygame.draw.rect(win, BUTTON, [weg + 10, hig + 20, 140, 40])
                win.blit(Next, (weg + 10+25 , hig + 40-15))
            else:
                pygame.draw.rect(win, DARKBUTTON, [weg + 10, hig + 20, 140, 40])
                win.blit(Next, (weg + 10+25 , hig + 40-15))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg + 10 <= mouse[0] <= weg + 10 + 140 and hig + 20 <= mouse[1] <= hig + 20+ 40:
                    slider.disable()
                    output.disable()
                    slider.hide()
                    output.hide()
                    del slider
                    del output
                    return -1

            if weg+150 + 10 <= mouse[0] <= weg+150 + 10 + 140 and hig + 20 <= mouse[1] <= hig + 20+40:
                pygame.draw.rect(win, BUTTON, [weg+150 + 10, hig + 20, 140, 40])
                win.blit(Back, (weg+150 + 10+25 , hig + 40-15))
            else:
                pygame.draw.rect(win, DARKBUTTON, [weg+150 + 10, hig + 20, 140, 40])
                win.blit(Back, (weg+150 + 10+25 , hig + 40-15))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+150 + 10 <= mouse[0] <= weg+150 + 10 + 140 and hig + 20 <= mouse[1] <= hig + 20+ 40:
                    llll=slider.getValue()
                    slider.disable()
                    output.disable()
                    slider.hide()
                    output.hide()
                    del slider
                    del output
                    return llll

            if event.type == pygame.QUIT:
                run = False
                Ex(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2)

        output.setText(slider.getValue())
        output1=slider.getValue()
        if output1!=output2:
            screenfill(win,1)
        output2=output1

        pygame_widgets.update(events)
        pygame.display.update()

def steps(a,b,c,d,complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2):
    BUTTON = (96, 96, 96)
    DARKBUTTON = (64, 64, 64)
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    hig=85
    weg=5
    pygame.init()
    win = pygame.display.set_mode((520, 380))
    output2=output1=0
    output2X=output1X=0
    output2Y=output1Y=0
    output2Z=output1Z=0

    smallfont = pygame.font.SysFont('Corbel', 35)
    Ok = smallfont.render('Ok', True, WHITE)
    select = smallfont.render('Select count of steps', True, WHITE)
    select1 = smallfont.render('Select count of steps', True, BLACK)

    slider = Slider(win, 30, 60, 320, 20, min=0, max=9, step=1)
    slider1 = Slider(win, 30, 100, 320, 20, min=0, max=9, step=1)
    slider2 = Slider(win, 30, 140, 320, 20, min=0, max=9, step=1)
    slider3 = Slider(win, 30, 180, 320, 20, min=0, max=9, step=1)

    slider.setValue(a)
    slider1.setValue(b)
    slider2.setValue(c)
    slider3.setValue(d)

    output=TextBox(win,390, 55, 50, 30,fontSize=22,borderColour=BUTTON,colour=DARKBUTTON,textColour=WHITE,
                   borderThickness=5)
    outputX = TextBox(win, 390, 95, 50, 30, fontSize=22, borderColour=BUTTON, colour=DARKBUTTON, textColour=WHITE,
                     borderThickness=5)
    outputY = TextBox(win, 390, 135, 50, 30, fontSize=22, borderColour=BUTTON, colour=DARKBUTTON, textColour=WHITE,
                     borderThickness=5)
    outputZ = TextBox(win, 390, 175, 50, 30, fontSize=22, borderColour=BUTTON, colour=DARKBUTTON, textColour=WHITE,
                     borderThickness=5)
    output.disable()  # Act as label instead of textbox
    outputX.disable()
    outputY.disable()
    outputZ.disable()
    screenfill(win,0)
    clock = pygame.time.Clock()
    FPS=15

    screenfill(win, 3)
    screenfill(win, 4)
    screenfill(win, 5)
    screenfill(win, 6)
    run = True
    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:

            mouse = pygame.mouse.get_pos()

            win.blit(select1, (50, 1))
            win.blit(select, (52, 3))

            if weg+150 + 10 <= mouse[0] <= weg+150 + 10 + 140 and hig + 20+200 <= mouse[1] <= hig + 20+40+200:
                pygame.draw.rect(win, BUTTON, [weg+150 + 10, hig + 20+200, 140, 40])
                win.blit(Ok, (weg+150 + 10+25 , hig + 40-15+200))
            else:
                pygame.draw.rect(win, DARKBUTTON, [weg+150 + 10, hig + 20+200, 140, 40])
                win.blit(Ok, (weg+150 + 10+25 , hig + 40-15+200))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+150 + 10 <= mouse[0] <= weg+150 + 10 + 140 and hig + 20+200 <= mouse[1] <= hig + 20+ 40+200:
                    llll=slider.getValue()
                    slider.disable()
                    output.disable()
                    slider.hide()
                    output.hide()
                    del slider
                    del output

                    llll1=slider1.getValue()
                    slider1.disable()
                    outputX.disable()
                    slider1.hide()
                    outputX.hide()
                    del slider1
                    del outputX

                    llll2=slider2.getValue()
                    slider2.disable()
                    outputY.disable()
                    slider2.hide()
                    outputY.hide()
                    del slider2
                    del outputY

                    llll3=slider3.getValue()
                    slider3.disable()
                    outputZ.disable()
                    slider3.hide()
                    outputZ.hide()
                    del slider3
                    del outputZ

                    return [llll,llll1,llll2,llll3]

            if event.type == pygame.QUIT:
                run = False
                Ex(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2)

        output.setText(slider.getValue())
        outputX.setText(slider1.getValue())
        outputY.setText(slider2.getValue())
        outputZ.setText(slider3.getValue())

        output1=slider.getValue()
        output1X=slider1.getValue()
        output1Y = slider2.getValue()
        output1Z = slider3.getValue()

        if output1!=output2:
            screenfill(win,3)
        if output1X!=output2X:
            screenfill(win,4)
        if output1Y!=output2Y:
            screenfill(win,5)
        if output1Z!=output2Z:
            screenfill(win,6)

        output2=output1
        output2X=output1X
        output2Y = output1Y
        output2Z = output1Z

        pygame_widgets.update(events)
        pygame.display.update()

def setting(screen,diffuc,soundloud,complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2):

    hig=50
    weg=30
    pygame.init()
    output2=output1=0

    BUTTON = (96, 96, 96)
    DARKBUTTON = (64, 64, 64)
    YYELLOW = (196, 196, 0)
    DYELLOW = (127, 127, 0)
    RRED = (196, 0, 0)
    DRED = (127, 0, 0)
    GGREEN = (0, 196, 0)
    DGREEN = (0, 127, 0)
    WHITE = (255, 255, 255)
    BLACK=(0,0,0)

    smallfont = pygame.font.SysFont('Corbel', 35)
    bigfont = pygame.font.SysFont('Corbel', 50)

    Music = bigfont.render('Music', True, WHITE)
    Music1 = bigfont.render('Music', True, BLACK)
    reset = smallfont.render('Reset progress', True, BLACK)
    reset1 = smallfont.render('Reset progress', True, WHITE)
    diff = smallfont.render('difficulty', True, WHITE)
    diff1 = smallfont.render('difficulty', True, BLACK)
    Back = smallfont.render('Back', True, WHITE)

    slider = Slider(screen, 200, 65, 160, 20, min=0, max=100, step=1)
    output = TextBox(screen, 400, 60, 40, 30, fontSize=22,borderColour=BUTTON,colour=DARKBUTTON,textColour=WHITE,
                     borderThickness=5)
    pos=int(soundloud*100)
    slider.setValue(pos)

    output.disable()  # Act as label instead of textbox
    screenfill(screen,0)
    run = True

    pygame.display.set_caption('Settings')
    screen.blit(Music1, (weg + 23, hig + 3))
    screen.blit(Music, (weg + 25, hig + 5))
    screen.blit(reset, (weg + 23, hig + 3 + 30 + 35))
    screen.blit(reset1, (weg + 25, hig + 5 + 30 + 35))
    screen.blit(diff1, (weg + 23, hig + 3 + 30 + 35 + 55))
    screen.blit(diff, (weg + 25, hig + 5 + 30 + 35 + 55))
    pygame.draw.rect(screen, DARKBUTTON, [weg + 23 + 230, hig + 3 + 70, 30, 30])
    pygame.draw.rect(screen, DARKBUTTON, [weg, hig + 400 + 60, 140, 40])
    screen.blit(Back, (weg + 25, hig + 400 + 60 + 5))
    if diffuc == 1:
        col2 = DGREEN
    elif diffuc == 2:
        col2 = DYELLOW
    else:
        col2 = DRED
    pygame.draw.rect(screen, col2, [weg + 23 + 140, hig + 70 + 60, 30, 30])
    clock = pygame.time.Clock()
    FPS=15

    while run:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:

            mouse = pygame.mouse.get_pos()
            pygame.display.set_caption('Settings')
            screen.blit(Music1, (weg + 23, hig + 3))
            screen.blit(Music, (weg + 25, hig + 5))
            screen.blit(reset, (weg + 23, hig + 3 + 30 + 35))
            screen.blit(reset1, (weg + 25, hig + 5 + 30 + 35))
            screen.blit(diff1, (weg + 23, hig + 3 + 30 + 35 + 55))
            screen.blit(diff, (weg + 25, hig + 5 + 30 + 35 + 55))

            if weg + 23 + 230 <= mouse[0] <= weg + 23 + 230 + 30 and hig + 3 + 70 <= mouse[1] <= hig + 3 + 30 + 70:
                pygame.draw.rect(screen, BUTTON, [weg + 23 + 230, hig + 3 + 70, 30, 30])
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg + 23 + 230, hig + 3 + 70, 30, 30])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg + 23 + 230 <= mouse[0] <= weg + 23 + 230 + 30 and hig + 3 + 70 <= mouse[1] <= hig + 3 + 30 + 70:
                    screenfill(screen,0)
                    menuvalue = 1
                    complete = []
                    completecust=[]

                    slider.disable()
                    output.disable()
                    slider.hide()
                    output.hide()
                    del slider
                    del output
                    return [menuvalue,complete,soundloud,completecust]

            if weg + 23 + 140 <= mouse[0] <= weg + 23 + 140 + 30 and hig + 70 + 60 <= mouse[1] <= hig + 30 + 70 + 60:
                if diffuc == 1:
                    col1 = GGREEN
                elif diffuc == 2:
                    col1 = YYELLOW
                else:
                    col1 = RRED
                pygame.draw.rect(screen, col1, [weg + 23 + 140, hig + 70 + 60, 30, 30])
            else:
                if diffuc == 1:
                    col2 = DGREEN
                elif diffuc == 2:
                    col2 = DYELLOW
                else:
                    col2 = DRED
                pygame.draw.rect(screen, col2, [weg + 23 + 140, hig + 70 + 60, 30, 30])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg + 23 + 140 <= mouse[0] <= weg + 23 + 140 + 30 and hig + 70 + 60 <= mouse[
                    1] <= hig + 30 + 70 + 60:
                    screenfill(screen,0)
                    menuvalue = 6

                    slider.disable()
                    output.disable()
                    slider.hide()
                    output.hide()
                    del slider
                    del output
                    return [menuvalue,-1,soundloud,-1]

            if weg <= mouse[0] <= weg + 140 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg, hig + 400 + 60, 140, 40])
                screen.blit(Back, (weg + 25, hig + 400 + 60 + 5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig + 400 + 60, 140, 40])
                screen.blit(Back, (weg + 25, hig + 400 + 60 + 5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                    screenfill(screen,0)
                    menuvalue = 1

                    slider.disable()
                    output.disable()
                    slider.hide()
                    output.hide()
                    del slider
                    del output
                    return [menuvalue,-1,soundloud,-1]

            if event.type == pygame.QUIT:
                run = False
                Ex(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2)

        output.setText(slider.getValue())
        output1=slider.getValue()
        if output1!=output2:
            screenfill(screen,2)
            soundloud=(slider.getValue())/100
            pygame.mixer.music.set_volume(soundloud)
        output2=output1

        pygame_widgets.update(events)
        pygame.display.update()
