#Ben Solomon
#06/3/2021
#Retro platforming game with a dark plot underneath
#version 10.28

#holds Sir ball, all of its attributes, and blits him to the screen

import pygame, model

#pygame initialization
pygame.init()

w=model.w
h=model.h
surface=model.surface

class sirBall:
    def __init__(self, xDot, yDot, jump, in_jump, fall, in_fall, deaths,stage, armed):
        self.xDot = xDot
        self.yDot = yDot
        self.jump=jump
        self.in_jump=in_jump
        self.fall=fall
        self.in_fall=in_fall
        self.deaths=deaths
        self.stage=stage
        self.armed=armed
        self.prevX=0
        self.swordDir=1
        self.gems=0
        
    def setxDot(self, value):
        self.xDot=value
    def setyDot(self, value):
        self.yDot=value
    def setjump(self, value):
        self.jump=value
    def setin_jump(self, value):
        self.in_jump=value
    def setfall(self, value):
        self.fall=value
    def setin_fall(self, value):
        self.in_fall=value
    def setdeaths(self, value):
        self.deaths=value
    def setstage(self, value):
        self.stage=value
    def setarmed(self, value):
        self.armed=value

        
        
    def paintMeLikeAFrenchGirl(self):
        pygame.draw.ellipse(surface,model.WHITE,(self.xDot,self.yDot,w/20,w/20),0) 
        self.drawSword()
        
    def drawSword(self):
        if(self.armed):
            #pointing the sword in the direction of movement
            if(self.prevX<self.xDot):
                sword=model.Rsword
                surface.blit(sword, (self.xDot, self.yDot))
                self.swordDir=0
            elif(self.prevX>self.xDot):
                sword=model.Lsword
                surface.blit(sword, (self.xDot-w/50, self.yDot))
                self.swordDir=1
            elif(self.swordDir==0):
                sword=model.Rsword
                surface.blit(sword, (self.xDot, self.yDot))
            else:
                sword=model.Lsword
                surface.blit(sword, (self.xDot-w/50, self.yDot))

            self.prevX=self.xDot

        
        
        
        
        
        