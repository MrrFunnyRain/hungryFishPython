import pygame
import random
import math           # import things from python library 
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
pygame.init()

SIZE = (width,height) = (800,600)                 # screen size 
screen = pygame.display.set_mode(SIZE)

fontHello = pygame.font.SysFont("Times New Roman",30)
fontBig = pygame.font.SysFont("Times New Roman",70)    # state words 

BLACK = (0,0,0)
WHITE = (255,255,255)                        # state colour
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
fishPic = pygame.image.load("fishPic.png")        # fish
fishPic = pygame.transform.scale(fishPic,(fishPicWidth,fishPicHeight)) 

pointWidth = 70
pointHeight = 58
pointPic = pygame.image.load("pointPic.png")      # fish cans
pointPic = pygame.transform.scale(pointPic, (pointWidth, pointHeight))

heartWidth = 45
heartHeight = 42
heartPic = pygame.image.load("heartPic.png")      # heart 
heartPic = pygame.transform.scale(heartPic, (heartWidth, heartHeight))

bombWidth = 45
bombHeight = 42
bombPic = pygame.image.load("bombPic.png")        # bomb
bombPic = pygame.transform.scale(bombPic, (bombWidth, bombHeight))

Garbage1 = pygame.image.load("Garbage1.png")
Garbage2 = pygame.image.load("Garbage2.png")
Garbage3 = pygame.image.load("Garbage3.png")      # garbages 
Garbage4 = pygame.image.load("Garbage4.png")
Garbage5 = pygame.image.load("Garbage5.png")

backgroundPic1 = pygame.image.load("backgroundPic1.png")    # backgounds 
backgroundPic2 = pygame.image.load("backgroundPic2.png")

# picture used in LOSE
losePic1 = pygame.image.load("losePic1.png")       
losePic2 = pygame.image.load("losePIc2.png")

# picture used in MAIN
mainPic = pygame.image.load("mainPic.png")

# picture used in INSTRUCTIONS
instrPic = pygame.image.load("instrPic.jpg")
mousePic = pygame.image.load("mousePic.png")

# picture used in WIN
winPic = pygame.image.load("winPic.jpg")

sTypes = [Garbage1,Garbage2,Garbage3,Garbage4,Garbage5] # types available 

#litters
sX = []
sY = []
sSpeed = []
sLength = []
sHeight = []                              # making lists for litters
sType = [] # type of the garbage chosed 
sRect = []
sCollide = []

# points
pX = []
pY = []
pLength = []
pHeight = []                             # making lists for points
pRect = []
pCollide = []
pTime = []

# heart
hX = []
hY = []
hLength = []
hHeight = []
hRect = []                              # making lists for hearts
hCollide = []
hTime = []

# bomb
bX = []
bY = []
bLength = []
bHeight = []
bRect = []                             # making lists for bombs
bCollide = []
bTime = []

# state stages
STATE_MAIN = 1
STATE_GAME = 2
STATE_INSTR = 3       
STATE_MENU = 4
STATE_LOSE = 5
STATE_WIN = 6

state = STATE_MAIN
totalTime = 0 
gameTime = 0               # timer
start1 = 0

newTime = 3000
numLitter = 1              # timer
numPoint = 1              

lifeCount = 5
pScore = 0          # counts 
clockCount = 80

def fillPoints():
    global mx, my
    global pX, pY, pLength, pHeight, pRect, pScore, pCollide, pTime, start1
    global lifeCount
    
    pX.append(random.randint(70,730))
    pY.append(random.randint(200, 520))             # filling lists for points 
    pLength.append(70)
    pHeight.append(56)
    pCollide.append(False)
    pTime.append(pygame.time.get_ticks())
    print("fill --- p time      ", pTime)
    pRect.append(pygame.Rect(pX[-1], pY[-1], pLength[-1], pHeight[-1]))
    
