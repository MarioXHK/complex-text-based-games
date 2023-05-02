import pygame
from math import sqrt
#set up pygame stuff
pygame.init()  
pygame.display.set_caption("Pizzalike Platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
#Setting up collision function!
def collision(x,y,h,v,vx,vy,kind,duck = False):
    global map
    #I swear I'll turn this into a function that everything can use
    osimp = ((int((x)/40),int((y)/40),int((x+h)/40),int((y+v)/40),int((x+(h/2))/40),int((y+(h/2))/40)),(int((x+2)/40),int((y+2)/40),int((x+(h-2))/40),int((y+(v-2))/40)),(int((y-20)/40)))
    #Complicated tuple, Explanation: X and Y then First: Oversimplfied then otherway, Otherway meaning the thing plus the player's size.
    #Last part of the tuple is y divided by size 2. First tuple is the real numbers while the second is imperciseness to make physics correct ig
    try:
        if (map[osimp[0][3]][osimp[1][0]][1] or map[osimp[0][3]][osimp[1][2]][1] or map[osimp[0][3]][osimp[0][4]][1]) and vy > -0.1 and (y-v) % 40 <= 5 and kind == 0:
            return True#If the checker is below a block
        if (map[osimp[0][1]][osimp[1][0]][2] or map[osimp[0][1]][osimp[1][2]][2] or map[osimp[0][1]][osimp[0][4]][2]) and vy < 0.1 and kind == 1:
            return True#If the checker is above a block
        if (map[osimp[1][1]][osimp[0][0]][4] or map[osimp[1][3]][osimp[0][0]][4] or map[osimp[0][5]][osimp[0][0]][4]) and vx < 0.1 and kind == 2:
            return True#If the checker is to the right of a block
        if (map[osimp[1][1]][osimp[0][2]][3] or map[osimp[1][3]][osimp[0][2]][3] or map[osimp[0][5]][osimp[0][2]][3]) and vx > -0.1 and kind == 3:
            return True#If the checker is to the left of a block
        if (map[osimp[2]][osimp[1][0]][2] or map[osimp[2]][osimp[1][2]][2] or map[osimp[2]][osimp[0][4]][2]) and duck and kind == 4:
            return True#If the checker is ducking
        if kind == 5 and vy > -0.1 and (y-v) % 40 <= 5:
            if map[osimp[0][3]][osimp[1][0]][1] and map[osimp[0][3]][osimp[1][2]][1] and map[osimp[0][3]][osimp[0][4]][1]:
                return 2#If the checker is completely on a block
            elif map[osimp[0][3]][osimp[1][0]][1] or map[osimp[0][3]][osimp[1][2]][1] or map[osimp[0][3]][osimp[0][4]][1]:
                return 1#If the checker is on the edge of a block
    except:
        return False
    return False
    


#Setting up the classes
class player:#THE PLAYER OF THE GAME
    def __init__(self, startx, starty, name = "nul"):
        self.name = name
        self.x = startx
        #Player's X position
        self.y = starty
        #Player's Y position
        self.xsize = 40
        #Player's Horizontal Size
        self.ysize = 60
        #Player's Vertical Size
        self.vx = 0
        #Player's Horizontal Velocity
        self.vy = 0
        #Player's Vertical Velocity
        self.rx = self.x
        self.ry = self.y
        #Player's Render Positions (used for offset)
        
        self.ox = 0
        self.oy = 0
        #The offset for the previous
        
        self.bump = 0
        #Cancel moving timer
        
        self.controlling = False
        #If the player is being controlled
        
        self.slip = 0.5
        #How slippery the ground is
        self.defslip = self.slip
        #The default value for self.slip, cannot be changed
        
        self.fasterDown = False
        self.maxrun = 4
        #How fast can the player run
        
        self.vmod = 4
        #How fast can the player run's modifier
        
        self.onGround = True
        self.crouch = False
        self.steps = 10
        #How many loops to preform collision checks
    def controlhorz(self,dirr,run):
        self.controlling = True
        #Moves you in both directions
        hardtoaccel = 12
        #The speed in which speeding up becomes harder than slowing down
        if self.crouch:
            self.maxrun = 2
        elif run:
            self.maxrun = 8 * self.vmod
        else:
            self.maxrun = 4
        
        if dirr:
            if self.vx <= self.maxrun:
                if self.vx < hardtoaccel:
                    self.vx += self.slip
                else:
                    self.vx += self.slip/5
            else:
                self.vx -= self.slip/2
                if self.vx > self.maxrun:
                    self.vx += self.slip/2
        else:
            if self.vx >= 0-self.maxrun:
                if self.vx > 0-hardtoaccel:
                    self.vx -= self.slip
                else:
                    self.vx -= self.slip/5
            else:
                self.vx += self.slip/2
                if self.vx < 0-self.maxrun:
                    self.vx -= self.slip/2
    def jump(self):
        if self.onGround:
            self.vy = -10
    def duck(self, sneak):
        if self.bump > 0 or collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,4,self.crouch):
            return
        if sneak != self.crouch:
            if not self.crouch:
                self.ysize = 40
                self.y += 20
                self.oy -= 20
            else:
                self.ysize = 60
                self.y -= 20
                self.oy += 20
        self.crouch = sneak
    def retick(self):
        #Pre-render maths and some other scripts that update the player that don't involve moving (good for when the game is pawused)
        self.rx = self.x + self.ox
        self.ry = self.y + self.oy
        
    def move(self):
        if self.bump > 0:
            self.bump -= 1
            return
        
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
        if not collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,0):
            self.vy += .3
            #if the player let go of the jump early
            if self.fasterDown:
                self.vy += 0.6
        dodabump = [False, self.vx]
        for i in range(self.steps):#Does physics 10 times to be sure to not phase through anything.
        #Gravity stuff
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,0):#THE FLOOR
                self.onGround = True
                self.vy = 0
                self.y = (int((self.y+self.ysize)/40))*40-self.ysize
            
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,1):#Ceiling collision
                self.vy = 0
                self.y = (int((self.y)/40))*40+40
                
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,2):#Wall left
                self.x = (int((self.x+40)/40))*40
                if self.vx < -15:
                    dodabump[0] = True
                self.vx = 0
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,3):#Wall right
                self.x = (int((self.x+self.xsize)/40))*40-self.xsize
                if self.vx > 15:
                    dodabump[0] = True
                self.vx = 0
                    
            #Terminal Velocity
            if self.vy > 15:
                self.vy = 15
            self.fasterDown = False
            self.x += self.vx/self.steps
            self.y += self.vy/self.steps
            #Makes the movement less controllable while in air
            if self.onGround:
                self.slip = self.defslip
            else:
                self.slip = self.defslip/3
        if dodabump[0]:
            self.vx = 0-dodabump[1]/4
            self.vy = -5
            self.bump = 5
    def draw(self, off, zoom = 1):
        color = (100, 100, 100)
        if self.name == "w":
            color = (100, 200, 100)
        elif self.name == "m":
            color = (200, 100, 100)
        pygame.draw.rect(screen, color, (self.x*zoom-off[0], self.y*zoom-off[1], self.xsize*zoom, self.ysize*zoom))

