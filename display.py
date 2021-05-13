#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.2

#This blits everything

import pygame, model, stages, Luis, Marvin

#pygame initialization
pygame.init()
pygame.mixer.init()

w= model.w
h= model.h
surface= model.surface

#projects to screen
def view(stage, interact, numMess, keys, prevKey, deaths, wall_mad, wall_defeated, xDot, yDot, xWall, wStage, music, gemmap, gems):
    #background image
    background()

    #draws the wall
    drawWall(stage, wall_mad, xWall, wStage)
    
    #draws all the spikes
    drawSpikes(stage)

    #the stage blocks
    drawStage(stage)
   
    
    #blits character/messages
    characterBlit(stage, interact,numMess)
    
    #blits gems
    gemBlit(stage, gemmap)

    #writes #deaths and gems
    writeBasics(stage,deaths, gems) 

    #draws acessories (like arrows and stuff)
    drawAcessories(stage,wall_mad,xDot,wall_defeated)        

    #draws the dot
    drawDot(xDot,yDot)
    
    #music
    playMusic(wall_mad,music) 

#blits background
def background():
    DarkRealm= model.DarkRealm
    surface.blit(DarkRealm, (0, 0)) 

#plays music. Skip allows new song to play before old one finishes
    #skip: 0--> Do nothing  1--> Fallen_Reprise    2--> Mad
def playMusic(wall_mad,skip):
    if (skip==1):
        track='Audio/Fallen_Reprise.wav'
        pygame.mixer.music.stop()
    elif(skip==2):
        track='Audio/Mad.wav'
        pygame.mixer.music.stop()
    elif(not pygame.mixer.music.get_busy()):
        track='Audio/Fallen_Reprise.wav'
    else:
        return
        
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()
    