def addPoints():
    global mx, my
    global pX, pY, pLength, pHeight, pRect, pScore, pCollide, pTime, start1

    hitBox = pygame.Rect(mx, my, 55, 40)
    for i in range(len(pX)-1, -1, -1):   
        pRect[i] = pygame.Rect(pX[i], pY[i], pLength[i], pHeight[i])
        screen.blit(pointPic,pRect[i])              # add points on the screen 
        touched = hitBox.colliderect(pRect[i])

        if touched == 1:
            del pX[i]
            del pY[i]
            del pHeight[i]
            del pLength[i]
            del pTime[i]                          # disappear when two rect collide
            if pCollide[i] == False:
                pScore += 10  
                break

        elif touched != 1 and (pygame.time.get_ticks() - pTime[i]) >= 2000:
            print("tounched != 1         ", i, pTime[i] )
            del pX[i]
            del pY[i]
            del pLength[i]                        # delete if do not pick uo within 2000ms
            del pHeight[i] 
            del pTime[i] 
            
    if my<200:
        my=200    

def resetPoints():
    global pX, pY, pLength, pHeight, pRect, pScore, pCollide, pTime, start1
    pX = []
    pY = []
    pLength = []                                # reset lists for points 
    pHeight = []
    pRect = []
    pCollide = []
    pTime = []
    

    pX.append(random.randint(70,730))
    pY.append(random.randint(200, 520))
    pLength.append(70)
    pHeight.append(56)
    pCollide.append(False)
    pTime.append(pygame.time.get_ticks())
    
    pRect.append(pygame.Rect(pX[-1], pY[-1], pLength[-1], pHeight[-1]))
    
    

def fillHeart():
    global mx, my
    global hX, hY, hLength, hHeight, hRect, hCollide, hTime, start1
    global lifeCount
    
    hX.append(random.randint(70,730))
    hY.append(random.randint(200, 520))          # filling lists for hearts 
    hLength.append(70)
    hHeight.append(56)
    hCollide.append(False)
    hTime.append(pygame.time.get_ticks())
    
    hRect.append(pygame.Rect(hX[-1], hY[-1], hLength[-1], hHeight[-1]))
    
def addheart():
    global mx, my
    global hX, hY, hLength, hHeight, hRect, hCollide, hTime ,start1
    global lifeCount

    hitBox = pygame.Rect(mx, my, 55, 40)
    for i in range(len(hX)-1, -1, -1):   
        hRect[i] = pygame.Rect(hX[i], hY[i], hLength[i], hHeight[i])
        screen.blit(heartPic,hRect[i])
        touched = hitBox.colliderect(hRect[i])              # add hearts on the screen
        
        if touched == 1:
            del hX[i]
            del hY[i]
            del hHeight[i]
            del hLength[i]
            del hTime[i]                          # disappear when two rect collide
            if hCollide[i] == False:
                lifeCount += 1  
                break
        
        elif touched != 1 and (pygame.time.get_ticks() - hTime[i]) >= 2000:
            del hX[i]
            del hY[i]                       # delete if do not pick uo within 2000ms
            del hLength[i]
            del hHeight[i] 
            del hTime[i]         
        
        
    if my<200:
        my=200    

def resetHeart():
    global hX, hY, hLength, hHeight, hRect, hCollide, hTime, start1
    hX = []
    hY = []
    hLength = []
    hHeight = []
    hRect = []
    hCollide = []                              # reset lists for hearts
    hTime = []

    hX.append(random.randint(70,730))
    hY.append(random.randint(200, 520))
    hLength.append(70)
    hHeight.append(56)
    hCollide.append(False)
    hTime.append(pygame.time.get_ticks())
    
    hRect.append(pygame.Rect(hX[-1], hY[-1], hLength[-1], hHeight[-1]))
    
    
def fillBomb():
    global mx, my
    global bX, bY, bLength, bHeight, bRect, bCollide, bTime,start1
    global lifeCount
    
    bX.append(random.randint(70,730))
    bY.append(random.randint(200, 520))
    bLength.append(70)                        # filling lists for bombs 
    bHeight.append(56)
    bCollide.append(False)
    bTime.append(pygame.time.get_ticks())
    
    bRect.append(pygame.Rect(bX[-1], bY[-1], bLength[-1], bHeight[-1]))
    
