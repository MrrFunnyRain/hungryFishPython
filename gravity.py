import pygame
from pygame import*

init()
w=600
h=600
screen=display.set_mode((w,h))


def drawCrircle():
    draw.rect(screen,(0,0,0),(0,0,w,h))
    draw.rect(screen,(255,255,255),(300,y-a,10,10))
    display.flip()


a=0
y=300
jumping=False
running = True

myClock = time.Clock()
while running:
    if jumping==True:

        a-=1      
        if a==0:
            jumping=False

    drawCrircle()
    print(y)
    print(a)

    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        elif evnt.type==KEYDOWN:
            print (evnt.unicode)
            print (evnt.key)
            print (evnt.mod)
            if evnt.key==273:
                jumping=True
                a=10
    
    myClock.tick(10)