def writeBasics(stage,deaths, gems):
    text="Deaths "+str(deaths)
    textBounds=(18*w/20,h/20)
    messagePrint(w//40,text,textBounds,model.LGREY) 
    if(stage>=6):
        text="Crystals " + str(gems)
        textBounds=(w/15, h/20)
        messagePrint(w//40,text,textBounds,model.LGREY) 

        

def messagePrint(size,text,textB,color):
    #Text to screen
    font=pygame.font.SysFont('Calibri',size,False,False)
    text=font.render(text,True,color)  
    textBounds=text.get_rect()
    textBounds.center=textB
    
    surface.blit(text,textBounds)    
    

#draws the Dot character
def drawDot(xDot,yDot):
    pygame.draw.ellipse(surface,model.WHITE,(xDot,yDot,w/20,w/20),0) 
    
#selects which stage to draw then calls a method to actually draw it. Returns all blocks for collisions
def drawStage(stage):
    #makes mouse invisible while in the stages
    pygame.mouse.set_visible(False)
    
    if stage==1:
        return stages.drawStageOne()
    if stage==2:
        return stages.drawStageTwo()
    if stage==3:
        return stages.drawStageThree()
    if stage==4:
        return stages.drawStageFour()
    if stage==5:
        return stages.drawStageFive()
    if stage==6:
        return stages.drawStageSix()
    if stage==7:
        return stages.drawStageSeven()
    if stage==8:
        return stages.drawStageEight()
    if stage==9:
        return stages.drawStageNine()
    if stage==10:
        return stages.drawStageTen()
        
def drawSpikes(stage):
    if stage==6:
        return stages.drawStageSixSpikes()
    elif stage==7:
        return stages.drawStageSevenSpikes()
    elif stage==8:
        return stages.drawStageEightSpikes()
    elif stage==9:
        return stages.drawStageNineSpikes()
    else:
        return {}
           
    
#draws arrows and background messages
def drawAcessories(stage,wall_mad, xDot,wall_defeated):
    #opening instructions
    if(not wall_mad and not wall_defeated and stage==1):
        text="MOVE LEFT AND RIGHT USING ARROW KEYS"
        textBounds=(w/2,h/20)
        messagePrint(w//50,text,textBounds,model.LGREY)
        text="JUMP USING SPACEBAR"
        textBounds=(w/2,h/20+h/30)
        messagePrint(w//50,text,textBounds,model.LGREY)

    #blue button
    if(stage==1 and wall_mad):
        pygame.draw.rect(surface,model.BLUE,(89*w/200+1,22*h/25-h/50+1,2*w/15-w/25-1,h/50-1),0)
        
    #blits door
    if(stage==1 and wall_defeated):
        Door=model.Door
        #image of the exit door
        surface.blit(Door, (49*w/100,2*h/25,w/10,h/60)) 
        

def drawWall(stage, wall_mad, xWall, wStage):
    if(stage==wStage and wall_mad):
        pygame.draw.rect(surface,model.RED,(xWall,0,w,h),0)
    
def characterBlit(stage, interact,numMess):      
    #luis
    Luis.interact(interact, numMess, stage)
    Marvin.interact(interact, numMess, stage)


def gemBlit(stage, gemmap):
    if (stage==6):
        gemBlit6(gemmap)
    if (stage==7):
        gemBlit7(gemmap)
    if (stage==8):
        gemBlit8(gemmap)
    if (stage==9):
        gemBlit9(gemmap)


def gemBlit6(gemmap):
    crystal=model.crystal
    map=gemmap[0]
    #crystal 1
    if(map&10):
        surface.blit(crystal, (3*w/5,h/5,w/30,h/30))
    #crystal 2
    if(map&1):
        surface.blit(crystal, (9.5*w/10,h/5,w/30,h/30)) 
    
def gemBlit7(gemmap):
    crystal=model.crystal
    map=gemmap[1]
    #crystal 1
    if(map&100):
        surface.blit(crystal, (3*w/12,28*h/40,w/30,h/30))
    #crystal 2
    if(map&10):
        surface.blit(crystal, (86*w/120,84*h/120, w/30, h/30))
    #crystal 3
    if(map&1):
        surface.blit(crystal, (9.5*w/10,h/5,w/30,h/30))

def gemBlit8(gemmap):
    crystal=model.crystal
    map=gemmap[2]           
    if(map&0b10000):
        surface.blit(crystal, (12*w/30-w/30, 14*h/30-h/20, w/30, w/30))
    if(map&0b1000):
        surface.blit(crystal, (12*w/30, 14*h/30-h/20, w/30, w/30))
    if(map&0b100):
        surface.blit(crystal, (12*w/30+w/30, 14*h/30-h/20, w/30, w/30))
    if(map&0b10):                
        surface.blit(crystal, (w/3+w/10, 99*h/100-h/20, w/30, w/30))
    if(map&0b1):
        surface.blit(crystal, (2*w/3-w/10, 99*h/100-h/20, w/30, w/30))
        
def gemBlit9(gemmap):
    crystal=model.crystal
    map=gemmap[3]
    #top
    if(map&0b1000000000000):                
        surface.blit(crystal, (w/4+w/10, h/6-h/20, w/30, w/30))
    if(map&0b100000000000):                
        surface.blit(crystal, (w/2, h/6-h/20, w/30, w/30))
    if(map&0b10000000000):                
        surface.blit(crystal, (3*w/4-w/10, h/6-h/20, w/30, w/30))
    #steps  
    if(map&0b10000000):                
        surface.blit(crystal, (w/4+2*w/15,2*h/3-h/20, w/30, w/30))     
    if(map&0b1000000):                
        surface.blit(crystal, (w/4+3*w/15,11*h/30-h/20, w/30, w/30)) 
    if(map&0b100000):                
        surface.blit(crystal, (w/4+4*w/15,11*h/30-h/20, w/30, w/30)) 
    if(map&0b10000):                
        surface.blit(crystal, (w/4+5*w/15,2*h/3-h/20, w/30, w/30))  
    #bottom
    if(map&0b10):                
        surface.blit(crystal, (w/3,18*h/20, w/30, w/30))   
    if(map&0b1):                
        surface.blit(crystal, (2*w/3,18*h/20, w/30, w/30))