def addBomb():
    global mx, my
    global bX, bY, bLength, bHeight, bRect, bCollide, bTime,start1
    global lifeCount

    hitBox = pygame.Rect(mx, my, 55, 40)
    for i in range(len(bX)-1, -1, -1):                # add bombs on the screen
        bRect[i] = pygame.Rect(bX[i], bY[i], bLength[i], bHeight[i])
        screen.blit(bombPic,bRect[i])
        touched = hitBox.colliderect(bRect[i])
        if touched == 1:
            del bX[i]
            del bY[i]
            del bHeight[i]
            del bLength[i]                     # disappear when two rect collide
            del bTime[i]
            if bCollide[i] == False:
                clearLitter()
                break
            
        elif touched != 1 and (pygame.time.get_ticks() - bTime[i]) >= 2000:
            del bX[i]
            del bY[i]             # delete if do not pick uo within 2000ms
            del bLength[i]
            del bHeight[i] 
            del bTime[i]    
        
    if my<200:
        my=200    

def resetBomb():
    global bX, bY, bLength, bHeight, bRect, bCollide, bTime,start1
    bX = []
    bY = []
    bLength = []
    bHeight = []
    bRect = []
    bCollide = []
    bTime = []                          # reset lists for bombs
    

    bX.append(random.randint(70,730))
    bY.append(random.randint(200, 520))
    bLength.append(70)
    bHeight.append(56)
    bCollide.append(False)
    bTime.append(pygame.time.get_ticks())
    
    bRect.append(pygame.Rect(bX[-1], bY[-1], bLength[-1], bHeight[-1]))


#adds litter to the game
def fillLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType, sCollide, sRect,start1
    global sTime

    sX.append(800)
    sY.append(random.randint(200,550)) 
    sSpeed.append(random.randrange(10,25))
    sLength.append(random.randint(20,50))  # filling lists for litters
    sHeight.append(random.randint(20,50)) 
    sCollide.append(False)
    
    
    chosed = random.randint(0, len(sTypes) - 1)
    sType.append(sTypes[chosed])
    
    sType[-1] = pygame.transform.scale(sType[-1],(sLength[-1],sHeight[-1])) 
    
    sRect.append(pygame.Rect(sX[-1], sY[-1], sLength[-1], sHeight[-1]))
    
    
#shows the litter on the screen
def addLitter():
    global mx, my
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType, sCollide, sRect,start1
    global lifeCount
    global sTime
    hitBox = pygame.Rect(mx, my, 55, 40)                         # add litters on the screen
    for i in range(len(sX)):   
        sX[i] -= sSpeed[i]
        sRect[i] = pygame.Rect(sX[i], sY[i], sLength[i], sHeight[i])
        screen.blit(sType[i],sRect[i])
        touched = hitBox.colliderect(sRect[i])
        if touched == 1:
            if sCollide[i] == False:
                lifeCount -= 1                             # check for colliding
                sCollide[i] = True
                break
            
    if my<200:
        my=200
    

def resetLitter():
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter, sType, sCollide, sRect,start1
    sX = []
    sY = []
    sSpeed = []                                         # reset lists for litters
    sLength = []
    sHeight = []
    sType = [] # type of the garbage chosed
    sRect = []
    sCollide = []

    sX.append(800)
    sY.append(random.randint(200,550)) 
    sSpeed.append(random.randrange(10,25))
    sLength.append(random.randint(20,50))
    sHeight.append(random.randint(20,50)) 
    sCollide.append(False)
    chosed = random.randint(0, len(sTypes) - 1)
    sType.append(sTypes[chosed])
    
    sType[-1] = pygame.transform.scale(sType[-1],(sLength[-1],sHeight[-1])) 
    
    sRect.append(pygame.Rect(sX[-1], sY[-1], sLength[-1], sHeight[-1]))
    
