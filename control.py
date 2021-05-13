#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.2

#moves stuff around

import pygame, display, model, sys, Luis, Marvin

#pygame initialization
pygame.init()

w=model.w
h=model.h

#all moving parts
def controller(interact, xDot, yDot, xWall, wStage, wall_mad, wall_defeated, stage, keys, jump, in_jump, in_fall, fall, deaths, numMess, prevKey, music, gemmap, gems):
    music=0
    #if not currently interacting with a character, continue on
    if (not interact):
        #wall mechanics
        wall_mad,wall_defeated,xWall,wStage, music=wallMechanics(xDot,yDot,xWall,wStage,wall_mad, wall_defeated, stage, music)
        
        #moving the dot
        xDot,stage=moveDot(keys,xDot,yDot,stage)  
                
        #does a cute little jump action
        yDot,jump,in_jump=jumpDot(keys,xDot,yDot,jump,stage,in_jump,in_fall)
        yDot,fall,in_jump,in_fall=fallingDot(xDot,yDot,fall,stage,in_jump,in_fall)
        
        #keeps dot on the line
        yDot=stayOnLine(xDot,yDot,stage,in_jump,in_fall)
        
        #respawn
        xWall,wStage,xDot,yDot,stage,deaths, wall_defeated=respawn(xWall,wStage,xDot,yDot,stage,deaths,wall_mad, wall_defeated)   
        
        gemmap, gems= collectGem(xDot, yDot, stage, gemmap, gems)
        
    #does interaction
    numMess, interact = characterInteractions(xDot, yDot, numMess, interact, keys, prevKey, stage)
            
    #soon, add more leves
    stage, xDot, yDot, numMess, wall_mad, music= nextLevel(stage, wall_defeated, xDot, yDot, numMess, wall_mad, music)            
    #allows for test KEYUP
    prevKey=keys
    
    return interact, xDot, yDot, xWall, wStage, wall_mad, wall_defeated, stage, jump, in_jump, in_fall, fall, deaths, numMess, prevKey, music, gemmap, gems


#checks if Sir Ball went through a door
def nextLevel(stage, wall_defeated, xDot, yDot, numMess, wall_mad, music):
    if(stage==1 and wall_defeated and (xDot)>=49*w/100 and (xDot<=49*w/100+w/20) and (yDot<=2*h/5)):
        stage=6
        xDot=w/100
        yDot=0
        numMess=0
        wall_mad=False
        music=1
    door9=pygame.Rect(9*w/10, h/2-h/3, w/10, h/3)
    if(stage==9 and door9.collidepoint(xDot+w/40,yDot+w/40)):
        stage=10
        xDot=w/100
        yDot=14*h/30-h/20
        numMess=0
        #find more music    ######################################
    
    return stage, xDot, yDot, numMess, wall_mad, music

#starts, moves, and stops wall
def wallMechanics (xDot, yDot,xWall,wStage,wall_mad, wall_defeated, stage, music):
    #where the stage 1 button is
    block=pygame.Rect(89*w/200,22*h/25-h/50,2*w/15-w/25,h/50+1)    
    
    if(stage==1 and wall_mad and not wall_defeated and block.collidepoint(xDot+w/40,yDot+w/20)):
        wall_defeated=True
    if(not wall_defeated and not wall_mad and stage==5 and xDot>=12*w/20):
        wall_mad=True
        music=2
    if(wall_mad):
        xWall-=w/220
        if(xWall<=0):
            xWall=w
            wStage=wStage-1 

    return wall_mad,wall_defeated,xWall,wStage, music
    

    
#perform cute jump animation, only for upward motion
def jumpDot(keys,xDot,yDot,jump,stage,in_jump,in_fall):
    #where is the roof?
    ceiling=YCeiling(xDot, yDot, stage)
    
    #if not currently jumping and you push space
    if (keys[pygame.K_SPACE] and not in_jump and not in_fall):
        in_jump=True
        jump=1000
        
    #if not jumping, do nothing
    if (in_jump is False):
        return yDot,jump,in_jump
    
    #if going up, don't hit ceiling
    if (jump<=1000 and jump>500):
        yDot-=((h/65000)*(jump-500))**2
        if (yDot<ceiling):
            yDot=ceiling
            in_jump=False
    else:
        in_jump=False
        
    if(in_jump):
        jump-=25
    return yDot,jump,in_jump
    
#if the dot isn't on the groun, it falls to the ground
def fallingDot(x,y,fall,stage,in_jump,in_fall):
    
    yMaxi=YFloor(x,y,stage)
    
    if (not in_jump and y<yMaxi and not in_fall):
        fall=500
        in_fall=True
    elif(not in_fall):
        return y,0,in_jump,in_fall
    
    y+=((h/69000)*(fall-500))**2
    if (y>=yMaxi):
        y=yMaxi
        in_fall=False
       
    fall-=25

    return y,fall,in_jump,in_fall        
    
    
    
#stay on lines methods here
def stayOnLine(xDot,yDot,stage,in_jump, in_fall):
    if (in_jump or in_fall):
        return yDot
    return YFloor(xDot,yDot,stage) 
    
