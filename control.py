#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.27

#moves stuff around

import pygame, math, display, model, sys, Luis, Marvin

#pygame initialization
pygame.init()

w=model.w
h=model.h

#all moving parts
def controller(SirBall, keys, interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, gems, frame):
    #master control
   # if (keys[pygame.K_a] and not keys==prevKey):
    #    SirBall.setstage(SirBall.stage+1)  
     #   model.resetMovingObjects()
   # if (keys[pygame.K_b] and not keys==prevKey):
    #    SirBall.setstage(SirBall.stage-1)
     #   model.resetMovingObjects()

    
    music=0
    moveBlocks()
    #if not currently interacting with a character, continue on
    if (not interact):
        #wall mechanics
        wall_mad,wall_defeated,xWall,wStage, music=wallMechanics(SirBall,xWall,wStage,wall_mad, wall_defeated, music)
        
        #moving the dot
        moveDot(keys,SirBall)  
                
        #does a cute little jump action
        jumpDot(keys,SirBall)
        fallingDot(SirBall)
        
        #keeps dot on the line
        stayOnLine(SirBall)
        
        #respawn
        xWall,wStage,wall_defeated=respawn(xWall,wStage,wall_mad, wall_defeated, SirBall)   
        
        gemmap, gems= collectGem(SirBall, gemmap, gems)
        
        rightToBearArms(SirBall)
        
        killEnemy(SirBall)
        
        shootLazers(SirBall, frame)
        
    #does interaction
    numMess, interact, music = characterInteractions(SirBall, numMess, interact, keys, prevKey, music)
            
    #checks if goes through a door
    numMess, wall_mad, music= nextLevel(SirBall, wall_defeated, numMess, wall_mad, music)   
        
    #allows for test KEYUP
    prevKey=keys
    
    frame+=1
    
    return interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, gems, frame


#shoots lazers at SirBall from bananas      x, y, xDot, yDot
def shootLazers(SirBall, frame):
    xDot=SirBall.xDot+w/40
    yDot=SirBall.yDot+w/40
    for q in model.movingObjects:
        if (isinstance(q, display.stages.Banana)):
            if (q.alive and q.lastShot+100<frame):
                laser=display.stages.Lazer(q.x, q.y, xDot, yDot)
                model.addMovingObject(laser)
                q.setLastShot(frame)



#tests if SirBall killed an enemy 
def killEnemy(SirBall):
    ballRect=pygame.Rect(SirBall.xDot,SirBall.yDot,w/20,h/11)
    for x in model.movingObjects:
        if (isinstance(x, display.stages.Banana)):
            if(x.getBox().colliderect(ballRect) and x.alive):
                if(SirBall.armed):
                    x.setAlive(False)                
                
                
#moves all the movable blocks
def moveBlocks():
    for x in model.movingObjects:
        x.moveSelf()
        
