#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.27

#Update: Add more levels

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, sys, model, display, control, SirBallHimself

#pygame initialization
pygame.init()
clock = pygame.time.Clock()

w=model.w
h=model.h     


def main():
    #if currently interacting with a character and number message you're on
    interact=False
    numMess=0
    #ensures only one press
    prevKey=None
    #keeps track of frame number
    frame=0
    
    #which track is playing
    music=0
    
    #gems bitmap
    gemmap=[0b11, 0b111, 0b11111, 0b1111111111111, 0b11, 0b111111, 0b111111, 0b111, 0b11111, 0b11111]
    gems=0
    
    #lvl 1 wall
    wall_mad=False
    wall_defeated=False
    xWall=w
    wStage=5

    ###DOT VARIABLES
    #dot starting position
    xDot=w/20
    yDot=-h
    
    #Jump variables
    jump=0
    fall=0
    in_jump=False
    in_fall=False
    
    #number of deaths
    deaths=0

    #stage dot is on
    stage=16
                                  #xpos, ypos, controls jump and fall ani, numdeath, stagenum, ifHasSword
    SirBall=SirBallHimself.sirBall(xDot, yDot, jump, in_jump, fall, in_fall, deaths, stage,    False)

        
    while(True):
        keys=pygame.key.get_pressed()            
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                        
        #The Control. Does all moving parts
        interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, gems, frame = control.controller(SirBall,keys,  interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, gems, frame)
        
        #The View. Blits everything to the screen
        display.view(SirBall, interact, numMess, keys, prevKey, wall_mad, wall_defeated, xWall, wStage, music, gemmap, gems)
        
        #standard display output
        pygame.display.update()
        clock.tick(25) 

main()    

it= input("")
 
        
        
        
        
        
        
        
        
        
        