#Entity!
class entity:
    def __init__(self, startx, starty, name = "nul"):
        self.type = name
        self.x = startx
        #Entity's X position
        self.y = starty
        #Entity's Y position
        self.vx = 0
        #Player's Horizontal Velocity
        self.vy = 0
        #Player's Vertical Velocity
        self.xsize = 40
        #Entity's Horizontal Size
        self.ysize = 40
        #Entity's Vertical Size
        self.held = False
        #If the entity is being held
        
        self.slip = 0.5
        #How slippery the ground is
        self.defslip = self.slip
        #The default value for self.slip, cannot be changed
        
        self.onGround = True
        self.steps = 5
        #How many loops to preform collision checks
        
        if name == "cheese":
            self.xsize = 60
            self.ysize = 40
            self.vx = 3
    def move(self):
        if self.held:
            return
        self.onGround = False
        for i in range(self.steps):#Does physics 10 times to be sure to not phase through anything.
        #Gravity stuff
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,0):#THE FLOOR
                self.onGround = True
                self.vy = 0
                self.y = (int((self.y+self.ysize)/40))*40-self.ysize
            
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,1):#Ceiling collision
                self.vy = 0
                self.y = (int((self.y)/40))*40+40
                
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,2):#Wall left
                self.x = (int((self.x+40)/40))*40
                self.vx = 0-self.vx
            if collision(self.x,self.y,self.xsize,self.ysize,self.vx,self.vy,3):#Wall right
                self.x = (int((self.x+self.xsize)/40))*40-self.xsize
                self.vx = 0-self.vx
                    
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
        if self.name == "cheese":
            color = (200, 200, 100)
        elif self.name == "slime":
            color = (50, 200, 100)
        pygame.draw.rect(screen, color, (self.x*zoom-off[0], self.y*zoom-off[1], self.xsize*zoom, self.ysize*zoom))
