import pygame

screen = None
size = (0,0)

def init(scr, si):
    global screen
    global size
    screen = scr
    size = si

def getKeys():
    current_keys = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109,
    'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122, '[': 91, ']': 93, '\\': 92, '.': 46, '/': 47, ';': 59, "'": 39, 'backspace': 8, 'delete': 127, 'home': 278, 'end': 279, 'return': 13, 'insert': 277, 'page up': 280, 'right shift': 303, 'up': 273, 'page down': 281, 'right': 275, 'down': 274, 'left': 276,
    'right ctrl': 305, 'menu': 319, 'right alt': 307, 'space': 32, 'left alt': 308, 'left ctrl': 306, 'left shift': 304, 'caps lock': 301, 'tab': 301, '`': 301, '1': 301, '2': 301, '3': 301, '4':
    301, '5': 301, '6': 301, '7': 301, '8': 301, '9': 301, '0': 301, '-': 301, '=': 301, 'escape': 301, 'f1': 301, 'f2': 301, 'f3':
    301, 'f4': 301, 'f5': 301, 'f6': 287, 'f7': 301, 'f8': 301, 'f9': 301, 'f10': 301, 'f11': 301, 'f12': 301, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57}
    
    if pygame.key.get_focused() == True:
        bools = pygame.key.get_pressed()
        out = []
        for i in range(0,len(bools)):
            if bools[i] == 1:
                try:
                    out.append(list(current_keys.keys())[list(current_keys.values()).index(i)])
                except(ValueError):
                    pass
        return out
    return None

class button(object):
    def __init__(self,pos,mods, func, args=[], identification = '', type='tri-left', color1=(255,255,255), color2=(125,125,125), enabled=True):
        self.ident = identification
        self.pos = pos
        self.type = type
        self.colors = (color1, color2)
        self.color1 = color1
        self.function = func
        self.enabled = enabled
        self.recCli = False
        self.args = args
        self.mods = mods
        
    def draw(self, surface, mouse):
        pos = self.pos
        modifierR, modifierU = self.mods
        if self.type == 'tri-left':
            points = [(pos), (pos[0] + 45 + modifierR, pos[1] + 25 + modifierU), (pos[0]+45, pos[1]-25 - modifierU)]
            full = []
            x = points[0][0] - points[1][0]
            y = points[0][1] - points[1][1]
            if x < 0: x = -x 
            for i in range(0,x+1):
                p = points[0][0] + i
                q = points[0][1] - i
                full.append([p,q])

            l = (full[0][1])-full[len(full)-1][1]

            if l < 0: l = -l
            full.append([full[len(full)-1][0], full[0][1]+l])

            self.rect = pygame.Rect(pos[0],pos[1]-l, 45 + modifierR, l*2)
            #pygame.draw.rect(surface, (125,125,125), self.rect)
            #pygame.draw.polygon(surface, self.colors[0], full)
              
        if self.type == 'tri-right':
            points = [(pos[0]+45 + modifierR, pos[1]), (pos[0], pos[1] + 25 + modifierU), (pos[0], pos[1]-25-modifierU)]
            full = []
            x = points[0][0] - points[1][0]
            y = points[0][1] - points[1][1]
            if x < 0: x = -x
            for i in range(0,x+1):
                p = points[0][0] - i
                q = points[0][1] - i
                full.append([p,q])

            l = (full[0][1])-full[len(full)-1][1]

            if l < 0: l = -l
            full.append([full[len(full)-1][0], full[0][1]+l])

            
            self.rect = pygame.Rect(pos[0],pos[1]-l, 45 + modifierR, l*2)
            #pygame.draw.rect(surface, (125,125,125), self.rect)

        pygame.draw.polygon(surface, self.color1, full)
        self.hovered(mouse)
            
    def hovered(self, mouse):
        if self.enabled:
            if mouse.colliderect(self.rect):
                self.color1 = self.colors[1]
                if pygame.mouse.get_pressed()[0] == 1:
                    if self.recCli == False:
                        self.recCli = True
                        if str(type(self.function)) == "<class 'function'>":
                            if type(self.args) == list and len(self.args) > 0:
                                self.function(self.args)
                            else:
                                self.function()
                        else: print('must provide a function')
                else:
                    self.recCli = False

            else:
                self.color1 = self.colors[0]
        else:
            self.color1 = self.colors[1]

