import pygame,keyboard,texture,random,redactor,size,os

f=open('playerData.txt','r')
completeI=((f.readline())[10:-2]).split(',')
for i in range(len(completeI)):
    completeI[i]=int(completeI[i])

completecustI=((f.readline())[14:-2]).split(',')
for i in range(len(completecustI)):
    completecustI[i]=int(completecustI[i])

easycompleteI=((f.readline())[14:-2]).split(',')
for i in range(len(easycompleteI)):
    easycompleteI[i]=int(easycompleteI[i])

hardcompleteI=((f.readline())[14:-2]).split(',')
for i in range(len(hardcompleteI)):
    hardcompleteI[i]=int(hardcompleteI[i])

soundloudI=float((f.readline())[10:])
diffucI=int((f.readline())[7:])
f.close()

WIDTH = 613
HEIGHT = 613
FPS = 15

RED=(255,0,0)
YELLOW=(255,255,0)
YYELLOW=(196,196,0)
DYELLOW=(127,127,0)
RRED=(196,0,0)
DRED=(127,0,0)
GGREEN=(0,196,0)
DGREEN=(0,127,0)
BLACK = (0, 0, 0)
LIBLACK=(63,63,63)
GRAY = (128, 128, 128)
LIGRAY=(160,160,160)
LGRAY = (196, 196, 196)
LILGRAY=(245,245,245)
BUTTON= (96,96,96)
DARKBUTTON= (64,64,64)
WHITE = (255, 255, 255)
BRONZE=(51,255,51)
DIAMOND=(255,51,51)
GOLD=(255,255,51)

programIcon = pygame.image.load('images\icon.png')
pygame.display.set_icon(programIcon)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TheGame")
clock = pygame.time.Clock()

display=[[0] * 34 for i in range(34)]

keyboard.add_hotkey("W", lambda:move(0,-1,0,0,-1,-1,3,0,0)) #XV
keyboard.add_hotkey("A", lambda:move(-1,0,0,0,-1,-1,3,0,0)) #XV
keyboard.add_hotkey("S", lambda:move(0,1,0,0,-1,-1,3,0,0)) #XV
keyboard.add_hotkey("D", lambda:move(1,0,0,0,-1,-1,3,0,0)) #XV
keyboard.add_hotkey("SPACE", lambda:move(0,0,0,0,-1,-1,3,0,0)) #XV

keyboard.add_hotkey("R", lambda:restart()) #XV
keyboard.add_hotkey("ESC", lambda:menu()) #X

steps=0
def plstep():
    global steps
    steps-=1

banlist=banNlist=[]
ttype=-1

