
import pygame
import math
import globals
from Player import player
from Fireball import fireball
from Rope import rope
pygame.init()  
pygame.display.set_caption("top down grid with classes")  # sets the window title
screen = pygame.display.set_mode((832, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5
keys = [False, False, False, False, False] #this list holds whether each key has been pressed

AlivePotato = True
ticker = 0

#instantiate a player
p1 = player()

#instantiate a rope
r1 = rope()

#instantiate a fireball
ball = fireball()

#MAP: 1 is grass, 2 is brick
map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2],
       [2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 2,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,2],
       [2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0 ,0 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,2],
       [2, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2 ,2 ,0, 0,0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0 ,2 ,0, 0,2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2]]

brick = pygame.image.load('brick.png') #load your spritesheet

PotatoPic = pygame.image.load("potato.jpg")
PotatoPic.set_colorkey((255,0,255))


while not gameover:
    ticker += 1
    clock.tick(60) #FPS
    #input section@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = False
          
    #physics section@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    if keys[SPACE] == True: #check space for shooting      
            ball.shoot(p1.xpos, p1.ypos, p1.direction)

    ball.move(keys)

    #potato collision!
    if ball.collide(215, 215) == True and AlivePotato == True:
        ball.isAlive = False
        AlivePotato = False


    #r1.move(map, ticker, p1.xpos+p1.x_offset, p1.ypos+p1.y_offset, p1.x_offset, p1.y_offset)

    p1.move(keys, map)

    # RENDER--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    #draw map
    for i in range(28):
        for j in range(33):
            if map[i][j] == 1:
                screen.blit(dirt, (j * 50 + p1.x_offset, i * 50 + p1.y_offset), (0, 0, 50, 50))
            if map[i][j] == 2:
                screen.blit(brick, (j * 50 + p1.x_offset, i * 50 + p1.y_offset), (0, 0, 50, 50))
    
    #draw fireball
    if ball.isAlive == True:
        ball.draw(screen)
    #draw rope
    r1.draw(screen, p1.x_offset, p1.y_offset)
    #draw player
    p1.draw(screen, ticker)
    #draw potato
    if AlivePotato == True:
        screen.blit(PotatoPic, (200 + p1.x_offset, 200 + p1.y_offset))

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game
#loop------------------------------------------------------------------------------
pygame.quit()