class word(object):
    def __init__(self,text,pos,function,args=[],font='',color=(255,255,255),hColor=(125,125,125),fSize=70):
        self.text = text
        self.color = color
        self.hColor = hColor
        self.alt = color
        self.font = font
        self.size = fSize
        self.pos = pos
        self.func = function
        self.args = args

        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, True, self.color)

        if type(self.pos) == list:
            if self.pos[0] == 'center':
                self.pos = (size[0]/2 - text.get_width()/2, self.pos[1])
            
            elif self.pos[0] == 'left':
                self.pos = (size[0]/2.8 - text.get_width()/2, self.pos[1])
                
            else:
                self.pos = (0,0)

        #screen.blit(text, self.pos)
        self.rect = text.get_rect(left=(self.pos[0]), top=(self.pos[1]))

    def render(self,surface, function=None, args=None):
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, True, self.color)
        self.rect = text.get_rect(left=(self.pos[0]), top=(self.pos[1]))
        if function != None and str(type(function)) == "<class 'function'>":
            function(args)
        surface.blit(text, self.pos)
        

    def drawRect(self, color):

        pygame.draw.rect(screen, color, self.rect)

    def isHovered(self, mouse):
        if mouse.colliderect(self.rect):
            self.color = self.hColor
            if pygame.mouse.get_pressed()[0] == 1:
                if str(type(self.func)) == "<class 'function'>":
                    if type(self.args) == list and len(self.args) > 0:
                        self.func(self.args)
                    else: self.func()
        else:
            self.color = self.alt
        
class textBox(object):
    def __init__(self, size, pos, text='', bckg=(255,255,255), maxChar=10, constraint='true'):
        self.size = size
        self.pos = pos
        self.text = text
        self.bckg = bckg
        self.active = False
        self.recenkey = []
        self.keys = []
        self.maxChar = maxChar
        self.constraint = constraint
        
        if size[1] <= 55:
                self.size = (size[0], 55)
        if type(pos) != tuple:
            self.pos = (0,0)
        if type(text) != str:
            self.text = ''
        if type(bckg) != bool:
            self.bckg = False
        if type(maxChar) != int:
            return EnvironmentError

        self.rect = pygame.Rect(self.pos[0] - self.size[0], self.pos[1] - self.size[1], self.size[0], self.size[1])

    def isActive(self, mouse):
        if pygame.mouse.get_pressed()[0] == 1:
            if mouse.colliderect(self.rect):
                self.active = True
            else:
                self.active = False

    def addText(self):
        if type(getKeys()) == list
            if len(getKeys()) >= 1:
                self.keys = getKeys()
                for key in self.keys:
                    if key not in self.recenkey:
                        if key == 'backspace' or key == 'delete':
                            if self.active:
                                self.text = self.text[:-1]
                        elif self.active and len(self.text) <= self.maxChar -1 and len(key) == 1:
                            if self.constraint == 'true':
                                for i in self.keys:
                                    if i == 'left shift':
                                        k = key.upper()
                                    else:
                                        k = key
                                self.text += k
                            elif self.constraint == 'int':
                                try:
                                    v = int(key)
                                    self.text += key
                                except ValueError:
                                    pass
                            elif self.constraint == 'str':
                                try:
                                    v = int(key)
                                except ValueError:
                                    for i in self.keys:
                                        if i == 'left shift':
                                            k = key.upper()
                                        else:
                                                k = key
                                self.text += k
                        self.recenkey.append(key)
        for key in self.recenkey:
            if key not in self.keys:
                f = self.recenkey.index(key)
                self.recenkey.pop(f)
                self.recenkeys = []
        
        self.keys = []

    def draw(self, screen, color):
        if self.bckg:
            pygame.draw.rect(screen, color, self.rect)

    def render(self):
        pos = (self.pos[0] - self.size[0], self.pos[1] - self.size[1])
        text = word(self.text,pos, None, None, '', (0,255,0), (0,255,0), 72)
        text.render(screen)

    def run(self, mouse, screen, color):
        self.isActive(mouse)
        self.addText()
        self.draw(screen, color)
        self.render()
