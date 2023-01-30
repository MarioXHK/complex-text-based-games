import pygame
pygame.init()  
pygame.display.set_caption("PONG")  # sets the window title
screen = pygame.display.set_mode((1200, 900))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
font = pygame.font.Font(None ,74)


P1UP = 0
P1DOWN = 1
P2UP = 2
P2DOWN = 3

p2xpos = 50
p2ypos = 450
p1xpos = 1130
p1ypos = 450
p1v = 0
p2v = 0

p1points = 0

p2points = 0

keys = [False, False, False, False]

p1isOnEdge = False
p2isOnEdge = False
p1isOnUp = False
p2isOnUp = False

ballto = False
ballb = False
ballx = 600
bally = 450
ballv = 4
cooldown = 200
balb = 255

while not gameover:
    clock.tick(60)
    cooldown -= 1
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_UP:
                keys[P1UP]=True
            elif event.key == pygame.K_DOWN:
                keys[P1DOWN]=True
            if event.key == pygame.K_w:
                keys[P2UP]=True
            elif event.key == pygame.K_s:
                keys[P2DOWN]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[P1UP]=False
            elif event.key == pygame.K_DOWN:
                keys[P1DOWN]=False
            if event.key == pygame.K_w:
                keys[P2UP]=False
            elif event.key == pygame.K_s:
                keys[P2DOWN]=False
        
        
    if keys[P1UP]==True:
        p1v = -5
    elif keys[P1DOWN]==True:
        p1v = 5
    else:
        p1v = 0
    if keys[P2UP]==True:
        p2v = -5
    elif keys[P2DOWN]==True:
        p2v = 5
    else:
        p2v = 0
    
    
    #stop e
    if p1ypos < 0 or p1ypos > 800:
        p1isOnEdge = True
        p1v = 0
        if p1ypos < 0:
            p1isOnUp = True
        else:
            p1isOnUp = False
    
    if p2ypos < 0 or p2ypos > 800:
        p2isOnEdge = True
        p2v = 0
        if p2ypos < 0:
            p2isOnUp = True
        else:
            p2isOnUp = False
    
    
    if keys[P1DOWN]==True and p1isOnEdge == True and p1isOnUp == True: #will set the player free if they do the yes
        p1isOnEdge = False
        p1v = 5
    elif keys[P1UP]==True and p1isOnEdge == True and p1isOnUp == False:
        p1isOnEdge = False
        p1v = -5
    
    if keys[P2DOWN]==True and p2isOnEdge == True and p2isOnUp == True:
        p1isOnEdge = False
        p2v = 5
    elif keys[P2UP]==True and p2isOnEdge == True and p2isOnUp == False:
        p1isOnEdge = False
        p2v = -5
    
    
    if bally < 15:
        ballb = True
    elif bally > 885:
        ballb = False
    if (ballx < p2xpos+35 and ballx > p2xpos-15) and (bally-10 <= p2ypos+100 and bally+10 >= p2ypos):
        ballto = True
        ballv += 0.1
        if (ballx < p2xpos and ballx > p2xpos-15):
            balb = 0
    elif (ballx > p1xpos-15 and ballx < p1xpos+35) and (bally-10 <= p1ypos+100 and bally+10 >= p1ypos):
        ballto = False
        ballv += 0.1
        if (ballx > p1xpos+20 and ballx < p1xpos+35):
            balb = 0
    
    if ballx < 0 or ballx > 1200:
        cooldown = 200
        if ballx < 0:
            p1points += 1
            ballto = True
        else:
            p2points += 1
            ballto = False
    if ballv > 6:
        ballv = 6
    balb += 5
    if balb > 255:
        balb = 255
    
    if cooldown < 0:
        p1ypos+=p1v 
        p2ypos+=p2v
        if ballto == True:
            ballx += ballv
        else:
            ballx -= ballv
        if ballb == True:
            bally += ballv
        else:
            bally -= ballv
    else:
        p2xpos = 50
        p2ypos = 450
        p1xpos = 1130
        p1ypos = 450
        ballx = 600
        bally = 450
        ballv = 4
    
    #Render IG
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (250, 0, 0), (20, 20), p2points*5)
    pygame.draw.circle(screen, (0, 0, 250), (1180, 20), p1points*5)
    pygame.draw.rect(screen, (255, 255, 255), (p1xpos, p1ypos, 20, 100))
    pygame.draw.rect(screen, (255, 255, 255), (p2xpos, p2ypos, 20, 100))
    pygame.draw.circle(screen, (255, 255, balb), (ballx, bally), 15)
    text = font.render(str(p1points), 1, (255, 255, 255))
    screen.blit(text,(1100,10))
    text = font.render(str(p2points), 1, (255, 255, 255))
    screen.blit(text,(100,10))
    pygame.display.flip()