#Ben Solomon
#04/27/2021
#Retro platforming game with a dark plot underneath
#version 10.36

#This files is home to Marvin

import pygame, model, display

pygame.init()

w= model.w
h= model.h
surface= model.surface

Marvin=pygame.image.load("Images/Marvin.png").convert_alpha()
Marvin=pygame.transform.scale(Marvin,(w//12,w//12))

EvilMarvin=pygame.image.load("Images/EvilMarvin.png").convert_alpha()
EvilMarvin=pygame.transform.scale(EvilMarvin,(w//12,w//12))


x=2*w/3-w/40
y=78*h/100

#for battle sequence
#if fighting
mad=False
#if defeated
defeated=False
#decreases 100 each hit 3000
health=3000
#frame when last laser was shot
lastShot=0
#7 point diagonal direction system      7
direction=7
#for rotating laser fire
LuisObject=[0,0]

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
def setMad(value): 
    global mad
    mad=value
def setLuisObject(value):
    global LuisObject
    LuisObject=value
def setHealth(value):
    global health
    health=value
def setLastShot(value):
    global lastShot
    lastShot=value
def setDirection(value):
    global direction
    direction=value
def setDefeated(value):
    global defeated
    defeated=value

    


def interact(interact, numMess, SirBall):
    stage=SirBall.stage
    if (stage==10 and numMess<=19):
        MarvinTen(interact, numMess)
    if (stage==100 and numMess>999):
        Marvin100(interact, numMess, SirBall)
        
def Marvin100(interact, numMess, SirBall):
    if(numMess<=1007):
        surface.blit(Marvin, (x, y)) 
    else:
        surface.blit(EvilMarvin, (x,y))
        
    if(health<=0 and y<h+h/20):
        #speech bubble        
        pygame.draw.polygon(surface,model.WHITE,[(x,y),(x-w/100-w/40, y-h/10),(x+w/100-w/40,y-h/10)],3) 
        pygame.draw.ellipse(surface,model.WHITE,(x-w/8,y-h/4, w/4, h/5),3)
        pygame.draw.ellipse(surface,model.GREY,(x-w/8+1,y-h/4+1, w/4-2, h/5-1),0)
        #shouting noooooo
        text="NOOOOOOOOO"
        textBounds=(x, y-h/4+h/9)
        display.messagePrint(w//40,text,textBounds,model.WHITE)
        
        
    
    if(interact):
        #speech bubble        
        pygame.draw.polygon(surface,model.WHITE,[(x,y),(x-w/100-w/20, y-h/10),(x+w/100-w/20,y-h/10)],3) 
        pygame.draw.ellipse(surface,model.WHITE,(x-w/5,y-h/4, w/4, h/5),3)
        pygame.draw.ellipse(surface,model.GREY,(x-w/5+1,y-h/4+1, w/4-2, h/5-1),0)

        if(numMess==1002): 
            HundredBlit1("Well Well Well")
        elif(numMess==1003):
            HundredBlit2("Thanks for getting rid", "of Luis for me")
        elif(numMess==1004):
            HundredBlit2("He was becomming", "rather annoying")
        elif(numMess==1005):
            HundredBlit3("What?", "You still don't understand", "what's happening?")
        elif(numMess==1006):
            HundredBlit2("Allow me to change", "into something more")
        elif(numMess==1007):
            HundredBlit1("comfortable before explaining")
        elif(numMess==1008):
            HundredBlit1("Much better")
        elif(numMess==1009):
            HundredBlit1("You see...")
        elif(numMess==1010):
            HundredBlit2("Luis was only", "trying to help you")
        elif(numMess==1011):
            HundredBlit3("But you were", "foolish and did not", "heed his warnings")
        elif(numMess==1012):
            HundredBlit3("He wasn't the one", "planning on enslaving", "the Shadow Realm")
        elif(numMess==1013):
            HundredBlit1("I am!!!")
        elif(numMess==1014):
            HundredBlit3("HAHAHAHAHAHAHA", "HAHAHAHAHAHAHAHAHA", "HAHAHAHAHAHAHAHAH")
        elif(numMess==1015):
            HundredBlit2("But you messed with", "the one thing he loved")
        elif(numMess==1016):
            HundredBlit1("His precious fish")
        elif(numMess==1017):
            HundredBlit3("HAHAHAHAHAHAHA", "HAHAHAHAHAHAHAHAHA", "HAHAHAHAHAHAHAHAH")
        elif(numMess==1018):
            HundredBlit1("As you can see,")
        elif(numMess==1019):
            HundredBlit3("I've already enslaved", "a legion of bananas","to do my bidding")
        elif(numMess==1020):
            HundredBlit3("All I need are", str(SirBall.gems),"more gems")
        elif(numMess==1021):
            HundredBlit3("Before the entire", "Shadow Realm", "bends to my every whim!")
        elif(numMess==1022):
            HundredBlit1("In other words...")
        elif(numMess==1023):
            HundredBlit3("All I have to do", "is kill you, and", "take your crystals!!")
        elif(numMess==1024):
            HundredBlit3("HAHAHAHAHAHAHA", "HAHAHAHAHAHAHAHAHA", "HAHAHAHAHAHAHAHAH")
        elif(numMess==1025):
            HundredBlit2("Good luck", "Sir Ball")
        
        
def HundredBlit1(text):
    textBounds=(x-w/13, y-h/4+h/9)
    display.messagePrint(w//50,text,textBounds,model.WHITE)
        
def HundredBlit2(text1, text2):
    textBounds=(x-w/13,y-h/4+h/9-4*h/100)
    display.messagePrint(w//50,text1,textBounds,model.WHITE)
    textBounds=(x-w/13,y-h/4+h/9+2*h/100)
    display.messagePrint(w//50,text2,textBounds,model.WHITE)
        
def HundredBlit3(text1, text2, text3):
    textBounds=(x-w/13,y-h/4+h/9-6*h/100)
    display.messagePrint(w//50,text1,textBounds,model.WHITE)
    textBounds=(x-w/13,y-h/4+h/9-h/100)
    display.messagePrint(w//50,text2,textBounds,model.WHITE)
    textBounds=(x-w/13,y-h/4+h/9+4*h/100)
    display.messagePrint(w//50,text3,textBounds,model.WHITE)
        
        

    
        
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
        
        
        
        
        
        
