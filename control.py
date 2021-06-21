#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.30

#moves stuff around

import pygame, math, display, model, sys, Luis, Marvin

#pygame initialization
pygame.init()

w=model.w
h=model.h

#all moving parts
def controller(SirBall, keys, interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, frame):
    #master control
    #if (keys[pygame.K_a] and not keys==prevKey):
    #    SirBall.setstage(SirBall.stage+1)  
    #    model.resetMovingObjects()
    #if (keys[pygame.K_b] and not keys==prevKey):
    #    SirBall.setstage(SirBall.stage-1)
    #    model.resetMovingObjects()

    
    music=0
    moveBlocks()
    #if not currently interacting with a character, continue on
    if (not interact):
        #wall mechanics
        wall_mad,wall_defeated,xWall,wStage, music=wallMechanics(SirBall,xWall,wStage,wall_mad, wall_defeated, music)
        
        #moving the dot
        gemmap=moveDot(keys,SirBall, gemmap)  
                
        #does a cute little jump action
        jumpDot(keys,SirBall)
        fallingDot(SirBall)
        
        #keeps dot on the line
        stayOnLine(SirBall)
        
        #respawn
        xWall,wStage,wall_defeated=respawn(xWall,wStage,wall_mad, wall_defeated, SirBall)   
        
        gemmap= collectGem(SirBall, gemmap)
        
        music=rightToBearArms(SirBall, music)
        
        killEnemy(SirBall)
        
        #for final battle
        hitLuis(SirBall, frame)
        
        shootLazers(SirBall, frame)
        
        getRidOfDeadLasers()
        
    #does interaction
    numMess, interact, music = characterInteractions(SirBall, numMess, interact, keys, prevKey, music, frame)
            
    #checks if goes through a door
    numMess, wall_mad, music= nextLevel(SirBall, wall_defeated, numMess, wall_mad, music)   
        
    #allows for test KEYUP
    prevKey=keys
    
    frame+=1
    
    return interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, frame


#shoots lazers at SirBall from bananas      x, y, xDot, yDot
def shootLazers(SirBall, frame):
    xDot=SirBall.xDot+w/40
    yDot=SirBall.yDot+w/40
    for q in model.movingObjects:
        if (isinstance(q, display.stages.Banana)):
            if (q.alive and q.lastShot+q.frequency<frame):
                laser=display.stages.Lazer(q.x, q.y, xDot, yDot)
                model.addMovingObject(laser)
                q.setLastShot(frame)
                
def getRidOfDeadLasers():
    for q in model.movingObjects:
        if (isinstance(q, display.stages.Lazer)):
            if(q.x<-w/2 or q.x>2*w or q.y<-h/2 or q.y>2*h):
                q=None



#tests if SirBall killed an enemy 
def killEnemy(SirBall):
    ballRect=pygame.Rect(SirBall.xDot,SirBall.yDot,w/20,h/11)
    for x in model.movingObjects:
        if (isinstance(x, display.stages.Banana)):
            if(x.getBox().colliderect(ballRect) and x.alive):
                if(SirBall.armed):
                    x.setAlive(False)
                    SirBall.gems+=1
                
                
#moves all the movable blocks
def moveBlocks():
    for x in model.movingObjects:
        x.moveSelf()
        
