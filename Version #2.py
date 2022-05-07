import pygame
import random
import math
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
pygame.init()
#SIZE = (width,height) = (870,600)
SIZE = (width,height) = (800,600)
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

## picture
#litterPic = pygame.image.load("Garbage.png")
#litterPic = pygame.transform.scale(litterPic,(sLength,sHeight))
fishPicWidth = 53
fishPicHeight = 38
fishPic = pygame.image.load("fishPic.png")
fishPic = pygame.transform.scale(fishPic,(fishPicWidth,fishPicHeight)) 

#litters
sX = []
sY = []
sSpeed = []
sLitter = []
sLength = []
sHeight = []
sSection = []

STATE_MAIN = 1
STATE_GAME = 2
STATE_INSTR = 3
STATE_MENU = 4

state = STATE_MAIN

circleR = 10
    
## section 1 
#s1X = 800
#s1Y = random.randint(200,270)
#s1Speed = random.randrange(3,10)
#s1Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
#s1length = random.randint(20,50)
#s1height = random.randint(20,50)

## section 2
#s2X = 800
#s2Y = random.randint(270,340)
#s2Speed = random.randrange(3,10)
#s2Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
#s2length = random.randint(20,50)
#s2height = random.randint(20,50)

## section 3
#s3X = 800
#s3Y = random.randint(340,410)
#s3Speed = random.randrange(3,10)
#s3Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
#s3length = random.randint(20,50)
#s3height = random.randint(20,50)

## section 4
#s4X = 800
#s4Y = random.randint(410,480)
#s4Speed = random.randrange(3,10)
#s4Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # boolean for whether showing litter or not
#s4length = random.randint(20,50)
#s4height = random.randint(20,50)

## section 5 
#s5X = 800
#s5Y = random.randint(480,520)
#s5Speed = random.randrange(3,10)
#s5Litter = random.choice(['1','0','1','0','1','0','1','0','1','0']) # # boolean for whether showing litter or not
#s5length = random.randint(20,50)
#s5height = random.randint(20,50)
    

def distance(pt1x, pt1y, pt2x, pt2y):
    diffx = pt2x - pt1x
    diffy = pt2y - pt1y
    distSquared = diffx**2 + diffy**2
    return math.sqrt(distSquared)    

#adds litter to the game
def fillLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter
    for i in range(5):
        sX.append(800)
        sSpeed.append(random.randrange(1,2))
        sLitter.append(random.choice([1,1,1,0,1,0,1,0,1,0])) # # boolean for whether showing litter or not
        sLength.append(random.randint(20,40))
        sHeight.append(random.randint(20,40))
        sSection.append(random.choice([1,2,3,4,5]))
        
        if sSection[i] == 1:
            sY.append(random.randint(200,270))
        elif sSection[i] == 2:
            sY.append(random.randint(270,340))
        elif sSection[i] == 3:
            sY.append(random.randint(340,410))
        elif sSection[i] == 4:
            sY.append(random.randint(410,480))        
        elif sSection[i] == 5:
            sY.append(random.randint(480,520))
        print(sY[i])
    
#shows the litter on the screen
def addLitter():
    global mx, my
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter
    
    print("addLitter")
    
    # 1 first section (s1x,s1y, 200 <= s1y <= 270)
    pygame.draw.rect(screen, YELLOW,(0,200,800,70)) # section 1 background for illustrate
    print("frow the yellows")
    # 2 second section (s1x,s1y, 270 <= s1y <= 340)
    pygame.draw.rect(screen, WHITE,(0,270,800,70)) # section 1 background for illustrate
    
    # 3 third section (s1x,s1y, 340 <= s1y <= 410)
    pygame.draw.rect(screen, YELLOW,(0,340,800,70)) # section 1 background for illustrate 
    
    # 4 fourth section (s1x,s1y, 410 <= s1y <= 480)
    pygame.draw.rect(screen, WHITE,(0,410,800,70)) # section 1 background for illustrate
        
    # 5 fifth section (s1x,s1y, 480 <= s1y <= 550)
    pygame.draw.rect(screen, YELLOW,(0,480,800,70)) # section 1 background for illustrate
    
    for index in range(len(sLitter)):
        if sLitter[index] == 1:
            sX[index] -= sSpeed[index]
            pygame.draw.rect(screen, RED, (sX[index],sY[index],sLength[index],sHeight[index]))  
            #for i in range(5):
            #    litterPic = pygame.image.load("Garbage.png")
            #    litterPic = pygame.transform.scale(litterPic,(sLength[i],sHeight[i]))                
            #    screen.blit(litterPic,(sX[index],sY[index],sLength[index],sHeight[index]))
  
    
def resetLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter
    sX = []
    sY = []
    sSpeed = []
    sLitter = []
    sLength = []
    sHeight = []
    sSection = []    
    

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
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter    
    
    print("sdfsdfjhdPLAY GAME")
    screen.fill(BLACK)  # background
    
    pygame.mouse.set_visible(True)
    
    mx, my = pygame.mouse.get_pos()
    
    # Time as the game start:
    time = pygame.time.get_ticks() // 1000
    #print(time)
    
    # Menu part:
    pygame.draw.rect(screen,YELLOW,(350,0,100,50))
    
    # middle part(mouse follow):
    pygame.draw.rect(screen, WHITE,(0,200,width,350))
    if mx <= 0 :
        mx = 0
    elif mx >= 800 - fishPicWidth:
        mx = 800 - fishPicWidth
    if 0 <= mx <= 800 and 0 <= my <= 200:
        if 350 <= mx <= 450 and 0 <= my <= 50:
            pygame.mouse.set_visible(True)        
        else: 
            pygame.mouse.set_visible(False)
            my = 200
    elif 0 <= mx <= 800 and 550 - fishPicHeight<= my <= 600:
        pygame.mouse.set_visible(False)
        my = 550 - fishPicHeight
    
    addLitter()  
    # characters:               
    screen.blit(fishPic,(mx,my,100,100))    

    
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
            elif i == 1:
                state = STATE_GAME

            else:
                state = STATE_GAME   
    
    
running = True
myClock = pygame.time.Clock()

fillLitter()

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