def move(x,y,flag,enemy,enemyx,enemyy,type,ifp,count):
    global banlist,blind,invers,ttype,banNlist,k,start_ticks
    if menuvalue!=0 and menuvalue!=-1:
        return 0

    if enemy == 0:
        global yourpos,youritems
        X=yourpos[0]
        Y=yourpos[1]
    if enemy == 1:
        X=enemyx
        Y=enemyy

    XX=X+x
    YY=Y+y

    if ((not(XX, YY) in banNlist) and count==1):
        return(0)

    if invers>0 and enemy==0 and ifp==0:
        move(-x,-y,0,0,-1,-1,3,1,0)
        return(0)

    if display[XX][YY]==1 and enemy==0:
        restart()
        return 0
    outf=0

    if display[XX][YY]==0:
        outf=1
    if display[XX][YY] in keyss and enemy == 0:
        youritems.append(display[XX][YY])
        outf=1
    if display[XX][YY] in locks and enemy==0:
        if display[XX][YY]-1 in youritems:
            ttii=youritems.index(display[XX][YY]-1)
            youritems.pop(ttii)
            outf=1

    if (display[XX][YY]==3 and display[enemyx][enemyy] in blaen and enemy==1) \
            or (display[XX][YY] in blaen and enemy==0):
        restart()
        return 0

    if (display[XX][YY]==3 and display[enemyx][enemyy] in bluen and enemy==1):
        display[enemyx][enemyy] = 0
        invers=invers+random.randint(10,20)
    if display[XX][YY] in bluen and enemy==0:
        display[XX][YY]=0
        outf=1
        invers=invers+random.randint(10,20)

    if (display[XX][YY]==3 and display[enemyx][enemyy] in puren and enemy==1):
        display[enemyx][enemyy] = 0
        blind=blind+random.randint(10,20)
    if display[XX][YY] in puren and enemy==0:
        display[XX][YY]=0
        outf=1
        blind=blind+random.randint(10,20)

    if display[XX][YY] in prtls and flag==0:
        for i in range(0,len(display)):
            for n in range(0,len(display[i])):
                if display[i][n]==display[XX][YY]+10:
                    if enemy==0:
                        move(i-yourpos[0]+x,n-yourpos[1]+y,1,enemy,enemyx,enemyy,type,ifp,count)
                        return 0
                    else:
                        banlist.append((i+x,n+y))
                        move(i-enemyx+x,n-enemyy+y,1,enemy,enemyx,enemyy,type,0,count)
                        return 0
    if display[XX][YY] in prtks and flag==0:
        for i in range(0,len(display)):
            for n in range(0,len(display[i])):
                if display[i][n]==display[XX][YY]-10:
                    if enemy==0:
                        move(i-yourpos[0]+x,n-yourpos[1]+y,1,enemy,enemyx,enemyy,type,ifp,count)
                        return 0
                    else:
                        banlist.append((i+x,n+y))
                        move(i-enemyx+x,n-enemyy+y,1,enemy,enemyx,enemyy,type,0,count)
                        return 0

    minus=0
    if x==0 and y==0 and enemy==0 and outf == 0:
        minus=1
        outf=1

    if invers>0 and enemy==0 and outf==1 and minus==0:
        invers = invers - inverscur

    if outf==1 and enemy==0 and minus==0:
        display[XX][YY] = type
        display[X][Y] = 0
        if enemy == 0:
            yourpos[0] = XX
            yourpos[1] = YY
    if outf==1 and enemy==1 and not((enemyx+XX,enemyy+YY)) in banlist:
        display[XX][YY] = type
        display[X][Y] = 0
        if enemy == 0:
            yourpos[0] = XX
            yourpos[1] = YY

    if ((outf==1 or flag==1) and enemy==0) or (count==1):
        if count==0:
            banlist=banNlist=[]
        for XXX in range(0,34):
            for YYY in range(0,34):
                if ((display[XXX][YYY] in blaen or display[XXX][YYY] in bluen or display[XXX][YYY]\
                    in puren) and not((XXX, YYY) in banlist)) or ((display[XXX][YYY]==ttype and count==1)\
                        and ((XXX,YYY) in banNlist)):
                    nnn=0
                    while True:
                        nnn+=1
                        if ((display[XXX][YYY] in blaen or puren or bluen) and count==1)\
                                or (display[XXX][YYY] in blaen):
                            while True:
                                randomovex=random.randint(-1,1)
                                randomovey=random.randint(-1,1)
                                if not(randomovex==0 and randomovey==0):
                                    break
                        else:
                            randomovex = random.randint(-1, 1)
                            randomovey = random.randint(-1, 1)

                        if not((randomovex,randomovey) in bancomb) or (randomovex==0 and randomovey==0):
                            if display[XXX+randomovex][YYY+randomovey] == 0 or display[XXX+randomovex][YYY+randomovey]\
                                    in prtks or display[XXX+randomovex][YYY+randomovey] in prtls or \
                                    display[XXX+randomovex][YYY+randomovey] == 3 or \
                                    display[XXX+randomovex][YYY+randomovey]==display[XXX][YYY]:
                                break
                        if nnn>=100:
                            randomovex=randomovey=0
                            break

                    banlist.append((XXX+randomovex,YYY+randomovey))
                    if count==0 and (display[XXX][YYY] in puren or display[XXX][YYY] in bluen):
                        ttype=display[XXX][YYY]
                        banNlist.append((XXX + randomovex, YYY + randomovey))
                        move(randomovex,randomovey,0,1,XXX,YYY,display[XXX][YYY],0,1)
                        ttype = -1
                    if (((count==1) and (display[XXX][YYY] in puren or display[XXX][YYY] in bluen))\
                            and ttype==display[XXX][YYY]):
                        banNlist.append((XXX+randomovex,YYY+randomovey))
                        move(randomovex, randomovey, 0, 1, XXX, YYY, display[XXX][YYY], 0,2)
                        banNlist = []
                        ttype = -1
                    if (display[XXX][YYY] in blaen) and count==0:
                        move(randomovex, randomovey, 0, 1, XXX, YYY, display[XXX][YYY], 0, 2)

    if outf==1 and k==0:
        start_ticks = pygame.time.get_ticks()
        k=1
    if display[XX][YY]==4 and enemy == 0:
        if menuvalue==0:
            if not(levelcount-1 in easycomplete) and diffuc==1:
                easycomplete.append(levelcount - 1)
            if not (levelcount - 1 in complete) and diffuc == 2:
                complete.append(levelcount - 1)
            if not(levelcount-1 in hardcomplete) and diffuc==3:
                hardcomplete.append(levelcount - 1)
            nextlvl(0)
        if menuvalue==-1:
            if not(levelcountcust-1 in completecust):
                completecust.append(levelcountcust-1)
            nextlvl(0)
    if blind==0:
        texture.update(display,screen,0,0)
    if blind>0 and enemy==0 and outf==1 and minus==0:
        blind=blind-blindcur
        texture.update(display, screen, 1,0)
    if blind > 0 and enemy == 0 and outf == 1 and minus == 1:
        texture.update(display, screen, 1,0)
    if outf==1 and enemy==0 and minus==0:
        plstep()

def restart():
    global levelcount,blind,invers,levelcountcust,timer,k
    if (menuvalue!=0) and (menuvalue!=-1):
        return 0

    blind=invers=0
    if menuvalue==0:
        levelcount=levelcount-1
    if menuvalue==-1:
        levelcountcust = levelcountcust - 1
    nextlvl(1)
    k = 0