def rightToBearArms(SirBall):
    if(SirBall.stage==16 and SirBall.xDot+w/40>w//10 and SirBall.xDot-w/30<w//10 and SirBall.yDot<4*h/10 and SirBall.yDot>4*h/10-h/10):
        SirBall.setarmed(True)
    
#checks if Sir Ball went through a door    
def nextLevel(SirBall, wall_defeated, numMess, wall_mad, music):
    #goes through door on first stage
    if(SirBall.stage==1 and wall_defeated and (SirBall.xDot)>=49*w/100 and (SirBall.xDot<=49*w/100+w/20) and (SirBall.yDot<=2*h/5)):
        SirBall.setstage(6)
        SirBall.setxDot(w/100)
        SirBall.setyDot(0)
        numMess=0
        wall_mad=False
        music=1
    #goes through door on stage 9
    door9=pygame.Rect(9*w/10, h/2-h/3, w/10, h/3)
    if(SirBall.stage==9 and door9.collidepoint(SirBall.xDot+w/40,SirBall.yDot+w/40)):
        SirBall.setstage(10)
        SirBall.setxDot(w/100)
        SirBall.setyDot(14*h/30-h/20)
        numMess=0
    #goes through door on stage 15
    door15=pygame.Rect(17*w/20, h//5,w//12, h//5)
    if(SirBall.stage==15 and door15.collidepoint(SirBall.xDot+w/40,SirBall.yDot+w/40)):
        SirBall.setstage(16)
        SirBall.setxDot(w/100)
        SirBall.setyDot(h/2)
        numMess=0
        model.resetMovingObjects()

    
    return numMess, wall_mad, music

#starts, moves, and stops wall
def wallMechanics (SirBall,xWall,wStage,wall_mad, wall_defeated, music):
    #where the stage 1 button is
    block=pygame.Rect(89*w/200,22*h/25-h/50,2*w/15-w/25,h/50+1)    
    #presses the button to stop the wall
    if(SirBall.stage==1 and wall_mad and not wall_defeated and block.collidepoint(SirBall.xDot+w/40,SirBall.yDot+w/20)):
        wall_defeated=True
    #activates the stage 5 wall
    if(not wall_defeated and not wall_mad and SirBall.stage==5 and SirBall.xDot>=12*w/20):
        wall_mad=True
        music=2
    #moves the wall
    if(wall_mad):
        xWall-=w/220
        if(xWall<=0):
            xWall=w
            wStage=wStage-1 

    return wall_mad,wall_defeated,xWall,wStage, music
    

    
#perform cute jump animation, only for upward motion
def jumpDot(keys,SirBall):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    stage=SirBall.stage
    in_jump=SirBall.in_jump
    in_fall=SirBall.in_fall
    jump=SirBall.jump

    #where is the roof?
    ceiling=YCeiling(SirBall)
    
    #if not currently jumping and you push space
    if (keys[pygame.K_SPACE] and not in_jump and not in_fall):
        SirBall.setin_jump(True)
        SirBall.setjump(1000)
        
    #if jumping currently, continue
    if (in_jump):
        #if going up, don't hit ceiling
        if (jump<=1000 and jump>500):
            SirBall.setyDot(yDot-((jump-500)**2)*h/5700000)
            if (SirBall.yDot<ceiling):
                SirBall.setyDot(ceiling)
                SirBall.setin_jump(False)
        else:
            SirBall.setin_jump(False)
            
        if(in_jump):
            SirBall.setjump(jump-25)
    
#if the dot isn't on the groun, it falls to the ground
def fallingDot(SirBall):
    
    yMaxi=YFloor(SirBall)
    
    if (not SirBall.in_jump and SirBall.yDot<yMaxi-3*h/1000 and not SirBall.in_fall):
        SirBall.setfall(500)
        SirBall.setin_fall(True)
    #if Sir Ball is falling, make him fall
    if(SirBall.in_fall):
        SirBall.setyDot(SirBall.yDot+(h/8000000)*(SirBall.fall-500)**2)
        if (SirBall.yDot>=yMaxi):
            SirBall.setyDot(yMaxi)
            SirBall.setin_fall(False)
           
        SirBall.setfall(SirBall.fall-25)  
    
    
#stay on lines methods here
def stayOnLine(SirBall):
    if (not SirBall.in_jump and not SirBall.in_fall):
        SirBall.setyDot(YFloor(SirBall))
    
#returns the y value of the first floor below the ball
def YFloor(SirBall):
    #center of the Dot
    xDot=SirBall.xDot+w/40   
    yDot=SirBall.yDot+w/40
    maxi=2*h
    blocks=display.drawStage(SirBall)
    for x in blocks:
        if(x.left<=xDot and x.right>=xDot):
            if(x.top<maxi and x.top>=yDot):
                maxi=x.top
    return maxi-w/20

#returns the lowest platform above ball    
def YCeiling (SirBall):
    #center of Dot  
    xDot=SirBall.xDot+w/40
    yDot=SirBall.yDot+w/40
    ceiling=0
    blocks=display.drawStage(SirBall)
    for x in blocks:
        if(x.left<=xDot and x.right>=xDot):
            if(x.bottom>ceiling and x.bottom<=yDot):
                ceiling=x.bottom
    return ceiling

    
#moves dot left or right
def moveDot(keys,SirBall):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    stage=SirBall.stage
    
    if (keys[pygame.K_RIGHT] and moveRight(SirBall)):
        if (xDot+w/20)<w:
            SirBall.setxDot(xDot+w/200)
        else:
            SirBall.setxDot(0)
            SirBall.setstage(stage+1)
            model.resetMovingObjects()
    if (keys[pygame.K_LEFT] and moveLeft(SirBall)):
        if (xDot)>0:
            SirBall.setxDot(xDot-w/200)
        else:
            if (stage!=1):
                SirBall.setxDot(w-w/20)
                SirBall.setstage(stage-1)
                model.resetMovingObjects()

        


#These check if there is an object blocking them from moving in a direction
def moveLeft(SirBall):    
    #if by next move it would touch the wall, return False
    blocks=display.drawStage(SirBall)
    player= pygame.Rect(SirBall.xDot,SirBall.yDot+w/100,w/20-w/40,w/20-w/50)
    for x in blocks:
        if (x.colliderect(player)):
            return False
    return True  
    
def moveRight(SirBall):
    #if by next move it would touch the wall, return False
    blocks=display.drawStage(SirBall)
    player= pygame.Rect(SirBall.xDot+w/40,SirBall.yDot+w/100,w/20-w/40,w/20-w/50)
    for x in blocks:
        if (x.colliderect(player)):
            return False
    return True
       
#checks if hit bottom, ran into wall, or hit spikes 

def respawn(xWall,wStage,wall_mad, wall_defeated, SirBall):
    #hits floor
    if (SirBall.yDot+w/20>=h):
        resetForRespawn(SirBall, xWall, wStage, wall_defeated, wall_mad, False)

    #hits wall
    if(wall_mad and wStage==SirBall.stage and xWall<=SirBall.xDot+w/20):
        xWall, wStage, wall_defeated=resetForRespawn(SirBall, xWall, wStage, wall_defeated, wall_mad, True)

    #hits spikes
    spikes=display.drawSpikes(SirBall.stage)
    player= pygame.Rect(SirBall.xDot,SirBall.yDot+w/100,w/20,3*w/100)
    for x in spikes:
        if (x.colliderect(player)):
            xWall, wStage, wall_defeated=resetForRespawn(SirBall, xWall, wStage, wall_defeated, wall_mad, False)


    #if hits the enemy while unarmed
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    for x in model.movingObjects:
        if (isinstance(x, display.stages.Banana)):
            if(x.getBox().colliderect(ballRect) and x.alive):
                if(not SirBall.armed):
                    xWall, wStage, wall_defeated=resetForRespawn(SirBall, xWall, wStage, wall_defeated, wall_mad, False)

                            
    #if SirBall is hit by a laser           
    for laser in model.movingObjects:
        if (isinstance(laser, display.stages.Lazer)):
            if(ballRect.collidepoint(laser.point1) or ballRect.collidepoint(laser.point2) or ballRect.collidepoint(laser.point3) or ballRect.collidepoint(laser.point4)):
                xWall, wStage, wall_defeated=resetForRespawn(SirBall, xWall, wStage, wall_defeated, wall_mad, False)
                laser.x=-100
                laser.deltaX=0
                    
    return xWall,wStage,wall_defeated
    
#if Sir Ball has died, reset all the values here
def resetForRespawn(SirBall, xWall, wStage, wall_defeated, wall_mad, hit_wall):
    if(hit_wall):
        SirBall.setstage(5)
        SirBall.setxDot(w/8)
        SirBall.setdeaths(SirBall.deaths+1)
        xWall=w
        wStage=5
        wall_defeated=False
        resetY=h/2
        SirBall.setyDot(resetY)
    elif (wall_mad):
        SirBall.setxDot(7*w/8)
        SirBall.setdeaths(SirBall.deaths+1)
        resetY=0
        SirBall.setyDot(resetY)
    else:
        SirBall.setxDot(0)
        SirBall.setdeaths(SirBall.deaths+1)
        resetY=h/2
        SirBall.setyDot(resetY)
        
    while(True):
        SirBall.setyDot(YFloor(SirBall))
        if(SirBall.yDot>=h):
            if(SirBall.xDot>w/100):
                SirBall.setxDot(SirBall.xDot-w/100)
            resetY-=h/50
            SirBall.setyDot(resetY)
        else:
            break
                
    return xWall, wStage, wall_defeated

    
    

def characterInteractions (SirBall, numMess, interact, keys, prevKey, music):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    stage=SirBall.stage
    numMessPrev=numMess
    #if gets close to a character, begin interaction
    if((stage==10 and xDot>=4*w/15 and xDot<8*w/15 and yDot>=9*h/10-w/20 and numMess<=19) or 
    (xDot>=3*w/5 and xDot<9*w/10  and yDot>=4*h/5-w/20 and numMess<=15 and stage==1) or 
    (xDot>=2*w/5 and xDot<2*w/5+w/10 and yDot>=9*h/10-w/20 and numMess<=19 and stage==6)):
        interact=True
    #ends interaction after all messages shown
    if(stage==1 and numMess>15 or stage==6 and numMess>19 or stage==10 and numMess>19):
        interact=False
    if(stage==10 and (numMess==20 or numMess==100000)):
        music=3
        numMess+=1
    if(interact):
        #check if want to skip talk or go to next page
        if keys[pygame.K_s]:
            numMess=100000
        elif(keys[pygame.K_c] and not keys==prevKey):
            numMess+=1  
            
    #Luis moving down stage 10
    Ly=Luis.getY()
    if (stage==10 and numMess>=4 and Ly<75*h/100):
        Luis.setY(Ly+h/400)
    #wait for him to descend
    if (stage==10 and numMess>11 and  numMess<900 and Ly<75*h/100):
        numMess=numMessPrev
    if (stage==10 and numMess==11 and Ly>75*h/100):
        numMess+=1
    #Luis pushing Marvin stage 10
    if (stage==10 and numMess>=16):
        Lx=Luis.getX()
        Mx=Marvin.getX()
        My=Marvin.getY()
        #moving right
        if(My==78*h/100):
            Luis.setX(Lx+w/500)
            if(Lx+w/20>=Mx):
                Marvin.setX(Mx+w/500)
        #Marvin falling
        if(Mx>11*w/15-w/30 and My<2*h):
            Marvin.setY(My+h/100)
        #Luis comming back
        if (My==78*h/100+h/100):
            Luis.setX(2*w/3-w/7)  
            if(numMess==16):
                numMess+=1
    
    return numMess, interact, music
    
#collects gems for Sir Ball
def collectGem(SirBall, gemmap, gems):  
    stage=SirBall.stage
    #stage 6 gems
    if (stage==6):
        gemmap, gems=stage6Gems(SirBall, gemmap, gems)
    #stage 7 gems
    if (stage==7):
        gemmap, gems=stage7Gems(SirBall, gemmap, gems)    
    if (stage==8):
        gemmap, gems=stage8Gems(SirBall, gemmap, gems)
    if (stage==9):
        gemmap, gems=stage9Gems(SirBall, gemmap, gems)
    if (stage==10):
        gemmap, gems=stage10Gems(SirBall, gemmap, gems)
    if (stage==11):
        gemmap, gems=stage11Gems(SirBall, gemmap, gems)
    if (stage==12):
        gemmap, gems=stage12Gems(SirBall, gemmap, gems)
    if (stage==13):
        gemmap, gems=stage13Gems(SirBall, gemmap, gems)
    if (stage==14):
        gemmap, gems=stage14Gems(SirBall, gemmap, gems)
    if(stage==15):
        gemmap, gems=stage15Gems(SirBall, gemmap, gems)


    

        
    return gemmap, gems    
    
def stage6Gems(SirBall, gemmap, gems):
    map=gemmap[0]
    gem1=pygame.Rect(3*w/5,h/5,w/20,h/20)
    gem2=pygame.Rect(9.5*w/10,h/5,w/20,h/20)
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    #first gem
    if (map&10 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&1
        gems+=1
        gemmap[0]=map
    #second gem
    if (map&1 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&10
        gems+=1
        gemmap[0]=map
        
    return gemmap, gems

def stage7Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[1]
    gem1=pygame.Rect(3*w/12,28*h/40,w/20,h/20)
    gem2=pygame.Rect(86*w/120,84*h/120,w/20,h/20)
    gem3=pygame.Rect(9.5*w/10,h/5,w/20,h/20)
    #first gem
    if (map&100 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&11
        gems+=1
        gemmap[1]=map
    #second gem
    if (map&10 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&101
        gems+=1
        gemmap[1]=map
    #third gem
    if (map&1 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&110
        gems+=1
        gemmap[1]=map
        
    return gemmap, gems

def stage8Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[2]
    gem1=pygame.Rect(12*w/30-w/30, 14*h/30-h/20, w/30, h/20)
    gem2=pygame.Rect(12*w/30, 14*h/30-h/20, w/30, h/20)
    gem3=pygame.Rect(12*w/30+w/30, 14*h/30-h/20, w/30, h/20)
    gem4=pygame.Rect(w/3+w/10, 99*h/100-h/20, w/30, h/20)
    gem5=pygame.Rect(2*w/3-w/10, 99*h/100-h/20, w/30, h/20)

    #first gem
    if (map&0b10000 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111
        gems+=1
        gemmap[2]=map
    #second gem
    elif (map&0b1000 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b10111
        gems+=1
        gemmap[2]=map
    #third gem
    elif (map&0b100 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11011
        gems+=1
        gemmap[2]=map
    #fourth gem
    elif (map&0b10 and gem4.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11101
        gems+=1
        gemmap[2]=map
    #fifth gem
    elif (map&0b1 and gem5.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11110
        gems+=1
        gemmap[2]=map
        
    return gemmap, gems

def stage9Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[3]
    gem1=pygame.Rect(w/4+w/10, h/6-h/20, w/30, h/20)
    gem2=pygame.Rect(w/2, h/6-h/20, w/30, h/20)
    gem3=pygame.Rect(3*w/4-w/10, h/6-h/20, w/30, h/20)
    gem4=pygame.Rect(w/4, 2*h/3-h/20, w/30, h/20)
    gem5=pygame.Rect(w/4+w/15, 11*h/30-h/20, w/30, h/20)
    gem6=pygame.Rect(w/4+2*w/15,2*h/3-h/20, w/30, h/20)
    gem7=pygame.Rect(w/4+3*w/15,11*h/30-h/20, w/30, h/20)
    gem8=pygame.Rect(w/4+4*w/15,11*h/30-h/20, w/30, h/20)
    gem9=pygame.Rect(w/4+5*w/15,2*h/3-h/20, w/30, h/20)
    gem10=pygame.Rect(w/4+6*w/15,11*h/30-h/20, w/30, h/20)
    gem11=pygame.Rect(w/4+7*w/15,2*h/3-h/20, w/30, h/20)
    gem12=pygame.Rect(w/3,18*h/20, w/30, h/32)
    gem13=pygame.Rect(2*w/3,18*h/20, w/30, h/20)
    #first gem
    if (map&0b1000000000000 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b111111111111
        gems+=1
        gemmap[3]=map
    #second gem
    if (map&0b100000000000 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1011111111111
        gems+=1
        gemmap[3]=map
    #third gem
    if (map&0b10000000000 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1101111111111
        gems+=1
        gemmap[3]=map
    #etc
    if (map&0b10000000 and gem6.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111101111111
        gems+=1
        gemmap[3]=map
    if (map&0b1000000 and gem7.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111110111111
        gems+=1
        gemmap[3]=map
    if (map&0b100000 and gem8.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111111011111
        gems+=1
        gemmap[3]=map
    if (map&0b10000 and gem9.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111111101111
        gems+=1
        gemmap[3]=map
    if (map&0b10 and gem12.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111111111101
        gems+=1
        gemmap[3]=map
    if (map&0b1 and gem13.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111111111110
        gems+=1
        gemmap[3]=map

        
    return gemmap, gems
    
def stage10Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[4]
    gem1=pygame.Rect(w/50, 9*h/10-h/20, w/30, h/20)          
    gem2=pygame.Rect(19*w/20, 9*h/10-h/20, w/30, h/20) 
    #first gem
    if (map&10 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&1
        gems+=1
        gemmap[4]=map
    #second gem
    if (map&1 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&10
        gems+=1
        gemmap[4]=map
        
    return gemmap, gems
    
def stage11Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[5]
    gem1=pygame.Rect(5*w/12-4*w/15, 11*h/30-h/18, w/30, h/30) 
    gem2=pygame.Rect(5*w/12-2*w/15, 11*h/30-h/18, w/30, h/30) 
    gem3=pygame.Rect(5*w/12, 11*h/30-h/20, w/18, h/30) 
    gem4=pygame.Rect(5*w/12+2*w/15, 11*h/30-h/18, w/30, h/30) 
    gem5=pygame.Rect(5*w/12+4*w/15, 11*h/30-h/18, w/30, h/30) 
    gem6=pygame.Rect(5*w/12+6*w/15, 11*h/30-h/18, w/30, h/30) 
        
    #first gem
    if (map&0b100000 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11111
        gems+=1
        gemmap[5]=map
    #second gem...
    if (map&0b10000 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b101111
        gems+=1
        gemmap[5]=map
    if (map&0b1000 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b110111
        gems+=1
        gemmap[5]=map
    if (map&0b100 and gem4.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b111011
        gems+=1
        gemmap[5]=map
    if (map&0b10 and gem5.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b111101
        gems+=1
        gemmap[5]=map
    if (map&0b1 and gem6.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b111110
        gems+=1
        gemmap[5]=map

    return gemmap, gems
    
    
def stage12Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[6]
    gem1=pygame.Rect(2*w/6, h/10, w/30, h/30)          
    gem2=pygame.Rect(3*w/6, h/10, w/30, h/30) 
    gem3=pygame.Rect(4*w/6, h/10, w/30, h/30)          
    gem4=pygame.Rect(5*w/12, 13*h/32, w/30, h/30) 
    gem5=pygame.Rect(7*w/12, 13*h/32, w/30, h/30)          
    gem6=pygame.Rect(9*w/12, 13*h/32, w/30, h/30) 
    #first gem
    if (map&0b100000 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11111
        gems+=1
        gemmap[6]=map
    #second gem ...
    if (map&0b10000 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b101111
        gems+=1
        gemmap[6]=map
    if (map&0b1000 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b110111
        gems+=1
        gemmap[6]=map
    if (map&0b100 and gem4.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b111011
        gems+=1
        gemmap[6]=map
    if (map&0b10 and gem5.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b111101
        gems+=1
        gemmap[6]=map
    if (map&0b1 and gem6.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b111110
        gems+=1
        gemmap[6]=map
        
    return gemmap, gems   

def stage13Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[7]
    gem1=pygame.Rect(w/90, 3*h/12-h/20, w/30, h/30)          
    gem2=pygame.Rect(w/90+w/20, 3*h/12-h/20, w/30, h/30) 
    gem3=pygame.Rect(w/90+2*w/20, 3*h/12-h/20, w/30, h/30)           
    if (map&0b100 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11
        gems+=1
        gemmap[7]=map
    if (map&0b10 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b101
        gems+=1
        gemmap[7]=map
    if (map&0b1 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b110
        gems+=1
        gemmap[7]=map
        
    return gemmap, gems     

def stage14Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[8]
    gem1=pygame.Rect(w/4, h/2-h/20, w/30, h/30)          
    gem2=pygame.Rect(w/4+3*w/20, 6*h/10, w/30, h/30) 
    gem3=pygame.Rect(w/4+3*w/10, h/2-h/20, w/30, h/30)   
    gem4=pygame.Rect(w/4+9*w/20, 6*h/10, w/30, h/30) 
    gem5=pygame.Rect(w/4+6*w/10, h/2-h/20, w/30, h/30) 
    if (map&0b10000 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111
        gems+=1
        gemmap[8]=map
    if (map&0b1000 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b10111
        gems+=1
        gemmap[8]=map
    if (map&0b100 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11011
        gems+=1
        gemmap[8]=map
    if (map&0b10 and gem4.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11101
        gems+=1
        gemmap[8]=map
    if (map&0b1 and gem5.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11110
        gems+=1
        gemmap[8]=map

    return gemmap, gems  
    
def stage15Gems(SirBall, gemmap, gems):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    map=gemmap[9]
    gem1=pygame.Rect(9*w/12, 5*h/8, w/30, h/30)          
    gem2=pygame.Rect(10*w/12, 4*h/8, w/30, h/30) 
    gem3=pygame.Rect(9*w/12, 3*h/8, w/30, h/30)   
    gem4=pygame.Rect(9*w/12, 2*h/8, w/30, h/30) 
    gem5=pygame.Rect(3*w/5, h/6, w/30, h/30) 
    if (map&0b10000 and gem1.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b1111
        gems+=1
        gemmap[9]=map
    if (map&0b1000 and gem2.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b10111
        gems+=1
        gemmap[9]=map
    if (map&0b100 and gem3.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11011
        gems+=1
        gemmap[9]=map
    if (map&0b10 and gem4.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11101
        gems+=1
        gemmap[9]=map
    if (map&0b1 and gem5.collidepoint(xDot+w/40,yDot+w/40)):
        map=map&0b11110
        gems+=1
        gemmap[9]=map

    return gemmap, gems 










