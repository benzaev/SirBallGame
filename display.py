#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.28

#This blits everything

import pygame, model, stages, Luis, Marvin

#pygame initialization
pygame.init()
pygame.mixer.init()

w= model.w
h= model.h
surface= model.surface

#projects to screen
def view(SirBall, interact, numMess, keys, prevKey, wall_mad, wall_defeated, xWall, wStage, music, gemmap):
    #makes mouse invisible while in the stages
    pygame.mouse.set_visible(False)  
    
   #background image
    background(SirBall)

    #draws the wall
    drawWall(SirBall.stage, wall_mad, xWall, wStage)
    
    #draws all the spikes
    drawSpikes(SirBall.stage)

    #the stage blocks
    drawStage(SirBall)
   
    #blits character/messages
    characterBlit(SirBall.stage, interact,numMess)

    #blits gems
    gemBlit(SirBall.stage, gemmap)

    #writes #deaths and gems
    writeBasics(SirBall) 

    #draws acessories (like arrows and stuff)
    drawAcessories(SirBall,wall_mad,wall_defeated) 

    #draw Lazers    
    drawLazer()
    
    #test draw
    #pygame.draw.rect(surface,model.RED,(w/40,h/13, w/8, h/3),1) 


    #draws the dot      
    drawDot(SirBall)

        
    #music
    playMusic(wall_mad,music)         
    
#cycles through all moving objects and blits lazers to the screen
def drawLazer():
    for x in model.movingObjects:
        if (isinstance(x, stages.Lazer)):
            x.drawSelf()
            

#blits background
def background(SirBall):
    if(not SirBall.stage==100):
        DarkRealm= model.DarkRealm
        surface.blit(DarkRealm, (0, 0))
    else:
        Altar=model.Altar
        surface.blit(Altar, (0, 0))


#plays music. Skip allows new song to play before old one finishes
    #skip: 0--> Do nothing  1--> Fallen_Reprise    2--> Mad     3--> Ruins
def playMusic(wall_mad,skip):
    if (skip==1):
        track='Audio/Fallen_Reprise.wav'
        pygame.mixer.music.stop()
    elif(skip==2):
        track='Audio/Mad.wav'
        pygame.mixer.music.stop()
    elif(skip==3):
        track='Audio/Ruins.wav'
        pygame.mixer.music.stop()
    elif(not pygame.mixer.music.get_busy()):
        track='Audio/Fallen_Reprise.wav'
    else:
        return
        
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()
    
