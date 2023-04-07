import pygame,size,texture,random,os

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

def screenfill(screen,x):
    LGRAY = (196, 196, 196)
    BLACK=(0,0,0)
    GRAY = (128, 128, 128)

    screen.fill(LGRAY)
    for i in range(0, x*18+1, 18):
        pygame.draw.rect(screen, GRAY, [i, 54, 1, x*18], 1)
    for i in range(54, x*18+55, 18):
        pygame.draw.rect(screen, GRAY, [0, i, x*18, 1], 1)
    for i in range(0, x*18+1, 36):
        pygame.draw.rect(screen, BLACK, [i, 54, 1, x*18], 1)
    for i in range(54, x*18+55, 36):
        pygame.draw.rect(screen, BLACK, [0, i, x*18, 1], 1)

def Text(mess,colour,size,font):
    smallfont = pygame.font.SysFont(font, size)
    messa = smallfont.render(mess, True, colour)
    return messa

def Button(screen,event,mouse,x,y,weight,hight,colouroff,colouron,text='-1',xtext=0,ytext=0,border=0,
           bordercolour=(0,0,0),shapex=-1,shapey=0,shapetype='',shapeweight=0,shapehight=0,shapecolloff=(0,0,0),
           shapecollon=(0,0,0)):

    if x <= mouse[0] <= x + weight and y <= mouse[1] <= y + hight:
        if border>0:
            pygame.draw.rect(screen, bordercolour, [x-border, y-border, weight+border*2, hight+border*2])
        pygame.draw.rect(screen, colouron, [x,y,weight, hight])
        if shapetype=='square':
            pygame.draw.rect(screen,shapecollon,[x+shapex,y+shapey,shapeweight,shapehight])
        if shapetype=='circle':
            pygame.draw.circle(screen,shapecollon,[x+shapex,y+shapey],shapeweight)
        if shapetype=='rhomb':
            cr=[[x+int(round(weight/2)),y+shapey-1],[x+weight-shapex,int(round(hight/2))+4],
                [x+int(round(weight/2)),y+hight-shapey],[x+shapex,int(round(hight/2))+4]]
            pygame.draw.polygon(screen,shapecollon,cr)
        if text!='-1':
            screen.blit(text, (x+xtext, y+ytext))
    else:
        if border>0:
            pygame.draw.rect(screen, bordercolour, [x-border, y-border, weight+border*2, hight+border*2])
        pygame.draw.rect(screen, colouroff, [x,y,weight, hight])
        if shapetype=='square':
            pygame.draw.rect(screen,shapecolloff,[x+shapex,y+shapey,shapeweight,shapehight])
        if shapetype=='circle':
            pygame.draw.circle(screen,shapecolloff,[x+shapex,y+shapey],shapeweight)
        if shapetype == 'rhomb':
            cr=[[x+int(round(weight/2)),y+shapey-1],[x+weight-shapex,int(round(hight/2))+4],
                [x+int(round(weight/2)),y+hight-shapey],[x+shapex,int(round(hight/2))+4]]
            pygame.draw.polygon(screen, shapecolloff, cr)
        if text != '-1':
            screen.blit(text, (x+xtext, y+ytext))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x <= mouse[0] <= weight + x and y <= mouse[1] <= hight + y:
            return 1

def Check(screen,event,mouse,x,y,weight,hight,colouroff,colouron,on,border=0,bordercolour=(0,0,0),checkcoll=(0,255,0)):
    if x <= mouse[0] <= x + weight and y <= mouse[1] <= y + hight:
        if border > 0:
            pygame.draw.rect(screen, bordercolour, [x - border, y - border, weight + border * 2, hight + border * 2])
        pygame.draw.rect(screen, colouron, [x, y, weight, hight])

    else:
        if border > 0:
            pygame.draw.rect(screen, bordercolour, [x - border, y - border, weight + border * 2, hight + border * 2])
        pygame.draw.rect(screen, colouroff, [x, y, weight, hight])
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x <= mouse[0] <= weight + x and y <= mouse[1] <= hight + y and on==True:
            on=False
        elif x <= mouse[0] <= weight + x and y <= mouse[1] <= hight + y and on==False:
            on=True
    if on == True:
        pygame.draw.line(screen,checkcoll,[x+weight-4,y+2],[x+round(weight*0.4),y+hight-2],2)
        pygame.draw.line(screen, checkcoll, [x + round(weight * 0.4), y + hight-2], [x+2 , y+ round(hight * 0.6)], 2)
    return on