#Some fun ctions

#Scans the map for points of interest (searchfor)

def scanspawn(emap, searchfor):
    mapwith = []
    for i in range(len(emap)):
        for j in range(len(emap[0])):
            if emap[i][j] == searchfor:
                mapwith.append([j*40,i*40])#Adds the point of interests
    return mapwith

def smooth(inn, target, tipe, positive = True, speed = 0.1):
    if (inn > target and positive) or (inn < target and not positive):
        return inn
    if tipe == "line":
        return inn + speed

#Generate collisionmap function for maps when you're lazy! goes like [up, down, left, right] Also determines how something should be rendered

#takes the square shape around a square and returns specific values
def solidcheck(thing, inv = False):
    #Thing is the thing checked if nonsolid, if inv is true then It'll send the opposite
    nonsolid = {0,3,9}
    if not thing in nonsolid:
        if inv:
            return False
        else:
            return True
    else:
        if inv:
            return True
        else:
            return False

def cornerchecker(mop,og,cords):
    mep = [[],[],[]]
    for a in range(3):
        for b in range(3):
            try:
                mep[a].append(mop[cords[0]+a-1][cords[1]+b-1])
            except:
                mep[a].append([1])
    if solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [6,1]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [6,2]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [7,3]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [6,3]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [6,4]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [5,4]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [4,4]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [5,3]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [4,3]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [4,1]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0],True) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [5,1]
    elif solidcheck(mep[0][0][0]) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [4,2]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][0][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0]):
        return [5,2]
    elif solidcheck(mep[0][1][0], True) and solidcheck(mep[1][0][0], True) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][1][0]) and solidcheck(mep[2][2][0], True):
        return [0,3]
    elif solidcheck(mep[0][1][0], True) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0], True) and solidcheck(mep[2][0][0], True) and solidcheck(mep[2][1][0]):
        return [1,3]
    elif solidcheck(mep[0][1][0]) and solidcheck(mep[0][2][0], True) and solidcheck(mep[1][0][0], True) and solidcheck(mep[1][2][0]) and solidcheck(mep[2][1][0], True):
        return [0,4]
    elif solidcheck(mep[0][0][0], True) and solidcheck(mep[0][1][0]) and solidcheck(mep[1][0][0]) and solidcheck(mep[1][2][0], True) and solidcheck(mep[2][1][0], True):
        return [1,4]
    return og
    


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
            mape[i][j].append([0,0])
            if mape[i][j][0] in nonsolid:#For when something isn't solid
                if mape[i][j][0] == 3:#special case scenario: platform
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
            if mape[i][j][3] and mape[i][j][4]:
                mape[i][j][5][0] = 3
            elif mape[i][j][3]:
                mape[i][j][5][0] = 0
            elif mape[i][j][4]:
                mape[i][j][5][0] = 2
            else:
                mape[i][j][5][0] = 1
            if mape[i][j][1]:
                mape[i][j][5][1] = 0
                if mape[i][j][2]:
                    mape[i][j][5][0] += 4
            elif mape[i][j][2]:
                mape[i][j][5][1] = 2
            else:
                mape[i][j][5][1] = 1
    for i in range(len(mape)):
        for j in range(len(mape[0])):
            if mape[i][j][0] in nonsolid:
                continue
            mape[i][j][5] = cornerchecker(mape,mape[i][j][5],[i,j])
            
    
    return mape
