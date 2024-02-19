#Ben Solomon
#04/26/2021
#Retro platforming game with a dark plot underneath
#version 10.36  

#Update: Speed up movment and speed up jump

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
    music_off = False
    handled = False
    
    #gems bitmap
    gemmap=[0b11, 0b111, 0b11111, 0b1111111111111, 0b11, 0b111111, 0b111111, 0b111, 0b11111, 0b11111, 0b111, 0b111, 0b1111, 0b1111111111]
    
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
    stage=1
                                  #xpos, ypos, controls jump and fall ani, numdeath, stagenum, ifHasSword
    SirBall = SirBallHimself.sirBall(xDot, yDot, jump, in_jump, fall, in_fall, deaths, stage, False)

        
    while(True):
        keys=pygame.key.get_pressed()            
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()

        # check if turning off/on the music
        if event.type == pygame.MOUSEBUTTONDOWN and not handled:
            x, y = event.pos
            rect = pygame.Rect(0, h - 1*w//15, 1*w//15,1*w//15)
            handled = True

            if rect.collidepoint(x, y):
                if music_off:
                    music_off = False
                else:
                    music_off = True
        elif event.type == pygame.MOUSEBUTTONUP:
            handled = False
                 
        #The Control. Does all moving parts
        interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, frame = control.controller(SirBall,keys,  interact, xWall, wStage, wall_mad, wall_defeated, numMess, prevKey, music, gemmap, frame)
        
        #SirBall.armed=True
        
        #The View. Blits everything to the screen
        display.view(SirBall, interact, numMess, keys, prevKey, wall_mad, wall_defeated, xWall, wStage, music, gemmap, music_off)
        
        #standard display output
        pygame.display.update()
        clock.tick(25) 

main()    

it= input("")
 
        
        
        
        
        
        
        
        
        
        
