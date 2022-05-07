import pygame
import random
import math
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
pygame.init()
SIZE = (width,height) = (870,600)
#SIZE = (width,height) = (800,600)
screen = pygame.display.set_mode(SIZE)

fontHello = pygame.font.SysFont("Times New Roman",30)

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (127, 214, 105)
BLUE = (105, 185, 214)
RED = (214, 105, 105)
YELLOW = (245, 241, 135)

# Home page
testRect1 = pygame.Rect(200, 100, 200, 100)
testRect2 = pygame.Rect(200, 300, 200, 100)
rectList = [testRect1, testRect2]
titleList = ["Play Game", "Instructions"]
# Menu page
menuRect1 = pygame.Rect(275, 225, 250, 50)
menuRect2 = pygame.Rect(275, 300, 250, 50)
menuRect3 = pygame.Rect(275, 375, 250, 50)
menuRectList = [menuRect1, menuRect2, menuRect3]
menuTitleList = ["BACK TO HOME PAGE", "TRY AGAIN", "RESUME"]

#litters
sX = []
sY = []
sSpeed = []
sLitter = []
sLength = []
sHeight = []


STATE_MAIN = 1
STATE_GAME = 2
STATE_INSTR = 3
STATE_MENU = 4

state = STATE_MAIN

circleR = 10
    
# section 1 
s1X = 800
s1Y = random.randint(200,270)
s1Speed = random.randrange(1,3)
s1Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
s1length = random.randint(20,50)
s1height = random.randint(20,50)

# section 2
s2X = 800
s2Y = random.randint(270,340)
s2Speed = random.randrange(1,3)
s2Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
s2length = random.randint(20,50)
s2height = random.randint(20,50)

# section 3
s3X = 800
s3Y = random.randint(340,410)
s3Speed = random.randrange(1,3)
s3Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
s3length = random.randint(20,50)
s3height = random.randint(20,50)

# section 4
s4X = 800
s4Y = random.randint(410,480)
s4Speed = random.randrange(1,3)
s4Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
s4length = random.randint(20,50)
s4height = random.randint(20,50)

# section 5 
s5X = 800
s5Y = random.randint(480,520)
s5Speed = random.randrange(1,3)
s5Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # # boolean for whether showing litter or not
s5length = random.randint(20,50)
s5height = random.randint(20,50)
    

def distance(pt1x, pt1y, pt2x, pt2y):
    diffx = pt2x - pt1x
    diffy = pt2y - pt1y
    distSquared = diffx**2 + diffy**2
    return math.sqrt(distSquared)    

def addLitter():
    global mx, my
    global s1X, s1Y, s1Speed, s1Litter, s1length, s1height
    global s2X, s2Y, s2Speed, s2Litter, s2length, s2height
    global s3X, s3Y, s3Speed, s3Litter, s3length, s3height
    global s4X, s4Y, s4Speed, s4Litter, s4length, s4height
    global s5X, s5Y, s5Speed, s5Litter, s5length, s5height
    
    
    # 1 first section (s1x,s1y, 200 <= s1y <= 270)
    pygame.draw.rect(screen, YELLOW,(0,200,800,70)) # section 1 background for illustrate
    if s1Litter == '1':
        s1X -= s1Speed
        pygame.draw.rect(screen, RED, (s1X,s1Y,s1length,s1height))    


    # 2 second section (s1x,s1y, 270 <= s1y <= 340)
    pygame.draw.rect(screen, WHITE,(0,270,800,70)) # section 1 background for illustrate
    if s2Litter == '1':
        s2X -= s2Speed
        pygame.draw.rect(screen, RED, (s2X,s2Y,s2length,s2height))  
    
    # 3 third section (s1x,s1y, 340 <= s1y <= 410)
    pygame.draw.rect(screen, YELLOW,(0,340,800,70)) # section 1 background for illustrate
    if s3Litter == '1':
        s3X -= s3Speed
        pygame.draw.rect(screen, RED, (s3X,s3Y,s3length,s3height))  
    
    # 4 fourth section (s1x,s1y, 410 <= s1y <= 480)
    pygame.draw.rect(screen, WHITE,(0,410,800,70)) # section 1 background for illustrate
    if s4Litter == '1':
        s4X -= s4Speed
        pygame.draw.rect(screen, RED, (s4X,s4Y,s4length,s4height))    
        
    # 5 fifth section (s1x,s1y, 480 <= s1y <= 550)
    pygame.draw.rect(screen, YELLOW,(0,480,800,70)) # section 1 background for illustrate
    if s5Litter == '1':
        s5X -= s5Speed
        pygame.draw.rect(screen, RED, (s5X,s5Y,s5length,s5height))      
#resets the variables when called. is called when the try again and home buttons are pressed
def resetLitter1():
    global s1X, s1Y, s1Speed, s1Litter, s1length, s1height
    global s2X, s2Y, s2Speed, s2Litter, s2length, s2height
    global s3X, s3Y, s3Speed, s3Litter, s3length, s3height
    global s4X, s4Y, s4Speed, s4Litter, s4length, s4height
    global s5X, s5Y, s5Speed, s5Litter, s5length, s5height    
    
    
    # section 1 
    s1X = 800
    s1Y = random.randint(200,270)
    s1Speed = random.randrange(1,3)
    s1Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s1length = random.randint(20,50)
    s1height = random.randint(20,50)
    
    # section 2
    s2X = 800
    s2Y = random.randint(270,340)
    s2Speed = random.randrange(1,3)
    s2Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s2length = random.randint(20,50)
    s2height = random.randint(20,50)
    
    # section 3
    s3X = 800
    s3Y = random.randint(340,410)
    s3Speed = random.randrange(1,3)
    s3Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s3length = random.randint(20,50)
    s3height = random.randint(20,50)
    
    # section 4
    s4X = 800
    s4Y = random.randint(410,480)
    s4Speed = random.randrange(1,3)
    s4Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s4length = random.randint(20,50)
    s4height = random.randint(20,50)
    
    # section 5 
    s5X = 800
    s5Y = random.randint(480,520)
    s5Speed = random.randrange(1,3)
    s5Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # # boolean for whether showing litter or not
    s5length = random.randint(20,50)
    s5height = random.randint(20,50)

