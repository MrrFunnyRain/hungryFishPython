import pygame
import random
import math
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
pygame.init()

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

# picture used in GAME
fishPicWidth = 55
fishPicHeight = 40
fishPic = pygame.image.load("fishPic.png")
fishPic = pygame.transform.scale(fishPic,(fishPicWidth,fishPicHeight)) 

pointWidth = 70
pointHeight = 58
pointPic = pygame.image.load("pointPic.png")
pointPic = pygame.transform.scale(pointPic, (pointWidth, pointHeight))

Garbage1 = pygame.image.load("Garbage1.png")
Garbage2 = pygame.image.load("Garbage2.png")
Garbage3 = pygame.image.load("Garbage3.png")
Garbage4 = pygame.image.load("Garbage4.png")
Garbage5 = pygame.image.load("Garbage5.png")

backgroundPic1 = pygame.image.load("backgroundPic1.png")
backgroundPic2 = pygame.image.load("backgroundPic2.png")

# picture used in LOSE
losePic1 = pygame.image.load("losePic1.png")
losePic2 = pygame.image.load("losePIc2.png")

# picture used in MAIN
mainPic = pygame.image.load("mainPic.png")

# picture used in INSTRUCTIONS
instrPic = pygame.image.load("instrPic.jpg")
mousePic = pygame.image.load("mousePic.png")

sTypes = [Garbage1,Garbage2,Garbage3,Garbage4,Garbage5] # 有什么Type 选项 types available 

#litters
sX = []
sY = []
sSpeed = []
sLength = []
sHeight = []
sType = [] # type of the garbage chosed
sRect = []
sCollide = []

# points
pX = []
pY = []
pLength = []
pHeight = []
pRect = []

STATE_MAIN = 1
STATE_GAME = 2
STATE_INSTR = 3
STATE_MENU = 4
STATE_LOSE = 5

state = STATE_GAME
totalTime = 0
gameTime = 0

lifeCount = 5


def fillPoints():
    global mx, my
    global pX, pY, pLength, pHeight, pRect
    global lifeCount
    
    pX.append(random.randint(30,770))
    pY.append(random.randint(230, 520))
    pLength.append(70)
    pHeight.append(56)
    pRect.append(pygame.Rect(pX[-1], pY[-1], pLength[-1], pHeight[-1]))
    
def addPoints():
    global pX, pY, pLength, pHeight, pRect
    print("sdfhbshdfbhjsdbfsbfjshdfb", pX)
    for i in range(len(pX)):  
        pRect[i] = pygame.Rect(pX[i], pY[i], pLength[i], pHeight[i])
        screen.blit(pointPic,pRect[i])    
    
def resetPoints():
    global pX, pY, pLength, pHeight, pRect
    pX = []
    pY = []
    pLength = []
    pHeight = []
    pRect = []

    pX.append(random.randint(30,770))
    pY.append(random.randint(230, 520))
    pLength.append(70)
    pHeight.append(56)
    pRect.append(pygame.Rect(pX[-1], pY[-1], pLength[-1], pHeight[-1]))
    
    

#adds litter to the game
def fillLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType, sCollide

    sX.append(800)
    sY.append(random.randint(200,550))
    sSpeed.append(random.randrange(8,20))
    sLength.append(random.randint(20,50))
    sHeight.append(random.randint(20,50)) 
    sCollide.append(False)
    
    
    chosed = random.randint(0, len(sTypes) - 1)
    sType.append(sTypes[chosed])
    
    sType[-1] = pygame.transform.scale(sType[-1],(sLength[-1],sHeight[-1])) 
    
    sRect.append(pygame.Rect(sX[-1], sY[-1], sLength[-1], sHeight[-1]))
    
    
#shows the litter on the screen
def addLitter():
    global mx, my
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType, sCollide
    global lifeCount
    hitBox = pygame.Rect(mx, my, 55, 40)
    for i in range(len(sX)):   
        sX[i] -= sSpeed[i]
        sRect[i] = pygame.Rect(sX[i], sY[i], sLength[i], sHeight[i])
        #pygame.draw.rect(screen, RED, (sX[i],sY[i],sLength[i],sHeight[i])) 
        screen.blit(sType[i],sRect[i])
        touched = hitBox.colliderect(sRect[i])
        if touched == 1:
            if sCollide[i] == False:
                lifeCount -=1
                sCollide[i] = True
                break
    
    if my<200:
        my=200
    

def resetLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType
    sX = []
    sY = []
    sSpeed = []
    sLength = []
    sHeight = []
    sType = [] # type of the garbage chosed
    sRect = []
    sCollide = []

    sX.append(800)
    sY.append(random.randint(200,550))
    sSpeed.append(random.randrange(8,20))
    sLength.append(random.randint(20,50))
    sHeight.append(random.randint(20,50)) 
    sCollide.append(False)
    chosed = random.randint(0, len(sTypes) - 1)
    sType.append(sTypes[chosed])
    
    sType[-1] = pygame.transform.scale(sType[-1],(sLength[-1],sHeight[-1])) 
    
    sRect.append(pygame.Rect(sX[-1], sY[-1], sLength[-1], sHeight[-1]))
    
    
def drawScene(screen, mx, my, button):
    global state
    global totalTime
    global mainPic
    
    screen.fill(WHITE)
    mainPic = pygame.transform.scale(mainPic, (800, 600))
    screen.blit(mainPic, (0,0,800,600))
    
    pygame.mouse.set_visible(True)
    
    totalTime = pygame.time.get_ticks()

    pygame.draw.rect(screen, YELLOW, (350,475,150,60)) # statr game
    string1 = "START GAME"
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(360,495,150,60))    

    pygame.draw.rect(screen, YELLOW, (580,475,170,60)) # instructions
    string2 = "INSTRUCTIONS"
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(590,495,150,60))   
    
def playGame(screen, mx, my, button):
    global state
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter  
    global pX, pY, pLength, pHeight, pRect
    global gameTime, totaltime, interval 
    global backgroundPic1, backgroundPic2
    global lifeCount
    
    backgroundPic1 = pygame.transform.scale(backgroundPic1, (800, 200))
    screen.blit(backgroundPic1,(0,0,800,200))
    backgroundPic2 = pygame.transform.scale(backgroundPic2, (800, 400))
    screen.blit(backgroundPic2,(0,200,800,400))
    
    pygame.mouse.set_visible(False)
    
    mx, my = pygame.mouse.get_pos()
    
    gameTime = pygame.time.get_ticks()
    
    #print(totalTime, gameTime)
    phase1 = False 
    phase2 = False
    phase3 = False
    if 0 <= (gameTime - totalTime) <= 20000:
        if (gameTime - totalTime) %  40 == 0 :
            phase1 = True
            fillLitter()
            addLitter()     
            fillLitter()
            addLitter()        
            fillLitter()
            addLitter()
        #elif (gameTime - totalTime) %  40 == 0 :
            fillPoints()
            addPoints()
            
    elif 23000 <=  (gameTime - totalTime) <= 50000:
        pygame.draw.rect(screen, WHITE, (400,400,89,100))
        if (gameTime - totalTime) %  35 == 0 :
            phase1 = False
            phase2 = True            
            fillLitter()
            addLitter()     
            fillLitter()
            addLitter()        
    elif 50000 <=  (gameTime - totalTime)  <= 90000:
        pygame.draw.rect(screen, BLACK, (400,400,89,100))
        if (gameTime - totalTime) %  30 == 0 :
            phase1 = False
            phase2 = False
            phase3 = True
            fillLitter()
            addLitter()     
            fillLitter()
            addLitter()        

  
    # Menu part:
    pygame.draw.rect(screen,YELLOW,(350,0,100,50))
    string1 = "MENU"
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(370,15,120,70))  
    
    pygame.draw.circle(screen,BLUE,(55,53),35)
    screen.blit(fishPic,(30,30,100,100))
    pygame.draw.rect(screen, WHITE, (100,60,150,30),2)
    
    if lifeCount == 5:
        pygame.draw.rect(screen, RED, (101,61,149,29))
    elif lifeCount == 4:
        pygame.draw.rect(screen, RED, (101,61,119,29))
    elif lifeCount == 3:
        pygame.draw.rect(screen, RED, (101,61,89,29))
    elif lifeCount == 2:
        pygame.draw.rect(screen, RED, (101,61,59,29))
    elif lifeCount == 1:
        pygame.draw.rect(screen, RED, (101,61,29,29))    
    else:
        state = STATE_LOSE
    
    pygame.draw.rect(screen, YELLOW, (100,20,30,30))
    
    # middle part(mouse follow):
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
    addPoints()  

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
                resetPoints()
            else:
                state = STATE_GAME   

