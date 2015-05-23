###main.py

#Imports and initialisations...

import pygame,sys,random,time
from pygame.locals import*

pygame.init()

#Create class objects

class Obj(object):
    def __init__(self,rect,image=None): #This specifies the basic parameters for when we create the object
        self.rect=rect
        if image is not None:
            self.image=pygame.transform.scale(image,(self.rect.bottom,self.rect.right))#Self allows the components of the object to be used in any function of the class

        else:
            self.image=None

    def draw(self):
        global screen

        if self.image is not None:
            screen.blit(self.image,self.rect) #Draws image and rectangle onto screen

class Sprite(Obj):
    def __init__(self,states,state,velocity,*arg,**kwargs):
        self.states=states
        self.state=state
        self.velocity=velocity

        super(Sprite,self).__init__(*arg,**kwargs) #The sprite object, although individual, now inherits all the properties of the obj class

        for x in range(len(states)):
            self.states[x]=pygame.transform.scale(self.states[x],(self.rect.bottom,self.rect.right))

    def draw(self):
        screen.blit(self.states[self.state],self.rect)

    def act(self):
        self.rect.move_ip(self.velocity)

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

player=Sprite(rect=pygame.Rect(100,100,25,25),states=[pygame.image.load("prisoner_front.png")],state=0,velocity=(0,0))

key=[]

#Create game loop

while True:
    for event in pygame.event.get(): #Event loop
        if event.type==QUIT:
            terminate()

        if event.type==KEYDOWN:
            key.append(event.key)

        if event.type==KEYUP:
            key=[]
            player.velocity=(0,0)

    for event in key:
        if event==K_UP:
            player.velocity=(0,-10)

        if event==K_DOWN:
            player.velocity=(0,10)

        if event==K_LEFT:
            player.velocity=(-10,0)

        if event==K_RIGHT:
            player.velocity=(10,0)

    bg.draw()
    player.draw()
    player.act()

    pygame.display.update() #Update
    clock.tick(FPS)
