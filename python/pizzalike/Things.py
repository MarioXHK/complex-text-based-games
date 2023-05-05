import pygame

#Entity!
class entity:
    def __init__(self, startx, starty, name = "nul"):
        self.type = name
        self.x = startx
        #Entity's X position
        self.y = starty
        #Entity's Y position
        self.vx = 0
        #Entity's Horizontal Velocity
        self.vy = 0
        #Entity's Vertical Velocity
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
        self.wheeled = True
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