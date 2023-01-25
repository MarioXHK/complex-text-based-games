import pygame
import random
print("Defend, Moon!")
print("I really mean it, you're defending the moon!")
amongst = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Space Invaders")
doExit=False
clock = pygame.time.Clock()

#coolvars
playerx = 500
playery = 720
pewx = playerx
pewy = playery
vx = 0
speedto = 30
cory = False
corycooldown = 0
#pngs?
defender = pygame.image.load("defender.png")
alienback = pygame.image.load("back.png")
alienback2 = pygame.image.load("backagain.png")
alienmid = pygame.image.load("mid.png")
alienmid2 = pygame.image.load("midagain.png")
alienfront = pygame.image.load("front.png")
alienfront2 = pygame.image.load("frontagain.png")
keys = [False,False,False]
stuckin = True
#emlny
class alien:
    def __init__(self,type = "normal",xpos = 0,ypos = 0, xoffset = 0,):
        self.type = type
        self.live = True
        self.xpos = xpos
        self.ypos = ypos
        self.xoffset = xoffset
        self.left = False
        self.vxtimer = 0
        self.alldone = False
        self.oldypos = ypos
        self.frame = True
    def moove(self):
        global speedto
        if not self.live:
            return
        self.vxtimer += 1
        if self.vxtimer >= speedto:
            self.vxtimer = 0
            if (self.xpos <= 32 + self.xoffset or self.xpos >= 160 + self.xoffset):
                self.alldone = True
                if self.alldone:
                    if self.oldypos == self.ypos:
                        self.ypos += 16
                    else:
                        self.alldone = False
                        self.oldypos = self.ypos
                    
                    if self.xpos <= 64 + self.xoffset:
                        self.left = False
                    else:
                        self.left = True
            if not self.alldone:
                if not self.left:
                    self.xpos += 12
                else:
                    self.xpos -= 12
            if self.frame:
                self.frame = False
            else:
                self.frame = True
    def rendish(self):
        if self.frame:
            if self.type == "back":
                screen.blit(alienback, (self.xpos,self.ypos))
            elif self.type == "front":
                screen.blit(alienfront, (self.xpos-8,self.ypos))
            else:
                screen.blit(alienmid, (self.xpos-6,self.ypos))
        else:
            if self.type == "back":
                screen.blit(alienback2, (self.xpos,self.ypos))
            elif self.type == "front":
                screen.blit(alienfront2, (self.xpos-8,self.ypos))
            else:
                screen.blit(alienmid2, (self.xpos-6,self.ypos))
spacespiders = [alien("back",64,64)]


for f in range(1,12):
    spacespiders.append(alien("back", (f*64)+64, 64, f*64))
for p in range(2):
    for f in range(12):
        spacespiders.append(alien("middle", (f*64)+64, 192-(64*p), f*64))
for p in range(2):
    for f in range(12):
        spacespiders.append(alien("front", (f*64)+64, 320-(64*p), f*64))


class shoot:
    def __init__(self,enemy = False,xpos = 0,ypos = 0, atchto = 0,):
        self.enemy = enemy
        self.xpos = xpos
        self.ypos = ypos
        self.atchto = atchto
        self.power = 0
    def pew(self,power):
        self.power = power
    def moving(self):
        global spacespiders
        global playerx
        global playery
        global doExit
        if not self.power > 0:
            if self.enemy:
                self.xpos = spacespiders[self.atchto].xpos + 12
                self.ypos = spacespiders[self.atchto].ypos + 16
            else:
                self.xpos = playerx + 14
                self.ypos = playery - 16
        else:
            if self.enemy:
                self.ypos += self.power
            else:
                self.ypos -= self.power
        if self.enemy:
            if playery < self.ypos + 32 and playery > self.ypos and self.xpos + 8 > playerx and self.xpos < playerx + 32:
                doExit = True
            if (self.xpos >= playerx and self.xpos <= playerx + 32) and self.ypos >= playery:
                self.ypos = 1000
            if self.ypos > 768:
                self.power = 0
        else:
            for i in range(len(spacespiders)):
                if spacespiders[i].ypos < self.ypos + 32 and spacespiders[i].ypos > self.ypos and self.xpos + 4 > spacespiders[i].xpos and self.xpos < spacespiders[i].xpos + 32 and self.ypos < playery and spacespiders[i].live == True:
                    spacespiders[i].live = False
                    self.power = 0
                    
            if self.ypos < 0:
                self.power = 0
    def rendong(self):
        if self.power > 0:
            if self.enemy:
                pygame.draw.rect(screen, (255, 0, 0), (self.xpos, self.ypos, 8, 32))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (self.xpos, self.ypos, 4, 32))
fire = [shoot()]
for g in range(len(spacespiders)):
    fire.append(shoot(True,0,0,g))
    print(g)


#gaem loop
while not doExit:
    
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT:
            doExit = True;
        
        #inpoot
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0]=True
            elif event.key == pygame.K_RIGHT:
                keys[1]=True
            elif event.key == pygame.K_SPACE:
                keys[2]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0]=False
            elif event.key == pygame.K_RIGHT:
                keys[1]=False
            elif event.key == pygame.K_SPACE:
                keys[2]=False
    clock.tick(30)
    
    
    
    if keys[0]:
        vx = -6
    elif keys[1]:
        vx = 6
    else:
        vx = 0
    if keys[2]:
        fire[0].pew(20)
    #moving stuffff-==-=--==-=-=-= ???????????????!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    
    for d in range(len(spacespiders)):
        if spacespiders[d].live:
            if random.randrange(1000 ) == 0:
                fire[d+1 ].pew(12)
            
    
    
    playerx += vx
    
    if playerx < 0:
        playerx = 0
    elif playerx > 1024:
        playerx = 1024-32
    for j in range(len(spacespiders)):
        spacespiders[j].moove()
    for i in range(len(fire)):
        fire[i].moving()
    
    #speed up every down the go
    if corycooldown < 0:
        corycooldown = -10
        for j in range(len(spacespiders)):
            if spacespiders[j].alldone:
                cory = True
    corycooldown -= 1
    if cory:
        speedto -= 1
        cory = False
        corycooldown = 120
    #rendererrererer=========================================================================0
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    screen.blit(defender, (playerx,playery))
    for i in range(len(spacespiders)):
        if spacespiders[i].live:
            spacespiders[i].rendish()
    for i in range(len(fire)):
        fire[i].rendong()
            
    pygame.display.flip()#this actually puts the pixel on the screen
#end
pygame.quit()