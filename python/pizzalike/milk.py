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
        self.crouch = False
    def controlhorz(self,dirr,run,sneak):
        self.controlling = True
        self.crouch = sneak
        #Moves you in both directions
        if sneak:
            self.maxrun = 2
        elif run:
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
        #Trust me this takes up a lot less space
        osimp = ((int((self.x)/40),int((self.y)/40),int((self.x+40)/40),int((self.y+60)/40),int((self.y+20)/40)),(int((self.x+2)/40),int((self.y+2)/40),int((self.x+38)/40),int((self.y+58)/40)))
        '''
        Complicated tuple, Explanation: X and Y then First: Oversimplfied then otherway, Otherway meaning the thing plus the player's size.
        Last part of the tuple is y divided by size 2. First tuple is the real numbers while the second is imperciseness to make physics correct ig
        '''
        oversimpYall = int((self.y+20)/40)#Oversimplified Y divided by ysize
        try:
            if (theMap[osimp[0][3]][osimp[1][0]][1] or theMap[osimp[0][3]][osimp[1][2]][1]) and self.vy > -0.1 and kind == 0:
                return True
            if (theMap[osimp[0][1]][osimp[1][0]][2] or theMap[osimp[0][1]][osimp[1][2]][2]) and self.vy < 0.1 and kind == 1:
                return True
            if (theMap[osimp[1][1]][osimp[0][0]][4] or theMap[osimp[1][3]][osimp[0][0]][4] or theMap[oversimpYall][osimp[0][0]][3]) and self.vx < 0.1 and kind == 2:
                return True
            if (theMap[osimp[1][1]][osimp[0][2]][3] or theMap[osimp[1][3]][osimp[0][2]][3] or theMap[oversimpYall][osimp[0][2]][4]) and self.vx > -0.1 and kind == 3:
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
            self.y = (int((self.y)/40))*40+40
            
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
        if self.collision(theMap,1):#Ceiling collision
            self.vy = 0
            self.y = (int((self.y)/40))*40+40
        if self.collision(theMap,2):
            self.x = (int((self.x+40)/40))*40
            self.vx = 0
        if self.collision(theMap,3):
            self.x = (int((self.x+40)/40))*40-40
            self.vx = 0
        if self.collision(theMap,0):
            self.onGround = True
            self.vy = 0
            self.y = (int((self.y+60)/40))*40-60
        if self.collision(theMap,1):#Ceiling collision
            self.vy = 0
            self.y = (int((self.y)/40))*40+40
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
#Generate collisionmap function for maps when you're lazy! goes like [up, down, left, right]
def coolgen(mape):
    nonsolid = {0,3,9}
    for i in range(len(mape)):
        for j in range(len(mape[0])):
            for k in range(4):#Sets up the 4 things
                mape[i][j].append(False)
            if mape[i][j][0] in nonsolid:#For when something isn't solid
                if mape[i][j][0] == 3:
                    mape[i][j][1] = True
                continue
            #Now for all the solid things
            if i > 0:
                if mape[i-1][j][0] in nonsolid:#checks if anything is above it
                    mape[i][j][1]=(True)
            if i < len(mape)-1:
                if mape[i+1][j][0] in nonsolid:#checks if anything is below it
                    mape[i][j][2]=(True)
            if j > 0:
                if mape[i][j-1][0] in nonsolid:#checks if anything is to the left of it
                    mape[i][j][3]=(True)
            if j < len(mape[0])-1:
                if mape[i][j+1][0] in nonsolid:#checks if anything is to the right of it
                    mape[i][j][4]=(True)
    return mape
#Scans the map to see where to spawn the player ig
def scanspawn(emap):
    for i in range(len(emap)):
        for j in range(len(emap[0])):
            if emap[i][j] == 9:
                return [i*40,j*40+20]
    return [400,400]
