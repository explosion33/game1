import pygame, sys
from random import randint
from extras import *

f = open('settings.txt', 'r')
f.seek(0)
s = f.read()
opt = ''
setts = []

for i in range(0, len(s)-1):
    mid = '/'
    if s[i] == mid and s[i+1] == mid:
        setts.append(opt)
        opt = ''
    else:
        opt += s[i]

for i in range(0,len(setts)):
    if '/' in setts[i]:
        setts[i] = setts[i][1:] 
    
# PYGAME INIT       
pygame.init()
size = setts[0]
k = size.index('x')
size = (int(size[0:k]), int(size[k+1:len(size)]))

infoObject = pygame.display.Info()
screenSize = (infoObject.current_w, infoObject.current_h)
if screenSize[0] > 1920:
    size = (1500, 844)
    setts[0]= '1500x844'
if size == (1920,1080):
    screen = pygame.display.set_mode(screenSize, pygame.FULLSCREEN)
    size = screenSize
else:
    screen = pygame.display.set_mode(size)
init(screen, size)
mouse = pygame.Rect(0, 0, 2, 2)
mode = 'menu'

scale = int(size[0])/1920

def modeSwitch(args):
    global mode
    mode = args[0]

def exitGame():
    sys.exit()

# MAIN MENU OBJECTS
    #TEXT
option1 = word('Play', ['center', 50], modeSwitch, ['game'], '', (0,125,0), (0,255,0), int(92 * scale))
option2 = word('Settings', ['center', 125], modeSwitch, ['settings'], '',  (0,125,0), (0,255,0),  int(92 * scale))
quitButton = word('Quit', ['center', 200], exitGame, [], '', (0,125,0), (0,255,0), int(92 * scale))
buttons = [option1, option2, quitButton]

# SETTINGS OBJECTS

    #p1


cup1 = setts[1]
cdown1 = setts[2]
    #p2
cup2 = setts[3]
cdown2 = setts[4]

cpause = setts[5]
#(cpause)
    #TEXT
back = word('Back', (0,0), modeSwitch, ['menu'], '', (255,255,255), (105,105,105), 60)
cat1 = word('Game:', ['left', 60], None, None, '', (255,255,255), (255,255,255), 60)
resolution = word('Resolution:', ['center', 100], None, None, '', (255,255,255), (255,255,255), 60)
p = word('Pause: ', ['center', 180], None, None, '', (255,255,255), (255,255,255), 60)
cat2 = word('Player1:', ['left', 220], None, None, '', (255,255,255), (255,255,255), 60)
up = word('UP:', ['center', 280], None, None, '', (255,255,255), (255,255,255), 60)
down = word('DOWN:', ['center', 325], None, None, '', (255,255,255), (255,255,255), 60)

cat3 = word('Player2:', ['left', 365], None, None, '', (255,255,255), (255,255,255), 60)
up2 = word('UP:', ['center', 405], None, None, '', (255,255,255), (255,255,255), 60)
down2 = word('DOWN:', ['center', 450], None, None, '', (255,255,255), (255,255,255), 60)

resDisc = word('*Restarting the game is required when changing resolution', (0,0), None, None, '', (255,255,255), (255,255,255), 35)
resDisc = word('*Restarting the game is required when changing resolution', (size[0]-resDisc.rect.width-5, size[1]-resDisc.rect.height-5), None, None, '', (255,255,255), (255,255,255), 35)


    #res
#width = textBox((200,50), (resolution.pos[0] + 200 + resolution.rect.width, resolution.pos[1] + 50), setts[0], True, 4, 'int')
sup1 = textBox((200,50), (down.pos[0] + 200 + down.rect.width, up.pos[1] + 50), cup1, True, 1)
sdown1 = textBox((200,50), (down.pos[0] + 200 + down.rect.width, down.pos[1] + 50), cdown1, True, 1)
sup2 = textBox((200,50), (down2.pos[0] + 200 + down2.rect.width, up2.pos[1] + 50), cup2, True, 1)
sdown2 = textBox((200,50), (down2.pos[0] + 200 + down2.rect.width, down2.pos[1] + 50), cdown2, True, 1)
pc = textBox((200,50), (down.pos[0] + 200 + down.rect.width, p.pos[1] + 50), cpause, True, 1)

