import pygame
import random
pygame.init()  
pygame.display.set_caption("Oh, now he's plaing classical targets")  # sets the window title
screen = pygame.display.set_mode((1200, 900))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
class target:
    def __init__(self, xpos, ypos, sim = False, vx=2, vy=2, size = 20, color1 = (255,0,0), color2 = (255,255,255), color3 = (0,0,255)):
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.vx = vx*random.randrange(-5,5)
        self.vy = vy*random.randrange(-5,5)
        if self.vx == 0:
            self.vx = 1
        if self.vy == 0:
            self.vy = 1
        if sim:
            self.vy = self.vx
        self.flash = 0
    def move(self):
        bump1=False
        bump2=False
        ezsiz = self.size*5
        if self.xpos <= 0 + ezsiz or self.xpos >= 1200 - ezsiz:
            self.vx *= -1
            bump1 = True
        if self.ypos <= 0 + ezsiz or self.ypos >= 900 - ezsiz:
            self.vy *= -1
            bump2 = True
        if bump1 and bump2:
            print("CORNER BOUNCE LET'S GOOOOO!!!!!")
            self.flash = 255
        
        self.xpos += self.vx
        self.ypos += self.vy
    def draw(self):
        self.flash -= 5
        if self.flash < 0:
            self.flash = 0
        pygame.draw.circle(screen, (self.color1), (self.xpos, self.ypos), self.size*5)
        pygame.draw.circle(screen, (self.color2), (self.xpos, self.ypos), self.size*4)
        pygame.draw.circle(screen, (self.color3), (self.xpos, self.ypos), self.size*3)
        pygame.draw.circle(screen, (self.color2), (self.xpos, self.ypos), self.size*2)
        pygame.draw.circle(screen, (self.color1), (self.xpos, self.ypos), self.size)
        if self.flash > 1:
            pygame.draw.circle(screen, (self.flash,self.flash,self.flash), (self.xpos, self.ypos), self.size*5)


testtarget = target(600, 450, True)
xander = target(600,450, False,1,1, 30, (230,200,0),(50,50,50), (230,200,0))
rabbit = target(600,450, True,3,3, 10, (0,0,230),(255,255,255), (250,200,230))
coomer = target(600, 450, False,2.5,2.5, 15, (0,0,0),(255,255,255), (250,250,0))
clone = target(600, 450, False,2,2, 20, (0,255,255),(0,0,0), (255,255,0))
targettm = target(600, 450, False,2,2, 12, (200,0,0),(200,0,0), (255,255,255))

while not gameover: #GAME LOOP############################################################
    clock.tick(50) #FPS
    #INPUT!
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
    testtarget.move()
    xander.move()
    rabbit.move()
    coomer.move()
    clone.move()
    targettm.move()
    #RENDER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    screen.fill((0,0,0))
    xander.draw()
    clone.draw()
    testtarget.draw()
    coomer.draw()
    targettm.draw()
    rabbit.draw()
    pygame.display.flip()#Done in under 100 lines of code!