def clearLitter():
    del sX[:]
    del sY[:]
    sSpeed[:]                                   # clear all the litter on the screen by deleting all the objects in the list
    sLength[:] 
    sHeight[:]
    sType[:] # type of the garbage chosed
    sRect[:] 
    sCollide[:] 
    
def drawScene(screen, mx, my, button):
    global state
    global totalTime, enterTime, start1
    global mainPic

    screen.fill(WHITE)
    mainPic = pygame.transform.scale(mainPic, (800, 600))           # background
    screen.blit(mainPic, (0,0,800,600))
    
    pygame.mouse.set_visible(True)
    
    totalTime = pygame.time.get_ticks()                  # find time that leave main stage
    totalTime1 = pygame.time.get_ticks()//1000
    
    pygame.draw.rect(screen, RED, (100,145,610,80), 5) # title
    string1 = "HELP FISH GOING HOME"
    text1 = fontBig.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(110,165,250,80))       
    
    pygame.draw.rect(screen, YELLOW, (600,275,150,40), 5) # statr game
    string1 = "RUBY FANG"
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(615,290,150,40))       
    
    pygame.draw.rect(screen, YELLOW, (350,475,150,60)) # statr game
    string1 = "START GAME"
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(360,495,150,60))    

    pygame.draw.rect(screen, YELLOW, (580,475,170,60)) # instructions
    string2 = "INSTRUCTIONS"
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(590,495,150,60))   
    