#Generate collisionmap function for maps when you're lazy! goes like [up, down, left, right]
def coolgen(mape):
    nonsolid = {0,3}
    
    for i in range(len(mape)):
        for j in range(len(mape[0])):
            #Turns the map into a bunch of lists
            ep = []
            ep.append(mape[i][j])
            mape[i][j] = ep
    for i in range(len(mape)):
        for j in range(len(mape[0])):
            for k in range(4):#Sets up the 4 things
                mape[i][j].append(False)
            if mape[i][j][0] in nonsolid:#For when something isn't solid
                if mape[i][j][0] == 3:
                    mape[i][j][1] = True
                continue
            #Now for all the solid things
            if i > 0:
                if mape[i-1][j][0] in nonsolid:#checks if anything is above it
                    mape[i][j][1]=(True)
            if i < len(mape)-1:
                if mape[i+1][j][0] in nonsolid:#checks if anything is below it
                    mape[i][j][2]=(True)
            if j > 0:
                if mape[i][j-1][0] in nonsolid:#checks if anything is to the left of it
                    mape[i][j][3]=(True)
            if j < len(mape[0])-1:
                if mape[i][j+1][0] in nonsolid:#checks if anything is to the right of it
                    mape[i][j][4]=(True)
    return mape
#SETTING UP THE VARIABLES!
keys = [False,False,False,False,False]#For input
gaming = True#Alright, we're gaming
debug = False
offset = [0,0]

#MAP: 1 is grass, 2 is brick
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,2,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0],
       [1,0,2,2,2,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0],
       [1,0,0,0,0,0,0,0,1,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0],
       [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,2,2,0,0,2,2,2,2,2,2,2,0],
       [1,1,0,0,0,0,0,0,1,0,2,2,1,2,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,0,0,2,2,2,2,2,2,2,2,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
startpoint = scanspawn(map)
weegee = player(400,400,0,0)#THe player you play as

map = coolgen(map)

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
        weegee.controlhorz(False,keys[4],keys[3])
    elif keys[1]:
        weegee.controlhorz(True,keys[4],keys[3])
    
    #THE LAWS OF PHYSICS AKA HOW STUFF MOVES!
    weegee.move(map)
    #Scrolling?? Hopefully
    if weegee.x > 400 and weegee.x < len(map[0])*40-400:
        offset[0] = weegee.x - 400
    if weegee.y > 400 and weegee.y < len(map)*40-400:
        offset[1] = weegee.y - 400
    #The part where things get put on the screen, aka --==XXXTHE RENDER SECTIONXXX==--
    screen.fill((60,0,150)) #wipe screen so it doesn't smear
    
    for i in range (len(map)):
        for j in range(len(map[0])):
            if map[i][j][0]==1:
                pygame.draw.rect(screen, (120, 67, 10), (40*j-offset[0],40*i-offset[1], 40, 40))
            if map[i][j][0]==2:
                pygame.draw.rect(screen, (181, 58, 31), (40*j-offset[0],40*i-offset[1], 40, 40))
            if map[i][j][0]==3:
                pygame.draw.rect(screen, (255, 255, 255), (40*j-offset[0],40*i-offset[1], 40, 5))
            if debug:
                if map[i][j][1]:
                    pygame.draw.rect(screen, (255, 0, 0), (40*j-offset[0],40*i-offset[1], 40, 5))
                if map[i][j][2]:
                    pygame.draw.rect(screen, (255, 0, 0), (40*j-offset[0],(40*i-offset[1])+35, 40, 5))
                if map[i][j][3]:
                    pygame.draw.rect(screen, (255, 0, 0), (40*j-offset[0],40*i-offset[1], 5, 40))
                if map[i][j][4]:
                    pygame.draw.rect(screen, (255, 0, 0), ((40*j-offset[0])+35,(40*i-offset[1]), 5, 40))
    
    
    pygame.draw.rect(screen, (100, 200, 100), (weegee.x-offset[0], weegee.y-offset[1], 40, 60))
    pygame.display.flip()