def writeBasics(SirBall):
    text="Deaths "+str(SirBall.deaths)
    textBounds=(18*w/20,h/20)
    messagePrint(w//40,text,textBounds,model.LGREY) 
    if(SirBall.stage>=6):
        text="Crystals " + str(SirBall.gems)
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
def drawDot(SirBall):
    SirBall.paintMeLikeAFrenchGirl()
        
#selects which stage to draw then calls a method to actually draw it. Returns all blocks for collisions
def drawStage(SirBall):
    stage=SirBall.stage
    if stage==1:
        return stages.drawStageOne()
    elif stage==2:
        return stages.drawStageTwo()
    elif stage==3:
        return stages.drawStageThree()
    elif stage==4:
        return stages.drawStageFour()
    elif stage==5:
        return stages.drawStageFive()
    elif stage==6:
        return stages.drawStageSix()
    elif stage==7:
        return stages.drawStageSeven()
    elif stage==8:
        return stages.drawStageEight()
    elif stage==9:
        return stages.drawStageNine()
    elif stage==10:
        return stages.drawStageTen()
    elif stage==11: 
        return stages.drawStageEleven()
    elif stage==12:
        return stages.drawStageTwelve()
    elif stage==13:
        return stages.drawStageThirteen()
    elif stage==14:
        return stages.drawStageFourteen()
    elif stage==15:
        return stages.drawStageFifteen()
    elif stage==16:
        return stages.drawStageSixteen(SirBall)
    elif stage==17:
        return stages.drawStageSeventeen()
    elif stage==18:
        return stages.drawStageEighteenteen()
    #get more gems
    elif (stage>=19 and stage<100):
        return stages.drawStageMoreGems(SirBall)
    #altar
    elif stage==100:
        return stages.drawStage100()

        
def drawSpikes(stage):
    if stage==6:
        return stages.drawStageSixSpikes()
    elif stage==7:
        return stages.drawStageSevenSpikes()
    elif stage==8:
        return stages.drawStageEightSpikes()
    elif stage==9:
        return stages.drawStageNineSpikes()
    elif stage==10:
        return stages.drawStageTenSpikes()
    elif stage==11:
        return stages.drawStageElevenSpikes()
    elif stage==12:
        return stages.drawStageTwelveSpikes()
    elif stage==13:
        return stages.drawStageThirteenSpikes()
    elif stage==14:
        return stages.drawStageFourteenSpikes()
    elif stage==15:
        return stages.drawStageFifteenSpikes()
    elif stage==16:
        return stages.drawStageSixteenSpikes()
    elif stage==17:
        return stages.drawStageSeventeenSpikes()
    elif stage==18:
        return stages.drawStageEighteenSpikes()
    elif stage>=19 and stage<100:
        return stages.drawStageMoreGemsSpikes()

    else:
        return []
           
    
#draws arrows and background messages
def drawAcessories(SirBall,wall_mad,wall_defeated):
    xDot=SirBall.xDot
    stage=SirBall.stage
    #opening instructions
    if(not wall_mad and not wall_defeated and stage==1):
        text="MOVE LEFT AND RIGHT USING ARROW KEYS"
        textBounds=(w/2,h/20)
        messagePrint(w//50,text,textBounds,model.LGREY)
        text="JUMP USING SPACEBAR"
        textBounds=(w/2,h/20+h/30)
        messagePrint(w//50,text,textBounds,model.LGREY)
    #instructions for meeting bananas
    if(stage==16):
        text="USE THE SWORD TO DESTROY THE BANANAS"
        textBounds=(w/2,h/20)
        messagePrint(w//50,text,textBounds,model.LGREY)
        text="AVOID THE LASERS!"
        textBounds=(w/2,h/20+h/30)
        messagePrint(w//50,text,textBounds,model.LGREY)
    #text on signs stage 18
    if(stage==18):
        text="More Gems"
        textBounds=(151*w/200, 91*h/100-h//8)
        messagePrint(w//60,text,textBounds,model.BLACK)
        text="This Way"
        textBounds=(151*w/200, 91*h/100-h//8+h/30)
        messagePrint(w//60,text,textBounds,model.BLACK)
        text="THE ALTAR"
        textBounds=(151*w/200, 2*h/5-h//9)
        messagePrint(w//60,text,textBounds,model.BLACK)
        if(SirBall.gems<50 and SirBall.xDot>w/2 and SirBall.yDot<=2*h/5):
            text="YOU NEED MORE GEMS"
            textBounds=(w/2,h/20)
            messagePrint(w//50,text,textBounds,model.LGREY)
        elif(SirBall.gems>=50):
            text="YOU HAVE ENOUGH GEMS"
            textBounds=(w/2,h/20)
            messagePrint(w//50,text,textBounds,model.LGREY)
            text="GO TO THE ALTAR"
            textBounds=(w/2,h/20+h/30)
            messagePrint(w//50,text,textBounds,model.LGREY)
    #text on stage 19+
    if(stage>=19 and stage<100 and SirBall.gems<50):
        text="YOU NEED MORE GEMS"
        textBounds=(w/2,h/20)
        messagePrint(w//50,text,textBounds,model.LGREY)
            

    #blue button and arrows
    if(stage==1 and wall_mad and not wall_defeated):
        pygame.draw.rect(surface,model.BLUE,(89*w/200+1,22*h/25-h/50+1,2*w/15-w/25-1,h/50-1),0)
        #draw Arrow to button
        pygame.draw.rect(surface,model.YELLOW,(97*w/200, 130*h/200, 3*w/200, 20*h/200),0) 
        pygame.draw.polygon(surface,model.YELLOW,[(95*w/200, 150*h/200),(102*w/200, 150*h/200),(98.5*w/200, 160*h/200)],0)
    elif (stage==1 and wall_mad and wall_defeated):
        pygame.draw.rect(surface,model.YELLOW,(80*w/200, 60*h/200, 10*w/200, 4*h/200),0) 
        pygame.draw.polygon(surface,model.YELLOW,[(90*w/200, 58*h/200),(90*w/200, 66*h/200),(93*w/200, 62*h/200)],0)



        
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
    elif (stage==7):
        gemBlit7(gemmap)
    elif (stage==8):
        gemBlit8(gemmap)
    elif (stage==9):
        gemBlit9(gemmap)
    elif (stage==10):
        gemBlit10(gemmap)
    elif (stage==11):
        gemBlit11(gemmap)
    elif (stage==12):
        gemBlit12(gemmap)
    elif(stage==13):
        gemBlit13(gemmap)
    elif(stage==14):
        gemBlit14(gemmap)
    elif(stage==15):
        gemBlit15(gemmap)
    elif(stage==16):
        gemBlit16(gemmap)
    elif(stage==17):
        gemBlit17(gemmap)
    elif(stage==18):
        gemBlit18(gemmap)
    elif(stage>=19 and stage<100):
        gemBlit19(gemmap)


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
        
def gemBlit10(gemmap):
    crystal=model.crystal
    map=gemmap[4]
    
    #left
    if(map&10):
        surface.blit(crystal, (w/50, 9*h/10-h/20, w/30, h/30)) 
    #right
    if(map&1):
        surface.blit(crystal, (19*w/20, 9*h/10-h/20, w/30, h/30))
    
    
def gemBlit11(gemmap):
    crystal=model.crystal
    map=gemmap[5]
    #first                                              
    if(map&100000):
        surface.blit(crystal, (5*w/12-4*w/15, 11*h/30-h/20, w/30, h/30)) 
    #second...
    if(map&0b10000):
        surface.blit(crystal, (5*w/12-2*w/15, 11*h/30-h/20, w/30, h/30))
    if(map&0b1000):
        surface.blit(crystal, (5*w/12, 11*h/30-h/20, w/30, h/30))
    if(map&0b100):
        surface.blit(crystal, (5*w/12+2*w/15, 11*h/30-h/20, w/30, h/30))
    if(map&0b10):
        surface.blit(crystal, (5*w/12+4*w/15, 11*h/30-h/20, w/30, h/30))
    if(map&0b1):
        surface.blit(crystal, (5*w/12+6*w/15, 11*h/30-h/20, w/30, h/30))
    
def gemBlit12(gemmap):
    crystal=model.crystal
    map=gemmap[6]
    #first                                              
    if(map&0b100000):
        surface.blit(crystal, (2*w/6, h/10, w/30, h/30)) 
    #second...
    if(map&0b10000):
        surface.blit(crystal, (3*w/6, h/10, w/30, h/30)) 
    if(map&0b1000):
        surface.blit(crystal, (4*w/6, h/10, w/30, h/30)) 
    if(map&0b100):
        surface.blit(crystal, (5*w/12, 13*h/32, w/30, h/30)) 
    if(map&0b10):
        surface.blit(crystal, (7*w/12, 13*h/32, w/30, h/30)) 
    if(map&0b1):
        surface.blit(crystal, (9*w/12, 13*h/32, w/30, h/30)) 


#36 gems total not including bananas
def gemBlit13(gemmap):
    crystal=model.crystal
    map=gemmap[7]
    if(map&0b100):
        surface.blit(crystal, (w/90, 3*h/12-h/20, w/30, h/30)) 
    if(map&0b10):
        surface.blit(crystal, (w/90+w/20, 3*h/12-h/20, w/30, h/30)) 
    if(map&0b1):
        surface.blit(crystal, (w/90+2*w/20, 3*h/12-h/20, w/30, h/30)) 
        
#41 gems total
def gemBlit14(gemmap):
    crystal=model.crystal
    map=gemmap[8]
    if(map&0b10000):    
        surface.blit(crystal,(w/4, h/2-h/20, w/30, h/30))
    if(map&0b1000):    
        surface.blit(crystal,(w/4+3*w/20, 6*h/10, w/30, h/30))
    if(map&0b100):    
        surface.blit(crystal,(w/4+3*w/10, h/2-h/20, w/30, h/30))
    if(map&0b10):    
        surface.blit(crystal,(w/4+9*w/20, 6*h/10, w/30, h/30))
    if(map&0b1):    
        surface.blit(crystal,(w/4+6*w/10, h/2-h/20, w/30, h/30))

#46 total
def gemBlit15(gemmap):
    crystal=model.crystal
    map=gemmap[9]
    if(map&0b10000):    
        surface.blit(crystal,(9*w/12, 5*h/8, w/30, h/30))
    if(map&0b1000):    
        surface.blit(crystal,(10*w/12, 4*h/8, w/30, h/30))
    if(map&0b100):    
        surface.blit(crystal,(9*w/12, 3*h/8, w/30, h/30))
    if(map&0b10):    
        surface.blit(crystal,(9*w/12, 2*h/8, w/30, h/30))
    if(map&0b1):    
        surface.blit(crystal,(3*w/5, h/6, w/30, h/30))
        
#49 total
def gemBlit16(gemmap):
    crystal=model.crystal
    map=gemmap[10]
    if(map&0b100):    
        surface.blit(crystal,(w/3+w/40, 4*h/20, w/30, h/30))
    if(map&0b10):    
        surface.blit(crystal,(w/3+w/40, 12*h/20, w/30, h/30))
    if(map&0b1):   
        surface.blit(crystal,(20*w/30+w/40, 7*h/20, w/30, h/30))

#52 total
def gemBlit17(gemmap):
    crystal=model.crystal
    map=gemmap[11]
    if(map&0b100):    
        surface.blit(crystal,(w/3+w/40, 44*h/200, w/30, h/30))
    if(map&0b10):    
        surface.blit(crystal,(w/3+w/4, 44*h/200, w/30, h/30))
    if(map&0b1):    
        surface.blit(crystal,(w/3+w/2, 44*h/200, w/30, h/30))
        
#62 total
def gemBlit18(gemmap):
    crystal=model.crystal
    map=gemmap[12]
    if(map&0b1000):    
        surface.blit(crystal,(5*w/10, 9*h/10-h/20, w/30, h/30))
    if(map&0b100):    
        surface.blit(crystal,(6*w/10, 9*h/10-h/20, w/30, h/30))
    if(map&0b10):    
        surface.blit(crystal,(7*w/10, 9*h/10-h/20, w/30, h/30))
    if(map&0b1):    
        surface.blit(crystal,(8*w/10, 9*h/10-h/20, w/30, h/30))
        
#72 total
def gemBlit19(gemmap):
    crystal=model.crystal
    map=gemmap[13]
    if(map&0b1000000000):    
        surface.blit(crystal,(13*w/20, 3*h/10, w/30, h/30))
    if(map&0b100000000):    
        surface.blit(crystal,(13*w/20, 4*h/10, w/30, h/30))
    if(map&0b10000000):    
        surface.blit(crystal,(13*w/20, 5*h/10, w/30, h/30))
    if(map&0b1000000):    
        surface.blit(crystal,(13*w/20, 6*h/10, w/30, h/30))
    if(map&0b100000):    
        surface.blit(crystal,(8*w/20, 3*h/20, w/30, h/30))
    if(map&0b10000):    
        surface.blit(crystal,(9*w/20, 3*h/20, w/30, h/30))
    if(map&0b1000):    
        surface.blit(crystal,(10*w/20, 3*h/20, w/30, h/30))
    if(map&0b100):    
        surface.blit(crystal,(11*w/20, 3*h/20, w/30, h/30))
    if(map&0b10):    
        surface.blit(crystal,(6*w/15, 7*h/20, w/30, h/30))
    if(map&0b1):    
        surface.blit(crystal,(8*w/15, 7*h/20, w/30, h/30))





    
    
    

