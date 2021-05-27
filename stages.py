#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.22

#Holds the stages

import pygame, model

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
    pygame.draw.rect(surface,WHITE,(9*w/10,h/3,w/50,7*h/15),0)
    blocks.append(pygame.Rect(9*w/10,h/3,w/50,7*h/15))   
    #line on verticle line
    pygame.draw.rect(surface,WHITE,(91*w/100-w/40,h/3,w/20,h/80),0)
    blocks.append(pygame.Rect(91*w/100-w/40,h/3,w/20,h/80))  

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
        block1=movingObject(0, 1333, w/20, h/60, WHITE, 2000)
        model.addMovingObject(block1)
    blocks.append(model.movingObjects[0].drawBlock())   
    model.movingObjects[0].setX(model.movingObjects[0].x+1)
    #moving platform 2
    if(len(model.movingObjects)==1):
        block2=movingObject(666, 1333, w/20, h/60, WHITE, 2000)
        model.addMovingObject(block2)
    blocks.append(model.movingObjects[1].drawBlock())   
    model.movingObjects[1].setX(model.movingObjects[1].x+1)
    #moving platform 3
    if(len(model.movingObjects)==2):
        block3=movingObject(1333, 1333, w/20, h/60, WHITE, 2000)
        model.addMovingObject(block3)
    blocks.append(model.movingObjects[2].drawBlock())   
    model.movingObjects[2].setX(model.movingObjects[2].x+1)
    
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






#moving block wherever you want
class movingObject:
    def __init__(self, x, y, width, height, color, rate):
        self.x = x
        self.y = y 
        self.width=width
        self.height=height
        self.color=color
        self.rate=rate
        
    def setX(self, value):
        if(self.x>self.rate):
            self.x=-self.width
        else:
            self.x=value
            
    def setY(self, value):
        if(self.y>self.rate):
            self.y=0
        else:
            self.y=value   
            
    def drawBlock(self):
        pygame.draw.rect(surface,self.color,(self.x*w/self.rate,self.y*h/self.rate, self.width, self.height),1) 
        return (pygame.Rect(self.x*w/self.rate,self.y*h/self.rate, self.width, self.height))










    
    
    
    