#SETTING UP THE VARIABLES!
keys = [[False,False,False,False,False,False,False]]#For input
gaming = True#Alright, we're gaming
debug = False
offset = [0,0]
dozooming = False #if true, zooming will be enabled
#MAP: 1 is grass, 2 is brick
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,2,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,2,2,2,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,2,2,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,0,0,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, (400,200))
players = [player(320,1380,"w")]#THe player you play as
p1dom = 1 #How much player 1 has dominance over scrolling
zoom = 1
zoomy = 1
maxdis = 600 #Max distance a player is allowed to be away from the other before they get pulled
map = coolgen(map)
for o in range(len(players)-1):
    keys.append(keys[0])

while gaming:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT:
            gaming = False
        
        #inpoot-------------------------------------------------------
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0][0]=True
            elif event.key == pygame.K_RIGHT:
                keys[0][1]=True
            if event.key == pygame.K_UP:
                keys[0][2]=True
            if event.key == pygame.K_DOWN:
                keys[0][3]=True
            if event.key == pygame.K_z:
                keys[0][4]=True
            if event.key == pygame.K_LSHIFT:
                keys[0][5]=True
            if event.key == pygame.K_x:
                keys[0][6]=True
            if event.key == pygame.K_SPACE:
                debug=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0][0]=False
            elif event.key == pygame.K_RIGHT:
                keys[0][1]=False
            if event.key == pygame.K_UP:
                keys[0][2]=False
            if event.key == pygame.K_DOWN:
                keys[0][3]=False
            if event.key == pygame.K_z:
                keys[0][4]=False
            if event.key == pygame.K_LSHIFT:
                keys[0][5]=False
            if event.key == pygame.K_x:
                keys[0][6]=False
            if event.key == pygame.K_SPACE:
                debug=False
    clock.tick(60)
    #PLAYER INPUT!!!
    for i in range(len(players)):
        players[i].controlling = False#For when the player isn't controlling
        if keys[i][4]:
            players[i].jump()
        if (not keys[i][4]) and players[i].vy < -0.5:
            players[i].fasterDown = True
        players[i].duck(keys[i][3])
        if keys[i][0]:
            players[i].controlhorz(False,keys[i][5])
        elif keys[i][1]:
            players[i].controlhorz(True,keys[i][5])
    
    #THE LAWS OF PHYSICS AKA HOW STUFF MOVES!
        players[i].move()
        players[i].retick()
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
        average[0] += players[i].rx
        average[1] += players[i].ry
    for i in range(p1dom):
        average[0] += players[0].rx
        average[1] += players[0].ry
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
    for i in range (len(map)):
        for j in range(len(map[0])):
            myx = (40*zoom)*j-offset[0]
            myy = (40*zoom)*i-offset[1]
            if map[i][j][0]==1:
                if dozooming:
                    pygame.draw.rect(screen, (120, 67, 10), (myx,myy, 40*zoom, 40*zoom))
                else:
                    screen.blit(ground, (myx, myy), (map[i][j][5][0]*40, map[i][j][5][1]*40, 40, 40))
            if map[i][j][0]==2:
                if dozooming:
                    pygame.draw.rect(screen, (181, 58, 31), (myx,myy, 40*zoom, 40*zoom))
            if map[i][j][0]==3:
                if dozooming:
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