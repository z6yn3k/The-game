def level1():
    global lv
    lv='''
    ,2,2,2,2,2,
    ,2,3,0,0,2,
    ,2,0,0,0,2,
    ,2,0,0,4,2,
    ,2,2,2,2,2'''
    levelgen()

def level2():
    global lv
    lv = '''
    ,2,2,2,2,2,2,
    ,2,3,0,0,0,2,
    ,2,1,1,0,1,2,
    ,2,0,0,0,1,2,
    ,2,4,1,0,0,2,
    ,2,2,2,2,2,2'''
    levelgen()

def level3():
    global lv
    lv = '''
    ,2,2,2,2,2,2,2,
    ,2,3,1,0,0,51,2,
    ,2,0,1,0,1,1,2,
    ,2,0,0,0,0,0,2,
    ,2,0,1,1,1,52,2,
    ,2,0,1,4,0,0,2,
    ,2,2,2,2,2,2,2'''
    levelgen()

def level4():
    global lv
    lv = '''
    ,2,2,2,2,2,2,2,2,
    ,2,1,0,0,0,0,0,2,
    ,2,0,0,0,0,54,0,2,
    ,2,0,0,0,3,0,0,2,
    ,2,0,51,0,0,52,0,2,
    ,2,0,53,0,0,0,0,2,
    ,2,0,0,0,4,0,0,2,
    ,2,2,2,2,2,2,2,2'''
    levelgen()