def main(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2):
    pygame.display.set_caption('Redactor')
    pygame.mixer.music.load("music\credits.mp3")
    pygame.mixer.music.play(-1)
    keyss = [51, 53, 55, 57, 59, 61, 63, 65, 67]
    locks = [52, 54, 56, 58, 60, 62, 64, 66, 68]
    prtls = [71, 72, 73, 74, 75, 76, 77, 78, 79]
    prtks = [81, 82, 83, 84, 85, 86, 87, 88, 89]
    blaen = [91, 92, 93, 94, 95, 96, 97, 98, 99]
    bluen = [101, 102, 103, 104, 105, 106, 107, 108, 109]
    puren = [111, 112, 113, 114, 115, 116, 117, 118, 119]

    LGRAY = (196, 196, 196)
    LLGRAY = (220, 220, 220)
    GRAY = (128, 128, 128)
    BLACK=(0,0,0)
    LBLACK=(64,64,64)
    DGRAY=(96,96,96)
    DLGRAY=(150,150,150)
    YELLOW=(255,255,0)
    LYELLOW=(255,255,64)
    LGREEN=(64,255,64)
    BLUE=(0,0,255)
    LBLUE=(64,64,255)
    RED=(255,0,0)
    LRED=(255,64,64)
    WHITE=(255,255,255)
    BUTTON = (96, 96, 96)
    DARKBUTTON = (64, 64, 64)
    PURPLE = (148, 0, 211)
    LPURPLE = (188, 40, 251)
    DRED=(127,0,0)

    Size = size.number(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2)
    if Size==-1:
        return 0
    Size+=2
    WIDTH=612
    HEIGHT=Size*18+55+32
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    choicenum1=choicenum2=choicenumP=0

    FPS=15
    run=True
    display = [[0] * Size for i in range(Size)] #!

    for x in range(0,len(display)):
        display[x][0]=2
        display[x][len(display)-1]=2
        display[0][x]=2
        display[len(display)-1][x]=2

    choice=1
    screenfill(screen,Size)

    Borders=Text('Killing borders', BLACK, 15, 'Arial')
    Blind=Text('Curse of blind', BLACK, 15, 'Arial')
    Reverse=Text('Curse of reverse', BLACK, 15, 'Arial')
    Back=Text('Back to menu', WHITE, 20,'Corbel')
    SAB=Text('Save and back', WHITE, 20,'Corbel')
    photo = pygame.image.load("images\lockmini.png")

    on1=on2=on3=False
    no=False
    steps=random.randint(50,200)
    while run:
        portals1=[]
        portals2=[]

        blacks=[]
        blueks=[]
        purpes=[]
        redcount=0
        blackcount = 0
        bluecount = 0
        purplecount = 0
        finishcount=0
        for i in range(0,len(display)):
            for n in range(0,len(display)):
                if display[i][n] in blaen:
                    blackcount+=1
                    blacks.append(display[i][n])
                if display[i][n] in bluen:
                    bluecount+=1
                    blueks.append(display[i][n])
                if display[i][n] in puren:
                    purplecount+=1
                    purpes.append(display[i][n])
                if display[i][n] in prtls:
                    portals1.append(display[i][n])
                if display[i][n] in prtks:
                    portals2.append(display[i][n])
                if display[i][n] == 3:
                    redcount+=1
                if display[i][n] == 4:
                    finishcount+=1

        clock.tick(FPS)

        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()
            for y in range(72,Size*18+36,18):
                for x in range(18, Size*18-18, 18):

                    if Button(screen,event,mouse,x+1,y+1,16,16,LGRAY,LLGRAY)==1:
                        cellpos=([int(x/18),int((y-54)/18)])#!
                        if no==False or not((choice in prtks) or (choice in prtls)):
                            display[cellpos[0]][cellpos[1]]=choice
                        break

            if Button(screen,event,mouse,55,5,20,20,BLACK,LBLACK,border=2,bordercolour=DGRAY) == 1:
                choice=1
                break
            if Button(screen,event,mouse,5,5,20,20,LGRAY,LLGRAY,border=2,bordercolour=DGRAY) == 1:
                choice=0
                break

            if Button(screen,event,mouse,30,5,20,20,GRAY,DLGRAY,border=2,bordercolour=DGRAY) == 1:
                choice=2
                break

            if redcount>0 and (choice==3):
                BCOLR=DRED
                choice=1
            if redcount<1:
                BCOLR=DGRAY
            if Button(screen,event,mouse,80,5,20,20,RED,LRED,border=2,bordercolour=BCOLR) == 1 and redcount<1:
                choice=3

            if Button(screen,event,mouse,105,5,20,20,BLUE,LBLUE,border=2,bordercolour=DGRAY) == 1:
                choice=4

            if Button(screen,event,mouse,130,5,20,20,YELLOW,LYELLOW,border=2,bordercolour=DGRAY,shapetype='square',
                      shapex=4,shapey=4,shapehight=12,shapeweight=12,shapecollon=LLGRAY,shapecolloff=LGRAY) == 1:
                choice=locks[choicenum1]

            if choice in locks:
                if 520 <= mouse[0] <= 520 + 20 and 5 <= mouse[1] <= 5 + 20:
                    pygame.draw.rect(screen, DLGRAY, [520, 5, 20, 20])
                    pygame.draw.polygon(screen, BUTTON,
                                        [[520 + 5 - 1, 5 + 10], [520 + 20 - 5, 5 + 1], [520 + 20 - 5, 5 + 20 - 1]])
                else:
                    pygame.draw.rect(screen, GRAY, [520, 5, 20, 20])
                    pygame.draw.polygon(screen, DARKBUTTON,
                                        [[520 + 5 - 1, 5 + 10], [520 + 20 - 5, 5 + 1], [520 + 20 - 5, 5 + 20 - 1]])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 520 <= mouse[0] <= 520 + 20 and 5 <= mouse[1] <= 5 + 20:
                        choicenum1 -= 1
                        if choicenum1 < 0:
                            choicenum1 += 9
                        choice = locks[choicenum1]
                        break

            if choice in locks:
                if 550 <= mouse[0] <= 550+20 and 5 <= mouse[1] <= 5+20:
                    pygame.draw.rect(screen,DLGRAY,[550,5,20,20])
                    pygame.draw.polygon(screen, BUTTON, [[550+20-5,5+10],[550+5-1,5+1],[550+5-1,5+20-1]])
                else:
                    pygame.draw.rect(screen,GRAY,[550,5,20,20])
                    pygame.draw.polygon(screen, DARKBUTTON, [[550+20-5,5+10],[550+5-1,5+1],[550+5-1,5+20-1]])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 550 <= mouse[0] <= 550+20 and 5 <= mouse[1] <= 5+20:
                        choicenum1+=1
                        if choicenum1>8:
                            choicenum1-=9
                        choice = locks[choicenum1]
                        break

            if Button(screen,event,mouse,155,5,20,20,LGRAY,LLGRAY,border=2,bordercolour=DGRAY,shapetype='square',
                      shapex=4,shapey=4,shapehight=12,shapeweight=12,shapecollon=LYELLOW,shapecolloff=YELLOW) == 1:
                choice = keyss[choicenum2]

            if choice in keyss:
                if 520 <= mouse[0] <= 520 + 20 and 5 <= mouse[1] <= 5 + 20:
                    pygame.draw.rect(screen, DLGRAY, [520, 5, 20, 20])
                    pygame.draw.polygon(screen, BUTTON,
                                        [[520 + 5 - 1, 5 + 10], [520 + 20 - 5, 5 + 1], [520 + 20 - 5, 5 + 20 - 1]])
                else:
                    pygame.draw.rect(screen, GRAY, [520, 5, 20, 20])
                    pygame.draw.polygon(screen, DARKBUTTON,
                                        [[520 + 5 - 1, 5 + 10], [520 + 20 - 5, 5 + 1], [520 + 20 - 5, 5 + 20 - 1]])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 520 <= mouse[0] <= 520 + 20 and 5 <= mouse[1] <= 5 + 20:
                        choicenum2 -= 1
                        if choicenum2 < 0:
                            choicenum2 += 9
                        choice = keyss[choicenum2]
                        break

            if choice in keyss:
                if 550 <= mouse[0] <= 550 + 20 and 5 <= mouse[1] <= 5 + 20:
                    pygame.draw.rect(screen, DLGRAY, [550, 5, 20, 20])
                    pygame.draw.polygon(screen, BUTTON,
                                        [[550 + 20 - 5, 5 + 10], [550 + 5 - 1, 5 + 1], [550 + 5 - 1, 5 + 20 - 1]])
                else:
                    pygame.draw.rect(screen, GRAY, [550, 5, 20, 20])
                    pygame.draw.polygon(screen, DARKBUTTON,
                                        [[550 + 20 - 5, 5 + 10], [550 + 5 - 1, 5 + 1], [550 + 5 - 1, 5 + 20 - 1]])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 550 <= mouse[0] <= 550 + 20 and 5 <= mouse[1] <= 5 + 20:
                        choicenum2 += 1
                        if choicenum2 > 8:
                            choicenum2 -= 9
                        choice = keyss[choicenum2]
                        break


            if Button(screen, event, mouse, 180, 5, 20, 20, PURPLE, LPURPLE, border=2, bordercolour=DGRAY,
                      shapetype='circle',
                      shapex=10, shapey=10, shapehight=6, shapeweight=6, shapecollon=LRED, shapecolloff=RED) == 1:
                choice=prtls[choicenumP]

            if (choice in prtls) or (choice in prtks):
                if not (prtls[choicenumP] in portals1):
                    choice = prtls[choicenumP]
                    no=False
                if not (prtks[choicenumP] in portals2):
                    choice = prtks[choicenumP]
                    no=False
                if (prtls[choicenumP] in portals1) and (prtks[choicenumP] in portals2):
                    no=True

            if (choice in prtls) or (choice in prtks):
                if 520 <= mouse[0] <= 520 + 20 and 5 <= mouse[1] <= 5 + 20:
                    pygame.draw.rect(screen, DLGRAY, [520, 5, 20, 20])
                    pygame.draw.polygon(screen, BUTTON,
                                            [[520 + 5 - 1, 5 + 10], [520 + 20 - 5, 5 + 1], [520 + 20 - 5, 5 + 20 - 1]])
                else:
                    pygame.draw.rect(screen, GRAY, [520, 5, 20, 20])
                    pygame.draw.polygon(screen, DARKBUTTON,
                                            [[520 + 5 - 1, 5 + 10], [520 + 20 - 5, 5 + 1], [520 + 20 - 5, 5 + 20 - 1]])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 520 <= mouse[0] <= 520 + 20 and 5 <= mouse[1] <= 5 + 20:
                        choicenumP -= 1
                        if choicenumP < 0:
                            choicenumP += 9
                        choice = prtls[choicenumP]
                        break

            if (choice in prtls) or (choice in prtks):
                if 550 <= mouse[0] <= 550 + 20 and 5 <= mouse[1] <= 5 + 20:
                    pygame.draw.rect(screen, DLGRAY, [550, 5, 20, 20])
                    pygame.draw.polygon(screen, BUTTON,
                                            [[550 + 20 - 5, 5 + 10], [550 + 5 - 1, 5 + 1], [550 + 5 - 1, 5 + 20 - 1]])
                else:
                    pygame.draw.rect(screen, GRAY, [550, 5, 20, 20])
                    pygame.draw.polygon(screen, DARKBUTTON,
                                            [[550 + 20 - 5, 5 + 10], [550 + 5 - 1, 5 + 1], [550 + 5 - 1, 5 + 20 - 1]])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 550 <= mouse[0] <= 550 + 20 and 5 <= mouse[1] <= 5 + 20:
                        choicenumP += 1
                        if choicenumP > 8:
                            choicenumP -= 9
                        choice = prtls[choicenumP]
                        break

            if blackcount==9 and (choice in blaen):
                BCOL=DRED
                choice=1
            if blackcount < 9:
                BCOL=DGRAY
            if Button(screen, event, mouse, 205, 5, 20, 20, LGRAY, LLGRAY, border=2, bordercolour=BCOL,
                      shapetype='rhomb',
                      shapex=1, shapey=1, shapehight=3, shapeweight=3, shapecollon=LBLACK, shapecolloff=BLACK) == 1 and\
                    blackcount<9:
                while True:
                    bl=random.randint(91,99)
                    if not(bl in blacks):
                        break
                choice=bl

            if bluecount==9 and (choice in bluen):
                BCOL1=DRED
                choice=1
            if bluecount<9:
                BCOL1=DGRAY
            if Button(screen, event, mouse, 230, 5, 20, 20, LGRAY, LLGRAY, border=2, bordercolour=BCOL1,
                      shapetype='rhomb',
                      shapex=1, shapey=1, shapehight=3, shapeweight=3, shapecollon=LBLUE, shapecolloff=BLUE) == 1\
                    and bluecount<9:
                while True:
                    bl = random.randint(101, 109)
                    if not (bl in blueks):
                        break
                choice = bl

            if purplecount==9 and (choice in puren):
                BCOL2=DRED
                choice=1
            if purplecount<9:
                BCOL2=DGRAY
            if Button(screen, event, mouse, 255, 5, 20, 20, LGRAY, LLGRAY, border=2, bordercolour=BCOL2,
                      shapetype='rhomb',
                      shapex=1, shapey=1, shapehight=3, shapeweight=3, shapecollon=LPURPLE, shapecolloff=PURPLE) == 1\
                    and purplecount<9:
                while True:
                    bl = random.randint(111, 119)
                    if not (bl in purpes):
                        break
                choice = bl

            screen.blit(Borders, (5, 30))
            on1=Check(screen,event,mouse,90,30,20,20,GRAY,DLGRAY,on1,2,DGRAY)
            if on1 == True:
                for x in range(0, len(display)):
                    display[x][0] = 1
                    display[x][len(display) - 1] = 1
                    display[0][x] = 1
                    display[len(display) - 1][x] = 1
            else:
                for x in range(0, len(display)):
                    display[x][0] = 2
                    display[x][len(display) - 1] = 2
                    display[0][x] = 2
                    display[len(display) - 1][x] = 2

            screen.blit(Blind, (120, 30))
            on2=Check(screen,event,mouse,210,30,20,20,GRAY,DLGRAY,on2,2,DGRAY)

            screen.blit(Reverse, (240, 30))
            on3=Check(screen,event,mouse,340,30,20,20,GRAY,DLGRAY,on3,2,DGRAY)

            Steps = Text('Steps: ' + str(steps), WHITE, 15, 'Arial')
            if Button(screen, event, mouse, 380, 30, 80, 20,GRAY,DLGRAY,Steps,5,1,2,DGRAY) == 1:
                a=int((steps-steps%1000)/1000)
                b=int((steps-steps%100-a*1000)/100)
                c = int((steps - steps % 10 - a * 1000-b*100)/10)
                d = int(steps - a * 1000-b*100-c*10)

                stepsS=size.steps(a,b,c,d,complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2)
                steps=stepsS[0]*1000+stepsS[1]*100+stepsS[2]*10+stepsS[3]
                if steps==0:
                    steps=1
                WIDTH = 612
                HEIGHT = Size * 18 + 55 + 32
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                screenfill(screen, Size)
                choice=1
                pygame.draw.rect(screen, LGREEN, [578, 3, 24, 24])

            if Button(screen,event,mouse,5,Size*18+54+5,180,25,DARKBUTTON,BUTTON,Back,25,5) == 1:
                return 0
            if Button(screen,event,mouse,440,Size*18+54+5,160,25,DARKBUTTON,BUTTON,SAB,25,5) == 1 and redcount==1\
                    and finishcount>0:
                output=['\n']
                while True:
                    timnums = []
                    something=[]
                    br=0
                    levels = os.listdir('customLvls')
                    for i in range(len(levels)):
                        tim = levels[i]
                        tim = tim.split('_')
                        timnums.append(int(tim[1]))
                        something.append([tim[2],tim[3],tim[4]])
                    for i in range(len(timnums)-1):
                        if abs(timnums[i+1]-timnums[i])>1 or ((timnums[i]==min(timnums)) and timnums[i]!=0):
                            os.rename('customLvls\custlv_'+str(timnums[i+1])+'_'+something[i+1][0]+'_'+something[i+1][1]
                                      +'_'+something[i+1][2],'customLvls\custlv_'+str(int(int(timnums[i+1])-1))
                                      +'_'+something[i+1][0]+'_'+something[i+1][1]+'_'+something[i+1][2])
                            br+=1
                            break
                    if br==0:
                        break

                timnums=[]
                levels=os.listdir('customLvls')
                if len(levels)>0:
                    for i in range(len(levels)):
                        tim=levels[i]
                        tim=tim.split('_')
                        timnums.append(tim[1])
                    for i in range(len(levels)+1):
                        if not(str(i) in timnums):
                            Numlvl=int(i)
                            break
                else:
                    Numlvl=0

                f=open('customLvls\custlv_'+str(Numlvl)+'_b'+str(on2)+'_r'+str(on3)+'_s'+str(steps)+'.txt','w')
                for i in range(len(display)):
                    strin='    ,'
                    for n in range(len(display)):
                        if i==n==len(display)-1:
                            strin = strin + str(display[n][i])
                        else:
                            strin=strin+str(display[n][i])+','
                    output.append(strin+'\n')
                f.writelines(output)
                f.close()
                return 0

            if redcount!=1 or finishcount==0:
                screen.blit(photo,(410,Size*18+56))
            else:
                pygame.draw.rect(screen,LGRAY,[410,Size*18+56,24,30])
            if not(choice in locks) and not(choice in keyss) and not(choice in prtls) and not(choice in prtks):
                pygame.draw.rect(screen, LGRAY, [550, 5, 20, 20])
                pygame.draw.rect(screen, LGRAY, [520, 5, 20, 20])

            if event.type == pygame.QUIT:
                Ex(complete2,completecust2,soundloud2,diffuc2,easycomplete2,hardcomplete2)

        bordcol = LGREEN
        if no == False:
            bordcol = LGREEN
        if no == True:
            bordcol = DRED
        if not (choice in prtks) and not (choice in prtls):
            bordcol = LGREEN
        pygame.draw.rect(screen, bordcol, [578, 3, 24, 24])
        texture.texture(choice, screen,580 / 18, 5 / 18, 2)
        for xx in range(0,Size):
            for yy in range(0,Size):
                texture.texture(display,screen,xx,yy,1)
        pygame.display.update()




