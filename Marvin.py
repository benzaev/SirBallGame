#Ben Solomon
#04/27/2021
#Retro platforming game with a dark plot underneath
#version 10.27

#This files is home to Marvin

import pygame, model, display

pygame.init()

w= model.w
h= model.h
surface= model.surface

Marvin=pygame.image.load("Images/Marvin.png").convert_alpha()
Marvin=pygame.transform.scale(Marvin,(w//12,w//12))

x=2*w/3-w/40
y=78*h/100

def getX():
    return x
def getY():
    return y
def setX(value):
    global x
    x=value
def setY(value):
    global y
    y=value

def interact(interact, numMess, stage):
    if (stage==10 and numMess<=19):
        MarvinTen(interact, numMess)
    
        
def MarvinTen(interact, numMess):
    #the character will disappear after talking to
    surface.blit(Marvin, (x, y))   

    if(interact and numMess<17):
        #speech bubble        
        pygame.draw.polygon(surface,model.WHITE,[(x,y),(3*w/5+3*w/30,4*h/5-w/10),(3*w/5+3*w/25,4*h/5-w/10)],3) 
        pygame.draw.ellipse(surface,model.WHITE,(3*w/5,50*h/100, w/4, h/5),3)
        pygame.draw.ellipse(surface,model.GREY,(3*w/5+1,50*h/100+1, w/4-2, h/5-2),0)
        
        if (numMess==0):
            TenBlit2("(hey sir ball)", "(over here)")
        elif(numMess==1):
            TenBlit3("we have to be", "quiet, or else luis", "might hear us")
        elif(numMess==2):
            TenBlit3("and before you", "speak, listen to me", "very carefully")
        elif(numMess==3):
            TenBlit3("i saw you talking", "to luis, and I have", "to warn you...")
        elif(numMess==4):
            TenBlit2("He isn't trying to", "help you. He is Evil!")
        elif(numMess==5):
            TenBlit3("Every time something", "new comes down here,", "he tricks them")
        elif(numMess==6):
            TenBlit3("He tells them that", "they only need 50", "crystals to escape")
        elif(numMess==7):
            TenBlit1("But really its 50,000!")
        elif(numMess==8):
            TenBlit2("And he doesn't even", "plan on escaping!!")
        elif(numMess==9):
            TenBlit3("HE PLANS ON USING", "ALL HIS CRYSTALS", "TO ENSLAVE US!!!!")
        elif(numMess==10):
            TenBlit1("YOU NEED TO DEFEAT HIM!!")
        elif(numMess==11):
            TenBlit3("HE HAS ALREADY MADE", "THE REST OF US TOO WEAK", "TO FIGHT BACK!!!")
        elif(numMess==12):
            TenBlit2("AAAAAHHHH", "Luis!!")
        elif(numMess==13):
            TenBlit1("Oh, um... nothing")
        elif(numMess==14):
            TenBlit1("Isn't that right, Sir Ball?")
        elif(numMess==15):
            TenBlit1("...")
        elif(numMess==16):
            TenBlit2("Hey stop that!", "Aaaaaahh")
        
def TenBlit1(text):
    textBounds=(2*w/3+w/15,60*h/100)
    display.messagePrint(w//50,text,textBounds,model.WHITE)
        
def TenBlit2(text1, text2):
    textBounds=(2*w/3+w/15,58*h/100)
    display.messagePrint(w//50,text1,textBounds,model.WHITE)
    textBounds=(2*w/3+w/15,63*h/100)
    display.messagePrint(w//50,text2,textBounds,model.WHITE)
        
def TenBlit3(text1, text2, text3):
    textBounds=(2*w/3+w/15,55*h/100)
    display.messagePrint(w//50,text1,textBounds,model.WHITE)
    textBounds=(2*w/3+w/15,60*h/100)
    display.messagePrint(w//50,text2,textBounds,model.WHITE)
    textBounds=(2*w/3+w/15,65*h/100)
    display.messagePrint(w//50,text3,textBounds,model.WHITE)
        
        
        
        
        
        