def nextlvl(trig):
    global levelcount,lv,blind,invers,blindcur,inverscur,blind,invers,steps,running,menuvalue,levelcountcust,timer,\
        start_ticks,k
    if menuvalue==0:
        lc=levelcount
    if menuvalue==-1:
        lc=levelcountcust

    timer = hardtime[levelcount]

    if lc==9 and trig==0 and lc==levelcount:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("music\ingame2.mp3")
        pygame.mixer.music.play(-1)


    if menuvalue == 0:
        steps=stepss[levelcount]
    if menuvalue == -1:
        steps = stepsscust[levelcountcust]

    filename=''
    blind=invers=0
    for i in range(0,34):
        for n in range(0,34):
            display[i][n]=0
    if menuvalue==0:
        filename='levels\level_'+str(levelcount)+'.txt'
    if menuvalue==-1:
        kist=os.listdir('customLvls')
        for u in range(len(kist)):
            filename='custlv_'+str(levelcountcust)
            if filename in kist[u]:
                filename='customLvls\\'+kist[u]
                break
    try:
        levels=open(filename)
    except:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("music\mainmenu.mp3")
        pygame.mixer.music.play(-1)
        if menuvalue==0:
            menuvalue=2
        if menuvalue==-1:
            menuvalue=8
        return 0
    lv=levels.read()
    levels.close()

    if menuvalue==0:
        if levelcount in blcurlvl:
            blindcur1=1
            blind=0
        else:
            blindcur=1
            blindcur1=0
            blind=0
        if levelcount in incurlvl:
            inverscur=0
            invers=1
        else:
            inverscur=1
            invers=0
    if menuvalue==-1:
        if levelcountcust in blcurlvlcust:
            blindcur1=1
            blind=0
        else:
            blindcur=1
            blindcur1=0
            blind=0
        if levelcountcust in incurlvlcust:
            inverscur=0
            invers=1
        else:
            inverscur=1
            invers=0

    levelgen()
    texture.update(display,screen,blind,0)
    if menuvalue==0:
        levelcount+=1
    if menuvalue==-1:
        levelcountcust+=1
    if blindcur1==1:
        blindcur=0
        blind=1
    k = 0

def levelgen():
    #edit lvl format
    lvunp=lv.split(',')
    kkount=-1
    while True:
        kkount=kkount+1
        try:
            if lvunp[kkount]=='\n    ':
                lvunp.pop(kkount)
        except:
            break
    lenlvunp=int(len(lvunp)**0.5)
    lvunp1=[[0] * lenlvunp for i in range(lenlvunp)]
    for i in range(0,lenlvunp):
        for n in range(0,lenlvunp):
            lvunp1[i].append(lvunp[n+(i*lenlvunp)])
            lvunp1[i].pop(0)
    lvunp=lvunp1

    #determine special cells
    global yourpos,youritems
    for i in range(0,len(lvunp)):
        for n in range(0,len(lvunp[i])):
            #player position
            if lvunp[i][n]=='3':
                yourpos=[n,i]

    youritems=[]
    #level generation
    for i in range(0,len(lvunp)):
        for n in range(0,len(lvunp[i])):
            display[n][i]=int(lvunp[i][n])

def menu():
    global menuvalue
    if (not(menuvalue)==0) and (not(menuvalue)==-1) and (not(menuvalue)==-2):
        return 0

    pygame.mixer.music.stop()
    pygame.mixer.music.load("music\mainmenu.mp3")
    pygame.mixer.music.play(-1)

    screenfill()
    if menuvalue==0:
        menuvalue=2
    if menuvalue==-1:
        menuvalue=8
    if menuvalue==-2:
        menuvalue=1

def screenfill():
    screen.fill(LGRAY)
    for i in range(0,640,18):
        pygame.draw.rect(screen, GRAY, [i, 0, 1, 620], 1)
    for i in range(0,640,18):
        pygame.draw.rect(screen, GRAY, [0, i, 620, 1], 1)
    for i in range(0,640,36):
        pygame.draw.rect(screen, BLACK, [i, 0, 1, 620], 1)
    for i in range(0,640,36):
        pygame.draw.rect(screen, BLACK, [0, i, 620, 1], 1)

#input data
keyss=[51,53,55,57,59,61,63,65,67]
locks=[52,54,56,58,60,62,64,66,68]
prtls=[71,72,73,74,75,76,77,78,79]
prtks=[81,82,83,84,85,86,87,88,89]
blaen=[91,92,93,94,95,96,97,98,99]
bluen=[101,102,103,104,105,106,107,108,109]
puren=[111,112,113,114,115,116,117,118,119]
bancomb=[(2,2),(2,1),(2,-1),(2,-2),(1,2),(1,1),(1,-1),(1,-2),(-1,2),(-1,1),(-1,-1),(-1,-2),(-2,2),(-2,1),(-2,-1),
         (-2,-2)]
#later
diffuc=diffucI

#100-x+1

countlevels=len(os.listdir('levels'))
resstepss=[4,7,18,41,41,55,136,95,72,166,105,342,108,174,260,-1]
resblcurlvl=[3,6,8,12,14]
resincurlvl=[1,5,6,10,14]
easystepss=[5,8,20,46,46,61,150,105,80,173,116,379,119,192,286,-1]
easyblcurlvl=[3,14]
easyincurlvl=[6,8]
hardblcurlvl=[1,2,3,5,6,7,8,11,12,14]
hardincurlvl=[0,1,3,6,5,6,9,10,14]
#for diffucult

hardtime=[1,1,3,8,7,12,15,21,21,42,22,78,39,95,69,-1]
#always in code, only hard

if diffuc==2:
    stepss=resstepss
    blcurlvl=resblcurlvl
    incurlvl=resincurlvl
if diffuc==3:
    stepss=resstepss
    blcurlvl=hardblcurlvl
    incurlvl=hardincurlvl
if diffuc==1:
    stepss=easystepss
    blcurlvl=easyblcurlvl
    incurlvl=easyincurlvl

blind=invers=0
levelcount=0
blindcur=inverscur=1

complete=completeI
easycomplete=easycompleteI
hardcomplete=hardcompleteI

completecust=completecustI

yourpos=[]
running = True
menuvalue=-2
menu()

#Game block
#nextlvl(1)
screenfill()
texture.update(display,screen,0,menuvalue)

bigfont1 = pygame.font.SysFont('Arial', 50)
smallfont = pygame.font.SysFont('Corbel', 35)
bigfont = pygame.font.SysFont('Corbel', 50)
ssmallfont=pygame.font.SysFont('Arial', 20)
ultrasmall=pygame.font.SysFont('Arial', 15)
Ssmallfont = pygame.font.SysFont('Corbel', 25)

