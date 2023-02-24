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
speedto = 40
cory = False
corycooldown = 0
score = 0
lives = 2
#pngs?
defender = pygame.image.load("defender.png")
heart = pygame.image.load("heart.png")
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
    def __init__(self,type = "normal",xpos = 0,ypos = 0, xoffset = 0,speed = 8):
        self.type = type
        self.speed = speed
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
        global doexit
        if not self.live:
            return
        if self.ypos > 700:
            doExit = True
        self.vxtimer += 1
        if self.vxtimer >= speedto:
            self.vxtimer = 0
            if (self.xpos <= 32 + self.xoffset or self.xpos >= 160 + self.xoffset):
                self.alldone = True
                if self.alldone:
                    if self.oldypos == self.ypos:
                        self.ypos += self.speed
                    else:
                        self.alldone = False
                        self.oldypos = self.ypos
                    
                    if self.xpos <= 64 + self.xoffset:
                        self.left = False
                    else:
                        self.left = True
            if not self.alldone:
                if not self.left:
                    self.xpos += self.speed
                else:
                    self.xpos -= self.speed
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
        self.cooldownyouidot = 0
    def pew(self,power):
        if self.power >= 0:
            self.power = power
    def moving(self):
        self.cooldownyouidot -= 1
        global spacespiders
        global playerx
        global playery
        global doExit
        global shield
        global lives
        global score
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
        
        for i in range(len(shield)):#All shots can destroy shields, and they prioritize shields over other stuffs
            if shield[i].ypos < self.ypos + 32 and shield[i].ypos > self.ypos and self.xpos + 4 > shield[i].xpos and self.xpos < shield[i].xpos + 32 and self.ypos < playery and shield[i].health > 0:
                shield[i].health -= 1
                self.power = 0
                if not self.enemy:
                    self.xpos = playerx + 14
                    self.ypos = playery - 16
            
            
        
        if self.enemy:#The script that tells who to murder
            if playery < self.ypos + 32 and playery > self.ypos and self.xpos + 8 > playerx and self.xpos < playerx + 32 and self.cooldownyouidot <= 0:
                #spacespiders = restart(spacespiders)
                playerx = 512
                lives -= 1
                self.cooldownyouidot = 100
                self.power = 0
                if lives == -1:
                    doExit = True
                return True
            if (self.xpos >= playerx and self.xpos <= playerx + 32) and self.ypos >= playery:
                self.ypos = 1000
            if self.ypos > 768:
                self.power = 0
        else:
            for i in range(len(spacespiders)):
                if spacespiders[i].ypos < self.ypos + 32 and spacespiders[i].ypos > self.ypos and self.xpos + 4 > spacespiders[i].xpos and self.xpos < spacespiders[i].xpos + 32 and self.ypos < playery and spacespiders[i].live == True:
                    spacespiders[i].live = False
                    self.power = 0
                    score += 10
                    self.xpos = playerx + 14
                    self.ypos = playery - 16
                    
            if self.ypos < 0:
                self.power = 0
        return False
    def rendong(self):
        if self.power > 0:
            if self.enemy:
                pygame.draw.rect(screen, (255, 0, 0), (self.xpos, self.ypos, 8, 32))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (self.xpos, self.ypos, 4, 32))


fire = [shoot()]
for g in range(len(spacespiders)):
    fire.append(shoot(True,0,0,g))
    
    
class barrier:
    def __init__(self,xpos = 0,ypos = 0):
        self.xpos = xpos
        self.ypos = ypos
        self.health = 5
    def rendie(self):
        color = self.health*50
        if self.health > 0:
            pygame.draw.rect(screen, (0, color, 0), (self.xpos, self.ypos, 32, 32))
shield = []
def blocker(x,y):
    global shield
    for k in range(2):
        for l in range(4):
            shield.append(barrier((l*32)+x,(k*32)+y))

def restart(spiders):#Completely useless function as of now as I've learned that the aliens don't even reset their positions when you die
    global playerx
    global fire
    space = []
    playerx = 512
    for f in range(12):
        if spiders[f].live:
            space.append(alien("back", (f*64)+64, 64, f*64))
    for p in range(2):
        for f in range(12):
            if spiders[f+12+(p*12)].live:
                spacespiders.append(alien("middle", (f*64)+64, 192-(64*p), f*64))
    for p in range(2):
        for f in range(12):
            if spiders[f+36+(p*12)].live:
                spacespiders.append(alien("front", (f*64)+64, 320-(64*p), f*64))
    fire = [shoot()]
    for g in range(len(space)):
        fire.append(shoot(True,0,0,g))
    return space


blocker(64,576)
blocker(320,576)
blocker(576,576)
blocker(832,576)


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
    
    wedone = True
    for d in range(len(spacespiders)):
        if spacespiders[d].live:
            if random.randrange((1000 + len(spacespiders)) ) == 0:
                fire[d+1 ].pew(12)
        wedone = False
            
    if wedone:
        doexit = True
    
    playerx += vx
    
    if playerx < 0:
        playerx = 0
    elif playerx > 1024:
        playerx = 1024-32
    for j in range(len(spacespiders)):
        spacespiders[j].moove()
    for i in range(len(fire)):
        if fire[i].moving():
            break
    
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
    for i in range(lives):
        screen.blit(heart, (32+(i*48),700))
    for i in range(len(shield)):
        shield[i].rendie()
    for i in range(len(spacespiders)):
        if spacespiders[i].live:
            spacespiders[i].rendish()
    for i in range(len(fire)):
        fire[i].rendong()
    
    print(score)
    pygame.display.flip()#this actually puts the pixel on the screen
#end
pygame.quit()