#returns the y value of the first floor below the ball
def YFloor(xDot,yDot,stage):
    #center of the Dot
    xDot+=w/40   
    yDot+=w/40
    maxi=2*h
    blocks=display.drawStage(stage)
    for x in blocks:
        if(x.left<=xDot and x.right>=xDot):
            if(x.top<maxi and x.top>=yDot):
                maxi=x.top
    return maxi-w/20

#returns the lowest platform above ball    
def YCeiling (xDot, yDot, stage):
    #center of Dot  
    xDot+=w/40
    yDot+=w/40
    ceiling=0
    blocks=display.drawStage(stage)
    for x in blocks:
        if(x.left<=xDot and x.right>=xDot):
            if(x.bottom>ceiling and x.bottom<=yDot):
                ceiling=x.bottom
    return ceiling

    
#moves dot left or right
def moveDot(keys,xDot,yDot,stage):
    if keys[pygame.K_RIGHT]:
        if (not moveRight(xDot,yDot,stage)):
            return xDot,stage
        if (xDot+w/20)<w:
            xDot+=w/200
        else:
            xDot=0
            stage+=1
    if keys[pygame.K_LEFT]:
        if (not moveLeft(xDot,yDot,stage)):
            return xDot,stage
        if (xDot)>0:
            xDot-=w/200
        else:
            if (stage!=1):
                xDot=w-w/20
                stage-=1
                
    return xDot,stage
        


#These check if there is an object blocking them from moving in a direction
def moveLeft(xDot,yDot,stage):    
    #if by next move it would touch the wall, return False
    blocks=display.drawStage(stage)
    player= pygame.Rect(xDot,yDot+w/100,w/20-w/40,w/20-w/50)
    for x in blocks:
        if (x.colliderect(player)):
            return False
    return True  
    
def moveRight(xDot,yDot,stage):
    #if by next move it would touch the wall, return False
    blocks=display.drawStage(stage)
    player= pygame.Rect(xDot+w/40,yDot+w/100,w/20-w/40,w/20-w/50)
    for x in blocks:
        if (x.colliderect(player)):
            return False
    return True
       
#checks if hit bottom, ran into wall, or hit spikes
def respawn(xWall,wStage,xDot,yDot,stage,deaths,wall_mad, wall_defeated):
    #hits floor
    if (yDot+w/20>=h):
        if(wall_mad):
            xDot=7*w/8
            yDot=YFloor(xDot,0,stage)
            deaths+=1
        else:   
            xDot=w/8
            yDot=YFloor(xDot,h/3,stage)
            deaths+=1
    #hits wall
    if(wall_mad and wStage==stage and xWall<=xDot+w/20):
        stage=5
        xDot=w/8
        yDot=YFloor(xDot,h/2,stage)
        deaths+=1
        xWall=w
        wStage=5
        wall_defeated=False
    #hits spikes
    spikes=display.drawSpikes(stage)
    player= pygame.Rect(xDot,yDot+w/100,w/20,3*w/100)
    for x in spikes:
        if (x.colliderect(player)):
            xDot=w/8
            yDot=YFloor(xDot,h/3,stage)
            deaths+=1
    
    return xWall,wStage,xDot,yDot,stage,deaths, wall_defeated
    
    

def characterInteractions (xDot, yDot, numMess, interact, keys, prevKey, stage):
    numMessPrev=numMess
    if((stage==10 and xDot>=4*w/15 and xDot<8*w/15 and yDot>=9*h/10-w/20 and numMess<=19) or 
    (xDot>=3*w/5 and xDot<9*w/10  and yDot>=4*h/5-w/20 and numMess<=15 and stage==1) or 
    (xDot>=2*w/5 and xDot<2*w/5+w/10 and yDot>=9*h/10-w/20 and numMess<=19 and stage==6)):
        interact=True
    if(stage==1 and numMess>15 or stage==6 and numMess>19 or stage==10 and numMess>19):
        interact=False
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
    if (stage==10 and numMess>11 and Ly<75*h/100):
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
    
    return numMess, interact
    
#collects gems for Sir Ball
def collectGem(xDot, yDot, stage, gemmap, gems):  
    #stage 6 gems
    if (stage==6):
        gemmap, gems=stage6Gems(xDot,yDot, gemmap, gems)
    #stage 7 gems
    if (stage==7):
        gemmap, gems=stage7Gems(xDot,yDot, gemmap, gems)    
    if (stage==8):
        gemmap, gems=stage8Gems(xDot, yDot, gemmap, gems)
    if (stage==9):
        gemmap, gems=stage9Gems(xDot, yDot, gemmap, gems)

    return gemmap, gems    
    
def stage6Gems(xDot, yDot, gemmap, gems):
    map=gemmap[0]
    gem1=pygame.Rect(3*w/5,h/5,w/20,h/20)
    gem2=pygame.Rect(9.5*w/10,h/5,w/20,h/20)
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

def stage7Gems(xDot,yDot, gemmap, gems):
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

def stage8Gems(xDot,yDot, gemmap, gems):
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

def stage9Gems(xDot,yDot, gemmap, gems):
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

