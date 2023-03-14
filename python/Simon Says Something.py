import pygame #AAAAAAAAAAAAAAAAAAAAAAAAAAAA
import random #Random landdddd
import math #A divide by 0 error
import winsound #BEEP BOOP MOTHERF-
#THIS SHYTUFDIOHDGF NEEDS TO EXIST FOR THE REST OF THE GAME TO EXIST!
pygame.init()
pygame.display.set_caption("Honeydew!")
screen = pygame.display.set_mode((800,800))
#Game varabllllllllllllllllllllllllllllll
xpos = 0
ypos = 0
mousePos = (xpos,ypos)
hasClicked = False
pattern = []
playerPattern = []
playerTurn = True
pi = 3.1415926535897932384626433832795
ded = False

def collision(xpos, ypos):
    if math.sqrt((xpos - 400)**2 + (ypos - 400)**2)>200 or math.sqrt((xpos - 400)**2 + (ypos - 400)**2)<100:
        print("outside the ring")
        return -1
    elif xpos < 400 and ypos < 400:
        print("over red button")
        pygame.draw.arc(screen, (255,0,0),(200,200,400,400),pi/2,pi,100)
        pygame.display.flip()
        winsound.Beep(440,400)
        return 0
    elif xpos < 400 and ypos > 400:
        print("over green button")
        pygame.draw.arc(screen, (0,255,0),(200,200,400,400),pi,3*pi/2,100)
        pygame.display.flip()
        winsound.Beep(640,400)
        return 1
    elif xpos > 400 and ypos < 400:
        print("over yellow button")
        pygame.draw.arc(screen, (255,255,0),(200,200,400,400),pi*2,pi/2,100)
        pygame.display.flip()
        winsound.Beep(240,400)
        return 3
    else:
        print("over blue button")
        pygame.draw.arc(screen, (0,0,255),(200,200,400,400),3*pi/2,pi*2,100)
        pygame.display.flip()
        winsound.Beep(840,400)
        return 2

pygame.draw.arc(screen, (155,0,0),(200,200,400,400),pi/2,pi,100)
pygame.draw.arc(screen, (0,155,0),(200,200,400,400),pi,3*pi/2,100)
pygame.draw.arc(screen, (0,0,155),(200,200,400,400),3*pi/2,pi*2,100)
pygame.draw.arc(screen, (155,155,0),(200,200,400,400),pi*2,pi/2,100)
pygame.display.flip()
#GAMELOOP LET'S GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
while True:
    event = pygame.event.wait()
    #INPUT SECTIONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.MOUSEBUTTONDOWN:
        hasClicked=True
        print("Cookie click")
    
    if event.type == pygame.MOUSEBUTTONUP:
        hasClicked = False
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
    
    #Player's turn?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if playerTurn:
        if len(playerPattern) < len(pattern):
            if hasClicked:
                playerPattern.append(collision(mousePos[0], mousePos[1]))
                hasClicked=False
            for i in range(len(playerPattern)):
                if playerPattern[i] != pattern[i]:
                    ded = True
                    
        else:
            playerTurn = False
            pygame.time.wait(800)
    
    
    #Update sectinnn__________________________________________________________________________xXUpdateSectionXx
    if ded:
        pattern.clear()
        playerPattern.clear()
        pygame.draw.arc(screen, (255,0,0),(200,200,400,400),pi,pi*2,100)
        pygame.draw.arc(screen, (200,0,0),(200,200,400,400),pi*2,pi/2,100)
        pygame.display.flip()
        print("AAAAAAAAAAA")
        winsound.Beep(1500,1000)
        screen.fill((0,0,0))
        ded = False
    elif not playerTurn:
        print("Starting machine turn")
        pattern.append(random.randrange(0,4))
        for i in range(len(pattern)):
            if pattern[i] == 0:
                pygame.draw.arc(screen, (255,0,0),(200,200,400,400),pi/2,pi,100)
                pygame.display.flip()
                winsound.Beep(440,500)
            elif pattern[i] == 1:
                pygame.draw.arc(screen, (0,255,0),(200,200,400,400),pi,3*pi/2,100)
                pygame.display.flip()
                winsound.Beep(640,500)
            elif pattern[i] == 2:
                pygame.draw.arc(screen, (0,0,255),(200,200,400,400),3*pi/2,pi*2,100)
                pygame.display.flip()
                winsound.Beep(840,500)
            elif pattern[i] == 3:
                pygame.draw.arc(screen, (255,255,0),(200,200,400,400),pi*2,pi/2,100)
                pygame.display.flip()
                winsound.Beep(240,500)
            pygame.draw.arc(screen, (155,0,0),(200,200,400,400),pi/2,pi,100)
            pygame.draw.arc(screen, (0,155,0),(200,200,400,400),pi,3*pi/2,100)
            pygame.draw.arc(screen, (0,0,155),(200,200,400,400),3*pi/2,pi*2,100)
            pygame.draw.arc(screen, (155,155,0),(200,200,400,400),pi*2,pi/2,100)
            pygame.display.flip()
            playerTurn = True
            playerPattern.clear()
    
    
    #RENDER?!?!?!?!!??!?!?!!?
        
        
    #DRAW THE SHADOW OF ISRAPHEL ARCS!
    pygame.draw.arc(screen, (155,0,0),(200,200,400,400),pi/2,pi,100)
    pygame.draw.arc(screen, (0,155,0),(200,200,400,400),pi,3*pi/2,100)
    pygame.draw.arc(screen, (0,0,155),(200,200,400,400),3*pi/2,pi*2,100)
    pygame.draw.arc(screen, (155,155,0),(200,200,400,400),pi*2,pi/2,100)
    pygame.display.flip()
#the end----------------------------------
pygame.quit()