controls = [sup1,sdown1,sup2,sdown2,pc]

#res2 = word('844', (width.pos[0], width.pos[1] - width.rect.height), None, None, '', (255,255,255), (255,255,255), 72)

def switch(args):
    direction = args[0]
    obj = args[1]
    objS = obj[1]
    obj = obj[0]
    txt = args[2]

    options = ['1500x844', '1750x985', '1920x1080']
   
    x = int(options.index(txt.text))
    if direction == 'right':
        x += 1
    elif direction == 'left':
        x -= 1

    txt.text = options[x]

    if direction == 'right':
        objS.enabled = True
        if x == len(options)-1:
            obj.enabled = False
        else:
            obj.enabled = True
    elif direction == 'left':
        objS.enabled = True
        if x == 0:
            obj.enabled = False
        else:
            obj.enabled = True

    if x==0 and obj.ident=='left':
        obj.enabled = False
        objS.enabled= True
    elif x == len(options)-1 and obj.ident=='right':
        obj.enabled= False
        objS.enabled= True

def reloc(args):
    two = args[0]
    three = args[1]
    four = args[2]

    if four.pos[0] != (two.pos[0] + 45 + two.mods[0] + three.pos[0])/2 - four.rect.width/2:
        x1 = two.pos[0] + 45 + two.mods[0]
        x2 = three.pos[0]
        x = (x1 + x2)/2
        x = x - four.rect.width/2
        four.pos = (x, four.pos[1])


arrowL = button((resolution.rect.left + resolution.rect.width + 5, resolution.rect.top + resolution.rect.height/2), (-15,-18), switch, [], 'left', 'tri-left',(255,255,255),(125,125,125))
midTxt = word(setts[0], (arrowL.pos[0] + 60, resolution.pos[1]), None, None, '',(255,255,255), (255,255,255), 70)
arrowR = button((midTxt.rect.right + 15, midTxt.rect.top+ midTxt.rect.height/2), (-15,-18), switch, [], 'right', 'tri-right')

options = ['1500x844', '1750x985', '1920x1080']
if options.index(midTxt.text) == 0:
    arrowL.enabled = False
elif options.index(midTxt.text) == len(options) -1:
    arrowR.enabled = False

arrowL.args = ['left', [arrowL,arrowR], midTxt]
arrowR.args = ['right', [arrowR,arrowL], midTxt]

# Game Objects
maxSpeed = 3
numCol = 0
score1 = 0
score2 = 0
paused = False
recentP = False

def pauseMenu():
    menu = pygame.Surface((size[0]/3, size[1]/3))
    menu.fill((0,0,0))
    border = pygame.Rect(0, 0, size[0]/3, size[1]/3)
    pygame.draw.rect(menu, (255,255,255), border, 7)
    Title = word('Paused', (0,30), None, None, '', (255,255,255), (255,255,255))
    Quit = word('Resume', (0,130), pause, None, '', (255,255,255), (125,125,125))
    Exit = word('Quit', (0,180), modeSwitch, ['menu'], '', (255,255,255), (125,125,125))
    
    buttons = [Title, Quit, Exit]

    pos = (size[0]/2 - menu.get_width()/2, size[1]/2 - menu.get_height()/2)

    for btn in buttons:
        btn.pos = (menu.get_width()/2 - btn.rect.width/2, btn.pos[1])
        btn.render(menu)
        rect = pygame.Rect(btn.pos[0] + pos[0], btn.pos[1] + pos[1], btn.rect.width, btn.rect.height)
        btn.rect = rect
        btn.drawRect((225,0,0))
        btn.isHovered(mouse)
        btn.render(menu)
    

    

    screen.blit(menu, pos)

def pause():
    global paused
    if paused:
        paused = False
    else:
        paused = True
    #(paused)
    #('::')



if size != (1920, 1080):
    ballSpeed = (1,1)
else:
    ballSpeed = (2,2)
pos = (int(size[0]/2), int(size[1]/2))
p1y = size[1]/2 - size[1]/8
p2y = size[1]/2 - size[1]/8