def playGame(screen, mx, my, button):
    global state, STATE_WIN
    global sX, sY, sSpeed, sLength, sHeight, sSection, sLitter
    global pX, pY, pLength, pHeight, pRect
    global hX, hY, hLength, hHeight, hRect, hCollide
    global backgroundPic1, backgroundPic2
    global lifeCount
    global newTime, enterTime, gameTime, totalTime, clockCount, gameTime1, start1
    global numLitter, numPoint
    global pScore
    
    backgroundPic1 = pygame.transform.scale(backgroundPic1, (800, 200))
    screen.blit(backgroundPic1,(0,0,800,200))
    backgroundPic2 = pygame.transform.scale(backgroundPic2, (800, 400))     # background
    screen.blit(backgroundPic2,(0,200,800,400))
    
    pygame.mouse.set_visible(False)
    
    mx, my = pygame.mouse.get_pos()
    
    gameTime = pygame.time.get_ticks()                 # timer: find the time current time in game stage 
    gameTime1 = pygame.time.get_ticks()//1000
    
    
    # clock
    if (pygame.time.get_ticks()) - start1 >= 1000:
        clockCount -= 1                                # clock (counting down from 80)
        start1 = pygame.time.get_ticks()
    
    pygame.draw.circle(screen, BLACK, (741, 38), 23)
    text1 = fontHello.render(str(clockCount),0,WHITE)
    screen.blit(text1,pygame.Rect(730,30,70,70))           

    
    addLitter()
    addPoints()
    addheart()                                          # add list 
    addBomb()
    #if gameTime - totalTime > newTime: # newTime = 3000
        #for i in range(numLitter): # numLitter = 1
            #fillLitter()
            #fillLitter()
            #fillLitter()
        #for p in range(numPoint):                       # A way that Mr.Van Rooyen taught me
            #fillPoints()
        #totalTime = pygame.time.get_ticks()
        #if (gameTime - enterTime) % 40 == 0:
            #numLitter += 1
            ##if (gameTime - totalTime) %  40 == 0 :
        
        ##newTime *= 0.95
    if 60 <= clockCount <= 80:
        if (gameTime - totalTime) %  40 == 0 :
            fillLitter()                                 # fill the lists and restrict different frequncies for different phases
            fillLitter()     
            fillLitter()
    elif 30 <=  clockCount <= 60:
        if (gameTime - totalTime) %  36 == 0 :        
            fillLitter()                             
            fillLitter()   
            fillLitter()
    elif 0 <=  clockCount  <= 30:
        if (gameTime - totalTime) %  30 == 0 :
            fillLitter()    
            fillLitter()     
            fillLitter()
    elif clockCount <= 0:# 80000
        state = STATE_WIN
        resetLitter()
        resetPoints()
        resetHeart()                               # Win page 
        resetBomb()
        clockCount = 80
        #pScore = 0
        lifeCount = 5
    
    # Points set
    if (gameTime - totalTime) %  90 == 0 :
        fillPoints()                          # fill list for points 
    
    # Hearts set
    if (gameTime - totalTime) %  361 == 0 and 0 <=  clockCount  <= 60:
        fillHeart()                           # fill lists for heart
    
    # Bomb set
    if (gameTime - totalTime) %  330 == 0 and 0 <=  clockCount  <= 60:
        fillBomb()                          # fill lists for bomb
    
    # Menu part:
    pygame.draw.rect(screen,YELLOW,(350,0,100,50))
    string1 = "MENU"                                  
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(370,15,120,70))  
    
    
    pygame.draw.circle(screen,BLUE,(55,53),35)
    screen.blit(fishPic,(30,30,100,100))
    pygame.draw.rect(screen, WHITE, (100,60,150,30),2)
    
    if lifeCount >= 5:
        pygame.draw.rect(screen, RED, (101,61,149,29))
    elif lifeCount == 4:
        pygame.draw.rect(screen, RED, (101,61,119,29))
    elif lifeCount == 3:
        pygame.draw.rect(screen, RED, (101,61,89,29))       # restricting and calculating Hp
    elif lifeCount == 2:
        pygame.draw.rect(screen, RED, (101,61,59,29))
    elif lifeCount == 1:
        pygame.draw.rect(screen, RED, (101,61,29,29))  
    else:
        state = STATE_LOSE
    
    # point got
    pygame.draw.rect(screen, YELLOW, (100,20,150,30))
    text = fontHello.render("Points: " + str(pScore), 0, BLACK)     # calculating points
    screen.blit(text,pygame.Rect(110,25,150,70))  
    
    # middle part(mouse follow):
    if mx <= 0 :
        mx = 0
    elif mx >= 800 - fishPicWidth:
        mx = 800 - fishPicWidth                         # setting up the control part: fish follow mouse
    if 0 <= mx <= 800 and 0 <= my <= 200:
        if 350 <= mx <= 450 and 0 <= my <= 50:
            pygame.mouse.set_visible(True)        
        else: 
            pygame.mouse.set_visible(False)
            my = 200
    elif 0 <= mx <= 800 and 550 - fishPicHeight<= my <= 600:
        pygame.mouse.set_visible(False)
        my = 550 - fishPicHeight
    
    # characters:               
    screen.blit(fishPic,(mx,my,100,100))                 

    
def drawMenu(screen, mx, my, button):
    global state, pScore,start1
    screen.fill(BLACK)        
    pygame.draw.rect(screen, WHITE, (200,150,400,300))
    
    pygame.mouse.set_visible(True)   # mouse visible 
    
    for i in range(len(menuRectList)):
        menuRectangle = menuRectList[i] 
        pygame.draw.rect(screen, GREEN, menuRectangle)                # draw small menu:  
        text = fontHello.render(menuTitleList[i] , 1, (255, 0, 0))	#                 back to home page 
        screen.blit(text, menuRectangle)	                        #                 try again 
        
        if menuRectangle.collidepoint(mx, my) and button == 1:	        #                 resume 
            if i == 0:
                state = STATE_MAIN
                resetLitter()
                resetPoints()
                resetHeart()                        # reset all the variables when click back to main stage
                resetBomb()
                clockCount = 80
                pScore = 0
                lifeCount = 5
            elif i == 1:
                state = STATE_GAME
                resetLitter()
                resetPoints()
                resetHeart()                            # reset all the variables and restart the game
                resetBomb()
                clockCount = 80
                pScore = 0
                lifeCount = 5
            else:
                state = STATE_GAME                 # start game

