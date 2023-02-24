#Partially Completed Paint Program
#Created By Dr. Mo on 11/2019

#student instructions:
#Mild: add the other color values to the bottom of the code
#Medium: add options to change the brush size and/or wipe the screen
#Spicy: add a rainbow brush, rectangle drawing function, etc.
import random
import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("python paint program")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((200,200,200))
clock = pygame.time.Clock()

xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
brushsize = 20
draw = False


UP = 0
DOWN = 1
SPACE = 2
keys = [False,False,False]

#color definitions (you have to add these to the game, and you can add more if you want)
BLUE = (0,0,255)
RED = (255, 0,0)
GREEN = (0,255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
TEAL = (0,255,255)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

rainred = 255
raingreen = 0
rainblue = 0
incred = False
incgreen = False
incblue = False
decred = False
decgreen = False
decblue = False
allcolors = False

RAINBOW = (rainred,raingreen,rainblue)

color = RED
#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    clock.tick(60)
#RAINBOW CODE!!!
    if rainred == 255 and raingreen == 0 and rainblue == 0:
        decblue = False
        incgreen = True
    if rainred == 255 and raingreen == 255 and rainblue == 0:
        decred = True
        incgreen = False
    if rainred == 0 and raingreen == 255 and rainblue == 0:
        decred = False
        incblue = True
    if rainred == 0 and raingreen == 255 and rainblue == 255:
        decgreen = True
        incblue = False
    if rainred == 0 and raingreen == 0 and rainblue == 255:
        decgreen = False
        incred = True
    if rainred == 255 and raingreen == 0 and rainblue == 255:
        decblue = True
        incred = False
    if incred == True:
        rainred += 1
    if decred == True:
        rainred -= 1
    if incgreen == True:
        raingreen += 1
    if decgreen == True:
        raingreen -= 1
    if incblue == True:
        rainblue += 1
    if decblue == True:
        rainblue -= 1
    RAINBOW = (rainred,raingreen,rainblue)
#input section----------------------------------------------
    oldmousePos = mousePos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close game window
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False

        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_SPACE:
                keys[SPACE]=True
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                keys[SPACE]=False
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
    
    if keys[UP] == True:
        brushsize += 1
    if keys[DOWN] == True and brushsize != 1:
        brushsize -= 1
    if keys[SPACE] == True:
        brushsize = 20
#update/timer section---------------------------------------    
    if draw == True:
        if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >750:
            color = RED
            allcolors = False
        if mousePos[0] > 50 and mousePos[0] < 100 and mousePos[1] >750:
            color = GREEN
            allcolors = False
        if mousePos[0] > 100 and mousePos[0] < 150 and mousePos[1] >750:
            color = BLUE
            allcolors = False
        if mousePos[0] > 150 and mousePos[0] < 200 and mousePos[1] >750:
            color = YELLOW
            allcolors = False
        if mousePos[0] > 200 and mousePos[0] < 250 and mousePos[1] >750:
            color = TEAL
            allcolors = False
        if mousePos[0] > 250 and mousePos[0] < 300 and mousePos[1] >750:
            color = PURPLE
            allcolors = False
        if mousePos[0] > 300 and mousePos[0] < 350 and mousePos[1] >750:
            color = WHITE
            allcolors = False
        if mousePos[0] > 350 and mousePos[0] < 400 and mousePos[1] >750:
            color = BLACK
            allcolors = False
        if mousePos[0] > 400 and mousePos[0] < 450 and mousePos[1] >750:
            screen.fill((200,200,200))
        if mousePos[0] > 450 and mousePos[0] < 500 and mousePos[1] >750:
            allcolors = True
#render section---------------------------------------------
    if allcolors == True:
        color = RAINBOW
    if draw == True:
        pygame.draw.circle(screen, color, (mousePos), (brushsize/2)-1) #player paintbrush
        pygame.draw.line(screen, color, (oldmousePos),(mousePos), width = brushsize)
    
    #color changing rectangles at bottom of screen 
    pygame.draw.rect(screen, RED, (0,750,50,50))
    pygame.draw.rect(screen, GREEN, (50, 750, 50, 50))
    pygame.draw.rect(screen, BLUE, (100, 750, 50, 50))
    pygame.draw.rect(screen, YELLOW, (150,750,50,50))
    pygame.draw.rect(screen, TEAL, (200, 750, 50, 50))
    pygame.draw.rect(screen, PURPLE, (250, 750, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 750, 50, 50))
    pygame.draw.rect(screen, BLACK, (350, 750, 50, 50))
    pygame.draw.rect(screen, WHITE, (400, 750, 50, 50))
    pygame.draw.line(screen, BLACK, (400, 750),(450,800), width = 5)
    pygame.draw.line(screen, BLACK, (450, 750),(400,800), width = 5)
    pygame.draw.rect(screen, RAINBOW, (450, 750, 50, 50))
    #more colors go here!
        
    pygame.display.flip()
    

#end game loop##############################################
    print(brushsize)
pygame.quit()
