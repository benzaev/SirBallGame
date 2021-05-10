#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.19

#Holds the model

import pygame

#pygame initialization
pygame.init()

#open window and set size
surface= pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("Adventures of Sir BALL")


#Load images
Mountains = pygame.image.load("Images/Mountains.png")
Mountains=pygame.transform.scale(Mountains,(w,h))

DarkRealm= pygame.image.load("Images/The_Shadow_Realm.jpg")
DarkRealm= pygame.transform.scale(DarkRealm, (w, h))

Gregory=pygame.image.load("Images/Gregory.png").convert_alpha()
Gregory=pygame.transform.scale(Gregory,(w//12,w//12))

crystal=pygame.image.load("Images/crystal.png").convert_alpha()
crystal=pygame.transform.scale(crystal,(w//30,w//30))

Banana=pygame.image.load("Images/innocentBanana.png").convert_alpha()
Banana=pygame.transform.scale(Banana,(w//8,w//12))

Pusheen=pygame.image.load("Images/pusheen.png").convert_alpha()
Pusheen=pygame.transform.scale(Pusheen,(w//8,w//8))

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