def instrPage(screen,mx,my,button):
    global start1
    global instrPic, mousePic, fishPic, Garbage1,Garbage2, Garbage3, Garbage4, Garbage5, heartPic, pointPic, bombPic
    instrPic = pygame.transform.scale(instrPic, (800,600))
    screen.blit(instrPic,(0, 0, 800, 600))                         # background
    pygame.draw.rect(screen, WHITE,(80,60,620,460))
    
    # first instruction about using mouse:
    string1 = "Use mouse to control fish. "
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(120,90,150,60))    
    mousePic = pygame.transform.scale(mousePic, (50, 50))
    screen.blit(mousePic,(450,70,50,50))
    fishPic = pygame.transform.scale(fishPic, (60, 50)) # fish
    screen.blit(fishPic,(520,70, 50, 50))    

    # second instruction about litters:
    string2 = "Do hit on any litter, it will decrease your Hp scale."
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(120,120,150,60))   
    string2 = "Your highest Hp scale is 5, you will lose the game "
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(120,150,150,60))   
    string2 = "if it becomes zero."
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(120,180,150,60))     
    Garbage1 = pygame.transform.scale(Garbage1, (50, 50)) # garbage 
    screen.blit(Garbage1,(120,210, 50, 50))
    Garbage2 = pygame.transform.scale(Garbage2, (50, 50))  # garbage 
    screen.blit(Garbage2,(190,210, 50, 50))
    Garbage3 = pygame.transform.scale(Garbage3, (50, 50))  # garbage 
    screen.blit(Garbage3,(260,210, 50, 50))
    Garbage4 = pygame.transform.scale(Garbage4, (50, 50))  # garbage 
    screen.blit(Garbage4,(330,210, 50, 50))
    Garbage5 = pygame.transform.scale(Garbage5, (50, 50))  # garbage 
    screen.blit(Garbage5,(400,210, 50, 50))
    
    # third instruction about bomb, points and heart:
    string2 = "You want to collect fish cans for points,  " # fish cans for points
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(120,260,150,60))   
    pointPic = pygame.transform.scale(pointPic, (50, 50))  
    screen.blit(pointPic,(530, 230, 50, 50))
    
    string2 = "to pick up hearts for returning blood, "    # heart for returning blood 
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(120,290,150,60))   
    heartPic = pygame.transform.scale(heartPic, (50, 50))  
    screen.blit(heartPic,(580,  270, 50, 50))    
    
    string2 = "to pick up bombs for clearing garbages. "   # bomb for clearing garbages
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(120,320,150,60))     
    bombPic = pygame.transform.scale(bombPic, (50, 50))  
    screen.blit(bombPic,(515, 295, 50, 50))    
    
    pygame.draw.rect(screen, YELLOW, (285,470,120,70)) # button for playing game
    string1 = "PLAY"
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(320,485,120,70)) 
    string2 = "GAME"
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(310,505,120,70))       

def losePage(screen,mx,my,button):
    global losePic1, losePic2, start1
    
    pygame.mouse.set_visible(True)       
    
    screen.fill(WHITE)
    losePic2 = pygame.transform.scale(losePic2, (800,350))
    screen.blit(losePic2,(0,250,800,350))
    losePic1 = pygame.transform.scale(losePic1, (300,320))      # background 
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
    
