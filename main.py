###main.py

#Imports and initialisations...

import pygame,sys,random,time
from pygame.locals import*

pygame.init()

#Create class objects

class Obj(object):
    def __init__(self,image,rect): #This specifies the basic parameters for when we create the object
        self.rect=rect
        self.image=pygame.transform.scale(image,(self.rect.bottom,self.rect.right))#Self allows the components of the object to be used in any function of the class


    def draw(self):
        global screen

        screen.blit(self.image,self.rect) #Draws image and rectangle onto screen

#Create functions

def terminate():
    pygame.quit()
    sys.exit()

#Any constant variables will we assigned in CAPITALS

WIDTH=1280
HEIGHT=720

FPS=50

CAPTION="Human rising"

#Create the global screen

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(CAPTION)

#Initialise other variables

clock=pygame.time.Clock()

bg=Obj(image=pygame.image.load("Grass.png"),rect=pygame.Rect(0,0,HEIGHT,WIDTH))

key=0

#Create game loop

while True:
    for event in pygame.event.get(): #Event loop
        if event.type==QUIT:
            terminate()

        if event.type==KEYDOWN:
            key=event.key

        if event.type==KEYUP:
            key=0        

    bg.draw()

    pygame.display.update() #Update
    clock.tick(FPS)