def rightToBearArms(SirBall, music):
    if(SirBall.stage==16 and SirBall.xDot+w/40>w//10 and SirBall.xDot-w/30<w//10 and SirBall.yDot<4*h/10 and SirBall.yDot>4*h/10-h/10 and not SirBall.armed):
        SirBall.setarmed(True)
        music=4
        
    return music

    
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
    #goes through doors on stage 18
    door18=pygame.Rect(69*w/80, h//13,w/10, h/3)
    door182=pygame.Rect(69*w/80, 23*h//40, w/10, h/3)
    ballRect=pygame.Rect(SirBall.xDot,SirBall.yDot,w/20,h/11)
    if(SirBall.stage==18 and door18.colliderect(ballRect) and SirBall.gems>=50):
        SirBall.setstage(100)
        SirBall.setxDot(w/100)
        SirBall.setyDot(2*h/3-w/20)
        numMess=0
        model.resetMovingObjects()
        SirBall.armed=True
    if(SirBall.stage==18 and door182.colliderect(ballRect) and SirBall.gems<50):
        SirBall.setstage(19)
        SirBall.setxDot(w/5)
        SirBall.setyDot(4*h/5-w/20)
        numMess=0
        model.resetMovingObjects()
    #door on stage 19+
    door19=pygame.Rect(w/40,h/13, w/8, h/3)
    if(SirBall.stage>=19 and SirBall.stage<100 and door19.colliderect(ballRect) and SirBall.gems>=50):
        SirBall.setstage(100)
        SirBall.setxDot(w/100)
        SirBall.setyDot(2*h/3-w/20)
        numMess=0
        model.resetMovingObjects()  
        SirBall.armed=True

    
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
        SirBall.setLastHit(0)

        
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
def moveDot(keys,SirBall, gemmap):
    #checks to see if Sir Ball is on a moving platform
    for q in model.movingObjects:
        if (isinstance(q, display.stages.movingObject)):
            #if Sir Ball is on a moving platform
            if(SirBall.xDot+w/40>q.x*w/q.rate and SirBall.xDot+w/40<q.x*w/q.rate+q.width  and (SirBall.yDot+w/20)//1==q.y*h//q.rate):
                if(q.direction==1 and moveRight(SirBall)):
                    SirBall.setxDot(SirBall.xDot+4*w/q.rate)
                    if(SirBall.xDot+w/20>w):
                        SirBall.setxDot(0)
                        SirBall.setstage(SirBall.stage+1)
                        model.resetMovingObjects()
                        SirBall.prevX=-1
                        #if past stage 19, reset gemmap
                        if(SirBall.stage>19):
                            gemmap[13]=0b1111111111
                elif(q.direction==3 and moveLeft(SirBall)):
                    SirBall.setxDot(SirBall.xDot-4*w/q.rate)
                    if(SirBall.xDot<0):
                        SirBall.setxDot(w-w/20)
                        SirBall.setstage(SirBall.stage-1)
                        model.resetMovingObjects()
                        SirBall.prevX=w
    
    if (keys[pygame.K_RIGHT] and moveRight(SirBall)):
        if (SirBall.xDot+w/20)<w:
            SirBall.setxDot(SirBall.xDot+w/200)
        else:
            SirBall.setxDot(0)
            SirBall.setstage(SirBall.stage+1)
            model.resetMovingObjects()
            SirBall.prevX=-1
            #if past stage 19, reset gemmap
            if(SirBall.stage>19):
                gemmap[13]=0b1111111111
    if (keys[pygame.K_LEFT] and moveLeft(SirBall)):
        if (SirBall.xDot)>0:
            SirBall.setxDot(SirBall.xDot-w/200)
        else:
            if (SirBall.stage!=1):
                SirBall.setxDot(w-w/20)
                SirBall.setstage(SirBall.stage-1)
                model.resetMovingObjects()
                SirBall.prevX=w

    return gemmap


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
    #ensures death counter only inc once
    prevDeaths=SirBall.deaths
    
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
                
    if(SirBall.deaths>prevDeaths):
        SirBall.setdeaths(prevDeaths+1)
                                        
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
        SirBall.setxDot(w/40)
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
            
    SirBall.prevX=-1
    
    if(SirBall.gems>0 and not SirBall.stage==100):
        SirBall.gems=SirBall.gems-1
        
    return xWall, wStage, wall_defeated

    
    

def characterInteractions (SirBall, numMess, interact, keys, prevKey, music, frame):
    xDot=SirBall.xDot
    yDot=SirBall.yDot
    stage=SirBall.stage
    numMessPrev=numMess
    #if gets close to a character, begin interaction
    if((stage==10 and xDot>=4*w/15 and xDot<8*w/15 and yDot>=9*h/10-w/20 and numMess<=19) or 
    (xDot>=3*w/5 and xDot<9*w/10  and yDot>=4*h/5-w/20 and numMess<=15 and stage==1) or 
    (xDot>=2*w/5 and xDot<2*w/5+w/10 and yDot>=9*h/10-w/20 and numMess<=19 and stage==6) or
    (SirBall.stage==100 and xDot>=w/2-w/7 and xDot<w/2-w/15 and yDot>3*h/4 and not SirBall.in_jump and not SirBall.in_fall)):
        interact=True
    #ends interaction after all messages shown
    if(stage==1 and numMess>15 or stage==6 and numMess>19 or stage==10 and numMess>19 or stage==100 and numMess>5):
        interact=False
    if(stage==10 and (numMess==20 or numMess==100000)):
        music=3
        numMess+=1
    if(interact):
        #check if want to skip talk or go to next page
        if keys[pygame.K_s] and not stage==100:
            numMess=100000
        elif(keys[pygame.K_c] and not keys==prevKey):
            numMess+=1  
            if(stage==100 and numMess==3):
                music=5
            
    #Luis Marvin pushing stage 10
    numMess= interactionPushing10(SirBall, numMess, numMessPrev)
    
    if(stage==100):
        if(not Luis.LuisDefeated):
            numMess, music=LuisBattleInteraction(SirBall, numMess, numMessPrev, frame, music)
    
    return numMess, interact, music
    
def LuisBattleInteraction(SirBall, numMess, numMessPrev, frame, music):
    #talking to Luis and taking his fish
    if(numMess==4 and SirBall.xDot<w/2+w/8):   #don't move on until Sir Ball finished moving
        numMess=3
    if(numMess==5 and SirBall.xDot<w/2+w/8):   #don't move on until Sir Ball finished moving
        numMess=4
    if((numMess==3 or numMess==4) and SirBall.xDot<w/2+w/8):   #keep moving Sir Ball
        SirBall.setxDot(SirBall.xDot+w/200)
    if(numMess==3 and SirBall.xDot+w/40>w/2):   #once half way, change to mad Luis
        numMess+=1  
    #fish falling!
    if(numMess>=4 and not Luis.isMad and Luis.LuisObject<2*h):
        Luis.setLuisObject(Luis.LuisObject+h/200)

    #Luis Rising to battle
    if(numMess==6 and Luis.y>h/3):
        Luis.setY(Luis.y-h/200)
    elif(numMess==6 and Luis.y<h/3):
        numMess=7
        Luis.setIsMad(True)

    #Luis moving side to side
    if(Luis.isMad and Luis.health>=1800):
        numMess=Luis.SideToSideMid(numMess)  
        Luis.QuadLaser(frame, 50)
        
    #Luis moving in a squre
    if(Luis.isMad and Luis.health>=1600 and Luis.health<1800):
        Luis.Square()
        Luis.TargetLaser(SirBall, frame, 30)

            
    #Luis moving up and down and back and forth
    if(Luis.isMad and Luis.health>=1200 and Luis.health<1600):
        Luis.ZigZag()
        Luis.StarLaser(frame, 80)

    #Luis back and forth up high
    if(Luis.isMad and Luis.health>=800 and Luis.health<1200):
        Luis.SideToSideHigh()
        Luis.RotatingShot(frame, 20)
        
    if(Luis.isMad and Luis.health>=400 and Luis.health<800):
        Luis.ZigZag()
        Luis.StarLaser(frame, 50)
        
    if(Luis.isMad and Luis.health>0 and Luis.health<400):
        Luis.Square()
        Luis.RotatingLaserStar(SirBall, frame, 80)
        
    if(Luis.isMad and Luis.health<=0):
        if(Luis.y<h+h/20):
            Luis.setY(Luis.y+h/100)
        else:
            Luis.setLuisDefeated(True)
            Luis.setIsMad(False)
            music=6
    

    return numMess, music
    
def hitLuis(SirBall, frame):
    ballRect=pygame.Rect(SirBall.xDot,SirBall.yDot,w/20,h/11)
    LuisRect=pygame.Rect(Luis.x, Luis.y, w/15, h/7)
    if(ballRect.colliderect(LuisRect) and frame-50>SirBall.lastHit and Luis.isMad):
        Luis.setHealth(Luis.health-100)
        SirBall.setLastHit(frame)
        if(Luis.health==1500 or Luis.health==700):
            if(Luis.movmentDir==0):
                Luis.setMovmentDir(1)
            elif(Luis.movmentDir==2):
                Luis.setMovmentDir(3)
            elif(Luis.movmentDir==4):
                Luis.setMovmentDir(5)
            elif(Luis.movmentDir==6):
                Luis.setMovmentDir(7)
        if(Luis.health==1100):
            Luis.setMovmentDir(0)
            Luis.setLuisObject([0,0])
        if(Luis.health==300):
            Luis.setMovmentDir(4)
            Luis.setLastShot([0,0])


    
#Moving the characters on stage 10
def interactionPushing10(SirBall, numMess, numMessPrev):
    #Luis moving down stage 10
    Ly=Luis.getY()
    if (SirBall.stage==10 and numMess>=4 and Ly<75*h/100):
        Luis.setY(Ly+h/400)
    #wait for him to descend
    if (SirBall.stage==10 and numMess>11 and  numMess<900 and Ly<75*h/100):
        numMess=numMessPrev
    if (SirBall.stage==10 and numMess==11 and Ly>75*h/100):
        numMess+=1
    #Luis pushing Marvin stage 10
    if (SirBall.stage==10 and numMess>=16):
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
    return numMess
    
#collects gems for Sir Ball
def collectGem(SirBall, gemmap):  
    stage=SirBall.stage
    #stage 6 gems
    if (stage==6):
        gemmap=stage6Gems(SirBall, gemmap)
    #stage 7 gems
    if (stage==7):
        gemmap=stage7Gems(SirBall, gemmap)    
    if (stage==8):
        gemmap=stage8Gems(SirBall, gemmap)
    if (stage==9):
        gemmap=stage9Gems(SirBall, gemmap)
    if (stage==10):
        gemmap=stage10Gems(SirBall, gemmap)
    if (stage==11):
        gemmap=stage11Gems(SirBall, gemmap)
    if (stage==12):
        gemmap=stage12Gems(SirBall, gemmap)
    if (stage==13):
        gemmap=stage13Gems(SirBall, gemmap)
    if (stage==14):
        gemmap=stage14Gems(SirBall, gemmap)
    if(stage==15):
        gemmap=stage15Gems(SirBall, gemmap)
    if(stage==16):
        gemmap=stage16Gems(SirBall, gemmap)
    if(stage==17):
        gemmap=stage17Gems(SirBall, gemmap)
    if(stage==18):
        gemmap=stage18Gems(SirBall, gemmap)
    if(stage>=19 and stage<100):
        gemmap=stage19Gems(SirBall, gemmap)
        
    return gemmap    
    
def stage6Gems(SirBall, gemmap):
    map=gemmap[0]
    gem1=pygame.Rect(3*w/5,h/5,w/20,h/20)
    gem2=pygame.Rect(9.5*w/10,h/5,w/20,h/20)
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    #first gem
    if (map&10 and gem1.colliderect(ballRect)):
        map=map&1
        SirBall.gems+=1
        gemmap[0]=map
    #second gem
    if (map&1 and gem2.colliderect(ballRect)):
        map=map&10
        SirBall.gems+=1
        gemmap[0]=map
        
    return gemmap

def stage7Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[1]
    gem1=pygame.Rect(3*w/12,28*h/40,w/20,h/20)
    gem2=pygame.Rect(86*w/120,84*h/120,w/20,h/20)
    gem3=pygame.Rect(9.5*w/10,h/5,w/20,h/20)
    #first gem
    if (map&100 and gem1.colliderect(ballRect)):
        map=map&11
        SirBall.gems+=1
        gemmap[1]=map
    #second gem
    if (map&10 and gem2.colliderect(ballRect)):
        map=map&101
        SirBall.gems+=1
        gemmap[1]=map
    #third gem
    if (map&1 and gem3.colliderect(ballRect)):
        map=map&110
        SirBall.gems+=1
        gemmap[1]=map
        
    return gemmap

def stage8Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[2]
    gem1=pygame.Rect(12*w/30-w/30, 14*h/30-h/20, w/30, h/20)
    gem2=pygame.Rect(12*w/30, 14*h/30-h/20, w/30, h/20)
    gem3=pygame.Rect(12*w/30+w/30, 14*h/30-h/20, w/30, h/20)
    gem4=pygame.Rect(w/3+w/10, 99*h/100-h/20, w/30, h/20)
    gem5=pygame.Rect(2*w/3-w/10, 99*h/100-h/20, w/30, h/20)

    #first gem
    if (map&0b10000 and gem1.colliderect(ballRect)):
        map=map&0b1111
        SirBall.gems+=1
        gemmap[2]=map
    #second gem
    elif (map&0b1000 and gem2.colliderect(ballRect)):
        map=map&0b10111
        SirBall.gems+=1
        gemmap[2]=map
    #third gem
    elif (map&0b100 and gem3.colliderect(ballRect)):
        map=map&0b11011
        SirBall.gems+=1
        gemmap[2]=map
    #fourth gem
    elif (map&0b10 and gem4.colliderect(ballRect)):
        map=map&0b11101
        SirBall.gems+=1
        gemmap[2]=map
    #fifth gem
    elif (map&0b1 and gem5.colliderect(ballRect)):
        map=map&0b11110
        SirBall.gems+=1
        gemmap[2]=map
        
    return gemmap

def stage9Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
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
    if (map&0b1000000000000 and gem1.colliderect(ballRect)):
        map=map&0b111111111111
        SirBall.gems+=1
        gemmap[3]=map
    #second gem
    if (map&0b100000000000 and gem2.colliderect(ballRect)):
        map=map&0b1011111111111
        SirBall.gems+=1
        gemmap[3]=map
    #third gem
    if (map&0b10000000000 and gem3.colliderect(ballRect)):
        map=map&0b1101111111111
        SirBall.gems+=1
        gemmap[3]=map
    #etc
    if (map&0b10000000 and gem6.colliderect(ballRect)):
        map=map&0b1111101111111
        SirBall.gems+=1
        gemmap[3]=map
    if (map&0b1000000 and gem7.colliderect(ballRect)):
        map=map&0b1111110111111
        SirBall.gems+=1
        gemmap[3]=map
    if (map&0b100000 and gem8.colliderect(ballRect)):
        map=map&0b1111111011111
        SirBall.gems+=1
        gemmap[3]=map
    if (map&0b10000 and gem9.colliderect(ballRect)):
        map=map&0b1111111101111
        SirBall.gems+=1
        gemmap[3]=map
    if (map&0b10 and gem12.colliderect(ballRect)):
        map=map&0b1111111111101
        SirBall.gems+=1
        gemmap[3]=map
    if (map&0b1 and gem13.colliderect(ballRect)):
        map=map&0b1111111111110
        SirBall.gems+=1
        gemmap[3]=map

        
    return gemmap
    
def stage10Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[4]
    gem1=pygame.Rect(w/50, 9*h/10-h/20, w/30, h/20)          
    gem2=pygame.Rect(19*w/20, 9*h/10-h/20, w/30, h/20) 
    #first gem
    if (map&10 and gem1.colliderect(ballRect)):
        map=map&1
        SirBall.gems+=1
        gemmap[4]=map
    #second gem
    if (map&1 and gem2.colliderect(ballRect)):
        map=map&10
        SirBall.gems+=1
        gemmap[4]=map
        
    return gemmap
    
def stage11Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[5]
    gem1=pygame.Rect(5*w/12-4*w/15, 11*h/30-h/18, w/30, h/30) 
    gem2=pygame.Rect(5*w/12-2*w/15, 11*h/30-h/18, w/30, h/30) 
    gem3=pygame.Rect(5*w/12, 11*h/30-h/20, w/18, h/30) 
    gem4=pygame.Rect(5*w/12+2*w/15, 11*h/30-h/18, w/30, h/30) 
    gem5=pygame.Rect(5*w/12+4*w/15, 11*h/30-h/18, w/30, h/30) 
    gem6=pygame.Rect(5*w/12+6*w/15, 11*h/30-h/18, w/30, h/30) 
        
    #first gem
    if (map&0b100000 and gem1.colliderect(ballRect)):
        map=map&0b11111
        SirBall.gems+=1
        gemmap[5]=map
    #second gem...
    if (map&0b10000 and gem2.colliderect(ballRect)):
        map=map&0b101111
        SirBall.gems+=1
        gemmap[5]=map
    if (map&0b1000 and gem3.colliderect(ballRect)):
        map=map&0b110111
        SirBall.gems+=1
        gemmap[5]=map
    if (map&0b100 and gem4.colliderect(ballRect)):
        map=map&0b111011
        SirBall.gems+=1
        gemmap[5]=map
    if (map&0b10 and gem5.colliderect(ballRect)):
        map=map&0b111101
        SirBall.gems+=1
        gemmap[5]=map
    if (map&0b1 and gem6.colliderect(ballRect)):
        map=map&0b111110
        SirBall.gems+=1
        gemmap[5]=map

    return gemmap
    
    
def stage12Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[6]
    gem1=pygame.Rect(2*w/6, h/10, w/30, h/30)          
    gem2=pygame.Rect(3*w/6, h/10, w/30, h/30) 
    gem3=pygame.Rect(4*w/6, h/10, w/30, h/30)          
    gem4=pygame.Rect(5*w/12, 13*h/32, w/30, h/30) 
    gem5=pygame.Rect(7*w/12, 13*h/32, w/30, h/30)          
    gem6=pygame.Rect(9*w/12, 13*h/32, w/30, h/30) 
    #first gem
    if (map&0b100000 and gem1.colliderect(ballRect)):
        map=map&0b11111
        SirBall.gems+=1
        gemmap[6]=map
    #second gem ...
    if (map&0b10000 and gem2.colliderect(ballRect)):
        map=map&0b101111
        SirBall.gems+=1
        gemmap[6]=map
    if (map&0b1000 and gem3.colliderect(ballRect)):
        map=map&0b110111
        SirBall.gems+=1
        gemmap[6]=map
    if (map&0b100 and gem4.colliderect(ballRect)):
        map=map&0b111011
        SirBall.gems+=1
        gemmap[6]=map
    if (map&0b10 and gem5.colliderect(ballRect)):
        map=map&0b111101
        SirBall.gems+=1
        gemmap[6]=map
    if (map&0b1 and gem6.colliderect(ballRect)):
        map=map&0b111110
        SirBall.gems+=1
        gemmap[6]=map
        
    return gemmap   

def stage13Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[7]
    gem1=pygame.Rect(w/90, 3*h/12-h/20, w/30, h/30)          
    gem2=pygame.Rect(w/90+w/20, 3*h/12-h/20, w/30, h/30) 
    gem3=pygame.Rect(w/90+2*w/20, 3*h/12-h/20, w/30, h/30)           
    if (map&0b100 and gem1.colliderect(ballRect)):
        map=map&0b11
        SirBall.gems+=1
        gemmap[7]=map
    if (map&0b10 and gem2.colliderect(ballRect)):
        map=map&0b101
        SirBall.gems+=1
        gemmap[7]=map
    if (map&0b1 and gem3.colliderect(ballRect)):
        map=map&0b110
        SirBall.gems+=1
        gemmap[7]=map
        
    return gemmap     

def stage14Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[8]
    gem1=pygame.Rect(w/4, h/2-h/20, w/30, h/30)          
    gem2=pygame.Rect(w/4+3*w/20, 6*h/10, w/30, h/30) 
    gem3=pygame.Rect(w/4+3*w/10, h/2-h/20, w/30, h/30)   
    gem4=pygame.Rect(w/4+9*w/20, 6*h/10, w/30, h/30) 
    gem5=pygame.Rect(w/4+6*w/10, h/2-h/20, w/30, h/30) 
    if (map&0b10000 and gem1.colliderect(ballRect)):
        map=map&0b1111
        SirBall.gems+=1
        gemmap[8]=map
    if (map&0b1000 and gem2.colliderect(ballRect)):
        map=map&0b10111
        SirBall.gems+=1
        gemmap[8]=map
    if (map&0b100 and gem3.colliderect(ballRect)):
        map=map&0b11011
        SirBall.gems+=1
        gemmap[8]=map
    if (map&0b10 and gem4.colliderect(ballRect)):
        map=map&0b11101
        SirBall.gems+=1
        gemmap[8]=map
    if (map&0b1 and gem5.colliderect(ballRect)):
        map=map&0b11110
        SirBall.gems+=1
        gemmap[8]=map

    return gemmap  
    
def stage15Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[9]
    gem1=pygame.Rect(9*w/12, 5*h/8, w/30, h/30)          
    gem2=pygame.Rect(10*w/12, 4*h/8, w/30, h/30) 
    gem3=pygame.Rect(9*w/12, 3*h/8, w/30, h/30)   
    gem4=pygame.Rect(9*w/12, 2*h/8, w/30, h/30) 
    gem5=pygame.Rect(3*w/5, h/6, w/30, h/30) 
    if (map&0b10000 and gem1.colliderect(ballRect)):
        map=map&0b1111
        SirBall.gems+=1
        gemmap[9]=map
    if (map&0b1000 and gem2.colliderect(ballRect)):
        map=map&0b10111
        SirBall.gems+=1
        gemmap[9]=map
    if (map&0b100 and gem3.colliderect(ballRect)):
        map=map&0b11011
        SirBall.gems+=1
        gemmap[9]=map
    if (map&0b10 and gem4.colliderect(ballRect)):
        map=map&0b11101
        SirBall.gems+=1
        gemmap[9]=map
    if (map&0b1 and gem5.colliderect(ballRect)):
        map=map&0b11110
        SirBall.gems+=1
        gemmap[9]=map

    return gemmap 
    
def stage16Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[10]
    gem1=pygame.Rect(w/3+w/40, 4*h/20, w/30, h/30)          
    gem2=pygame.Rect(w/3+w/40, 12*h/20, w/30, h/30) 
    gem3=pygame.Rect(20*w/30+w/40, 7*h/20, w/30, h/30)   
    if (map&0b100 and gem1.colliderect(ballRect)):
        map=map&0b11
        SirBall.gems+=1
        gemmap[10]=map
    if (map&0b10 and gem2.colliderect(ballRect)):
        map=map&0b101
        SirBall.gems+=1
        gemmap[10]=map
    if (map&0b1 and gem3.colliderect(ballRect)):
        map=map&0b110
        SirBall.gems+=1
        gemmap[10]=map


    return gemmap 
    
def stage17Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[11]
    gem1=pygame.Rect(w/3+w/40, 44*h/200, w/30, h/30)          
    gem2=pygame.Rect(w/3+w/4, 44*h/200, w/30, h/30) 
    gem3=pygame.Rect(w/3+w/2, 44*h/200, w/30, h/30)   
    if (map&0b100 and gem1.colliderect(ballRect)):
        map=map&0b11
        SirBall.gems+=1
        gemmap[11]=map
    if (map&0b10 and gem2.colliderect(ballRect)):
        map=map&0b101
        SirBall.gems+=1
        gemmap[11]=map
    if (map&0b1 and gem3.colliderect(ballRect)):
        map=map&0b110
        SirBall.gems+=1
        gemmap[11]=map

    return gemmap 
    
def stage18Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[12]
    gem1=pygame.Rect(5*w/10, 9*h/10-h/20, w/30, h/30)          
    gem2=pygame.Rect(6*w/10, 9*h/10-h/20, w/30, h/30) 
    gem3=pygame.Rect(7*w/10, 9*h/10-h/20, w/30, h/30) 
    gem4=pygame.Rect(8*w/10, 9*h/10-h/20, w/30, h/30) 
    
    if (map&0b1000 and gem1.colliderect(ballRect)):
        map=map&0b111
        SirBall.gems+=1
        gemmap[12]=map
    if (map&0b100 and gem2.colliderect(ballRect)):
        map=map&0b1011
        SirBall.gems+=1
        gemmap[12]=map
    if (map&0b10 and gem3.colliderect(ballRect)):
        map=map&0b1101
        SirBall.gems+=1
        gemmap[12]=map
    if (map&0b1 and gem4.colliderect(ballRect)):
        map=map&0b1110
        SirBall.gems+=1
        gemmap[12]=map

    return gemmap 

def stage19Gems(SirBall, gemmap):
    ballRect=pygame.Rect(SirBall.xDot+w/200,SirBall.yDot+w/200,w/25,w/25)
    map=gemmap[13]
    gem1=pygame.Rect(13*w/20, 3*h/10, w/30, h/30)          
    gem2=pygame.Rect(13*w/20, 4*h/10, w/30, h/30) 
    gem3=pygame.Rect(13*w/20, 5*h/10, w/30, h/30) 
    gem4=pygame.Rect(13*w/20, 6*h/10, w/30, h/30) 
    gem5=pygame.Rect(8*w/20, 3*h/20, w/30, h/30)          
    gem6=pygame.Rect(9*w/20, 3*h/20, w/30, h/30) 
    gem7=pygame.Rect(10*w/20, 3*h/20, w/30, h/30) 
    gem8=pygame.Rect(11*w/20, 3*h/20, w/30, h/30) 
    gem9=pygame.Rect(6*w/15, 7*h/20, w/30, h/30)          
    gem10=pygame.Rect(8*w/15, 7*h/20, w/30, h/30) 
    
    if (map&0b1000000000 and gem1.colliderect(ballRect)):
        map=map&0b111111111
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b100000000 and gem2.colliderect(ballRect)):
        map=map&0b1011111111
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b10000000 and gem3.colliderect(ballRect)):
        map=map&0b1101111111
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b1000000 and gem4.colliderect(ballRect)):
        map=map&0b1110111111
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b100000 and gem5.colliderect(ballRect)):
        map=map&0b1111011111
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b10000 and gem6.colliderect(ballRect)):
        map=map&0b1111101111
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b1000 and gem7.colliderect(ballRect)):
        map=map&0b1111110111
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b100 and gem8.colliderect(ballRect)):
        map=map&0b1111111011
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b10 and gem9.colliderect(ballRect)):
        map=map&0b1111111101
        SirBall.gems+=1
        gemmap[13]=map
    if (map&0b1 and gem10.colliderect(ballRect)):
        map=map&0b1111111110
        SirBall.gems+=1
        gemmap[13]=map


    return gemmap 