canMove = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    xm, ym = pygame.mouse.get_pos()
    mouse.center = (xm,ym)

    if mode == 'menu':

        for btn in buttons:
            btn.render(screen)
            btn.isHovered(mouse)
        
        p1y = size[1]/2 - size[1]/8
        p2y = size[1]/2 - size[1]/8

        score1 = 0
        score2 = 0
        if size != (1920,1080):
            ballSpeed = (1,1)
        else:
            ballSpeed = (2,2)
        pos = (int(size[0]/2), int(size[1]/2))
        maxSpeed = 3
        numCol = 0
        if paused:
            paused = False
        recentP = False

        pygame.display.flip()
        screen.fill((0,0,0))

    elif mode == 'settings':
        
        arrowL.draw(screen, mouse)
        arrowR.draw(screen, mouse)
        midTxt.render(screen, reloc, [arrowL, arrowR, midTxt])

        back.render(screen)
        back.isHovered(mouse)
        cat1.render(screen)
        cat2.render(screen)
        cat3.render(screen)
        resolution.render(screen)
        up.render(screen)
        down.render(screen)
        up2.render(screen)
        down2.render(screen)
        resDisc.render(screen)
        p.render(screen)

        if back.rect.colliderect(mouse):
            for box in controls:
                box.active = False
        

        for box in controls:
            box.run(mouse, screen, (40,40,40))
            box.text = box.text.lower()


        #width.run(mouse, screen, (40,40,40))

        if sup1.active == False and len(sup1.text) == 0:
            sup1.text = 'w'
        if sdown1.active == False and len(sdown1.text) == 0:
            sdown1.text = 's'
        if sup2.active == False and len(sup2.text) == 0:
            sup2.text = 'o'
        if sdown2.active == False and len(sdown2.text) == 0:
            sdown2.text = 'l'
        if pc.active == False and len(pc.text) == 0:
            pc.text = 'p'

        for box in controls:
            for i in controls:
                if box != i:
                    if box.text == i.text:
                        i.text = ''


#        if width.text != '':     
#            if int(width.text) < 1250 and width.active == False:
#                width.text = '1250'
        

        cup1 = sup1.text
        cdown1 = sdown1.text
        cup2 = sup2.text
        cdown2 = sdown2.text
        cpause = pc.text

