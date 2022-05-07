import pygame
import random
import math
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
pygame.init()
SIZE = (width,height) = (800,600)
screen = pygame.display.set_mode(SIZE)

fontHello = pygame.font.SysFont("Times New Roman",30)

GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
circleX = 400
showCircle = True

testRect1 = pygame.Rect(200, 100, 200, 100)
testRect2 = pygame.Rect(200, 300, 200, 100)
rectList = [testRect1, testRect2]
titleList = ["Play Game", "Instructions"]

STATE_MAIN = 1
STATE_GAME = 2
STATE_INSTR = 3

state = STATE_MAIN

herox = width//2
heroy = height//2
heroRadius = 10
heroSpeed = 5
heroEats = 0
winEats = 40

foodx = 0
foody = 0
foodRadius = 10

enemyxList = []
enemyyList = []
enemyRadius = heroRadius
enemySpeed = 0

gameTime = 0

KEY_LEFT = False
KEY_RIGHT = False
KEY_UP = False
KEY_DOWN = False

def distance(pt1x, pt1y, pt2x, pt2y):
    diffx = pt2x - pt1x
    diffy = pt2y - pt1y
    distSquared = diffx**2 + diffy**2
    return math.sqrt(distSquared)

def circleCollision(circle1x, circle1y, circle2x, circle2y, radius1, radius2):
    dist = distance(circle1x, circle1y, circle2x, circle2y)
    
    if dist <= radius1 + radius2:
        return True
    return False

def resetHero ():
    global herox, heroy, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP, heroEats
    herox = width//2
    heroy = height//2
    heroEats = 0
    KEY_DOWN = False
    KEY_LEFT = False
    KEY_RIGHT = False
    KEY_UP = False

def addEnemy():
    global enemyxList, enemyyList
    xStart = random.randint(foodRadius, width-enemyRadius)
    enemyxList.append(xStart)
    yStart= random.randint(foodRadius, height - enemyRadius)    
    enemyyList.append(yStart)
    

def resetEnemy():
    global enemyxList, enemyyList, enemySpeed
    enemyxList = []
    enemyyList = []
    xStart = random.randint(foodRadius, width-enemyRadius)
    enemyxList.append(xStart)
    yStart= random.randint(foodRadius, height - enemyRadius)    
    enemyyList.append(yStart)
    enemySpeed = 1
    
    
def resetFood():
    global foodx, foody
    foodx = random.randint(foodRadius, width-foodRadius)
    foody = random.randint(foodRadius, height - foodRadius)    
     
    
# here's the game
def playGame(screen, mx, my, button):
    global state, herox, heroy, heroRadius, enemyx, enemyy, heroEats
    
    # drawing all characters/enemies/whatever
    pygame.draw.rect(screen, RED, (0, 0, width, height))
    text = fontHello.render("Food Eaten: " + str(heroEats) , 1, BLACK)	
    screen.blit(text, (2*width//3, 0, 100, 10))
    
    points = (pygame.time.get_ticks() - gameTime) // 1000
    text = fontHello.render("Points: " + str(points) , 1, BLACK)	
    screen.blit(text, (width//3, 0, 100, 10))
    
       
    pygame.draw.circle(screen, GREEN, (herox, heroy), heroRadius)
    pygame.draw.circle(screen, BLUE, (foodx, foody), foodRadius)
    
    for i in range(len(enemyxList)):
        pygame.draw.circle(screen, BLACK, (enemyxList[i], enemyyList[i]), enemyRadius)
    # check for change to characters/enemies/whatever
    if circleCollision(herox, heroy, foodx, foody, heroRadius, foodRadius):
        heroRadius += 1
        heroEats += 1
        resetFood()
        addEnemy()
    
    for i in range(len(enemyxList)):
        if circleCollision(herox, heroy, enemyxList[i], enemyyList[i], heroRadius, enemyRadius):
            state = STATE_MAIN
        
    if heroEats >= winEats:
        state = STATE_MAIN
    
    # movement of charaters/enemies/whatever
    if KEY_LEFT == True and herox - heroRadius > 0:
        herox -= heroSpeed
    elif KEY_RIGHT == True and herox + heroRadius < width:
        herox += heroSpeed
    elif KEY_UP == True and heroy - heroRadius > 0:
        heroy -= heroSpeed
    elif KEY_DOWN == True and heroy + heroRadius < height:
        heroy += heroSpeed
    
    for i in range(len(enemyxList)):
        if enemyxList[i] > herox:
            enemyxList[i] -= enemySpeed
        if enemyxList[i] < herox:
            enemyxList[i] += enemySpeed
        if enemyyList[i] < heroy:
            enemyyList[i] += enemySpeed
        if enemyyList[i] > heroy:
            enemyyList[i] -= enemySpeed
            
    
        
    if herox - heroRadius <= 0 or herox + heroRadius >= width or heroy - heroRadius == 0 or heroy + heroRadius == height:
        state = STATE_MAIN
        
    

# clear the screen, draw off screen and then display
def drawScene(screen, mx, my, button):
    global state, foodx, foody
    screen.fill(BLACK)
    
    for i in range(len(rectList)):
        rectangle = rectList[i]
        pygame.draw.rect(screen, GREEN, rectangle)
        text = fontHello.render(titleList[i] , 1, (255, 0, 0))	
        screen.blit(text, rectangle)
        
        if rectangle.collidepoint(mx, my) and button == 1:
            if i == 0:
                state = STATE_GAME
                resetFood()
                resetHero()
                resetEnemy()
                gameTime = pygame.time.get_ticks()
                print(gameTime)
            else:
                state = STATE_INSTR
        

running = True
myClock = pygame.time.Clock()

mx = my = 0
while running:   # this is our game loop
    button = 0

    # Check all the events that happen
    for evnt in pygame.event.get():
        # if the user tries to close the window, then raise the "flag"
        if evnt.type == pygame.QUIT:
            running = False
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_LEFT:
                if state == STATE_GAME:
                    KEY_LEFT = True
            elif evnt.key == pygame.K_RIGHT:
                if state == STATE_GAME:
                    KEY_RIGHT = True
            elif evnt.key == pygame.K_UP:
                if state == STATE_GAME:
                    KEY_UP = True
            elif evnt.key == pygame.K_DOWN:
                if state == STATE_GAME:
                    KEY_DOWN = True          
        if evnt.type == pygame.KEYUP:
            if evnt.key == pygame.K_LEFT:
                if state == STATE_GAME:
                    KEY_LEFT = False
            elif evnt.key == pygame.K_RIGHT:
                if state == STATE_GAME:
                    KEY_RIGHT = False
            elif evnt.key == pygame.K_UP:
                if state == STATE_GAME:
                    KEY_UP = False
            elif evnt.key == pygame.K_DOWN:
                if state == STATE_GAME:
                    KEY_DOWN = False          
        if evnt.type == pygame.MOUSEMOTION:
            mx, my = evnt.pos
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            button = evnt.button
            if button == 3:
                state = STATE_MAIN
        
    # traffic cop
    if state == STATE_MAIN:
        drawScene(screen, mx, my, button)
    elif state == STATE_GAME:
        playGame(screen, mx, my, button)
    else:
        pygame.draw.rect(screen, BLUE, (0, 0, width, height))
        
    pygame.display.flip()

    # waits long enough to have 60 fps
    myClock.tick(60)

pygame.quit()