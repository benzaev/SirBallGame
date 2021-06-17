#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.28

#Holds the stages and has a couple auxillary classes for little objects

import pygame, model, math

#pygame initialization
pygame.init()

w=model.w
h=model.h
surface=model.surface

WHITE=model.WHITE

###########################################################   LEVEL ONE   ############################################################

def drawStageOne():
    #contains all the blocks so I can test colides
    blocks=[]  
    #flat first
    pygame.draw.rect(surface,WHITE,(0,2*h/3,2*w/5,h/3+1),1)  
    blocks.append(pygame.Rect(0,2*h/3,2*w/5,h/3+1))  
    #low flat
    pygame.draw.rect(surface,WHITE,(2*w/5,9*h/10,w/5,h/5+1),1)
    blocks.append(pygame.Rect(2*w/5,9*h/10,w/5,h/5+1))  
    #flat end    
    pygame.draw.rect(surface,WHITE,(3*w/5,4*h/5,8*w/25,h/5+1),1)
    blocks.append(pygame.Rect(3*w/5,4*h/5,8*w/25,h/5+1))
    #low end
    pygame.draw.rect(surface,WHITE,(23*w/25,9*h/10,2*w/25,h/5+1),1)  
    blocks.append(pygame.Rect(23*w/25,9*h/10,2*w/25,h/5+1))    
    #flat high 1
    pygame.draw.rect(surface,WHITE,(w/2,2*h/5,w/10,w/60),3)  
    blocks.append(pygame.Rect(w/2,2*h/5,w/10,w/60))   
    #flat high 2
    pygame.draw.rect(surface,WHITE,(3*w/4,h/5,w/20,w/60),3)  
    blocks.append(pygame.Rect(3*w/4,h/5,w/20,w/60))       
    
    #beefy verticle line
    pygame.draw.rect(surface,WHITE,(9*w/10,h/3,w/50,7*h/15),1)
    blocks.append(pygame.Rect(9*w/10,h/3,w/50,7*h/15))   
    #line on verticle line
    pygame.draw.rect(surface,WHITE,(91*w/100-w/40,29*h/90,w/20,h/80),1)
    blocks.append(pygame.Rect(91*w/100-w/40,29*h/90,w/20,h/80))  

    #button#
    #base
    pygame.draw.rect(surface,WHITE,(17*w/40,22*h/25,2*w/15,h/50+1),2)
    blocks.append(pygame.Rect(17*w/40,22*h/25,2*w/15,h/50+1))  
    #button button
    pygame.draw.rect(surface,WHITE,(89*w/200,22*h/25-h/50,2*w/15-w/25,h/50+1),2)
    blocks.append(pygame.Rect(89*w/200,22*h/25-h/50,2*w/15-w/25,h/50+1))  
    #rivots
    pygame.draw.circle(surface,WHITE, (17*w/40+(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+2*(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+3*(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+4*(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+5*(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+6*(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+7*(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+8*(2*w/15)/10,22*h/25+w/170),w/200,1)
    pygame.draw.circle(surface,WHITE, (17*w/40+9*(2*w/15)/10,22*h/25+w/170),w/200,1)
    
    return blocks    
    
def drawStageTwo():
    blocks=[]  
    #low first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,2*w/5,h/5+1),1)  
    blocks.append(pygame.Rect(0,9*h/10,2*w/5,h/5+1)) 
    #high first
    pygame.draw.rect(surface,WHITE,(0,h/3,w/3,h/60),1)  
    blocks.append(pygame.Rect(0,h/3,w/3,h/60))  
    #first step
    pygame.draw.rect(surface,WHITE,(8*w/20,18*h/30,w/8,h/60),1)  
    blocks.append(pygame.Rect(8*w/20,18*h/30,w/8,h/60))
    #last high
    pygame.draw.rect(surface,WHITE,(2*w/3,h/3,w/3+1,h/60),1)  
    blocks.append(pygame.Rect(2*w/3,h/3,w/3+1,h/60))
    return blocks
    
def drawStageThree():
    blocks=[]  
    #flat first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/5,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/5,h/5+1))     
    #low flat 2
    pygame.draw.rect(surface,WHITE,(2*w/5,9*h/10,w/5,h/5+1),1)  
    blocks.append(pygame.Rect(2*w/5,9*h/10,w/5,h/5+1)) 
    #low flat 3
    pygame.draw.rect(surface,WHITE,(4*w/5,9*h/10,w/5,h/5+1),1) 
    blocks.append(pygame.Rect(4*w/5,9*h/10,w/5,h/5+1)) 
    #medium step 1
    pygame.draw.rect(surface,WHITE,(w/5,3*h/5,w/5,h/60),1) 
    blocks.append(pygame.Rect(w/5,3*h/5,w/5,h/60)) 
    #medium step 2
    pygame.draw.rect(surface,WHITE,(3*w/5,3*h/5,w/5,h/60),1) 
    blocks.append(pygame.Rect(3*w/5,3*h/5,w/5,h/60)) 
    #high first
    pygame.draw.rect(surface,WHITE,(0,h/3,w/5,h/60),1)  
    blocks.append(pygame.Rect(0,h/3,w/5,h/60))
    #high end
    pygame.draw.rect(surface,WHITE,(4*w/5,h/3,w/5,h/60),1)  
    blocks.append(pygame.Rect(4*w/5,h/3,w/5,h/60)) 
    return blocks
    
def drawStageFour():
    blocks=[]  
    #low first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/15,h/5+1)) 
    #low 2
    pygame.draw.rect(surface,WHITE,(2*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(2*w/15,9*h/10,w/15,h/5+1)) 
    #low 3
    pygame.draw.rect(surface,WHITE,(4*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(4*w/15,9*h/10,w/15,h/5+1)) 
    #low 4
    pygame.draw.rect(surface,WHITE,(6*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(6*w/15,9*h/10,w/15,h/5+1))    
    #low 5
    pygame.draw.rect(surface,WHITE,(8*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(8*w/15,9*h/10,w/15,h/5+1))     
    #low 6
    pygame.draw.rect(surface,WHITE,(10*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(10*w/15,9*h/10,w/15,h/5+1))    
    #low 7
    pygame.draw.rect(surface,WHITE,(12*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(12*w/15,9*h/10,w/15,h/5+1))    
    #low last
    pygame.draw.rect(surface,WHITE,(14*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(14*w/15,9*h/10,w/15,h/5+1)) 
    #high first
    pygame.draw.rect(surface,WHITE,(0,h/3,w/5,h/60),1)  
    blocks.append(pygame.Rect(0,h/3,w/5,h/60)) 
    #high middle
    pygame.draw.rect(surface,WHITE,(w/3,h/3,w/3,h/60),1)  
    blocks.append(pygame.Rect(w/3,h/3,w/3,h/60)) 
    #high end
    pygame.draw.rect(surface,WHITE,(4*w/5,h/3,w/5,h/60),1)  
    blocks.append(pygame.Rect(4*w/5,h/3,w/5,h/60))
    return blocks
    
def drawStageFive():
    blocks=[]  
    #there can only be one
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w,h/5+1),1)  
    blocks.append(pygame.Rect(0,9*h/10,w,h/5+1)) 
    #step 1 high
    pygame.draw.rect(surface,WHITE,(-1,h/3,w/10,h/60),1)  
    blocks.append(pygame.Rect(-1,h/3,w/10,h/60)) 
    #step 2
    pygame.draw.rect(surface,WHITE,(w/5,h/2,w/10,h/60),1)  
    blocks.append(pygame.Rect(w/5,h/2,w/10,h/60)) 
    #step 3
    pygame.draw.rect(surface,WHITE,(w/3,2*h/3,w/10,h/60),1)  
    blocks.append(pygame.Rect(w/3,2*h/3,w/10,h/60)) 
    
    #image of the exit door
    Door=model.Door
    surface.blit(Door, (17*w/20, 9*h/10-h//3)) 
    
    return blocks

###########################################################   LEVEL TWO   ############################################################

def drawStageSix():
    #contains all the blocks so I can test colides
    blocks=[] 
    #block. No going back to stage 5
    blocks.append(pygame.Rect(-1,-1,w/200,h+2))  
    #flat first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/5,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/5,h/5+1))     
    #low flat 2
    pygame.draw.rect(surface,WHITE,(2*w/5,9*h/10,w/5,h/5+1),1)  
    blocks.append(pygame.Rect(2*w/5,9*h/10,w/5,h/5+1)) 
    #low flat 3
    pygame.draw.rect(surface,WHITE,(4*w/5,9*h/10,w/5,h/5+1),1) 
    blocks.append(pygame.Rect(4*w/5,9*h/10,w/5,h/5+1))     
    #step 1
    pygame.draw.rect(surface,WHITE,(3*w/12,3*h/4,w/20,h/60),1) 
    blocks.append(pygame.Rect(3*w/12,3*h/4,w/20,h/60)) 
    #step 2
    pygame.draw.rect(surface,WHITE,(46*w/100,h/2,w/20,h/60),1) 
    blocks.append(pygame.Rect(46*w/100,h/2,w/20,h/60)) 
    #step 3
    pygame.draw.rect(surface,WHITE,(3*w/5,h/4,w/20,h/60),1) 
    blocks.append(pygame.Rect(3*w/5,h/4,w/20,h/60))      
    #backwards step 3
    pygame.draw.rect(surface,WHITE,(3*w/12,h/4,w/20,h/60),1)   
    blocks.append(pygame.Rect(3*w/12,h/4,w/20,h/60))  
    #high 1
    pygame.draw.rect(surface,WHITE,(-1,h/10,w/4,h/60),1)
    blocks.append(pygame.Rect(-1,h/10,w/4,h/60))       
    #high 2
    pygame.draw.rect(surface,WHITE,(w/3,h/10,w/4,h/60),1)  
    blocks.append(pygame.Rect(w/3,h/10,w/4,h/60)) 
    #verticle end high
    pygame.draw.rect(surface,WHITE,(9*w/12,h/7+h/10,w/50,h/2-h/5),1)
    blocks.append(pygame.Rect(9*w/12,h/7+h/10,w/50,h/2-h/5))
    #verticle end low
    pygame.draw.rect(surface,WHITE,(87*w/120,9*h/12,w/50,3*h/12+1),1) 
    blocks.append(pygame.Rect(87*w/120,9*h/12,w/50,3*h/12+1))        
    #end
    pygame.draw.rect(surface,WHITE,(5*w/6,h/4,w/6+1,h/60),1)
    blocks.append(pygame.Rect(5*w/6,h/4,w/6+1,h/60))
    
    return blocks
    
def drawStageSixSpikes():
    spike=model.spike
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes
    surface.blit(spike, (13*w/30,h/10-h/17,w/20,h/20))
    spikes.append(pygame.Rect(27*w/60,h/10-h/24,w/60,h/22))
    
    surface.blit(spike, (13*w/30-w/40,h/10-h/17,w/20,h/20))
    spikes.append(pygame.Rect(27*w/60-w/40,h/10-h/24,w/60,h/22))

    surface.blit(spike, (13*w/30-w/20,h/10-h/17,w/20,h/20))
    spikes.append(pygame.Rect(27*w/60-w/20,h/10-h/24,w/60,h/22))
    
    return spikes

    
def drawStageSeven():
    #contains all the blocks so I can test colides
    blocks=[] 
    #low start
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/5,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/5,h/5+1))     
    #high start
    pygame.draw.rect(surface,WHITE,(-1,h/4,w/6,h/60),1)
    blocks.append(pygame.Rect(-1,h/4,w/6,h/60))     
    #step 1
    pygame.draw.rect(surface,WHITE,(3*w/12,3*h/4,w/20,h/60),1) 
    blocks.append(pygame.Rect(3*w/12,3*h/4,w/20,h/60)) 
    #step 2
    pygame.draw.rect(surface,WHITE,(43*w/100,h/2,w/20,h/60),1) 
    blocks.append(pygame.Rect(43*w/100,h/2,w/20,h/60)) 
    #step 3
    pygame.draw.rect(surface,WHITE,(3*w/5,h/4,w/20,h/60),1) 
    blocks.append(pygame.Rect(3*w/5,h/4,w/20,h/60)) 
    #step 4
    pygame.draw.rect(surface,WHITE,(3*w/5,3*h/4,w/20,h/60),1) 
    blocks.append(pygame.Rect(3*w/5,3*h/4,w/20,h/60))
    #backwards step 3
    pygame.draw.rect(surface,WHITE,(3*w/12,12*h/40,w/20,h/60),1)   
    blocks.append(pygame.Rect(3*w/12,12*h/40,w/20,h/60))                
    #verticle end high
    pygame.draw.rect(surface,WHITE,(9*w/12,h/7+h/10,w/50,h/2-h/5),1)
    blocks.append(pygame.Rect(9*w/12,h/7+h/10,w/50,h/2-h/5))
    #verticle end low
    pygame.draw.rect(surface,WHITE,(87*w/120,9*h/12,w/50,3*h/12+1),1) 
    blocks.append(pygame.Rect(87*w/120,9*h/12,w/50,3*h/12+1))        
    #high end
    pygame.draw.rect(surface,WHITE,(5*w/6,h/4,w/6+1,h/60),1)
    blocks.append(pygame.Rect(5*w/6,h/4,w/6+1,h/60))
    #low end
    pygame.draw.rect(surface,WHITE,(4*w/5,9*h/10,w/5,h/5+1),1) 
    blocks.append(pygame.Rect(4*w/5,9*h/10,w/5,h/5+1)) 
    return blocks
    
def drawStageSevenSpikes():
    spike=model.spike
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes
    surface.blit(spike, (31*w/120,19*h/80,w/20,h/60))
    spikes.append(pygame.Rect(33*w/120,21*h/80,w/60,h/22))
    
    return spikes
    
    
    
def drawStageEight():
    #contains all the blocks so I can test colides
    blocks=[]        
    #high start
    pygame.draw.rect(surface,WHITE,(0,h/4,w/6+1,h/60),1)
    blocks.append(pygame.Rect(0,h/4,w/6+1,h/60))
    #low start
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/5,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/5,h/5+1)) 
    #top block
    pygame.draw.rect(surface, WHITE,(w/4, h/5, w/2, h/60), 1)
    blocks.append(pygame.Rect(w/4, h/5, w/2, h/60)) 
    #bottom top
    pygame.draw.rect(surface, WHITE,(w/4, 14*h/30, 14*w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4,14*h/30, 14*w/30, h/60)) 
    #step 1
    pygame.draw.rect(surface, WHITE,(w/3, 4*h/5, w/20, h/60), 1)
    blocks.append(pygame.Rect(w/3, 4*h/5, w/20, h/60)) 
    #step 2
    pygame.draw.rect(surface, WHITE,(w/2, 4*h/5, w/20, h/60), 1)
    blocks.append(pygame.Rect(w/2, 4*h/5, w/20, h/60))
    #step 3
    pygame.draw.rect(surface, WHITE,(2*w/3, 4*h/5, w/20, h/60), 1)
    blocks.append(pygame.Rect(2*w/3, 4*h/5, w/20, h/60))
    #bottom
    pygame.draw.rect(surface, WHITE,(w/3+w/20, 99*h/100, w/3-w/20, h/60), 1)
    blocks.append(pygame.Rect(w/3+w/20, 99*h/100, w/3-w/20, h/60))
    #step 4
    pygame.draw.rect(surface, WHITE,(5*w/6, 3*h/5, w/20, h/60), 1)
    blocks.append(pygame.Rect(5*w/6, 3*h/5, w/20, h/60))
    #last block
    pygame.draw.rect(surface, WHITE,(11*w/12, 14*h/30, w/12+1, h/60), 1)
    blocks.append(pygame.Rect(11*w/12, 14*h/30, w/12+1, h/60))
    return blocks
    
    
def drawStageEightSpikes():
    spike=model.spike
    spikeD=model.spikeD
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes
    #top left
    surface.blit(spike, (11*w/40,14*h/30-h/17,w/20,h/20))
    spikes.append(pygame.Rect(11*w/40+w/60,14*h/30-h/24,w/60,h/22))
    surface.blit(spike, (11*w/40-w/40,14*h/30-h/17,w/20,h/20))
    spikes.append(pygame.Rect(11*w/40+w/60-w/40,14*h/30-h/24,w/60,h/22))
    #bottom center
    surface.blit(spike, (w/2,99*h/100-h/17,w/20,h/20))
    spikes.append(pygame.Rect(w/2+w/60,99*h/100-h/24,w/60,h/22))
    surface.blit(spike, (w/2-w/40,99*h/100-h/17,w/20,h/20))
    spikes.append(pygame.Rect(w/2+w/60-w/40,99*h/100-h/24,w/60,h/22))
    
    
    #spikesD    w/4, 14*h/30, 14*w/30, h/60
    surface.blit(spikeD, (29*w/60,14*h/30-h/100,w/20,h/20))
    spikes.append(pygame.Rect(29*w/60+w/60,14*h/30+h/100,w/60,h/22))
    
    return spikes
    
    
    
def drawStageNine():
 #contains all the blocks so I can test colides
    blocks=[]        
    #first block
    pygame.draw.rect(surface, WHITE,(0, 14*h/30, w/5, h/60), 1)
    blocks.append(pygame.Rect(0, 14*h/30, w/5, h/60))
    #top layer
    pygame.draw.rect(surface, WHITE,(w/4, h/6, w/2, h/20), 1)
    blocks.append(pygame.Rect(w/4, h/6, w/2, h/30))
    #middle layer
    pygame.draw.rect(surface, WHITE,(w/4, 2*h/3+h/10, w/2, h/60), 1)
    blocks.append(pygame.Rect(w/4, 2*h/3+h/10, w/2, h/60))
    #bottom layer
    pygame.draw.rect(surface, WHITE,(w/4, 19*h/20, w/2, h/20), 1)
    blocks.append(pygame.Rect(w/4, 19*h/20, w/2, h/20))
    #step 1
    pygame.draw.rect(surface, WHITE,(w/4, 2*h/3, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4, 2*h/3, w/30, h/60))
    #step 2
    pygame.draw.rect(surface, WHITE,(w/4+w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+w/15, 11*h/30, w/30, h/60))
    #step 3
    pygame.draw.rect(surface, WHITE,(w/4+2*w/15, 2*h/3, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+2*w/15, 2*h/3, w/30, h/60))
    #step 4
    pygame.draw.rect(surface, WHITE,(w/4+w/5, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+w/5, 11*h/30, w/30, h/60))
    #step 5
    pygame.draw.rect(surface, WHITE,(w/4+4*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+4*w/15, 11*h/30, w/30, h/60))
    #step 6
    pygame.draw.rect(surface, WHITE,(w/4+w/3, 2*h/3, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+w/3, 2*h/3, w/30, h/60))
    #step 7
    pygame.draw.rect(surface, WHITE,(w/4+6*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+6*w/15, 11*h/30, w/30, h/60))
    #step 8
    pygame.draw.rect(surface, WHITE,(w/4+7*w/15, 2*h/3, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+7*w/15, 2*h/3, w/30, h/60))
    #lower step
    pygame.draw.rect(surface, WHITE,(w/4+8*w/15,  2*h/3+h/8, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+8*w/15,  2*h/3+h/8, w/30, h/60))
    #lowest step
    pygame.draw.rect(surface, WHITE,(w/4+8*w/15, 19*h/20 , w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+8*w/15, 19*h/20 , w/30, h/60))
    #end
    pygame.draw.rect(surface, WHITE,(9*w/10,h/2, w/10, h/60), 1)
    blocks.append(pygame.Rect(9*w/10,h/2, w/10, h/60))
    
    #image of the exit door
    Door=model.Door
    surface.blit(Door, (9*w/10-w/90, h/2-h/3))
    
    return blocks
    
    
def drawStageNineSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes
    #top side
    surface.blit(spikeL, (w/4-11*w/300,h/6-h/60,w/20,h/20))
    spikes.append(pygame.Rect(w/4-w/30+w/60,h/6+h/70,w/60,h/30))
    
    #top row 
    surface.blit(spikeD, (w/4-w/90,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+2*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+3*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+4*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+5*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+6*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+7*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+8*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+9*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+10*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+11*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+12*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+13*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+14*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+15*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+16*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+17*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+18*w/40,h/5-h/170,w/20,h/20))
    surface.blit(spikeD, (w/4-w/90+19*w/40,h/5-h/170,w/20,h/20))
    spikes.append(pygame.Rect(w/4, h/5+h/50,w/2, h/30))

    #middle row 
    surface.blit(spike, (w/4-w/90,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+2*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+3*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+4*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+5*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+6*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+7*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+8*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+9*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+10*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+11*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+12*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+13*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+14*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+15*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+16*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+17*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+18*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    surface.blit(spike, (w/4-w/90+19*w/40,2*h/3+h/10-h/17-h/170,w/20,h/20))
    spikes.append(pygame.Rect(w/4+w/80, 22*h/30, w/2-w/40, h/30))
    
    return spikes
    
def drawStageTen():
#contains all the blocks so I can test colides
    blocks=[]         
    #block. No going back to stage 5
    blocks.append(pygame.Rect(-1,-1,w/200,h+2))  
    #first block
    pygame.draw.rect(surface, WHITE,(0, 14*h/30, w/5, h/60), 1)
    blocks.append(pygame.Rect(0, 14*h/30, w/5, h/60))
    #low first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/15,h/5+1)) 
    #low 2
    pygame.draw.rect(surface,WHITE,(2*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(2*w/15,9*h/10,w/15,h/5+1)) 
    #long low 3-6
    pygame.draw.rect(surface,WHITE,(4*w/15,9*h/10,7*w/15,h/5+1),1) 
    blocks.append(pygame.Rect(4*w/15,9*h/10,7*w/15,h/5+1))     
    #low 7
    pygame.draw.rect(surface,WHITE,(12*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(12*w/15,9*h/10,w/15,h/5+1))    
    #low last
    pygame.draw.rect(surface,WHITE,(14*w/15,9*h/10,w/15,h/5+1),1) 
    blocks.append(pygame.Rect(14*w/15,9*h/10,w/15,h/5+1)) 
    
    return blocks
    
def drawStageTenSpikes():
    spike=model.spike
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes
    #left
    surface.blit(spike, (9*w/60,9*h/10-h/17,w/20,h/20))
    spikes.append(pygame.Rect(9*w/60+w/60,9*h/10-h/24,w/60,h/22))
    #right
    surface.blit(spike, (12*w/15,9*h/10-h/17,w/20,h/20))
    spikes.append(pygame.Rect(12*w/15+w/60,9*h/10-h/24,w/60,h/22))

    return spikes
    
def drawStageEleven():
    #contains all the blocks so I can test colides
    blocks=[]   
    #first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/10,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/10,h/5+1)) 
    #lowest
    pygame.draw.rect(surface,WHITE,(w/10,39*h/40,8*w/10,h/5),1) 
    blocks.append(pygame.Rect(w/10,39*h/40,8*w/10,h/5))
    
    #moving platform 1
    if(model.movingObjects==[]):
        block1=movingObject(0, 1333, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block1)
    blocks.append(model.movingObjects[0].drawSelf())   
    #moving platform 2
    if(len(model.movingObjects)==1):
        block2=movingObject(666, 1333, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block2)
    blocks.append(model.movingObjects[1].drawSelf())   
    #moving platform 3
    if(len(model.movingObjects)==2):
        block3=movingObject(1333, 1333, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block3)
    blocks.append(model.movingObjects[2].drawSelf())       
    #step -four 
    pygame.draw.rect(surface, WHITE,(5*w/12-4*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12-4*w/15, 11*h/30, w/30, h/60))
    #step -three 
    pygame.draw.rect(surface, WHITE,(5*w/12-3*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12-3*w/15, 11*h/30, w/30, h/60))
    #step -two 
    pygame.draw.rect(surface, WHITE,(5*w/12-2*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12-2*w/15, 11*h/30, w/30, h/60))
    #step -one 
    pygame.draw.rect(surface, WHITE,(5*w/12-w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12-w/15, 11*h/30, w/30, h/60))
    #step two 
    pygame.draw.rect(surface, WHITE,(5*w/12, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(w/4+w/6, 11*h/30, w/30, h/60))
    #step three 
    pygame.draw.rect(surface, WHITE,(5*w/12+w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12+w/15, 11*h/30, w/30, h/60))
    #step four
    pygame.draw.rect(surface, WHITE,(5*w/12+2*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12+2*w/15, 11*h/30, w/30, h/60))
    #step five
    pygame.draw.rect(surface, WHITE,(5*w/12+3*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12+3*w/15, 11*h/30, w/30, h/60))
    #step six
    pygame.draw.rect(surface, WHITE,(5*w/12+4*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12+4*w/15, 11*h/30, w/30, h/60))
    #step seven
    pygame.draw.rect(surface, WHITE,(5*w/12+5*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12+5*w/15, 11*h/30, w/30, h/60))
    #step eight
    pygame.draw.rect(surface, WHITE,(5*w/12+6*w/15, 11*h/30, w/30, h/60), 1)
    blocks.append(pygame.Rect(5*w/12+6*w/15, 11*h/30, w/30, h/60))
    #heighest
    pygame.draw.rect(surface,WHITE,(w/10,h/6,8*w/10,h/30),1) 
    blocks.append(pygame.Rect(w/10,39*h/40,8*w/10,h/5))
    #low last
    pygame.draw.rect(surface,WHITE,(9*w/10,9*h/10,w/10,h/5+1),1) 
    blocks.append(pygame.Rect(9*w/10,9*h/10,w/10,h/5+1))   
    
    return blocks
    
    
def drawStageElevenSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes    
    #first line
    offset=-6*w/40
    n=32
    while(n>0):
        surface.blit(spikeD, (w/4-w/90+offset,h/5-h/50,w/20,h/20))
        n-=1
        offset+=w/40
    spikes.append(pygame.Rect(w/10, h/5+h/100,8*w/10, h/30))

    #bottom row 
    surface.blit(spike, (w/4-w/90-6*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90-5*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90-4*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90-3*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90-2*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90-w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+2*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+3*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+4*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+5*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+6*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+7*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+8*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+9*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+10*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+11*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+12*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+13*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+14*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+15*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+16*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+17*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+18*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+19*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+20*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+21*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+22*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+23*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+24*w/40,9*h/10+h/100,w/20,h/20))
    surface.blit(spike, (w/4-w/90+25*w/40,9*h/10+h/100,w/20,h/20))
    spikes.append(pygame.Rect(w/10, 9*h/10+h/30,8*w/10, h/30))    
    return spikes


def drawStageTwelve():
    #contains all the blocks so I can test colides
    blocks=[]  
     
    #stationary blocks
    #first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/6,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/6,h/5+1))
    #spikey wall
    pygame.draw.rect(surface, WHITE,(99*w/100, 0, w/16+1, h/2), 1)
    blocks.append(pygame.Rect(99*w/100, 0, w/16+1, h/2))
    #end block
    pygame.draw.rect(surface,WHITE,(5*w/6+w/20-1,9*h/10,w/6,h/5+1),1) 
    blocks.append(pygame.Rect(5*w/6+w/20-1,9*h/10,w/6,h/5+1)) 
    
    #moving blocks
    #moving vertical row 1
    if(model.movingObjects==[]):
        block=movingObject(500, 200, w/20, h/60, WHITE, 1800, 2)
        model.addMovingObject(block)
        block=movingObject(500, 800, w/20, h/60, WHITE, 1800, 2)
        model.addMovingObject(block)
        block=movingObject(500, 1400, w/20, h/60, WHITE, 1800, 2)
        model.addMovingObject(block)
        #moving horizontal
        block=movingObject(0, 300, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        block=movingObject(666, 300, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        block=movingObject(1333, 300, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        #moving vertical row 2
        block=movingObject(1500, 400, w/20, h/60, WHITE, 1800, 0)
        model.addMovingObject(block)
        block=movingObject(1500, 1000, w/20, h/60, WHITE, 1800, 0)
        model.addMovingObject(block)
        block=movingObject(1500, 1600, w/20, h/60, WHITE, 1800, 0)
        model.addMovingObject(block)
        #middle blocks for gems
        block=movingObject(300, 560, w/20, h/60, WHITE, 1200, 1)
        model.addMovingObject(block)
        block=movingObject(700, 560, w/20, h/60, WHITE, 1200, 1)
        model.addMovingObject(block)
        block=movingObject(1100, 560, w/20, h/60, WHITE, 1200, 1)
        model.addMovingObject(block)
    
    
    blocks.append(model.movingObjects[0].drawSelf())   
    blocks.append(model.movingObjects[1].drawSelf())  
    blocks.append(model.movingObjects[2].drawSelf())
    blocks.append(model.movingObjects[3].drawSelf())   
    blocks.append(model.movingObjects[4].drawSelf())  
    blocks.append(model.movingObjects[5].drawSelf()) 
    blocks.append(model.movingObjects[6].drawSelf())   
    blocks.append(model.movingObjects[7].drawSelf())  
    blocks.append(model.movingObjects[8].drawSelf())
    blocks.append(model.movingObjects[9].drawSelf())
    blocks.append(model.movingObjects[10].drawSelf())
    blocks.append(model.movingObjects[11].drawSelf())


    return blocks


def drawStageTwelveSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes    
    #first line
    offset=0
    n=11
    while(n>0):
        surface.blit(spikeL, (105*w/110,-h/100+offset,w/20,h/20))
        n-=1
        offset+=h/23
    spikes.append(pygame.Rect(107*w/110,0,w/20,h/2))
    #roof spikes
    offset=-w/40
    n=40
    while(n>0):
        surface.blit(spikeD, (offset, -h/30, w/20, h/20))
        n-=1
        offset+=w/40
    spikes.append(pygame.Rect(0,0,w,h/30))

    return spikes

def drawStageThirteen():
    #contains all the blocks so I can test colides
    blocks=[]   
    #no going back and hitting spikey wall
    blocks.append(pygame.Rect(0, 0, w/1000, h/2))
    #first
    pygame.draw.rect(surface,WHITE,(0,9*h/10,w/6,h/5+1),1) 
    blocks.append(pygame.Rect(0,9*h/10,w/6,h/5+1)) 
    #gems go here
    pygame.draw.rect(surface,WHITE,(0,3*h/12,w/6,h/30),1) 
    blocks.append(pygame.Rect(0,3*h/12,w/6,h/30))
    #end block
    pygame.draw.rect(surface,WHITE,(10*w/11,h/2,w/5,h/60),1) 
    blocks.append(pygame.Rect(10*w/11,h/2,w/5,h/60)) 
    
    #if need to instantiate moving objects
    if(model.movingObjects==[]):
        #moves back and fourth
        block=movingObject(500, 1800, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        #upward row one
        block=movingObject(900, 0, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        block=movingObject(900, 500, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        block=movingObject(900, 1000, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        block=movingObject(900, 1500, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        #downward row two
        block=movingObject(1100, 0, w/20, h/60, WHITE, 2000, 2)
        model.addMovingObject(block)
        block=movingObject(1100, 500, w/20, h/60, WHITE, 2000, 2)
        model.addMovingObject(block)
        block=movingObject(1100, 1000, w/20, h/60, WHITE, 2000, 2)
        model.addMovingObject(block)
        #upward row two
        block=movingObject(1100, 1500, w/20, h/60, WHITE, 2000, 2)
        model.addMovingObject(block)
        block=movingObject(1300, 0, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        block=movingObject(1300, 500, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        block=movingObject(1300, 1000, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        block=movingObject(1300, 1500, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)
        #moves back and fourth to gems
        block=movingObject(500, 500, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        
    #bottom oscillating block
    if(model.movingObjects[0].x>800):
        model.movingObjects[0].setDirection(3)
    elif(model.movingObjects[0].x<340):
        model.movingObjects[0].setDirection(1)
    
    #top oscillating block
    if(model.movingObjects[13].x>800):
        model.movingObjects[13].setDirection(3)
    elif(model.movingObjects[13].x<340):
        model.movingObjects[13].setDirection(1)

    #draws the blocks
    blocks.append(model.movingObjects[0].drawSelf())
    blocks.append(model.movingObjects[1].drawSelf())   
    blocks.append(model.movingObjects[2].drawSelf())  
    blocks.append(model.movingObjects[3].drawSelf())
    blocks.append(model.movingObjects[4].drawSelf())
    blocks.append(model.movingObjects[5].drawSelf())
    blocks.append(model.movingObjects[6].drawSelf())
    blocks.append(model.movingObjects[7].drawSelf())
    blocks.append(model.movingObjects[8].drawSelf())
    blocks.append(model.movingObjects[9].drawSelf())   
    blocks.append(model.movingObjects[10].drawSelf())  
    blocks.append(model.movingObjects[11].drawSelf())
    blocks.append(model.movingObjects[12].drawSelf())
    blocks.append(model.movingObjects[13].drawSelf())

    return blocks
    

def drawStageThirteenSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes    
    #roof spikes
    offset=-w/40
    n=42
    while(n>0):
        surface.blit(spikeD, (offset, -h/30, w/20, h/20))
        n-=1
        offset+=w/40
    spikes.append(pygame.Rect(0,0,w,h/30))

    return spikes
    

def drawStageFourteen():
    #contains all the blocks so I can test colides
    blocks=[]       
    #start block
    pygame.draw.rect(surface,WHITE,(0,h/2,w/10,h/60),1) 
    blocks.append(pygame.Rect(0,h/2,w/10,h/60))
    #steps for spikes
    pygame.draw.rect(surface,WHITE,(w/4,h/2,w/30,h/60),1) 
    blocks.append(pygame.Rect(w/4,h/2,w/30,h/60))
    
    pygame.draw.rect(surface,WHITE,(w/4+w/10,h/2,w/30,h/60),1) 
    blocks.append(pygame.Rect(w/4+w/10,h/2,w/30,h/60))
    
    pygame.draw.rect(surface,WHITE,(w/4+2*w/10,h/2,w/30,h/60),1) 
    blocks.append(pygame.Rect(w/4+2*w/10,h/2,w/30,h/60))
    
    pygame.draw.rect(surface,WHITE,(w/4+3*w/10,h/2,w/30,h/60),1) 
    blocks.append(pygame.Rect(w/4+3*w/10,h/2,w/30,h/60))
    
    pygame.draw.rect(surface,WHITE,(w/4+4*w/10,h/2,w/30,h/60),1) 
    blocks.append(pygame.Rect(w/4+4*w/10,h/2,w/30,h/60))
    
    pygame.draw.rect(surface,WHITE,(w/4+5*w/10,h/2,w/30,h/60),1) 
    blocks.append(pygame.Rect(w/4+5*w/10,h/2,w/30,h/60))
    
    pygame.draw.rect(surface,WHITE,(w/4+6*w/10,h/2,w/30,h/60),1) 
    blocks.append(pygame.Rect(w/4+6*w/10,h/2,w/30,h/60))
    
    #if need to instantiate the moving blocks
    if(model.movingObjects==[]):
        #moves in a square
        block=movingObject(200, 200, w/15, h/60, WHITE, 1500, 2)
        model.addMovingObject(block)
        block=movingObject(900, 1400, w/15, h/60, WHITE, 1500, 1)
        model.addMovingObject(block)
                        
    #move it in a square
    if(model.movingObjects[0].y==1400 and model.movingObjects[0].x==200):
        model.movingObjects[0].setDirection(1)
    elif(model.movingObjects[0].y==1400 and model.movingObjects[0].x==1400):
        model.movingObjects[0].setDirection(0)
    elif(model.movingObjects[0].y==200 and model.movingObjects[0].x==1400):
        model.movingObjects[0].setDirection(3)
    elif(model.movingObjects[0].y==200 and model.movingObjects[0].x==200):
        model.movingObjects[0].setDirection(2)
    
    #same thing for the second one
    if(model.movingObjects[1].y==1400 and model.movingObjects[1].x==200):
        model.movingObjects[1].setDirection(1)
    elif(model.movingObjects[1].y==1400 and model.movingObjects[1].x==1400):
        model.movingObjects[1].setDirection(0)
    elif(model.movingObjects[1].y==200 and model.movingObjects[1].x==1400):
        model.movingObjects[1].setDirection(3)
    elif(model.movingObjects[1].y==200 and model.movingObjects[1].x==200):
        model.movingObjects[1].setDirection(2)
    
    #draws the block
    blocks.append(model.movingObjects[0].drawSelf())
    blocks.append(model.movingObjects[1].drawSelf())

    return blocks
    

def drawStageFourteenSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #initalize moving spike
    if(len(model.movingObjects)==2):
        #moves in a square
        sharp=movingObject(600, 1090, w/20, h/20, 0, 2500, 1)
        model.addMovingObject(sharp)
        sharp=movingObject(1200, 1090, w/20, h/20, 0, 2500, 1)
        model.addMovingObject(sharp) 
        sharp=movingObject(1800, 1090, w/20, h/20, 0, 2500, 1)
        model.addMovingObject(sharp)
        sharp=movingObject(1800, 1242, w/20, h/20, 2, 2500, 3)
        model.addMovingObject(sharp)
        
        
        
    for x in range(2, 6):
        #make spikes goes back and forth
        if(model.movingObjects[x].x==2152 and model.movingObjects[x].y==1090):
            model.movingObjects[x].setDirection(2)
            model.movingObjects[x].setType(1)
            model.movingObjects[x].setX(2180)
        if(model.movingObjects[x].x==2180 and model.movingObjects[x].y==1242):
            model.movingObjects[x].setDirection(3)
            model.movingObjects[x].setType(2)
        if(model.movingObjects[x].x==532 and model.movingObjects[x].y==1242):
            model.movingObjects[x].setDirection(0)
            model.movingObjects[x].setType(3)
        if(model.movingObjects[x].x==532 and model.movingObjects[x].y==1090):
            model.movingObjects[x].setDirection(1)
            model.movingObjects[x].setType(0)
        
    #blits moving spike
    spikes.append(model.movingObjects[2].drawSpike())
    spikes.append(model.movingObjects[3].drawSpike())
    spikes.append(model.movingObjects[4].drawSpike())
    spikes.append(model.movingObjects[5].drawSpike())

        
    #roof spikes
    offset=-w/40
    n=42
    while(n>0):
        surface.blit(spikeD, (offset, -h/30, w/20, h/20))
        n-=1
        offset+=w/40
    spikes.append(pygame.Rect(0,0,w,h/30))

    return spikes
    
def drawStageFifteen():
    #contains all the blocks so I can test colides
    blocks=[]       
    #static blocks
    #start block
    pygame.draw.rect(surface,WHITE,(0,h/3,w/10,h/60),1) 
    blocks.append(pygame.Rect(0,h/3,w/10,h/60))   
    #stops from going past door
    blocks.append(pygame.Rect(999*w/1000,0,w/10,h))  
    
    #initalize moving blocks
    if(model.movingObjects==[]):
        #back and fourth
        block=movingObject(500, 800, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        #fast downward row
        block=movingObject(230, 0, w/20, h/60, WHITE, 500, 0)
        model.addMovingObject(block)   
        block=movingObject(230, 100, w/20, h/60, WHITE, 500, 0)
        model.addMovingObject(block)   
        block=movingObject(230, 200, w/20, h/60, WHITE, 500, 0)
        model.addMovingObject(block)   
        block=movingObject(230, 300, w/20, h/60, WHITE, 500, 0)
        model.addMovingObject(block)   
        block=movingObject(230, 400, w/20, h/60, WHITE, 500, 0)
        model.addMovingObject(block)   
        #up down spike carrier
        block=movingObject(1200, 200, w/40, h/60, WHITE, 2000, 2)
        model.addMovingObject(block) 
        block=movingObject(1200, 1800, w/40, h/60, WHITE, 2000, 0)
        model.addMovingObject(block) 
        #end moving up and down
        block=movingObject(800, 360, w/3+1, h/60, WHITE, 1200, 0)
        model.addMovingObject(block) 
        
        
        
    #top oscillating block
    if(model.movingObjects[0].x>800):
        model.movingObjects[0].setDirection(3)
    elif(model.movingObjects[0].x<340):
        model.movingObjects[0].setDirection(1)
    #up down spike carrier
    if(model.movingObjects[6].y<200):
        model.movingObjects[6].setDirection(2)
    elif(model.movingObjects[6].y>500):
        model.movingObjects[6].setDirection(0)
    if(model.movingObjects[7].y<1500):
        model.movingObjects[7].setDirection(2)
    elif(model.movingObjects[7].y>1800):
        model.movingObjects[7].setDirection(0)
    
    #draws the block
    for x in range (0, 9):
        blocks.append(model.movingObjects[x].drawSelf())
        
        
    #image of the exit door
    Door=pygame.transform.scale(model.Door, (w//12, h//5))
    surface.blit(Door, (17*w/20, h//5)) 

    return blocks
    
def drawStageFifteenSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #roof spikes
    offset=-w/40
    n=40
    while(n>0):
        surface.blit(spikeD, (offset, -h/30, w/20, h/20))
        n-=1
        offset+=w/40
    spikes.append(pygame.Rect(0,0,w,h/30))

    #top spike attatched to block
    surface.blit(spikeD, (1176*w/2000, (model.movingObjects[6].y-10)*h/2000, w/20, h/20))    
    spikes.append(pygame.Rect(1176*w/2000+w/80,(model.movingObjects[6].y-10)*h/2000+h/40,w/20-w/40,h/20))
    #bottom spike attatched to block
    surface.blit(spike, (1176*w/2000, (model.movingObjects[7].y)*h/2000-h/16, w/20, h/20))    
    spikes.append(pygame.Rect(1176*w/2000+w/80,(model.movingObjects[7].y)*h/2000+h/40-h/16,w/20-w/40,h/20))
    
    return spikes
    
def drawStageSixteen(SirBall):
    #contains all the blocks so I can test colides
    blocks=[]       
    #static blocks
    #prevent going back
    blocks.append(pygame.Rect(0,-h,w/100,2*h))
    #start block
    pygame.draw.rect(surface,WHITE,(0,2*h/3,w/10,h/2),1) 
    blocks.append(pygame.Rect(0,2*h/3,w/10,h/2)) 
    #lower platform
    pygame.draw.rect(surface,WHITE,(w/10,6*h/7,w/4,h/2),1) 
    blocks.append(pygame.Rect(w/10,6*h/7,w/4,h/2)) 
    #platform with sword
    pygame.draw.rect(surface,WHITE,(w/10,4*h/10,w/10,h/20),1) 
    blocks.append(pygame.Rect(w/10,4*h/10,w/10,h/20)) 
    
    if(not SirBall.armed):
        #image of the sword
        Vsword=model.Vsword
        surface.blit(Vsword, (w//10, 4*h/10-h//17))
        
    #initialize the evil bananas        x , y, min, max, dir, alive
    if(model.movingObjects==[]):
        banana=Banana(w/3, h/20, h/20, h/3, 2, True, 100)
        model.addMovingObject(banana)
        banana=Banana(20*w/30, h/3, h/10, 2*h/3, 2, True, 100)
        model.addMovingObject(banana)
    #initialize the moving blocks
        block=movingObject(300, 900, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block) 
        block=movingObject(1300, 900, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        
    model.movingObjects[0].drawSelf()
    model.movingObjects[1].drawSelf()
    blocks.append(model.movingObjects[2].drawSelf())
    blocks.append(model.movingObjects[3].drawSelf())

    return blocks
    
def drawStageSixteenSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #fl00r spikes
    offset=34*w/100
    n=28
    while(n>0):
        surface.blit(spike, (offset, h-h/20, w/20, h/20))
        n-=1
        offset+=w/40
        
    spikes.append(pygame.Rect(34*w/100,h-h/20,w,h/30))
    
    return spikes
    
def drawStageSeventeen():
    #contains all the blocks so I can test colides
    blocks=[]       
    #static blocks
    #start block
    pygame.draw.rect(surface,WHITE,(0,2*h/3,w/10,h/2),1) 
    blocks.append(pygame.Rect(0,2*h/3,w/10,h/2)) 
    #spikey wall
    pygame.draw.rect(surface, WHITE,(99*w/100, 0, w/16+1, h/2), 1)
    blocks.append(pygame.Rect(99*w/100, 0, w/16+1, h/2))
    
    
    
    if(model.movingObjects==[]):
        #initialize the evil bananas        x , y, min, max, dir, alive, frequency
        banana=Banana(w/3, h/20, w/3, 2*w/3, 1, True, 90)
        model.addMovingObject(banana)
        banana=Banana(20*w/30, h/3, h/10, 2*h/3, 2, True, 100)
        model.addMovingObject(banana)
        #moving upward
        block=movingObject(230, 1500, w/20, h/60, WHITE, 1500, 0)
        model.addMovingObject(block)   
        block=movingObject(230, 1000, w/20, h/60, WHITE, 1500, 0)
        model.addMovingObject(block)   
        block=movingObject(230, 500, w/20, h/60, WHITE, 1500, 0)
        model.addMovingObject(block) 
        #moving right
        block=movingObject(0, 400, w/20, h/60, WHITE, 1500, 1)
        model.addMovingObject(block)   
        block=movingObject(400, 400, w/20, h/60, WHITE, 1500, 1)
        model.addMovingObject(block)   
        block=movingObject(800, 400, w/20, h/60, WHITE, 1500, 1)
        model.addMovingObject(block) 
        block=movingObject(1200, 400, w/20, h/60, WHITE, 1500, 1)
        model.addMovingObject(block)
        #moving left
        block=movingObject(0, 1800, w/20, h/60, WHITE, 2000, 3)
        model.addMovingObject(block)   
        block=movingObject(400, 1800, w/20, h/60, WHITE, 2000, 3)
        model.addMovingObject(block)   
        block=movingObject(800, 1800, w/20, h/60, WHITE, 2000, 3)
        model.addMovingObject(block) 
        block=movingObject(1200, 1800, w/20, h/60, WHITE, 2000, 3)
        model.addMovingObject(block)
        block=movingObject(1600, 1800, w/20, h/60, WHITE, 2000, 3)
        model.addMovingObject(block)
        
    
    model.movingObjects[0].drawSelf()
    model.movingObjects[1].drawSelf()
    
    for x in range(2, 14):
        blocks.append(model.movingObjects[x].drawSelf())


    return blocks
    
    
def drawStageSeventeenSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes    
    #side line
    offset=0
    n=11
    while(n>0):
        surface.blit(spikeL, (105*w/110,-h/100+offset,w/20,h/20))
        n-=1
        offset+=h/23
    spikes.append(pygame.Rect(107*w/110,0,w/20,h/2))
    
    #floor spikes
    offset=3*w/40+w/80
    n=40
    while(n>0):
        surface.blit(spike, (offset, h-h/18, w/20, h/20))
        n-=1
        offset+=w/40
        
    spikes.append(pygame.Rect(34*w/100,h-h/20,w,h/30))
    
    return spikes
    
    
    
def drawStageEighteenteen():
    #contains all the blocks so I can test colides
    blocks=[]       
    #static blocks
    #start block
    pygame.draw.rect(surface,WHITE,(0,4*h/5,2*w/10,h/2),1) 
    blocks.append(pygame.Rect(0,4*h/5,2*w/10,h/2)) 
    #Low wall 2
    pygame.draw.rect(surface, WHITE,(5*w/10, 9*h/10, 6*w/10, h/5+1), 1)
    blocks.append(pygame.Rect(5*w/10, 9*h/10, 6*w/10, h/5+1))
    #High wall 1
    pygame.draw.rect(surface, WHITE,(5*w/10, 2*h/5, 6*w/10, h/60), 1)
    blocks.append(pygame.Rect(5*w/10, 2*h/5, 6*w/10, h/60))
    #they have to go through doors
    blocks.append(pygame.Rect(999*w/1000, 0, w/20, h))


    #blits signs    
    sign=model.sign
    surface.blit(sign, (7*w/10, 9*h/10-h//6)) 
    sign=model.sign
    surface.blit(sign, (7*w/10, 2*h/5-h//6)) 
    door=model.Door
    surface.blit(door, (17*w/20, h//13)) 
    door=model.Door
    surface.blit(door, (17*w/20, 23*h//40)) 
    
    #moving blocks
    if(model.movingObjects==[]):
        #moving upward
        block=movingObject(450, 1500, w/20, h/60, WHITE, 1500, 0)
        model.addMovingObject(block)   
        block=movingObject(450, 1000, w/20, h/60, WHITE, 1500, 0)
        model.addMovingObject(block)   
        block=movingObject(450, 500, w/20, h/60, WHITE, 1500, 0)
        model.addMovingObject(block) 
        #initialize the evil bananas        x , y, min, max, dir, alive, frequency
        banana=Banana(15*w/30, 15*h/50, 0, 15*h/50, 0, True, 90)
        model.addMovingObject(banana)
        banana=Banana(15*w/30, 25*h/50, 23*h/50, 40*h/50, 2, True, 110)
        model.addMovingObject(banana)
        
    #draw moving blocks
    for x in range(0, 3):
        blocks.append(model.movingObjects[x].drawSelf())
        
    #draw bananas
    model.movingObjects[3].drawSelf()
    model.movingObjects[4].drawSelf()

    return blocks
    
def drawStageEighteenSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #spikes    
    
    #ceiling of bottom
    offset=5*w/10-w/80
    n=20
    while(n>0):
        surface.blit(spikeD, (offset, 2*h/5-h/100, w/20, h/20))
        n-=1
        offset+=w/40
        
    spikes.append(pygame.Rect(5*w/10, 2*h/5+h/80, w, h/30))
    
    return spikes
    
def drawStageMoreGems(SirBall):
    #contains all the blocks so I can test colides
    blocks=[]       
    #static blocks
    #no going back
    blocks.append(pygame.Rect(0,0,w/1000,h))     
    #start block
    pygame.draw.rect(surface,WHITE,(0,4*h/5,w/4,h/2),1) 
    blocks.append(pygame.Rect(0,4*h/5,w/4,h/2)) 
    #high left
    pygame.draw.rect(surface,WHITE,(0,2*h/5,w/4,h/60),1) 
    blocks.append(pygame.Rect(0,2*h/5,w/4,h/60)) 
    #high long
    pygame.draw.rect(surface,WHITE,(11*w/30,h/5,w/4,h/60),1) 
    blocks.append(pygame.Rect(11*w/30,h/5,w/4,h/60)) 
    #high right
    pygame.draw.rect(surface,WHITE,(11*w/12,2*h/5,w/8,h/60),1) 
    blocks.append(pygame.Rect(11*w/12,2*h/5,w/4,h/60))
    #if have enough gems stop them from going farther
    if(SirBall.stage>=19 and SirBall.stage<100 and SirBall.gems>=50):
        blocks.append(pygame.Rect(999*w/1000, 0, w/1000, h))
        #make it easier to get back
        pygame.draw.rect(surface,WHITE,(w/4,11*h/12,w,h),1) 
        blocks.append(pygame.Rect(w/4,11*h/12,w,h))
        

    #moving blocks
    if(model.movingObjects==[]):
        #moving downward
        block=movingObject(440, 1000, w/20, h/60, WHITE, 1500, 2)
        model.addMovingObject(block)   
        block=movingObject(440, 500, w/20, h/60, WHITE, 1500, 2)
        model.addMovingObject(block)   
        block=movingObject(440, 0, w/20, h/60, WHITE, 1500, 2)
        model.addMovingObject(block) 
        #bottom oscilate
        block=movingObject(600, 780, w/20, h/60, WHITE, 800, 1)
        model.addMovingObject(block)
        #middle oscilate
        block=movingObject(700, 1200, w/20, h/60, WHITE, 2000, 1)
        model.addMovingObject(block)
        #spikey block
        block=movingObject(755, 0, w/40, h/25, WHITE, 800, 2)
        model.addMovingObject(block)
        #moving upward
        block=movingObject(1700, 1332, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)   
        block=movingObject(1700, 666, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block)   
        block=movingObject(1700, 0, w/20, h/60, WHITE, 2000, 0)
        model.addMovingObject(block) 
        #banana
        banana=Banana(10*w/30, 20*h/50, 10*w/30, 16*w/30, 1, True, 80-(SirBall.stage-19)*3)
        model.addMovingObject(banana)
        
        
    #bottom oscillating block
    if(model.movingObjects[3].x>755):
        model.movingObjects[3].setDirection(3)
    elif(model.movingObjects[3].x<480):
        model.movingObjects[3].setDirection(1)
    #middle oscillating block
    if(model.movingObjects[4].x>1100):
        model.movingObjects[4].setDirection(3)
    elif(model.movingObjects[4].x<700):
        model.movingObjects[4].setDirection(1)    
        
        
    #draw moving blocks
    for x in range(0, 9):
        blocks.append(model.movingObjects[x].drawSelf())
        
    #draw bananas
    model.movingObjects[9].drawSelf()
    
    if(SirBall.gems>=50):
        #blits door    
        door=model.Door
        surface.blit(door, (w/40, h//13)) 
 
       

    return blocks
    
def drawStageMoreGemsSpikes():
    spike=model.spike
    spikeD=model.spikeD
    spikeL=model.spikeL
    spikeR=model.spikeR
    #contains all the spikes so I can test collides
    spikes=[] 
    
    #cause there was a wierd bug
    if(not(model.movingObjects==[])):
        #attatched spike facing up
        surface.blit(spike, (93*w/100, (model.movingObjects[5].y-50)*h/800, w/20, h/20))    
        spikes.append(pygame.Rect(93*w/100+w/80,(model.movingObjects[5].y-50)*h/800+h/40,w/20-w/40,h/20))
        #facing right
        surface.blit(spikeR, (191*w/200, (model.movingObjects[5].y-20)*h/800, w/20, h/20))    
        spikes.append(pygame.Rect(191*w/200+w/80,(model.movingObjects[5].y-20)*h/800+h/40,w/20-w/40,h/20))
        #facing down spike attatched to block
        surface.blit(spikeD, (93*w/100, (model.movingObjects[5].y+16)*h/800, w/20, h/20))    
        spikes.append(pygame.Rect(93*w/100+w/80,(model.movingObjects[5].y+16)*h/800+h/40,w/20-w/40,h/20))
        #facing left
        surface.blit(spikeL, (181*w/200, (model.movingObjects[5].y-20)*h/800, w/20, h/20))    
        spikes.append(pygame.Rect(181*w/200+w/80,(model.movingObjects[5].y-20)*h/800+h/40,w/20-w/40,h/20))
    
    return spikes
    
    
#Altar stage
def drawStage100():
    #contains all the blocks so I can test colides
    blocks=[]       
    #static blocks
    #no going back
    blocks.append(pygame.Rect(0,0,w/1000,h))  
    #start block
    pygame.draw.rect(surface,WHITE,(0,2*h/3,w/10,h/2),1) 
    blocks.append(pygame.Rect(0,2*h/3,w/10,h/2))       


    return blocks
    
    
    
    
    
    
    

###########################################################################Objects###################################################################
#moving object wherever you want
#increase rate to make the object move slower
#direction: 0--> up  1--> right  2--> down  3--> left
#type is either color or direction of spike
class movingObject:
    def __init__(self, x, y, width, height, type, rate, direction):
        self.x = x
        self.y = y 
        self.width=width
        self.height=height
        self.type=type
        self.rate=rate
        self.direction=direction
        
    def setX(self, value):
        if(self.x>self.rate):
            self.x=-self.width
        elif(self.x<-self.width):
            self.x=self.rate
        else:
            self.x=value
            
    def setY(self, value):
        if(self.y>self.rate):
            self.y=0
        elif(self.y<-self.height):
            self.y=self.rate
        else:
            self.y=value  
    
    def setDirection(self, value):
        self.direction=value
        
    def setType(self, value):
        self.type=value
            
            
    def moveSelf(self):
        if(self.direction==0):
            self.setY(self.y-4)
        elif(self.direction==1):
            self.setX(self.x+4)
        elif(self.direction==2):
            self.setY(self.y+4)
        elif(self.direction==3):
            self.setX(self.x-4)
            
    def drawSelf(self):
        pygame.draw.rect(surface,self.type,(self.x*w/self.rate,self.y*h/self.rate, self.width, self.height),1) 
        return (pygame.Rect(self.x*w/self.rate,self.y*h/self.rate, self.width, self.height))

    def drawSpike(self):
        spike=model.spike
        spikeD=model.spikeD
        spikeL=model.spikeL
        spikeR=model.spikeR
        
        if(self.type==0):
            surface.blit(spike, (self.x*w/self.rate,self.y*h/self.rate,self.width,self.height))
            return (pygame.Rect(self.x*w/self.rate+w/80,self.y*h/self.rate+h/40,self.width-w/40,self.height))
        elif(self.type==1):
            surface.blit(spikeR, (self.x*w/self.rate,self.y*h/self.rate,self.width,self.height))
            return (pygame.Rect(self.x*w/self.rate+w/80,self.y*h/self.rate+h/40,self.width-w/40,self.height))
        elif(self.type==2):
            surface.blit(spikeD, (self.x*w/self.rate,self.y*h/self.rate,self.width,self.height))
            return (pygame.Rect(self.x*w/self.rate+w/80,self.y*h/self.rate+h/40,self.width-w/40,self.height))
        elif(self.type==3):
            surface.blit(spikeL, (self.x*w/self.rate,self.y*h/self.rate,self.width,self.height))
            return (pygame.Rect(self.x*w/self.rate+w/80,self.y*h/self.rate+h/40,self.width-w/40,self.height))
            
#(x,y)= location of banana
#min/max =min/max value of x or y before changing directions
#standard clockwise dir system: 0=up 1=right 2=down 3=left
#lastShot=frame when last lazer whas shot
#frequency=how often to shoot a laser
class Banana:
    def __init__(self, x, y, min, max, dir, alive, frequency):
        self.x=x
        self.y=y
        self.min=min
        self.max=max
        self.dir=dir
        self.alive=alive
        self.lastShot=0
        self.frequency=frequency
        
    def setDir(self, value):
        self.dir=value
    def setAlive(self,value):
        self.alive=value

        
    def setX(self, value):
        if(value>self.max):
            self.setDir(3)
        elif(value<self.min):
            self.setDir(1)
        else:
            self.x=value
            
    def setY(self, value):
        if(value>self.max):
            self.setDir(0)
        elif(value<self.min):
            self.setDir(2)
        else:
            self.y=value 
            
    def setLastShot(self, value):
        self.lastShot=value
        
    def moveSelf(self):
        if(self.dir==0):
            self.setY(self.y-h/300)
        elif(self.dir==1):
            self.setX(self.x+w/300)
        elif(self.dir==2):
            self.setY(self.y+h/300)
        elif(self.dir==3):
            self.setX(self.x-w/300)
            
    def drawSelf(self):
        if(self.alive):
            EvilBanana=model.EvilBanana
            surface.blit(EvilBanana, (self.x, self.y))
            
    def getBox(self):
        return (pygame.Rect(self.x+w/200,self.y,w/15,h/13))
        
#lazer object that bananas shoot
class Lazer:
    def __init__(self, x, y, xDot, yDot):
        self.x=x
        self.y=y
        self.deltaX, self.deltaY, =self.calcSlope(x, y, xDot, yDot)
        self.point1=(self.x, self.y)
        self.point2=(self.x+30*self.deltaX, self.y+30*self.deltaY)
        self.point3=(self.x+30*self.deltaX-10*self.deltaY, self.y+30*self.deltaY+10*self.deltaX)
        self.point4=(self.x-10*self.deltaY, self.y+10*self.deltaX)        

        
    def moveSelf(self):
        self.x+=self.deltaX*10
        self.y+=self.deltaY*10
        self.point1=(self.x, self.y)
        self.point2=(self.x+30*self.deltaX, self.y+30*self.deltaY)
        self.point3=(self.x+30*self.deltaX-10*self.deltaY, self.y+30*self.deltaY+10*self.deltaX)
        self.point4=(self.x-10*self.deltaY, self.y+10*self.deltaX) 
            
    #calculates the slope of a line that goes 1 distance per move
    def calcSlope(self, x, y, xDot, yDot):
        slope=(yDot-y)/(xDot-x)
        deltaX=1/math.sqrt((slope**2)+1)
        deltaY=math.sqrt(1-(deltaX**2))
        if(xDot<x):
            slope*=-1
            deltaX=deltaX*(-1)
        if(yDot<y):
            slope*=-1
            deltaY=deltaY*(-1)        
        return deltaX, deltaY
        
    def drawSelf(self):        
        pygame.draw.polygon(surface,model.RED,((self.point1), (self.point2),(self.point3),(self.point4)),0) 
            

        

        
        
        
        
        








    
    
    
    