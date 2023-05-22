import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4

timer = 0

class bomb:
    def __init__(self):
        self.xpos = -10
        self.ypos = -10
        self.isAlive = False
        self.timer = 100
        self.exploding = False

    def draw(self, offset):
        if self.isAlive ==True:
            pygame.draw.circle(screen, (255, 0, 255), (self.xpos-offset, self.ypos), 10)
        if self.exploding == True:
            pygame.draw.circle(screen, (255, 255, 0), (self.xpos-offset, self.ypos), 20)

    def place(self, x, y, offset, direction):
        self.isAlive=True
        self.timer = 100
        if direction == RIGHT:
            self.xpos = x + 50
            self.ypos = y +20
        elif direction == LEFT:
            self.xpos = x
            self.ypos = y+20

    def update(self, offset, direction):
        self.timer-=1
        if self.timer <=0 and self.timer > -50:
            self.exploding = True
           
            #play explosion sound here
            #print("offset", offset)
            #print("checking", int((ypos)/50),int((xpos-offset)/50))
            if direction == RIGHT:
                if map[int((ypos)/50)][int((xpos-self.off)/50)+1]==2:
                    print("erasing wall!")
                    map[int((ypos)/50)][int((xpos-self.off)/50)+1]=0
            if direction == LEFT:
                if map[int((ypos)/50)][int((xpos-self.off)/50)-1]==2:
                    print("erasing wall!")
                    map[int((ypos)/50)][int((xpos-self.off)/50)-1]=0
        elif self.timer<=-50:
            self.exploding = False
            self.isAlive = False
           

b1 = bomb()


#MAP: 1 is grass, 2 is brick
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,0],
       [1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2 ,2 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0 ,2 ,0, 0,0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,0]]

brick = pygame.image.load('brick.png') #load your spritesheet
dirt = pygame.image.load('dirt.png') #load your spritesheet
Link = pygame.image.load('link.png') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
xpos = 400 #xpos of player
ypos = 400 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
offset = 0
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
moving = False

#animation variables variables
frameWidth = 32
frameHeight = 48
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

while not gameover:
    timer+=1
    clock.tick(60) #FPS
   
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_SPACE:
                keys[SPACE] = True
                print("space pressed! ")

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_SPACE:
                keys[SPACE]=False
                print("space released!")
   

    #place bomb
   
    if keys[SPACE]==True:
        print("placing bomb")
        keys[SPACE]=False
        b1.place(xpos, ypos, offset, direction)

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx = -3
        RowNum = 0
        direction = LEFT
        moving = True
        if xpos > 1200:
            offset += 3
       
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx=3
        RowNum = 1
        direction = RIGHT
        moving = True
        if xpos > 400:
            offset -= 3
    #turn off velocity
    else:
        vx = 0
        moving = False
       
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        RowNum = 2
        isOnGround = False
        direction = UP
        moving = True
   
   
       
    xpos+=vx #update player xpos
    ypos+=vy
    #print(vx, vy)
   
    #COLLISION
   
    #collision with feetsies
    if map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==2:
        isOnGround = True
        vy=0
       
    else:
        isOnGround = False
       
    #bump your head, ouch!
    if map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==2:
        vy=0
       
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos+frameHeight-10)/50)][int((xpos-10)/50)]==1 or map[int((ypos)/50)][int((xpos-offset-10)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos-offset-10)/50)]==2 or map[int((ypos)/50)][int((xpos-offset-10)/50)]==2 ) and direction == LEFT:
        xpos+=3
        if xpos > 400:
            offset += 3
       
    #right collision needed here
    if (map[int((ypos+frameHeight-10)/50)][int((xpos+frameWidth+5)/50)]==1 or map[int((ypos)/50)][int((xpos+frameWidth+5)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos+frameWidth+5)/50)]==2 or map[int((ypos)/50)][int((xpos+frameWidth+5)/50)]==2 ) and direction == RIGHT:
        xpos-=3
        if xpos < 1200:
            offset -= 3
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 800:
        xpos-=3
    if xpos<0:
        xpos+=3

    print(xpos, offset)
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        vy = 0
        ypos = 800-frameHeight
   
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
   

       
    if b1.isAlive == True:
        b1.update(offset, direction)
    #ANIMATION-------------------------------------------------------------------
       
    # Update Animation Information

    if moving == True: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>7:
           frameNum = 0
 
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
           
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
   
    #draw map
    for i in range (16):
        for j in range(32):
            if map[i][j]==1:
                screen.blit(dirt, (j*50+offset, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(brick, (j*50+offset, i*50), (0, 0, 50, 50))
    b1.draw(offset)
    #print(offset)
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()