exitt = smallfont.render('Save and exit', True, WHITE)
levelss=smallfont.render('Levels', True, WHITE)
guide=smallfont.render('Guide', True, WHITE)
MMeenn=bigfont.render('Game v1.0', True, WHITE)
MMeenn2=bigfont.render('Game v1.0', True, BLACK)
Back=smallfont.render('Back', True, WHITE)
Next=smallfont.render('Next', True, WHITE)
BackToMenu=smallfont.render('Back to menu', True, WHITE)
Credits=smallfont.render('???', True, WHITE)
Credits1=smallfont.render('Credits', True, WHITE)
Settings=smallfont.render('Settings', True, WHITE)
Music=bigfont.render('Music', True, WHITE)
Music1=bigfont.render('Music',True, BLACK)
reset=smallfont.render('Reset progress',True, BLACK)
reset1=smallfont.render('Reset progress',True, WHITE)
diff=smallfont.render('difficulty', True, WHITE)
diff1=smallfont.render('difficulty', True, BLACK)
normal=smallfont.render('normal', True, WHITE)
easy=smallfont.render('easy', True, WHITE)
hard=smallfont.render('hard', True, WHITE)
Rem=Ssmallfont.render('Remove golden border', True, WHITE)

redactor1=smallfont.render('Redactor', True, WHITE)
create=smallfont.render('Create level', True, WHITE)
mylevels=smallfont.render('Custom levels', True, WHITE)

nnormal=smallfont.render('normal', True, WHITE)
nnormal1=smallfont.render('normal', True, BLACK)
eeasy=smallfont.render('easy', True, WHITE)
eeasy1=smallfont.render('easy', True, BLACK)
hhard=smallfont.render('hard', True, WHITE)
hhard1=smallfont.render('hard', True, BLACK)

text1=bigfont.render('You complete this game.', True, BLACK)
text11=bigfont.render('You complete this game.', True, WHITE)
text2=bigfont.render('Programmer: z6yn3k', True, BLACK)
text21=bigfont.render('Programmer: z6yn3k', True, WHITE)
text3=bigfont.render('Composer: metafel4a', True, BLACK)
text31=bigfont.render('Composer: metafel4a', True, WHITE)
text4=bigfont.render('Thanks for playing!', True, BLACK)
text41=bigfont.render('Thanks for playing!', True, WHITE)

icon1 = pygame.image.load("images\musicon.png")
photo = pygame.image.load("images\lock.png")
lcountt=1
soundloud=soundloudI
pygame.mixer.music.set_volume(soundloud)

countlevelscust = len(os.listdir('customLvls'))
stepsscust = []
blcurlvlcust = []
incurlvlcust = []
timnums = []
timer=0
k=0

leveLs = os.listdir('customLvls')
if len(leveLs) > 0:
    for i in range(len(leveLs)):
        tim = leveLs[i]
        tim = tim.split('_')
        stepsscust.append(int((tim[4])[1:-4]))
        if tim[2] == 'bTrue':
            blcurlvlcust.append(int((tim[1])))
        if tim[3] == 'rTrue':
            incurlvlcust.append(int((tim[1])))
stepsscust.append(-1)

weg=30
hig=50
kount=0

