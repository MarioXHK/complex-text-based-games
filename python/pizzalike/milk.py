import pygame
from math import sqrt
#set up pygame stuff
pygame.init()  
pygame.display.set_caption("Pizzalike Platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
#Setting up the classes
class player:#THE PLAYER OF THE GAME
    def __init__(self, startx, starty, name = "nul"):
        self.name = name
        self.x = startx
        self.y = starty
        self.xsize = 40
        self.ysize = 60
        self.vx = 0
        self.vy = 0
        self.controlling = False
        self.defslip = 0.5
        self.slip = 0.5
        self.fasterDown = False
        self.maxrun = 4
        self.onGround = True
        self.onRecord = [True,False]
        self.crouch = False
        self.steps = 5#How many loops to preform collision checks
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
            self.vy = -10
    def collision(self,theMap, kind):
        #Trust me this takes up a lot less space
        osimp = ((int((self.x)/40),int((self.y)/40),int((self.x+self.xsize)/40),int((self.y+self.ysize)/40),int((self.x+(self.xsize/2))/40),int((self.y+(self.ysize/2))/40)),(int((self.x+2)/40),int((self.y+2)/40),int((self.x+(self.xsize-2))/40),int((self.y+(self.ysize-2))/40)))
        #Complicated tuple, Explanation: X and Y then First: Oversimplfied then otherway, Otherway meaning the thing plus the player's size.
        #Last part of the tuple is y divided by size 2. First tuple is the real numbers while the second is imperciseness to make physics correct ig
        try:
            if (theMap[osimp[0][3]][osimp[1][0]][1] or theMap[osimp[0][3]][osimp[1][2]][1] or theMap[osimp[0][3]][osimp[0][4]][1]) and self.vy > -0.1 and (self.y-self.ysize) % 40 <= 5 and kind == 0:
                return True#If the player is below a block
            if (theMap[osimp[0][1]][osimp[1][0]][2] or theMap[osimp[0][1]][osimp[1][2]][2] or theMap[osimp[0][1]][osimp[0][4]][2]) and self.vy < 0.1 and kind == 1:
                return True#If the player is above a block
            if (theMap[osimp[1][1]][osimp[0][0]][4] or theMap[osimp[1][3]][osimp[0][0]][4] or theMap[osimp[0][5]][osimp[0][0]][4]) and self.vx < 0.1 and kind == 2:
                return True#If the player is to the right of a block
            if (theMap[osimp[1][1]][osimp[0][2]][3] or theMap[osimp[1][3]][osimp[0][2]][3] or theMap[osimp[0][5]][osimp[0][2]][3]) and self.vx > -0.1 and kind == 3:
                return True#If the player is to the left of a block
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
        if not self.collision(theMap,0):
            self.vy += .3
            #if the player let go of the jump early
            if self.fasterDown:
                self.vy += 0.6
        
        for i in range(self.steps):#Does physics 10 times to be sure to not phase through anything.
        #Gravity stuff
            if self.collision(theMap,0):
                self.onGround = True
                self.vy = 0
                self.y = (int((self.y+self.ysize)/40))*40-self.ysize
            
            if self.collision(theMap,1):#Ceiling collision
                self.vy = 0
                self.y = (int((self.y)/40))*40+40
                
            if self.collision(theMap,2):#Wall collision (2 and 3)
                self.x = (int((self.x+40)/40))*40
                self.vx = 0
            if self.collision(theMap,3):
                self.x = (int((self.x+self.xsize)/40))*40-self.xsize
                self.vx = 0
            
            #Terminal Velocity
            if self.vy > 10:
                self.vy = 10
            self.fasterDown = False
            self.x += self.vx/self.steps
            self.y += self.vy/self.steps
            #Makes the movement less controllable while in air
            if self.onGround:
                self.slip = self.defslip
            else:
                self.slip = self.defslip/3
    def draw(self, off, zoom = 1):
        color = (100, 100, 100)
        if self.name == "w":
            color = (100, 200, 100)
        elif self.name == "m":
            color = (200, 100, 100)
        pygame.draw.rect(screen, color, (self.x*zoom-off[0], self.y*zoom-off[1], self.xsize*zoom, self.ysize*zoom))





#Scans the map to see where to spawn the player ig

def scanspawn(emap):
    for i in range(len(emap)):
        for j in range(len(emap[0])):
            if emap[i][j] == 9:
                return [i*40,j*40+20]
    return [400,400]

def smooth(inn, target, tipe, positive = True, speed = 0.1):
    if (inn > target and positive) or (inn < target and not positive):
        return inn
    if tipe == "line":
        return inn + speed

#Generate collisionmap function for maps when you're lazy! goes like [up, down, left, right]

def coolgen(mape):
    nonsolid = {0,3,9}
    
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
keys = [1,[False,False,False,False,False]]#For input
gaming = True#Alright, we're gaming
debug = True
offset = [0,0]
dozooming = True #if true, zooming will be enabled
#MAP: 1 is grass, 2 is brick
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,2,0,0,2,2,2,2,2,2,2],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,2,2,2,2,2,2,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,3,3,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,2,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,1,1,1,1],
       [1,0,2,2,2,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,1,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,1,1,1,1],
       [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,2,2,0,0,2,2,2,2,2,2,2,0,1,1,1,1],
       [1,1,0,0,0,0,0,0,1,0,2,2,1,2,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,0,0,2,2,2,2,2,2,2,2,0,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

ground = pygame.image.load('ground.png')


startpoint = scanspawn(map)
players = [player(400,400,"w"),player(400,400,"m")]#THe player you play as
p1dom = 1 #How much player 1 has dominance over scrolling
zoom = 1
zoomy = 1
maxdis = 600 #Max distance a player is allowed to be away from the other before they get pulled
map = coolgen(map)
for o in range(len(players)-1):
    keys.append([False,False,False,False,False])

while gaming:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT:
            gaming = False
        
        #inpoot-------------------------------------------------------
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_1:
                keys[0]=1
            if event.key == pygame.K_LEFT:
                keys[keys[0]][0]=True
            elif event.key == pygame.K_RIGHT:
                keys[keys[0]][1]=True
            if event.key == pygame.K_UP:
                keys[keys[0]][2]=True
            if event.key == pygame.K_DOWN:
                keys[keys[0]][3]=True
            elif event.key == pygame.K_LSHIFT:
                keys[keys[0]][4]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[keys[0]][0]=False
            elif event.key == pygame.K_RIGHT:
                keys[keys[0]][1]=False
            if event.key == pygame.K_UP:
                keys[keys[0]][2]=False
            if event.key == pygame.K_DOWN:
                keys[keys[0]][3]=False
            elif event.key == pygame.K_LSHIFT:
                keys[keys[0]][4]=False
    clock.tick(60)
    
    #PLAYER INPUT!!!
    for i in range(len(players)):
        players[i].controlling = False#For when the player isn't controlling
        if keys[i+1][2]:
            players[i].jump()
        if (not keys[i+1][2]) and players[i].vy < -0.5:
            players[i].fasterDown = True
        if keys[i+1][0]:
            players[i].controlhorz(False,keys[i+1][4],keys[i+1][3])
        elif keys[i+1][1]:
            players[i].controlhorz(True,keys[i+1][4],keys[i+1][3])
    
    #THE LAWS OF PHYSICS AKA HOW STUFF MOVES!
        players[i].move(map)
    #4 later
    pdisx = []
    pdisy = []
    if len(players) > 1:
        for i in range(len(players)-1):
            pdisx.append(int(abs(players[0].x-players[i+1].x)))
            pdisy.append(int(abs(players[0].y-players[i+1].y)))
    #Scrolling?? Definetly
    average = [0,0]
    for i in range(len(players)):
        average[0] += players[i].x
        average[1] += players[i].y
    for i in range(p1dom):
        average[0] += players[0].x
        average[1] += players[0].y
    average[0] = average[0]/(len(players)+p1dom)
    average[1] = average[1]/(len(players)+p1dom)
    if average[0] > 400*(1/zoom) and average[0] < len(map[0])*40-(400*(1/zoom)):
        offset[0] = (average[0] - 400)*zoom+(400*(zoom-1))
    elif average[0] > 400*(1/zoom):
        offset[0] = ((len(map[0])*40-(400*(1/zoom)))*zoom+(400*zoom*-1))-(400*(1-zoom))
    else:
        offset[0] = 0
    
    
    if average[1] > 400*(1/zoom) and average[1] < len(map)*40-(400*(1/zoom)):
        offset[1] = (average[1] - 400)*zoom+(400*(zoom-1))
    elif average[1] > 400*(1/zoom):
        offset[1] = ((len(map)*40-(400*(1/zoom)))*zoom+(400*zoom*-1))-(400*(1-zoom))
    else:
        offset[1] = 0
    #ZOOMING?!?!?!?!? Is that even possible?
    
    zoom = 1
    if dozooming:
        maxdis = 900
        if len(players) > 1:
            for i in range(len(players)-1):
                if pdisx[i] > 400 or pdisy[i] > 400:
                    if pdisx[i] > pdisy[i]:
                        zoom = 1.5-pdisx[i]/800
                    else:
                        zoom = 1.5-pdisy[i]/800
                    if zoom < 0.7:
                        zoom = 0.7
            
    else:
        maxdis = 700
    if len(players) > 1:
        #Pulls the player to the first player instantly)
        for d in range(len(players)):
                    if pdisx[d-1] > maxdis or pdisy[d-1] > maxdis:
                        players[d].x = players[0].x
                        players[d].y = players[0].y
    
    
    #The part where things get put on the screen, aka --==XXXTHE RENDER SECTIONXXX==--
    zoomy = smooth(zoomy,zoom,"line",False, -0.05)
    
    screen.fill((60,0,150)) #wipe screen so it doesn't smear
    ground = pygame.transform.scale(ground, (200*zoom,200*zoom))
    for i in range (len(map)):
        for j in range(len(map[0])):
            myx = (40*zoom)*j-offset[0]
            myy = (40*zoom)*i-offset[1]
            if map[i][j][0]==1:
                screen.blit(ground, (myx, myy), (0, 0, 40*zoom, 40*zoom)) 
            if map[i][j][0]==2:
                pygame.draw.rect(screen, (181, 58, 31), (myx,myy, 40*zoom, 40*zoom))
            if map[i][j][0]==3:
                pygame.draw.rect(screen, (255, 255, 255), (myx,myy, 40*zoom, 5*zoom))
            if debug:
                if map[i][j][1]:
                    pygame.draw.rect(screen, (255, 0, 0), (myx,myy, 40*zoom, 5*zoom))
                if map[i][j][2]:
                    pygame.draw.rect(screen, (255, 0, 0), (myx,myy+35*zoom, 40*zoom, 5*zoom))
                if map[i][j][3]:
                    pygame.draw.rect(screen, (255, 0, 0), (myx,myy, 5*zoom, 40*zoom))
                if map[i][j][4]:
                    pygame.draw.rect(screen, (255, 0, 0), (myx+35*zoom,myy, 5*zoom, 40*zoom))
    
    
    for k in range(len(players)):
        players[k].draw(offset,zoom)
    pygame.display.flip()