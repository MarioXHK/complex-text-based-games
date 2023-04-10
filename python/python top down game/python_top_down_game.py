import pygame
import random

#set up pygame stuff
pygame.init()  
pygame.display.set_caption("top down game")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

#game variables
timer = 0 #used for sheep movement
score = 0

#images and fonts
SheepPic = pygame.image.load("sheep.jpg")
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score:', True, (200, 200, 0))
text2 = font.render(str(score), True, (200, 200, 0))
text3 = font.render('YOU WIN!', True, (200, 200, 0))

#CONSTANTS (not required, just makes code easier to read)
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

#function defintions------------------------------------
#can you tell me what the parameters are for these functions, and what they return (if anything)?
class sheep:
    def __init__(self,x,y,simple = False,directx = random.randrange(0,2),directy = random.randrange(0,2), got = False):
        self.xpos = x
        self.ypos = y
        self.caught = got
        self.ouch = False
        self.ouch2 = False
        self.simple = simple
        self.stuntimer = 0
        if directx == 0:
            self.nega = False
            self.v = 1
        else:
            self.nega = True
            self.v = -1
        if directy == 0:
            self.mode = True
        else:
            self.mode = False
    def move(self):
        if self.caught:
            return
        slam = False
        if self.xpos > 800 or self.xpos < 0 or self.ypos > 800 or self.ypos < 0:#if the sheep hits one of the walls, it'll slam it's head on the wall and bounce back
            if abs(self.v) > 10:
                slam = True
            else:
                if self.mode:
                    if self.xpos > 800:
                        self.xpos = 752
                    else:
                        self.xpos = 16
                else:
                    if self.ypos > 800:
                        self.ypos = 752
                    else:
                        self.ypos = 16
                self.v = 0
                    
                    
        if slam and self.ouch == False:
            self.ouch = True
            self.stuntimer = random.randrange(100,300)
            if self.nega:
                if abs(self.v) < 15:
                    self.v = 0 + abs(self.v)
                else:
                    self.v = 15
            else:
                if abs(self.v) < 15:
                    self.v = 0 - abs(self.v)
                else:
                    self.v = -15
        if self.v == 0:
            if random.randrange(0,2) == 0:
                self.nega = False
            else:
                self.nega = True
            if random.randrange(0,2) == 0:
                self.mode = False
            else:
                self.mode = True 
        if random.randrange(0,10) == 0 and abs(self.v) > 10:
            if self.nega:
                self.nega = False
            else:
                self.nega = True
        if not self.ouch2:
            if self.nega:#Makes sure if to add or subtract
                self.v -= 1
            else:
                self.v += 1
        if self.stuntimer == 0:
            self.ouch = False
            self.ouch2 = False
        else:
            if self.v == 0:
                self.ouch2 = True
            self.stuntimer -= 1
            
        if self.mode:
            self.xpos += self.v
        else:
            self.ypos += self.v
    def braw(self):
        if self.caught:
            return #don't draw them if they're already caught!
        if self.simple:
            pygame.draw.rect(screen, (250, 100, 100), (self.xpos, self.ypos, 40, 40))
        else:
            screen.blit(SheepPic, (self.xpos, self.ypos))

def collision(PlayerX, PlayerY, shep):
    if PlayerX+40 > shep.xpos:
       if PlayerX < shep.xpos+40:
           if PlayerY+40 >shep.ypos:
               if PlayerY < shep.ypos+40:
                   if shep.caught == False: #only catch uncaught sheeps!
                    global score #make it so this function can change this value
                    score +=1
                    return True#catch da sheepies!
    return False



#create sheep!
#numbers in list represent xpos, ypos, direction moving, and whether it's been caught or not!
sheep0 = sheep(200, 400,True)
sheep1 = sheep(200, 400)
#make more sheeps here!
sheeps = []
sheepnum = 30
el = random.randint(1,sheepnum)
for i in range(sheepnum - el):
    sheeps.append(sheep(random.randrange(50,700),random.randrange(50,700)))
for i in range(el):
    sheeps.append(sheep(random.randrange(50,700),random.randrange(50,700),True))

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity (left/right speed) of player
vy = 0 #y velocity (up/down speed) of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

while score<len(sheeps): #GAME LOOP############################################################
    clock.tick(60) #FPS
    timer+=1
    
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        #check if a key has been PRESSED
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True

        #check if a key has been LET GO
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
          
    #physics
    #section--------------------------------------------------------------------
    
    #player movement!--------
    if keys[LEFT] == True:
        vx = -3
    elif keys[RIGHT] == True:
        vx = 3
    else:
        vx = 0
    if keys[UP] == True:
        vy = -3
    elif keys[DOWN] == True:
        vy = 3
    else:
        vy = 0


    #player/sheep collision!
    for i in range(len(sheeps)):
        if not sheeps[i].caught:
            sheeps[i].caught = collision(xpos, ypos, sheeps[i])

    #update player position
    xpos+=vx 
    ypos+=vy
    
    #update sheep position
    for i in range(len(sheeps)):
        sheeps[i].move()
  
    # RENDER
    # Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    #draw player
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 40, 40))

    #draw sheep
    for i in range(len(sheeps)):
        sheeps[i].braw()
    
    #display score
    screen.blit(text, (20, 20))
    text2 = font.render(str(score), True, (200, 200, 0))#update score number
    screen.blit(text2, (140, 20))

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------

#end screen
screen.fill((0,0,0)) 
screen.blit(text3, (400,400))
pygame.display.flip()
pygame.time.wait(2000)#pause for a bit before ending

pygame.quit()