def Ex():
    f=open('playerData.txt','w')
    TexT=[]
    TexT.append('complete='+str(complete)+'\n')
    TexT.append('completecust='+str(completecust)+'\n')
    TexT.append('easycomplete=' + str(easycomplete) + '\n')
    TexT.append('hardcomplete=' + str(hardcomplete) + '\n')
    TexT.append('soundloud='+str(soundloud)+'\n')
    TexT.append('diffuc='+str(diffuc))
    f.writelines(TexT)
    f.close()
    pygame.quit()
    exit()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if menuvalue==1:
            screen.blit(MMeenn2, (weg + 335, hig-10 + 5))
            screen.blit(MMeenn, (weg + 337, hig-10 + 7))
            pygame.display.set_caption('Menu')

            mouse = pygame.mouse.get_pos()
            if weg <= mouse[0] <= weg + 240 and hig+240 <= mouse[1] <= hig+240 + 40:
                pygame.draw.rect(screen, BUTTON, [weg , hig+240 , 240, 40])
                screen.blit(exitt, (weg+15 , hig+240+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig+240, 240, 40])
                screen.blit(exitt, (weg+15 , hig+240+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 240 and hig+240 <= mouse[1] <= hig+240 + 40:
                    Ex()

            if weg <= mouse[0] <= weg + 140 and hig <= mouse[1] <= hig + 40:
                pygame.draw.rect(screen, BUTTON, [weg , hig , 140, 40])
                screen.blit(levelss, (weg+15 , hig+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig, 140, 40])
                screen.blit(levelss, (weg+15 , hig+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig <= mouse[1] <= hig + 40:
                    menuvalue=2
                    screenfill()
                    break

            if weg <= mouse[0] <= weg + 140 and hig+60 <= mouse[1] <= hig+60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg , hig+60 , 140, 40])
                screen.blit(guide, (weg+15 , hig+60+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig+60, 140, 40])
                screen.blit(guide, (weg+15 , hig+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig+60 <= mouse[1] <= hig+60 + 40:
                    menuvalue=3 #open file
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\guide.mp3")
                    pygame.mixer.music.play(-1)
                    screenfill()
                    break

            if weg <= mouse[0] <= weg + 140 and hig+120 <= mouse[1] <= hig+120 + 40:
                pygame.draw.rect(screen, BUTTON, [weg , hig+120 , 140, 40])
                screen.blit(Settings, (weg+15 , hig+120+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig+120, 140, 40])
                screen.blit(Settings, (weg+15 , hig+120+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig+120 <= mouse[1] <= hig+120 + 40:
                    menuvalue=4
                    screenfill()
                    break

            if len(complete)-1 != countlevels:
                Credits2=Credits
            else:
                Credits2=Credits1
            if weg <= mouse[0] <= weg + 140 and hig+180 <= mouse[1] <= hig+180 + 40:
                pygame.draw.rect(screen, BUTTON, [weg , hig+180 , 140, 40])
                screen.blit(Credits2, (weg+15 , hig+180+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig+180, 140, 40])
                screen.blit(Credits2, (weg+15 , hig+180+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig+180 <= mouse[1] <= hig+180 + 40:
                    if len(complete)-1 == countlevels:
                        menuvalue=5
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("music\credits.mp3")
                        pygame.mixer.music.play(-1)
                        screenfill()
                    break
            if len(complete)-1 != countlevels:
                screen.blit(photo, (weg + 15 + 135, hig + 174 + 5))
                lvlcounter=ultrasmall.render((str(countlevels-len(complete)+1)), True, WHITE)
                if len(str(countlevels-len(complete)+1))==2:
                    screen.blit(lvlcounter, (weg + 15 + 135+10, hig + 174 + 5+21))
                else:
                    screen.blit(lvlcounter, (weg + 15 + 135 + 14, hig + 174 + 5 + 21))

        if menuvalue == 2:
            pygame.display.set_caption('Levels')
            mouse = pygame.mouse.get_pos()

            for y in range(18,600,54):
                for x in range(18, 600, 54):
                    levelc = int(((y - 18) / 54) * 11 + ((x - 18) / 54))
                    levelnum = ssmallfont.render(str(levelc), True, WHITE)

                    if len(str(levelc))==1:
                        if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                            if levelc in easycomplete and diffuc==1:
                                pygame.draw.rect(screen, BRONZE, [x - 2, y - 2, 40, 40])
                            if levelc in complete and diffuc==2:
                                pygame.draw.rect(screen, GOLD, [x-2, y-2, 40, 40])
                            if levelc in hardcomplete and diffuc==3:
                                pygame.draw.rect(screen, DIAMOND, [x-2, y-2, 40, 40])
                            pygame.draw.rect(screen, DARKBUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, BUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x + 13, y + 6))
                        else:
                            if levelc in easycomplete and diffuc==1:
                                pygame.draw.rect(screen, BRONZE, [x - 2, y - 2, 40, 40])
                            if levelc in complete and diffuc==2:
                                pygame.draw.rect(screen, GOLD, [x-2, y-2, 40, 40])
                            if levelc in hardcomplete and diffuc==3:
                                pygame.draw.rect(screen, DIAMOND, [x-2, y-2, 40, 40])
                            pygame.draw.rect(screen, BUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, DARKBUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x + 13, y + 6))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                                menuvalue=0
                                levelcount=levelc

                    if len(str(levelc))==2 and levelc<countlevels:
                        if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                            if levelc in easycomplete and diffuc==1:
                                pygame.draw.rect(screen, BRONZE, [x - 2, y - 2, 40, 40])
                            if levelc in complete and diffuc==2:
                                pygame.draw.rect(screen, GOLD, [x-2, y-2, 40, 40])
                            if levelc in hardcomplete and diffuc==3:
                                pygame.draw.rect(screen, DIAMOND, [x-2, y-2, 40, 40])
                            pygame.draw.rect(screen, DARKBUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, BUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x+9,y+6))
                        else:
                            if levelc in easycomplete and diffuc==1:
                                pygame.draw.rect(screen, BRONZE, [x - 2, y - 2, 40, 40])
                            if levelc in complete and diffuc==2:
                                pygame.draw.rect(screen, GOLD, [x-2, y-2, 40, 40])
                            if levelc in hardcomplete and diffuc==3:
                                pygame.draw.rect(screen, DIAMOND, [x-2, y-2, 40, 40])
                            pygame.draw.rect(screen, BUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, DARKBUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x+9,y+6))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                                menuvalue=0
                                levelcount = levelc

            if diffuc==2:
                Comlvl = bigfont1.render((str(len(complete)-1) + '/' + str(countlevels)), True, WHITE)
                Comlvl1 = bigfont1.render((str(len(complete)-1) + '/' + str(countlevels)), True, BLACK)
            if diffuc==3:
                Comlvl = bigfont1.render((str(len(hardcomplete)-1) + '/' + str(countlevels)), True, WHITE)
                Comlvl1 = bigfont1.render((str(len(hardcomplete)-1) + '/' + str(countlevels)), True, BLACK)
            if diffuc==1:
                Comlvl = bigfont1.render((str(len(easycomplete)-1) + '/' + str(countlevels)), True, WHITE)
                Comlvl1 = bigfont1.render((str(len(easycomplete)-1) + '/' + str(countlevels)), True, BLACK)
            screen.blit(Comlvl1, (488, 498))
            screen.blit(Comlvl, (490, 500))

            if weg+160 <= mouse[0] <= weg + 240+160 and hig+400+60 <= mouse[1] <= hig+400+60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg+160 , hig+400+60 , 240, 40])
                screen.blit(redactor1, (weg+25+160 , hig+400+60+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+160, hig+400+60, 240, 40])
                screen.blit(redactor1, (weg+25+160 , hig+400+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+160 <= mouse[0] <= weg+160 + 240 and hig+400+60 <= mouse[1] <= hig+400+60 + 40:
                    screenfill()
                    menuvalue=7
                    break

            if weg <= mouse[0] <= weg + 140 and hig+400+60 <= mouse[1] <= hig+400+60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg , hig+400+60 , 140, 40])
                screen.blit(Back, (weg+25 , hig+400+60+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig+400+60, 140, 40])
                screen.blit(Back, (weg+25 , hig+400+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig+400+60 <= mouse[1] <= hig+400+60 + 40:
                    screenfill()
                    menuvalue=1

            if menuvalue==0:
                timer=hardtime[levelcount]
                if levelcount in [0,1,2,3,4,5,6,7,8]:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\ingame.mp3")
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\ingame2.mp3")
                    pygame.mixer.music.play(-1)

                nextlvl(0)
                screenfill()
                texture.update(display, screen, 0, menuvalue)

        if menuvalue==3:
            pygame.display.set_caption('Guide')
            mouse = pygame.mouse.get_pos()
            slide = pygame.image.load("images\slide"+str(kount)+'.png')
            screen.blit(slide,(1,1))

            if weg+440 <= mouse[0] <= weg+440 + 140 and hig+460+60 <= mouse[1] <= hig+460+60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg+440 , hig+460+60 , 140, 40])
                screen.blit(Next, (weg+440+25 , hig+460+60+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+440, hig+460+60, 140, 40])
                screen.blit(Next, (weg+440+25 , hig+460+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+440 <= mouse[0] <= weg+440 + 140 and hig+460+60 <= mouse[1] <= hig+460+60 + 40:
                    kount+=1

            if weg+280 <= mouse[0] <= weg+280 + 140 and hig+460+60 <= mouse[1] <= hig+460+60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg+280 , hig+460+60 , 140, 40])
                screen.blit(Back, (weg+280+25 , hig+460+60+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+280, hig+460+60, 140, 40])
                screen.blit(Back, (weg+280+25 , hig+460+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+280 <= mouse[0] <= weg+280 + 140 and hig+460+60 <= mouse[1] <= hig+460+60 + 40:
                    kount-=1

            if weg-20 <= mouse[0] <= weg-20 + 280 and hig+460+60 <= mouse[1] <= hig+460+60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg-20 , hig+460+60 , 280, 40])
                screen.blit(BackToMenu, (weg-20+25 , hig+460+60+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg-20, hig+460+60, 280, 40])
                screen.blit(BackToMenu, (weg-20+25 , hig+460+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg-20 <= mouse[0] <= weg-20 + 280 and hig+460+60 <= mouse[1] <= hig+460+60 + 40:
                    screenfill()
                    menuvalue=1
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\mainmenu.mp3")
                    pygame.mixer.music.play(-1)
                    kount = 0

            if kount>30 or kount<0:
                screenfill()
                menuvalue=1
                pygame.mixer.music.stop()
                pygame.mixer.music.load("music\mainmenu.mp3")
                pygame.mixer.music.play(-1)
                kount = 0
                break

        if menuvalue == 4:
            timtime=size.setting(screen,diffuc,soundloud,complete,completecust,soundloud,diffuc,easycomplete,
                                 hardcomplete)

            menuvalue=timtime[0]
            if timtime[1]!=-1:
                complete=[-1]
                easycomplete=[-1]
                hardcomplete=[-1]
                diffuc=2
            if timtime[2]!=-1:
                soundloud=timtime[2]
            if timtime[3]!=-1:
                completecust=[-1]
            pygame.mixer.music.set_volume(soundloud)

        if menuvalue == 5:
            screen.blit(text1, (weg + 23, hig + 3))
            screen.blit(text11, (weg + 25, hig + 5))
            screen.blit(text2, (weg + 23, hig + 3+60))
            screen.blit(text21, (weg + 25, hig + 5+60))
            screen.blit(text3, (weg + 23, hig + 3+120))
            screen.blit(text31, (weg + 25, hig + 5+120))
            screen.blit(text4, (weg + 23, hig + 3+180))
            screen.blit(text41, (weg + 25, hig + 5+180))

            pygame.display.set_caption('Credits')
            mouse = pygame.mouse.get_pos()
            if weg <= mouse[0] <= weg + 140 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg, hig + 400 + 60, 140, 40])
                screen.blit(Back, (weg + 25, hig + 400 + 60 + 5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig + 400 + 60, 140, 40])
                screen.blit(Back, (weg + 25, hig + 400 + 60 + 5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                    screenfill()
                    menuvalue = 1
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\mainmenu.mp3")
                    pygame.mixer.music.play(-1)
                    break

        if menuvalue == 6:
            pygame.display.set_caption('Difficulty')
            mouse = pygame.mouse.get_pos()

            if weg+155 <= mouse[0] <= weg+155 + 190 and hig + 120 <= mouse[1] <= hig + 120+40:
                pygame.draw.rect(screen, BUTTON, [weg+155, hig + 120, 190, 40])
                screen.blit(easy, (weg + 155+25, hig+120+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+155, hig + 120, 190, 40])
                screen.blit(easy, (weg + 155+25, hig+120+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+155 <= mouse[0] <= weg+155 + 190 and hig + 120 <= mouse[1] <= hig + 120+40:
                    screenfill()
                    menuvalue = 4
                    diffuc = 1

                    blcurlvl = easyblcurlvl
                    incurlvl = easyincurlvl
                    stepss = easystepss
                    break

            if weg+155 <= mouse[0] <= weg+155 + 190 and hig + 120+60 <= mouse[1] <= hig + 120+40+60:
                pygame.draw.rect(screen, BUTTON, [weg+155, hig + 120+60, 190, 40])
                screen.blit(normal, (weg + 155+25, hig+120+5+60))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+155, hig + 120+60, 190, 40])
                screen.blit(normal, (weg + 155+25, hig+120+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+155 <= mouse[0] <= weg+155 + 190 and hig + 120+60 <= mouse[1] <= hig + 120+60+40:
                    screenfill()
                    menuvalue = 4
                    diffuc = 2

                    stepss = resstepss
                    blcurlvl = resblcurlvl
                    incurlvl = resincurlvl
                    break

            if weg+155 <= mouse[0] <= weg+155 + 190 and hig + 120+120 <= mouse[1] <= hig + 120+120+40:
                pygame.draw.rect(screen, BUTTON, [weg+155, hig + 120+120, 190, 40])
                screen.blit(hard, (weg + 155+25, hig+120+5+120))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+155, hig + 120+120, 190, 40])
                screen.blit(hard, (weg + 155+25, hig+120+120+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+155 <= mouse[0] <= weg+155 + 190 and hig+120 + 120 <= mouse[1] <= hig+120 + 120+40:
                    if countlevels == len(complete) - 1:
                        screenfill()
                        menuvalue = 4
                        diffuc=3

                        blcurlvl=hardblcurlvl
                        incurlvl=hardincurlvl
                        stepss = resstepss
                        break
            if len(complete) - 1 != countlevels:
                screen.blit(photo, (weg + 155+200, hig + 236))
                lvlcounter = ultrasmall.render((str(countlevels - len(complete) + 1)), True, WHITE)
                if len(str(countlevels - len(complete) + 1)) == 2:
                    screen.blit(lvlcounter, (weg + 155+200 + 10, hig + 236 + 21))
                else:
                    screen.blit(lvlcounter, (weg + 155+200 + 14, hig + 236 + 21))


        if menuvalue==7:
            pygame.display.set_caption('Redactor')
            mouse = pygame.mouse.get_pos()
            countlevelscust = len(os.listdir('customLvls'))

            if weg+155 <= mouse[0] <= weg+155 + 230 and hig + 120 <= mouse[1] <= hig + 120+40:
                pygame.draw.rect(screen, BUTTON, [weg+155, hig + 120, 230, 40])
                screen.blit(create, (weg + 155+25, hig+120+5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+155, hig + 120, 230, 40])
                screen.blit(create, (weg + 155+25, hig+120+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+155 <= mouse[0] <= weg+155 + 230 and hig + 120 <= mouse[1] <= hig + 120+40:
                    pygame.mixer.music.stop()
                    screenfill()
                    redactor.main(complete,completecust,soundloud,diffuc,easycomplete,hardcomplete)

                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\mainmenu.mp3")
                    pygame.mixer.music.play(-1)
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    screenfill()

                    countlevelscust = len(os.listdir('customLvls'))
                    stepsscust=[]
                    blcurlvlcust=[]
                    incurlvlcust=[]
                    timnums=[]
                    leveLs = os.listdir('customLvls')
                    if len(leveLs) > 0:
                        for i in range(len(leveLs)):
                            tim = leveLs[i]
                            tim = tim.split('_')
                            stepsscust.append(int((tim[4])[1:-4]))
                            if tim[2] == 'bTrue':
                                blcurlvlcust.append(int((tim[1])))
                            if tim[3] == 'rTrue':
                                incurlvlcust.append(int((tim[1])))
                    stepsscust.append(-1)
                    break


            if weg+155 <= mouse[0] <= weg+155 + 230 and hig + 120+60 <= mouse[1] <= hig + 120+40+60:
                pygame.draw.rect(screen, BUTTON, [weg+155, hig + 120+60, 230, 40])
                screen.blit(mylevels, (weg + 155+25, hig+120+5+60))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+155, hig + 120+60, 230, 40])
                screen.blit(mylevels, (weg + 155+25, hig+120+60+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+155 <= mouse[0] <= weg+155 + 230 and hig + 120+60 <= mouse[1] <= hig + 120+60+40:

                    while True:
                        timnums = []
                        something = []
                        br = 0
                        levells = os.listdir('customLvls')
                        for i in range(len(levells)):
                            tim = levells[i]
                            tim = tim.split('_')
                            timnums.append(int(tim[1]))
                            something.append([tim[2], tim[3], tim[4]])
                        for i in range(len(timnums) - 1):
                            if abs(timnums[i + 1] - timnums[i]) > 1 or ((timnums[i]==min(timnums)) and timnums[i]!= 0):
                                os.rename('customLvls\custlv_' + str(timnums[i + 1]) + '_' + something[i + 1][0] + '_'
                                          + something[i + 1][1]
                                          + '_' + something[i + 1][2],
                                          'customLvls\custlv_' + str(int(int(timnums[i + 1]) - 1))
                                          + '_' + something[i + 1][0] + '_' + something[i + 1][1] + '_' +
                                          something[i + 1][2])
                                br += 1
                                break
                        if br == 0:
                            break

                    countlevelscust = len(os.listdir('customLvls'))
                    stepsscust=[]
                    blcurlvlcust=[]
                    incurlvlcust=[]
                    timnums=[]
                    leveLs = os.listdir('customLvls')
                    if len(leveLs) > 0:
                        for i in range(len(leveLs)):
                            tim = leveLs[i]
                            tim = tim.split('_')
                            stepsscust.append(int((tim[4])[1:-4]))
                            if tim[2] == 'bTrue':
                                blcurlvlcust.append(int((tim[1])))
                            if tim[3] == 'rTrue':
                                incurlvlcust.append(int((tim[1])))
                    stepsscust.append(-1)

                    screenfill()
                    menuvalue = 8
                    break

            if weg+155 <= mouse[0] <= weg+155 + 230 and hig + 120+120 <= mouse[1] <= hig + 120+120+40:
                pygame.draw.rect(screen, BUTTON, [weg+155, hig + 120+120, 230, 40])
                screen.blit(Back, (weg + 155+25, hig+120+5+120))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+155, hig + 120+120, 230, 40])
                screen.blit(Back, (weg + 155+25, hig+120+120+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+155 <= mouse[0] <= weg+155 + 230 and hig+120 + 120 <= mouse[1] <= hig+120 + 120+40:
                    screenfill()
                    menuvalue = 2
                    break

        if menuvalue == 8:

            pygame.display.set_caption('Mylevels')
            mouse = pygame.mouse.get_pos()

            for y in range(18,600,54):
                for x in range(18, 600, 54):
                    levelc = int(((y - 18) / 54) * 11 + ((x - 18) / 54))
                    levelnum = ssmallfont.render(str(levelc), True, WHITE)

                    if len(str(levelc))==1 and levelc<countlevelscust:
                        if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                            if levelc in completecust:
                                pygame.draw.rect(screen, YELLOW, [x-2, y-2, 40, 40])
                            pygame.draw.rect(screen, DARKBUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, BUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x + 13, y + 6))
                        else:
                            if levelc in completecust:
                                pygame.draw.rect(screen, YELLOW, [x - 2, y - 2, 40, 40])
                            pygame.draw.rect(screen, BUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, DARKBUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x + 13, y + 6))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                                menuvalue=-1
                                levelcountcust=levelc

                    if len(str(levelc))==2 and levelc<countlevelscust:
                        if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                            if levelc in completecust:
                                pygame.draw.rect(screen, YELLOW, [x-2, y-2, 40, 40])
                            pygame.draw.rect(screen, DARKBUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, BUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x+9,y+6))
                        else:
                            if levelc in completecust:
                                pygame.draw.rect(screen, YELLOW, [x-2, y-2, 40, 40])
                            pygame.draw.rect(screen, BUTTON, [x, y, 36, 36])
                            pygame.draw.rect(screen, DARKBUTTON, [x + 8, y + 8, 20, 20])
                            screen.blit(levelnum, (x+9,y+6))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if x <= mouse[0] <= x + 36 and y <= mouse[1] <= y + 36:
                                menuvalue=-1
                                levelcountcust = levelc

            Comlvl = bigfont1.render(str(countlevelscust), True, WHITE)
            Comlvl1 = bigfont1.render(str(countlevelscust), True, BLACK)
            screen.blit(Comlvl1, (488, 498))
            screen.blit(Comlvl, (490, 500))

            if weg <= mouse[0] <= weg + 140 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg, hig + 400 + 60, 140, 40])
                screen.blit(Back, (weg + 25, hig + 400 + 60 + 5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg, hig + 400 + 60, 140, 40])
                screen.blit(Back, (weg + 25, hig + 400 + 60 + 5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg <= mouse[0] <= weg + 140 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                    screenfill()
                    menuvalue = 7
                    break

            if weg+160 <= mouse[0] <= weg+160 + 270 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                pygame.draw.rect(screen, BUTTON, [weg+160, hig + 400 + 60, 270, 40])
                screen.blit(Rem, (weg+160 + 25, hig + 400 + 60 + 5))
            else:
                pygame.draw.rect(screen, DARKBUTTON, [weg+160, hig + 400 + 60, 270, 40])
                screen.blit(Rem, (weg+160 + 25, hig + 400 + 60 + 5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if weg+160 <= mouse[0] <= weg+160 + 270 and hig + 400 + 60 <= mouse[1] <= hig + 400 + 60 + 40:
                    completecust=[-1]
                    screenfill()
                    menuvalue=7
                    break

            if menuvalue==-1:
                ranmus=random.randint(0,1)
                if ranmus==0:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\ingame.mp3")
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music\ingame2.mp3")
                    pygame.mixer.music.play(-1)
                nextlvl(1)
                screenfill()
                texture.update(display, screen, 0, menuvalue)

        if event.type == pygame.QUIT:
            Ex()



    text=''
    if blindcur==0:
        text=text+'blind, '
    if blind>0 and blindcur==1:
        text=text+'blind '+str(blind)+', '
    if inverscur==0:
        text=text+'reverse, '
    if invers>0 and inverscur==1:
        text=text+'reverse '+str(invers)+', '
    if diffuc==3:
        try:
            text=text+'time '+str(round(left))+', '
        except:
            pass

    if menuvalue==0 and diffuc==3 and k==1:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        left = (seconds-(timer+0.5))*(-1)
        left=round(left)
        if left <= 0 and menuvalue == 0 and diffuc == 3:
            restart()
    if k==0 and diffuc==3:
        left=hardtime[levelcount-1]

    if steps<1:
        restart()
    if menuvalue==0:
        pygame.display.set_caption("Level "+str(levelcount-1)+', '+text+str(steps)+' steps')
    if menuvalue==-1:
        pygame.display.set_caption("Level "+str(levelcountcust-1)+', '+text+str(steps)+' steps')
    pygame.display.update()

#wall-1 corridore-0 gamezone-2 player-3 finish-4
#keys-50<51+2n<70 locks-50<52+2n<70
#portals-70<71+n<80 linkportal-80<81+n<90
#black enemy kill 90<n<98 blue enemy invers 100<n<108 purple enemy blind 110<n<118