def winPage():
    global winPic
    global pScore, start1
    
    pygame.mouse.set_visible(True)  
    
    winPic = pygame.transform.scale(winPic, (800, 600))         # backgound 
    screen.blit(winPic,(0,0,800,600))        
    
    pygame.draw.rect(screen, WHITE, (245,155,350,60))           # strings 
    string1 = "YOU WIN!!!!!"
    text1 = fontBig.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(270,165,150,60))    
    
    pygame.draw.rect(screen, WHITE, (165,235,520,60))
    string2 = "CONGRATULATION"
    text2 = fontBig.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(190,245,150,60))       
    
    pygame.draw.rect(screen, WHITE, (165,315,520,60))
    text3 = fontBig.render("Your score is " + str(pScore), 0, BLACK)
    screen.blit(text3,pygame.Rect(190,325,150,60))      
    
    pygame.draw.rect(screen, YELLOW, (285,470,120,70)) # play again
    string1 = "PLAY"
    text1 = fontHello.render(string1,0,BLACK)
    screen.blit(text1,pygame.Rect(320,485,120,70)) 
    string2 = "AGAIN"
    text2 = fontHello.render(string2,0,BLACK)
    screen.blit(text2,pygame.Rect(310,505,120,70))     
    
    pygame.draw.rect(screen, YELLOW, (445,470,120,70)) # back to main stage
    string3 = "BACK TO"
    text3 = fontHello.render(string3,0,BLACK)
    screen.blit(text3,pygame.Rect(465,485,120,70)) 
    string4 = "MAIN MENU"
    text4 = fontHello.render(string4,0,BLACK)
    screen.blit(text4,pygame.Rect(448,505,120,70))      
    
    pygame.draw.rect(screen, YELLOW, (605,470,120,70)) # quit
    string5 = "QUIT"
    text5 = fontHello.render(string5,0,BLACK)
    screen.blit(text5,pygame.Rect(640,495,120,70))     
    
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
            if 350  <= mx <= 450  and 0 <= my <= 50 and state == STATE_GAME:
                lifeCount = 5                                                         # reset variables and change state 
                state = STATE_MENU
            elif 285 <= mx <= 405 and 470 <= my <= 540 and state == STATE_LOSE:
                resetLitter()
                resetPoints()
                resetHeart()
                resetBomb()                                                  # reset variables and change state 
                clockCount = 80
                pScore = 0
                lifeCount = 5
                state = STATE_GAME
            elif 445 <= mx <= 565 and 470 <= my <= 540 and state == STATE_LOSE: 
                lifeCount = 5                                                  # reset variables and change state 
                state = STATE_MAIN
            elif 605 <= mx and 470 <= my <= 540 and state == STATE_LOSE: 
                running = False                                                  # quit game
            elif 350 <= mx <= 500 and 475 <= my <= 535 and state == STATE_MAIN:
                lifeCount = 5                                                  # reset variables and change state 
                state = STATE_GAME
                start1 = pygame.time.get_ticks()
            elif 580 <= mx <= 750 and 475 <= my <= 535 and state == STATE_MAIN:
                state = STATE_INSTR                                              # change state to instruction 
                
            elif 285 <= mx <= 405 and 470 <= my <= 540 and state == STATE_WIN: # play again
                resetLitter()
                resetPoints()
                resetHeart()
                resetBomb()                                                  # reset variables and change state 
                clockCount = 80
                pScore = 0
                lifeCount = 5
                state = STATE_GAME
            elif 445 <= mx <= 565 and 470 <= my <= 540 and state == STATE_WIN: 
                lifeCount = 5                                                  # reset variables and change state 
                state = STATE_MAIN
            elif 605 <= mx and 470 <= my <= 540 and state == STATE_WIN: 
                running = False                                                                # quit game
            elif 285 <= mx <= 405 and 470 <= my <= 540 and state == STATE_INSTR: # play again
                resetLitter()
                resetPoints()
                resetHeart()                                                  # reset variables and change state 
                resetBomb()
                clockCount = 80
                pScore = 0
                lifeCount = 5
                state = STATE_GAME
    # traffic cop
    if state == STATE_MAIN:
        resetLitter()
        resetPoints()
        resetHeart()
        resetBomb()                                                            # state different mission for different stages 
        clockCount = 80
        pScore = 0
        lifeCount = 5
        drawScene(screen, mx, my, button)
    elif state == STATE_GAME:
        playGame(screen, mx, my, button)     
    elif state == STATE_MENU:
        drawMenu(screen,mx,my,button)
    elif state == STATE_LOSE:
        losePage(screen,mx,my,button)
    elif state == STATE_INSTR:
        instrPage(screen,mx,my,button)
    elif state == STATE_WIN:
        winPage()
    pygame.display.flip()

    myClock.tick(1000)

pygame.quit()
