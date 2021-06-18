#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.29

#Holds the model

import pygame

#pygame initialization
pygame.init()

#open window and set size
surface= pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("Adventures of Sir BALL")

#Load images
DarkRealm= pygame.image.load("Images/The_Shadow_Realm.jpg")
DarkRealm= pygame.transform.scale(DarkRealm, (w, h))

Altar= pygame.image.load("Images/Altar.jpg")
Altar= pygame.transform.scale(Altar, (w, h))

crystal=pygame.image.load("Images/crystal.png").convert_alpha()
crystal=pygame.transform.scale(crystal,(w//30,w//30))

Door=pygame.image.load("Images/Door.png").convert_alpha()
Door=pygame.transform.scale(Door,(w//8,h//3))

spike=pygame.image.load("Images/spikeU.png").convert_alpha()
spike=pygame.transform.scale(spike,(w//20,w//20))

spikeD=pygame.image.load("Images/spikeD.png").convert_alpha()
spikeD=pygame.transform.scale(spikeD,(w//20,w//20))

spikeL=pygame.image.load("Images/spikeL.png").convert_alpha()
spikeL=pygame.transform.scale(spikeL,(w//20,w//20))

spikeR=pygame.image.load("Images/spikeR.png").convert_alpha()
spikeR=pygame.transform.scale(spikeR,(w//20,w//20))

Vsword=pygame.image.load("Images/Vsword.png").convert_alpha()
Vsword=pygame.transform.scale(Vsword,(w//15,w//15))

Rsword=pygame.image.load("Images/Rsword.png").convert_alpha()
Rsword=pygame.transform.scale(Rsword,(w//13,w//13))

Lsword=pygame.image.load("Images/Lsword.png").convert_alpha()
Lsword=pygame.transform.scale(Lsword,(w//13,w//13))

EvilBanana=pygame.image.load("Images/lessInnocentBanana.png").convert_alpha()
EvilBanana=pygame.transform.scale(EvilBanana,(w//12,h//12))

sign=pygame.image.load("Images/sign.png").convert_alpha()
sign=pygame.transform.scale(sign,(w//9,h//6))

fish=pygame.image.load("Images/fish.png").convert_alpha()
fish=pygame.transform.scale(fish,(w//20,h//20))

#Color constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED  = (255,   0,  0)
GREEN   = (  0, 255,  0)
BLUE = (  0,  0, 255)
LGREEN= (47, 237, 47)
YELLOW=(255,255,0)
GREY=(34,34,34)
LGREY=(169,169,169)
ORANGE=(255, 165, 0)

#global objects that move around are stored here
movingObjects=[]

def addMovingObject(object):
    transfer=[]
    for obj in movingObjects:
        transfer.append(obj)
        
    transfer.append(object)    
    finishTransfer(transfer)
    
def finishTransfer(transfer):
    global movingObjects
    movingObjects=transfer
    
def resetMovingObjects():
    global movingObjects
    movingObjects=[]
    
    
    