def instrPage(screen,mx,my,button):
    global instrPic
    instrPic = pygame.transform.scale(instrPic, (800,600))
    screen.blit(instrPic,(0, 0, 800, 600)) 
    pygame.draw.rect(screen, WHITE,(80,60,620,460))
    
    mousePic = pygame.transform.scale(mousePic, (800, 200))
    screen.blit(mousePic,(0,0,800,200))
    fishPic = pygame.transform.scale(fishPic, (800, 400))
    screen.blit(fishPic,(0,200,800,400))
    Garbage1 = pygame.transform.scale(Garbage1, (800, 200))
    screen.blit(Garbage1,(0,0,800,200))
    Garbage2 = pygame.transform.scale(Garbage2, (800, 400))
    screen.blit(Garbage2,(0,200,800,400))
    Garbage3 = pygame.transform.scale(Garbage3, (800, 200))
    screen.blit(Garbage3,(0,0,800,200))
    Garbage4 = pygame.transform.scale(Garbage4, (800, 400))
    screen.blit(Garbage4,(0,200,800,400))
    Garbage5 = pygame.transform.scale(Garbage5, (800, 200))
    screen.blit(Garbage5,(0,0,800,200))
   
    

def losePage(screen,mx,my,button):
    global losePic1, losePic2
    
    pygame.mouse.set_visible(True)
    
    screen.fill(WHITE)
    losePic2 = pygame.transform.scale(losePic2, (800,350))
    screen.blit(losePic2,(0,250,800,350))
    losePic1 = pygame.transform.scale(losePic1, (300,320))
    screen.blit(losePic1,(240,100,200,400))
    
    pygame.draw.rect(screen, GREEN, (285,470,120,70)) # play again
    string1 = "PLAY"
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(320,485,120,70)) 
    string2 = "AGAIN"
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(310,505,120,70))  
    
    pygame.draw.rect(screen, GREEN, (445,470,120,70)) # back to main stage
    string3 = "BACK TO"
    text3 = fontHello.render(string3,0,BLACK)
    screen.blit(text3,pygame.Rect(465,485,120,70)) 
    string4 = "MAIN MENU"
    text4 = fontHello.render(string4,0,BLACK)
    screen.blit(text4,pygame.Rect(448,505,120,70))  
    
    
    pygame.draw.rect(screen, GREEN, (605,470,120,70)) # quit
    string5 = "QUIT"
    text5 = fontHello.render(string5,0,BLACK)
    screen.blit(text5,pygame.Rect(640,495,120,70))     
    
    

    
running = True
myClock = pygame.time.Clock()

#for i in range(10):
    #fillPoints()
    #print("I am working", pRect[i])

#fillPoints()
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
            if 350  <= mx <= 450  and 0 <= my <= 50 and state == STATE_GAME:
                lifeCount = 5
                state = STATE_MENU
            elif 285 <= mx <= 405 and 470 <= my <= 540 and state == STATE_LOSE:
                lifeCount = 5
                resetLitter()
                resetPoints()
                state = STATE_GAME
            elif 445 <= mx <= 565 and 470 <= my <= 540 and state == STATE_LOSE: 
                lifeCount = 5
                state = STATE_MAIN
            elif 605 <= mx and 470 <= my <= 540 and state == STATE_LOSE: 
                running = False
            elif 350 <= mx <= 500 and 475 <= my <= 535 and state == STATE_MAIN:
                lifeCount = 5
                state = STATE_GAME
            elif 580 <= mx <= 750 and 475 <= my <= 535 and state == STATE_MAIN:
                state = STATE_INSTR
       
    
    # traffic cop
    if state == STATE_MAIN:
        lifeCount = 5
        resetPoints()
        resetLitter()
        drawScene(screen, mx, my, button)
    elif state == STATE_GAME:
        playGame(screen, mx, my, button)     
    elif state == STATE_MENU:
        drawMenu(screen,mx,my,button)
    elif state == STATE_LOSE:
        losePage(screen,mx,my,button)
    elif state == STATE_INSTR:
        instrPage(screen,mx,my,button)
    pygame.display.flip()

    myClock.tick(1000)

pygame.quit()