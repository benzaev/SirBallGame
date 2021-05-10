#Ben Solomon
#04/27/2021
#Retro platforming game with a dark plot underneath
#version 10.19

#This files is home to Luis

import pygame, model, display

pygame.init()

w= model.w
h= model.h
surface= model.surface

Luis=pygame.image.load("Images/Luis.png").convert_alpha()
Luis=pygame.transform.scale(Luis,(w//12,w//12))

def interact(interact, numMess, stage):
    if (stage==1 and numMess<=15):
        LuisOne(interact, numMess)
    if (stage==6 and numMess<=19):
        LuisSix(interact, numMess)
    
        
def LuisOne(interact, numMess):
    #the character will disappear after talking to
    surface.blit(Luis, (3*w/5+4*w/25, 4*h/5-w/12))   

    if(interact):
        #speech bubble        
        pygame.draw.polygon(surface,model.WHITE,[(3*w/5+4*w/23,4*h/5-h/20),(3*w/5+3*w/30,4*h/5-w/10),(3*w/5+3*w/25,4*h/5-w/10)],3) 
        pygame.draw.ellipse(surface,model.WHITE,(3*w/5,44*h/100, w/4, h/5),3)
        pygame.draw.ellipse(surface,model.GREY,(3*w/5+1,44*h/100+1, w/4-2, h/5-2),0)
        #instructions
        text="Press C to continue"
        textBounds=(29*w/40,5*h/6)
        display.messagePrint(w//40,text,textBounds,model.LGREY)
        text="Press S to skip"
        textBounds=(29*w/40,11*h/12)
        display.messagePrint(w//40,text,textBounds,model.LGREY)

        if(numMess==0):      
            OneBlit3("Om nom", "nom nom", "MEOW???")
        elif(numMess==1):
            OneBlit2("Who goes there??", "State your purpose!!!")
        elif(numMess==2):
            OneBlit1("...")
        elif(numMess==3):   
            OneBlit3("And if you", "want my yummy fish,", "go away!")
        elif(numMess==4):
            OneBlit1("...")
        elif(numMess==5):
            OneBlit2("Well,", "who are you?!")
        elif(numMess==6):
            OneBlit3("Huh??", "You don't remember", "your own name??")   
        elif(numMess==7):
            OneBlit3("Hmmmm,", "I'll can you...", "Sir Ball!!!")                 
        elif(numMess==8):
            OneBlit3("Now that we", "are friends, you", "can have a bit")
        elif(numMess==9):
            OneBlit1("Nom nom")
        elif(numMess==10):
            OneBlit3("There's somethig", "I need to tell you,", "but not here")  
        elif(numMess==11):
            OneBlit2("It's", "DANGEROUS")  
        elif(numMess==12):
            OneBlit3("Meet me", "through the door", "to the right") 
        elif(numMess==13):
            OneBlit2("We can", "talk there")
        elif(numMess==14):
            OneBlit2("See you soon", "Sir Ball!")
        elif(numMess==15):
            OneBlit1("Om nom nom!")
            
def OneBlit1(text):
    textBounds=(29*w/40,55*h/100)
    display.messagePrint(w//25,text,textBounds,model.WHITE)
    
def OneBlit2(text1, text2):
    textBounds=(29*w/40,51*h/100)
    display.messagePrint(w//40,text1,textBounds,model.WHITE)  
    textBounds=(29*w/40,56*h/100)
    display.messagePrint(w//40,text2,textBounds,model.WHITE) 
    
def OneBlit3(text1, text2, text3):
    textBounds=(29*w/40,49*h/100)
    display.messagePrint(w//40,text1,textBounds,model.WHITE)
    textBounds=(29*w/40,54*h/100)
    display.messagePrint(w//40,text2,textBounds,model.WHITE)
    textBounds=(29*w/40,59*h/100)
    display.messagePrint(w//40,text3,textBounds,model.WHITE)  
            
            
            
def LuisSix(interact, numMess):
    #the character will disappear after talking to
    surface.blit(Luis, (2*w/5+w/10, 9*h/10-h/7)) 
    
    if(interact):
        #speech bubble        
        pygame.draw.polygon(surface,model.WHITE,[(22*w/45,3*h/4),(859*w/2070,7*h/10),(2251*w/5175,7*h/10)],3) 
        pygame.draw.ellipse(surface,model.WHITE,(326*w/1035,38*h/75, w/4, h/5),3)
        pygame.draw.ellipse(surface,model.GREY,(326*w/1035+1,38*h/75+1, w/4-2, h/5-2),0)
        
        
        if(numMess==0):
            SixBlit2("Oh good,", "you made it!")
        elif(numMess==1):
            SixBlit2("Welcome to the", "Shadow Realm")     
        elif(numMess==2):
            SixBlit1("My name is Luis")
        elif(numMess==3):
            SixBlit1("...")
        elif(numMess==4):
            SixBlit2("You don't talk", "much do you?")            
        elif(numMess==5):  
            SixBlit3("Well, anyway,", "no one knows", "how they got here")
        elif(numMess==6):      
            SixBlit3("But it sure is", "dreadful down here,", "isn't it?")
        elif(numMess==7):      
            SixBlit3("At least I found", "this fish to nibble", "om nom nom")
        elif(numMess==8):      
            SixBlit3("You want to", "leave this place,", "huh?")
        elif(numMess==9):
            SixBlit2("I can't", "blame you")
        elif(numMess==10):
            SixBlit2("There is only one", "way to escape")
        elif(numMess==11):
            SixBlit2("See those crystals", "up there?")
        elif(numMess==12):        
            SixBlit3("If you collect 100", "of them, and take", "them to the altar")
        elif(numMess==13):   
            SixBlit3("According to the", "ancient writtings,", "it should")
        elif(numMess==14):
            SixBlit2("open a portal", "back to the overworld")
        elif(numMess==15):     
            SixBlit3("And by the way,", "if you run into Marvin", "the Turtle")
        elif(numMess==16):  
            SixBlit3("don't listen to", "a word he says. he is", "a pathological liar")
        elif(numMess==17):
            SixBlit2("I know", "you can do it!")
        elif(numMess==18):  
            SixBlit1("Get those 100 crystals!") 
        elif(numMess==19):  
            SixBlit1("Good luck!")
       
       
def SixBlit1(text):
    textBounds=(53*w/120,60*h/100)
    display.messagePrint(w//40,text,textBounds,model.WHITE) 
    
def SixBlit2(text1, text2):
    textBounds=(53*w/120,58*h/100)
    display.messagePrint(w//40,text1,textBounds,model.WHITE)
    textBounds=(53*w/120,63*h/100)
    display.messagePrint(w//40,text2,textBounds,model.WHITE)
    
def SixBlit3(text1, text2, text3):
    textBounds=(53*w/120,55*h/100)
    display.messagePrint(w//40,text1,textBounds,model.WHITE)
    textBounds=(53*w/120,60*h/100)
    display.messagePrint(w//40,text2,textBounds,model.WHITE)
    textBounds=(53*w/120,65*h/100)
    display.messagePrint(w//40,text3,textBounds,model.WHITE)