import pygame

YELLOW=(255,255,0)
DYELLOW = (127,127,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BBLACK = (30,30,30)
RED = (255, 0, 0)
DRED= (127,0,0)
GREEN = (0, 255, 0)
DGREEN = (0,127,0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
LGRAY = (196, 196, 196)
PURPLE = (148, 0, 211)
DPURPLE = (74,0,105)
PINK = (255, 130, 171)
DPINK = (127,48,64)
DARKRED= (193,33,71)
DARKBLUE=(0, 0, 66)
DARKPUR=(96, 0, 96)
ORANGE=(255,140,0)
DORANGE=(127,70,0)
CYAN=(32,178,170)
DCYAN=(16,89,85)
SALMOON=(199,21,133)
DSALMOON=(99,10,66)
EMERALD=(0,250,154)
DEMERALD=(0,125,77)
YELREEN=(154,205,50)
DYELREEN=(77,102,25)

blaen=[91,92,93,94,95,96,97,98,99]
bluen=[101,102,103,104,105,106,107,108,109]
puren=[111,112,113,114,115,116,117,118,119]
prtls=[71,72,73,74,75,76,77,78,79]
prtks=[81,82,83,84,85,86,87,88,89]

def update(display,screen,blind,menuvalue):
    if menuvalue!=0 and menuvalue!=-1:
        return(0)
    for xx in range(0,34):
        for yy in range(0,34):
            if blind==0:
                texture(display,screen,xx,yy)
            if blind==1:
                if display[xx][yy]==3:
                    pygame.draw.rect(screen, BBLACK, [1, 1, 613, 613], 0)
                    texture(display, screen, xx, yy)
                    texture(display, screen, xx+1, yy)
                    texture(display, screen, xx-1, yy)
                    texture(display, screen, xx, yy-1)
                    texture(display, screen, xx+1, yy-1)
                    texture(display, screen, xx-1, yy-1)
                    texture(display, screen, xx, yy+1)
                    texture(display, screen, xx+1, yy+1)
                    texture(display, screen, xx-1, yy+1)
                    for xxx in range(0,34):
                        for yyy in range(0,34):
                            if display[xxx][yyy] in blaen:
                                tT = [[xxx * 18 + 3, yyy * 18 + 6 + 3], [xxx * 18 + 6 + 3, yyy * 18 + 3],
                                        [xxx * 18 + 12 + 3, yyy * 18 + 6 + 3],
                                        [xxx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
                                pygame.draw.polygon(screen, DARKRED, tT)
                            if display[xxx][yyy] in bluen:
                                tT = [[xxx * 18 + 3, yyy * 18 + 6 + 3], [xxx * 18 + 6 + 3, yyy * 18 + 3],
                                        [xxx * 18 + 12 + 3, yyy * 18 + 6 + 3],
                                        [xxx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
                                pygame.draw.polygon(screen, DARKBLUE, tT)
                            if display[xxx][yyy] in puren:
                                tT = [[xxx * 18 + 3, yyy * 18 + 6 + 3], [xxx * 18 + 6 + 3, yyy * 18 + 3],
                                        [xxx * 18 + 12 + 3, yyy * 18 + 6 + 3],
                                        [xxx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
                                pygame.draw.polygon(screen, DARKPUR, tT)

                            if (display[xxx][yyy] in prtks) or (display[xxx][yyy] in prtls):
                                if display[xxx][yyy] == 71 or display[xxx][yyy] == 81:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DRED, [xxx * 18 + 10, yyy * 18 + 10], 5, 0)
                                if display[xxx][yyy] == 72 or display[xxx][yyy] == 82:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DYELLOW, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)
                                if display[xxx][yyy] == 73 or display[xxx][yyy] == 83:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DGREEN, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)
                                if display[xxx][yyy] == 74 or display[xxx][yyy] == 84:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DPINK, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)
                                if display[xxx][yyy] == 75 or display[xxx][yyy] == 85:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DORANGE, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)
                                if display[xxx][yyy] == 76 or display[xxx][yyy] == 86:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DCYAN, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)
                                if display[xxx][yyy] == 77 or display[xxx][yyy] == 87:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DSALMOON, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)
                                if display[xxx][yyy] == 78 or display[xxx][yyy] == 88:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DEMERALD, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)
                                if display[xxx][yyy] == 79 or display[xxx][yyy] == 89:
                                    pygame.draw.rect(screen, DPURPLE, [xxx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
                                    pygame.draw.circle(screen, DYELREEN, [xxx * 18 + 9, yyy * 18 + 9], 5, 0)

                    texture(display, screen, xx, yy)
                    texture(display, screen, xx+1, yy)
                    texture(display, screen, xx-1, yy)
                    texture(display, screen, xx, yy-1)
                    texture(display, screen, xx+1, yy-1)
                    texture(display, screen, xx-1, yy-1)
                    texture(display, screen, xx, yy+1)
                    texture(display, screen, xx+1, yy+1)
                    texture(display, screen, xx-1, yy+1)
                    return 0

def texture(display,screen,xx,yy,tag=0):
    # defoult
    yyy=yy
    if tag==1:
        yyy=yy+3
    if tag==2:
        n=display
    else:
        n = display[xx][yy]
    if n == 1:
        pygame.draw.rect(screen, BLACK, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
    if n == 0:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
    if n == 2:
        pygame.draw.rect(screen, GRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
    if n == 3:
        pygame.draw.rect(screen, RED, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
    if n == 4:
        pygame.draw.rect(screen, BLUE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)

    # keys, locks
    if n == 52:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 5, yyy * 18 + 5, 9, 9], 0)
    if n == 51:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 5, yyy * 18 + 5, 9, 9], 0)
    if n == 54:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 4, yyy * 18 + 8, 11, 5], 0)
    if n == 53:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 4, yyy * 18 + 8, 11, 5], 0)
    if n == 56:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 8, yyy * 18 + 4, 5, 11], 0)
    if n == 55:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 8, yyy * 18 + 4, 5, 11], 0)
    if n == 58:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, LGRAY, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 57:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, YELLOW, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 60:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        tT = [[xx * 18 + 3, yyy * 18 + 6 + 3], [xx * 18 + 6 + 3, yyy * 18 + 3], [xx * 18 + 12 + 3, yyy * 18 + 6 + 3],
              [xx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
        pygame.draw.polygon(screen, LGRAY, tT)
    if n == 59:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        tT = [[xx * 18 + 3, yyy * 18 + 6 + 3], [xx * 18 + 6 + 3, yyy * 18 + 3], [xx * 18 + 12 + 3, yyy * 18 + 6 + 3],
              [xx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
        pygame.draw.polygon(screen, YELLOW, tT)
    if n == 62:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        tT = [[xx * 18 + 3, yyy * 18 + 6 + 6], [xx * 18 + 6 + 3, yyy * 18 + 6], [xx * 18 + 12 + 3, yyy * 18 + 6 + 6],
              [xx * 18 + 6 + 3, yyy * 18 + 6 + 6]]
        pygame.draw.polygon(screen, LGRAY, tT)
    if n == 61:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        tT = [[xx * 18 + 3, yyy * 18 + 6 + 6], [xx * 18 + 6 + 3, yyy * 18 + 6], [xx * 18 + 12 + 3, yyy * 18 + 6 + 6],
              [xx * 18 + 6 + 3, yyy * 18 + 6 + 6]]
        pygame.draw.polygon(screen, YELLOW, tT)
    if n == 64:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        tT = [[xx * 18+8 , yyy * 18+6], [xx * 18 + 7+7 , yyy * 18+6], [xx * 18+9 , yyy * 18 + 8+3 ],
              [xx * 18+3, yyy * 18 + 8+3 ]]
        pygame.draw.polygon(screen, LGRAY, tT)
    if n == 63:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        tT = [[xx * 18+8 , yyy * 18+6], [xx * 18 + 7+7 , yyy * 18+6], [xx * 18+9 , yyy * 18 + 8+3 ],
              [xx * 18+3, yyy * 18 + 8+3 ]]
        pygame.draw.polygon(screen, YELLOW, tT)
    if n == 66:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 5, yyy * 18 + 5, 9, 9], 0)
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 8, yyy * 18 + 8, 3, 3], 0)
    if n == 65:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 5, yyy * 18 + 5, 9, 9], 0)
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 8, yyy * 18 + 8, 3, 3], 0)
    if n == 68:
        pygame.draw.rect(screen, YELLOW, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, LGRAY, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
        pygame.draw.circle(screen, YELLOW, [xx * 18 + 9, yyy * 18 + 9], 3, 0)
    if n == 67:
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, YELLOW, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
        pygame.draw.circle(screen, LGRAY, [xx * 18 + 9, yyy * 18 + 9], 3, 0)

    # portals
    if n == 71 or n == 81:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, RED, [xx * 18 + 10, yyy * 18 + 10], 5, 0)
    if n == 72 or n == 82:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, YELLOW, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 73 or n == 83:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, GREEN, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 74 or n == 84:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, PINK, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 75 or n == 85:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, ORANGE, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 76 or n == 86:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, CYAN, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 77 or n == 87:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, SALMOON, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 78 or n == 88:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, EMERALD, [xx * 18 + 9, yyy * 18 + 9], 5, 0)
    if n == 79 or n == 89:
        pygame.draw.rect(screen, PURPLE, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.circle(screen, YELREEN, [xx * 18 + 9, yyy * 18 + 9], 5, 0)

    # enemies
    if n in blaen:
        tT = [[xx * 18 + 3, yyy * 18 + 6 + 3], [xx * 18 + 6 + 3, yyy * 18 + 3], [xx * 18 + 12 + 3, yyy * 18 + 6 + 3],
              [xx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.polygon(screen, BLACK, tT)
    if n in bluen:
        tT = [[xx * 18 + 3, yyy * 18 + 6 + 3], [xx * 18 + 6 + 3, yyy * 18 + 3], [xx * 18 + 12 + 3, yyy * 18 + 6 + 3],
              [xx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.polygon(screen, BLUE, tT)
    if n in puren:
        tT = [[xx * 18 + 3, yyy * 18 + 6 + 3], [xx * 18 + 6 + 3, yyy * 18 + 3], [xx * 18 + 12 + 3, yyy * 18 + 6 + 3],
              [xx * 18 + 6 + 3, yyy * 18 + 12 + 3]]
        pygame.draw.rect(screen, LGRAY, [xx * 18 + 1, yyy * 18 + 1, 17, 17], 0)
        pygame.draw.polygon(screen, PURPLE, tT)