import pygame

#set up pygame stuff
pygame.init()  
pygame.display.set_caption("Pizzalike Platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

class player:
    def __init__(self, startx, starty, startvx, startvy):
        self.x = startx
        self.y = starty
        self.vx = startvx
        self.vy = startvy
        self.controlling = False
        self.slip = 0.5
        self.maxrun = 4
    def controlhorz(self,dirr,run):
        self.controlling = True
        
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
        
        
    def move(self):
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
            
        
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.x = 0
            self.vx = 0
weegee = player(400,400,0,0)
keys = [False,False,False,False,False]
gaming = True
while gaming:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT:
            gaming = False;
        
        #inpoot-------------------------------------------------------
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0]=True
            elif event.key == pygame.K_RIGHT:
                keys[1]=True
            if event.key == pygame.K_SPACE:
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
            if event.key == pygame.K_SPACE:
                keys[2]=False
            if event.key == pygame.K_DOWN:
                keys[3]=False
            elif event.key == pygame.K_LSHIFT:
                keys[4]=False
    clock.tick(60)
    weegee.controlling = False#For when the player isn't controlling
    if keys[0]:
        weegee.controlhorz(False,keys[4])
    elif keys[1]:
        weegee.controlhorz(True,keys[4])
    weegee.move()
    #The part where things get put on the screen, aka --==XXXTHE RENDER SECTIONXXX==--
    screen.fill((60,0,150)) #wipe screen so it doesn't smear
    
    pygame.draw.rect(screen, (100, 200, 100), (weegee.x, weegee.y, 40, 60))
    
    pygame.display.flip()