#        if len(width.text) > 0:
#            i = int(width.text)/1920
#            i = i * 1080
#            i = int(i)
#        else:
#            i = ''

        #res2 = word('x' + str(i), (width.pos[0], width.pos[1] - width.rect.height), None, None, '', (255,255,255), (255,255,255), 72)
        #res2.render(screen)


        pygame.display.flip()
        screen.fill((0,0,0))

        f = open('settings.txt', 'w')
        f.write(str(midTxt.text) + '//')
        f.write(str(cup1) + '//')
        f.write(str(cdown1) + '//')
        f.write(str(cup2) + '//')
        f.write(str(cdown2) + '//')
        f.write(str(cpause) + '//')
        f.close()

    elif mode == 'game':

        score = word(str(score1) + ':' + str(score2), ['center', 0], None, None, '', (255,255,255), (255,255,255), 72)
        score.render(screen)

        p1 = pygame.Rect(10, p1y , 50, size[1]/4)
        p2 = pygame.Rect(size[0]-60, p2y, 50, size[1]/4)

        pygame.draw.rect(screen, (255,255,255), p1)
        pygame.draw.rect(screen, (255,255,255), p2)
        ballRect = pygame.draw.circle(screen, (255,255,255), pos, 60)

        if p1.colliderect(ballRect) or p2.colliderect(ballRect):

            if p1.colliderect(ballRect):
                cen = ballRect.centery
                relLocT =p1.centery - p1.height/2
                if cen > relLocT and cen < relLocT + p1.height/3:
                    collA = 'top'
                elif cen > relLocT + p1.height/3 and cen < relLocT + p1.height/3 + p1.height/3:
                    collA = 'mid'
                elif cen < relLocT:
                    collA = 'topT'
                elif cen < relLocT + p1.height:
                    collA = 'bottom'
                else:
                    collA = 'bottomB'
            else:
                cen = ballRect.centery
                relLocT =p2.centery - p2.height/2
                if cen > relLocT and cen < relLocT + p2.height/3:
                    collA = 'top'
                elif cen > relLocT + p2.height/3 and cen < relLocT + p2.height/3 + p2.height/3:
                    collA = 'mid'
                elif cen < relLocT:
                    collA = 'topT'
                elif cen < relLocT + p2.height:
                    collA = 'bottom'
                else:
                    collA = 'bottomB'


            #OLD SPEED GENERATOR
            '''a=1
            b=1
            if ballSpeed[0] < 0:
                a = -1
            if ballSpeed[1] < 0:
                b = -1
            ballSpeed = (randint(2,3) * a, randint(2,3) * b)
            ballSpeed = (-ballSpeed[0], -ballSpeed[1])'''

            #NEW SPEED GENERATOR
            if collA == 'mid':
                a,b = ballSpeed
                x = randint(a,5)

                y = int(x/2) + 1

                if ballSpeed[0] > 0:
                    x = -x

                if a < 0 and x < 0:
                    x = -x
                elif a > 0 and x > 0:
                    x = -x

                ballSpeed = (x,y)


            if collA == 'top' or collA == 'bottom' or collA == 'topT' or collA == 'bottomB':
                x,y = ballSpeed
                a,b = ballSpeed
                
                if x < 0: x = -x
                if y < 0: y = -y

                c = x
                x = y
                y = c

                if randint(0,1) == 1:
                    if x < 5:
                        x += 1
                elif randint(0,1) == 1:
                    if x > 2:
                        x -= 1
                
                if randint(0,1) == 1:
                    if y < 4:
                        y += 1
                elif randint(0,1) == 1:
                    if y > 1:
                        y -= 1

                if b > 0:
                    if collA == 'topT' or collA == 'bottomB':
                        if y < 0: y = -y
                    else:
                        if y > 0: y = -y
                elif b < 0:
                    if collA == 'topT' or collA == 'bottomB':
                        if y > 0: y = -y
                    else:
                        if y < 0: y = -y
                else:
                    if randint(0,1) == 1: y = 2
                    else: y = -2

                if a > 0:
                    if x > 0: x = -x
                if a < 0:
                    if x < 0: x = -x
                
                ballSpeed = (x,y)

        if ballRect.left <= 0:
            canMove = False
            score2 += 1
            
            pos = (int(size[0]/2), int(size[1]/2))

            #mode = 'menu'
        if ballRect.right >= size[0]:
            canMove = False
            score1 += 1
            
            pos = (int(size[0]/2), int(size[1]/2))
            
            #mode = 'menu'

        if ballRect.bottom >= size[1] or ballRect.top <= 0:
            ballSpeed = (ballSpeed[0], -ballSpeed[1])

        if canMove:
            if paused == False:
                x, y = ballRect.center
                x2, y2 = ballSpeed
    
                pos = (x+x2, y+y2)
        else:
            val = [randint(0,1),randint(0,1)]
            for i in range(0,2):
                if val[i] == 0:
                    val[i] -= 1
            if size != (1920,1080):
                ballSpeed = (val[0],val[1])
            else:
                ballSpeed = (2 * val[0], 2 * val[1])
            
            maxSpeed = 3
            numCol = 0
            canMove = True

        if type(getKeys()) == list:
            if len(getKeys()) >= 1:
                for key in getKeys():
                    if paused == False:
                        if p1.top > 0:
                            if key == cup1:
                                p1y -= 1.5
                        if p1.bottom < size[1]:
                            if key == cdown1:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                p1y += 1.5
                        if p2.top > 0:
                            if key == cup2:
                                p2y -= 1.5
                        if p2.bottom < size[1]:
                            if key == cdown2:
                                p2y += 1.5
                    if key == cpause:
                        if recentP == False:
                            recentP = True
                            #('pause')
                            pause()
                            #(paused)
        if recentP == True:
            if cpause not in getKeys():
                recentP = False
        
        if score1 == 10:
            mode = 'menu'
        elif score2 == 10:
            mode = menu

        if paused:
            pauseMenu()

        pygame.display.flip()
        screen.fill((0,0,0))

    elif mode == 'test':
        

        pygame.display.flip()
        screen.fill((0,0,0))