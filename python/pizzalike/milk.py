import pygame

#set up pygame stuff
pygame.init()  
pygame.display.set_caption("Pizzalike Platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
#Setting up the classes
class player:#THE PLAYER OF THE GAME
    def __init__(self, startx, starty, startvx, startvy):
        self.x = startx
        self.y = starty
        self.vx = startvx
        self.vy = startvy
        self.controlling = False
        self.defslip = 0.5
        self.slip = 0.5
        self.fasterDown = False
        self.maxrun = 4
        self.onGround = True
        self.onRecord = [True,False]
    def controlhorz(self,dirr,run):
        self.controlling = True
        #Moves you in both directions
        if run:
            self.maxrun = 8
        else:
            self.maxrun = 4
        
        if dirr:
            if self.vx <= self.maxrun:
                self.vx += self.slip
            else:
                self.vx -= self.slip/2
                if self.vx > self.maxrun:
                    self.vx = self.maxrun
        else:
            if self.vx >= 0-self.maxrun:
                self.vx -= self.slip
            else:
                self.vx += self.slip/2
                if self.vx < 0-self.maxrun:
                    self.vx = 0-self.maxrun
    def jump(self):
        if self.onGround:
            self.vy = -12
    def collision(self,theMap, kind):
        hitable = {1,2}
        #Trust me this takes up a lot less space
        oversimpY = int((self.y)/40)
        oversimpYP = int((self.y+60)/40)
        oversimpYL = int((self.y+2)/40)
        oversimpYPL = int((self.y+58)/40)
        oversimpX = int((self.x+2)/40)
        oversimpXP = int((self.x+38)/40)
        oversimpXrl = int((self.x)/40)
        oversimpXPrl = int((self.x+40)/40)
        try:
            for i in range(1,4):
                if (i in [theMap[oversimpYP][oversimpX],theMap[oversimpYP][oversimpXP]]) and self.vy > -0.1 and kind == 0:
                    return True
                if (i in [theMap[oversimpY][oversimpX],theMap[oversimpY][oversimpXP]]) and self.vy < 0.1 and i in hitable and kind == 1:
                    return True
                if (i in [theMap[oversimpYL][oversimpXrl],theMap[oversimpYPL][oversimpXrl]]) and self.vy > -0.1 and i in hitable and kind == 2:
                    return True
                if (i in [theMap[oversimpYL][oversimpXPrl],theMap[oversimpYPL][oversimpXPrl]]) and self.vy > -0.1 and i in hitable and kind == 3:
                    return True
        except:#If an error occures (most likely out of bounds) It'll teleport the player back the start
            print("OUT OF BOUNDS! Re-positioning!")
            self.x = 400
            self.y = 400
        return False
        
    def move(self,theMap):
        self.onGround = False
        #Actually makes you move
        if not self.controlling:#If you're not doing anything you'll be slown down
            if self.vx > 0:
                self.vx -= self.slip/2
                if self.vx < 0.1:
                    self.vx = 0
            elif self.vx < 0:
                self.vx += self.slip/2
                if self.vx > -0.1:
                    self.vx = 0
        #Collision--------------------------------
        
        #Gravity stuff
        if self.collision(theMap,0):
            self.onGround = True
            self.vy = 0
            self.y = (int((self.y+60)/40))*40-60
            
        else:
            self.vy += .2
            #if the player let go of the jump early
            if self.fasterDown:
                self.vy += .5
        
        if self.collision(theMap,1):#Ceiling collision
            self.vy = 0
        if self.collision(theMap,2):#Wall collision (2 and 3)
            self.x = (int((self.x+40)/40))*40
            self.vx = 0
        if self.collision(theMap,3):
            self.x = (int((self.x+40)/40))*40-40
            self.vx = 0
        
        #Terminal Velocity
        if self.vy > 10:
            self.vy = 10
        
        
        self.fasterDown = False
        self.x += self.vx
        self.y += self.vy
        #Corrections
        if self.collision(theMap,0):
            self.onGround = True
            self.vy = 0
            self.y = (int((self.y+60)/40))*40-60
        if self.collision(theMap,1):
            self.vy = 0
        if self.collision(theMap,2):
            self.x = (int((self.x+40)/40))*40
            self.vx = 0
        if self.collision(theMap,3):
            self.x = (int((self.x+40)/40))*40-40
            self.vx = 0
        #Makes the movement less controllable while in air
        if self.onGround:
            self.slip = self.defslip
        else:
            self.slip = self.defslip/3


#SETTING UP THE VARIABLES!
weegee = player(400,400,0,0)#THe player you play as
keys = [False,False,False,False,False]#For input
gaming = True#Alright, we're gaming

offset = [0,0]

#MAP: 1 is grass, 2 is brick
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,0,2,2,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,3 ,3, 3,3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,0,2,2,2,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,0,2,2,2,2,0],
       [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,0,2,2,2,2,2,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ,0 ,2, 2,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0,0,2,2,2,2,2,2,0],
       [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,0,2,2,2,2,2,2,2,0],
       [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 1 ,2 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0 ,2 ,0, 0,2,2,2,2,2,2,2,2,0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1,1,1,1,1,1,1,1,0]]


while gaming:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT:
            gaming = False
        
        #inpoot-------------------------------------------------------
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0]=True
            elif event.key == pygame.K_RIGHT:
                keys[1]=True
            if event.key == pygame.K_UP:
                keys[2]=True
            if event.key == pygame.K_DOWN:
                keys[3]=True
            elif event.key == pygame.K_LSHIFT:
                keys[4]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0]=False
            elif event.key == pygame.K_RIGHT:
                keys[1]=False
            if event.key == pygame.K_UP:
                keys[2]=False
            if event.key == pygame.K_DOWN:
                keys[3]=False
            elif event.key == pygame.K_LSHIFT:
                keys[4]=False
    clock.tick(60)
    
    #PLAYER INPUT!!!
    weegee.controlling = False#For when the player isn't controlling
    if keys[2]:
        weegee.jump()
    if (not keys[2]) and weegee.vy < -2:
        weegee.fasterDown = True
    if keys[0]:
        weegee.controlhorz(False,keys[4])
    elif keys[1]:
        weegee.controlhorz(True,keys[4])
    
    #THE LAWS OF PHYSICS AKA HOW STUFF MOVES!
    weegee.move(map)
    #Scrolling?? Hopefully
    if weegee.x > 400 and weegee.x < 1600:
        offset[0] = weegee.x - 400
    
    #The part where things get put on the screen, aka --==XXXTHE RENDER SECTIONXXX==--
    screen.fill((60,0,150)) #wipe screen so it doesn't smear
    
    for i in range (len(map)):
        for j in range(len(map[0])):
            if map[i][j]==1:
                pygame.draw.rect(screen, (120, 67, 10), (40*j-offset[0],40*i, 40, 40))
            if map[i][j]==2:
                pygame.draw.rect(screen, (181, 58, 31), (40*j-offset[0],40*i, 40, 40))
            if map[i][j]==3:
                pygame.draw.rect(screen, (255, 255, 255), (40*j-offset[0],40*i, 40, 5))
    
    
    pygame.draw.rect(screen, (100, 200, 100), (weegee.x-offset[0], weegee.y, 40, 60))
    pygame.display.flip()