def resetLitter():
    global s1X, s1Y, s1Speed, s1Litter, s1length, s1height
    global s2X, s2Y, s2Speed, s2Litter, s2length, s2height
    global s3X, s3Y, s3Speed, s3Litter, s3length, s3height
    global s4X, s4Y, s4Speed, s4Litter, s4length, s4height
    global s5X, s5Y, s5Speed, s5Litter, s5length, s5height    
    
    
    # section 1 
    s1X = 800
    s1Y = random.randint(200,270)
    s1Speed = random.randrange(1,3)
    s1Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s1length = random.randint(20,50)
    s1height = random.randint(20,50)
    
    # section 2
    s2X = 800
    s2Y = random.randint(270,340)
    s2Speed = random.randrange(1,3)
    s2Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s2length = random.randint(20,50)
    s2height = random.randint(20,50)
    
    # section 3
    s3X = 800
    s3Y = random.randint(340,410)
    s3Speed = random.randrange(1,3)
    s3Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s3length = random.randint(20,50)
    s3height = random.randint(20,50)
    
    # section 4
    s4X = 800
    s4Y = random.randint(410,480)
    s4Speed = random.randrange(1,3)
    s4Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
    s4length = random.randint(20,50)
    s4height = random.randint(20,50)
    
    # section 5 
    s5X = 800
    s5Y = random.randint(480,520)
    s5Speed = random.randrange(1,3)
    s5Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # # boolean for whether showing litter or not
    s5length = random.randint(20,50)
    s5height = random.randint(20,50)
    

def drawScene(screen, mx, my, button):
    global state
    screen.fill(BLACK)
    pygame.mouse.set_visible(True)
    
    for i in range(len(rectList)):
        rectangle = rectList[i]
        pygame.draw.rect(screen, GREEN, rectangle)
        text = fontHello.render(titleList[i] , 1, (255, 0, 0))	
        screen.blit(text, rectangle)
        
        if rectangle.collidepoint(mx, my) and button == 1:
            if i == 0:
                state = STATE_GAME
            else:
                state = STATE_INSTR



def playGame(screen, mx, my, button):
    global state
    screen.fill(BLACK)  # background
    
    pygame.mouse.set_visible(False)
    
    mx, my = pygame.mouse.get_pos()
    
    # Time as the game start:
    time = pygame.time.get_ticks() // 1000
    #print(time)
    
    # Menu part:
    pygame.draw.rect(screen,YELLOW,(350,0,100,50))
    
    # middle part(mouse follow):
    pygame.draw.rect(screen, WHITE,(0,200,width,350))
    if mx <= circleR :
        mx = circleR
    elif mx >= 800 - circleR:
        mx = 800 - circleR
    if 0 <= mx <= 800 and 0 <= my <= 200:
        if 350 <= mx <= 450 and 0 <= my <= 50:
            pygame.mouse.set_visible(True)        
        else: 
            pygame.mouse.set_visible(False)
            my = 200 + circleR
    elif 0 <= mx <= 800 and 550 <= my <= 600:
        pygame.mouse.set_visible(False)
        my = 550 - circleR
    
    addLitter()
    
    # characters:
    pygame.draw.circle(screen, BLUE, (mx,my), circleR) # fish

    
def drawMenu(screen, mx, my, button):
    global state
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (200,150,400,300))
    
    pygame.mouse.set_visible(True)
    
    for i in range(len(menuRectList)):
        menuRectangle = menuRectList[i] 
        pygame.draw.rect(screen, GREEN, menuRectangle)
        text = fontHello.render(menuTitleList[i] , 1, (255, 0, 0))	
        screen.blit(text, menuRectangle)
        
        if menuRectangle.collidepoint(mx, my) and button == 1:
            if i == 0:
                state = STATE_MAIN
                resetLitter()
            elif i == 1:
                state = STATE_GAME
                resetLitter()

            else:
                state = STATE_GAME   
    
    
running = True
myClock = pygame.time.Clock()

while running:   # this is our game loop
    button = 0
    # Check all the events that happen
    for evnt in pygame.event.get():
        # if the user tries to close the window, then raise the "flag"
        if evnt.type == pygame.QUIT:
            running = False
        #if evnt.type == pygame.KEYDOWN:
            
        #if evnt.type == pygame.KEYUP:
            
        if evnt.type == pygame.MOUSEMOTION:
            mx, my = evnt.pos
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            button = evnt.button
            if 350  <= mx <= 450  and 0 <= my <= 50:
                state = STATE_MENU
                
    
    addLitter()
    
    # traffic cop
    if state == STATE_MAIN:
        drawScene(screen, mx, my, button)
    elif state == STATE_GAME:
        playGame(screen, mx, my, button)
    elif state == STATE_MENU:
        drawMenu(screen,mx,my,button)
    else:
        pygame.draw.rect(screen, BLUE, (0, 0, width, height))
        
    pygame.display.flip()

    myClock.tick(60)

pygame.quit()