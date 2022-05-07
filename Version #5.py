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

# picture
fishPicWidth = 55
fishPicHeight = 40
fishPic = pygame.image.load("Fish.png")
fishPic = pygame.transform.scale(fishPic,(fishPicWidth,fishPicHeight)) 

#litters
sX = []
sY = []
sSpeed = []
sLength = []
sHeight = []
sType = []
sRect = []

STATE_MAIN = 1
STATE_GAME = 2
STATE_INSTR = 3
STATE_MENU = 4

state = STATE_MAIN


def distance(pt1x, pt1y, pt2x, pt2y):
    diffx = pt2x - pt1x
    diffy = pt2y - pt1y
    distSquared = diffx**2 + diffy**2
    return math.sqrt(distSquared)    

#adds litter to the game
def fillLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType

    sX.append(800)
    sY.append(random.randint(200,550))
    sSpeed.append(random.randrange(8,20))
    sLength.append(random.randint(20,50))
    sHeight.append(random.randint(20,50))  
    sType.append(random.choice(['Garbage1', 'Garbage2', 'Garbage3', 'Garbage4', 'Garbage5']))
    sRect.append(pygame.Rect(sX[-1], sY[-1], sLength[-1], sHeight[-1]))
    
#shows the litter on the screen
def addLitter():
    global mx, my
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType
    
    for i in range(len(sX)):      
        if sType[i] == 'Garbage1':
            pygame.draw.rect(screen, RED, (sX[i],sY[i],sLength[i],sHeight[i])) 
            Garbage1 = pygame.image.load("Garbage1.png")
            Garbage1 = pygame.transform.scale(Garbage1,(sLength[i],sHeight[i]))                
            screen.blit(Garbage1,(sX[i],sY[i],sLength[i],sHeight[i]))
            sX[i] -= sSpeed[i]
        elif sType[i] == 'Garbage2':
            pygame.draw.rect(screen, RED, (sX[i],sY[i],sLength[i],sHeight[i])) 
            Garbage2 = pygame.image.load("Garbage2.png")
            Garbage2 = pygame.transform.scale(Garbage2,(sLength[i],sHeight[i]))                
            screen.blit(Garbage2,(sX[i],sY[i],sLength[i],sHeight[i]))
            sX[i] -= sSpeed[i]
        elif sType[i] == 'Garbage3':
            pygame.draw.rect(screen, RED, (sX[i],sY[i],sLength[i],sHeight[i])) 
            Garbage3 = pygame.image.load("Garbage3.png")
            Garbage3 = pygame.transform.scale(Garbage3,(sLength[i],sHeight[i]))              
            screen.blit(Garbage3,(sX[i],sY[i],sLength[i],sHeight[i]))
            sX[i] -= sSpeed[i]
        elif sType[i] == 'Garbage4':
            pygame.draw.rect(screen, RED, (sX[i],sY[i],sLength[i],sHeight[i])) 
            Garbage4 = pygame.image.load("Garbage4.png")
            Garbage4 = pygame.transform.scale(Garbage4,(sLength[i],sHeight[i]))                
            screen.blit(Garbage4,(sX[i],sY[i],sLength[i],sHeight[i]))
            sX[i] -= sSpeed[i]        
        else: 
            pygame.draw.rect(screen, RED, (sX[i],sY[i],sLength[i],sHeight[i])) 
            sType[i] == 'Garbage5'
            Garbage5 = pygame.image.load("Garbage5.png")
            Garbage5 = pygame.transform.scale(Garbage5,(sLength[i],sHeight[i]))                
            screen.blit(Garbage5,(sX[i],sY[i],sLength[i],sHeight[i]))
            sX[i] -= sSpeed[i]

def resetLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType
    sX = []
    sY = []
    sSpeed = []
    sLitter = []
    sLength = []
    sHeight = []
    sSection = []    
    sType = []

    sX.append(800)
    sY.append(random.randint(200,550))
    sSpeed.append(random.randrange(8,20))
    sLength.append(random.randint(20,50))
    sHeight.append(random.randint(20,50))
    sType.append(random.choice(['Garbage1', 'Garbage2', 'Garbage3', 'Garbage4', 'Garbage5']))

def drawScene(screen, mx, my, button):
    global state
    global totalTime
    
    screen.fill(BLACK)
    pygame.mouse.set_visible(True)
    
    totalTime = pygame.time.get_ticks()
    
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
    global gameTime, totaltime, interval 
    screen.fill(BLACK)  # background
    
    pygame.mouse.set_visible(True)
    
    mx, my = pygame.mouse.get_pos()
    
    gameTime = pygame.time.get_ticks()
    #if 0 <= totalTime <= 
    
    print(totalTime, gameTime, (gameTime - totalTime))
    if (gameTime - totalTime) %  30 == 0 :
        fillLitter()
        addLitter()     
        fillLitter()
        addLitter()        
        fillLitter()
        addLitter()
    
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
                resetLitter()
                fillLitter()
            elif i == 1:
                state = STATE_GAME
                resetLitter()
            else:
                state = STATE_GAME   
    
    
running = True
myClock = pygame.time.Clock()

for i in range(1):
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

    myClock.tick(100)

pygame.quit()