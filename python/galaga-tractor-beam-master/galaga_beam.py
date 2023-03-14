#galaga tractor beam code

import pygame #bring in pygame library
pygame.init #initialize pygame
pi = 3.1415926535897932384626433832795
screen = pygame.display.set_mode((800, 800)) #create game screen
pygame.display.set_caption("galaga beam") #window title

class beam:#f1/0 it, we classin'
    def __init__(self,wack,reverse=False):
        self.rev = reverse
        self.numbs = wack
        if self.rev:
            self.frame = 2
        else:
            self.frame = 0
    def update(self):
        if self.rev:
            self.frame -= 1
            if self.frame < 0:
                self.frame = 2
        else:
            self.frame += 1
            if self.frame > 2:
                self.frame = 0
    def render(self):
        if self.frame == 0:
            color = (5, 100, 200)
        elif self.frame == 1:
            color = (25, 150, 150)
        elif self.frame == 2:
            color = (50, 200, 100)
        
        
        pygame.draw.arc(screen, (color), (self.numbs),  pi, 2*pi, 10)


#load alien ship image
alienShip = pygame.image.load("boss.jpg")

#draw alien ship
screen.blit(alienShip, (210, 180))
pygame.display.flip()

#top arc
pygame.draw.arc(screen, (5, 100, 200), (200, 200, 100, 100),  pi, 2*pi, 10)
pygame.display.flip() #update screen 
pygame.time.wait(2000)

#second arc
pygame.draw.arc(screen, (50, 200, 100), (190, 230, 120, 100),  pi, 2*pi, 10)
pygame.display.flip() #update screen 
pygame.time.wait(2000)

#add more here!
beams = []
for i in range(15):
    beams.append(beam((200-(i*10), 200+(i*30), 100+(i*20), 100)))
    for j in range(len(beams)):
        beams[j].update()
        beams[j].render()
    pygame.display.flip() #update screen 
    pygame.time.wait(100)
for i in range(20):
    for j in range(len(beams)):
        beams[j].update()
        beams[j].render()
    pygame.display.flip()
    pygame.time.wait(100)
