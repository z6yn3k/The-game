def right():
    global yourpos,youritems
    X=yourpos[0]
    Y=yourpos[1]
    XX=X+1
    if display[XX][Y]==1:
        restart()
        return 0

    outf=0
    if display[XX][Y]==0:
        outf=1
    if display[XX][Y] in keyss:
        youritems.append(display[XX][Y])
        outf=1
    if display[XX][Y] in locks:
        if display[XX][Y]-1 in youritems:
            ttii=youritems.index(display[XX][Y]-1)
            youritems.pop(ttii)
            outf=1
    if outf==1:
        display[XX][Y] = 3
        display[X][Y] = 0
        yourpos[0] = XX

    yourpos[1]=Y
    if display[XX][Y]==4:
        nextlvl()
    update()

def left():
    global yourpos,youritems
    X=yourpos[0]
    Y=yourpos[1]
    XX=X-1
    if display[XX][Y]==1:
        restart()
        return 0

    outf=0
    if display[XX][Y]==0:
        outf=1
    if display[XX][Y] in keyss:
        youritems.append(display[XX][Y])
        outf=1
    if display[XX][Y] in locks:
        if display[XX][Y]-1 in youritems:
            ttii=youritems.index(display[XX][Y]-1)
            youritems.pop(ttii)
            outf=1
    if outf==1:
        display[XX][Y] = 3
        display[X][Y] = 0
        yourpos[0] = XX

    yourpos[1]=Y
    if display[XX][Y]==4:
        nextlvl()
    update()

def down():
    global yourpos,youritems
    X=yourpos[0]
    Y=yourpos[1]
    YY=Y+1
    if display[X][YY]==1:
        restart()
        return 0

    outf=0
    if display[X][YY]==0:
        outf=1
    if display[X][YY] in keyss:
        youritems.append(display[X][YY])
        outf=1
    if display[X][YY] in locks:
        if display[X][YY]-1 in youritems:
            ttii=youritems.index(display[X][YY]-1)
            youritems.pop(ttii)
            outf=1
    if outf==1:
        display[X][YY] = 3
        display[X][Y] = 0
        yourpos[1] = YY

    yourpos[0]=X
    if display[X][YY]==4:
        nextlvl()
    update()

def up():
    global yourpos,youritems
    X=yourpos[0]
    Y=yourpos[1]
    YY=Y-1
    if display[X][YY]==1:
        restart()
        return 0

    outf=0
    if display[X][YY]==0:
        outf=1
    if display[X][YY] in keyss:
        youritems.append(display[X][YY])
        outf=1
    if display[X][YY] in locks:
        if display[X][YY]-1 in youritems:
            ttii=youritems.index(display[X][YY]-1)
            youritems.pop(ttii)
            outf=1
    if outf==1:
        display[X][YY] = 3
        display[X][Y] = 0
        yourpos[1] = YY

    yourpos[0]=X
    if display[X][YY]==4:
        nextlvl()
    update()
