import pygame
import random
import time
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
speedog = speedto
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
alienbonus = [pygame.image.load("bonus0.png"),pygame.image.load("bonus1.png"),pygame.image.load("bonus2.png")]
instructions = pygame.image.load("instructions.png")
boss = pygame.image.load("boss.png")
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
        if self.type == "boss":
            self.health = 30
        else:
            self.health = 1
    def moove(self):
        global speedto
        global doExit
        if not self.live:
            return
        self.vxtimer += 1
        if self.type == "bonus":
            if self.left:
                self.xpos -= self.speed
                if self.xpos < -32:
                    return True
                else:
                    return False
            else:
                self.xpos += self.speed
                if self.xpos > 1060:
                    return True
                else:
                    return False
        else:
            if self.vxtimer >= speedto:
                self.vxtimer = 0
                minx = 32
                maxx = 160
                if self.type == "boss":
                    minx = 0
                    maxx = 512
                if (self.xpos <= minx + self.xoffset or self.xpos >= maxx + self.xoffset):
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
        if self.ypos > 700:
            doExit = True
    def rendish(self):
        if self.type == "bonus":
            screen.blit(alienbonus[0], (self.xpos-32,self.ypos))
            return
        elif self.type == "boss":
            screen.blit(boss, (self.xpos,self.ypos))
            return
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
extra = alien("bonus", -64, 32, 0, 4)
extraonscreen = False

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
            if self.enemy:
                pygame.mixer.Sound.play(pewpew)
    def moving(self):
        self.cooldownyouidot -= 1
        global spacespiders
        global playerx
        global playery
        global speedto
        global shield
        global lives
        global score
        global extra
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
                if shield[i].health <= 0:
                    pygame.mixer.Sound.play(bwab)
                else:
                    pygame.mixer.Sound.play(brbr)
                self.power = 0
                if not self.enemy:
                    self.xpos = playerx + 14
                    self.ypos = playery - 16
            
            
        
        if self.enemy:#The script that tells who to murder
            if playery < self.ypos + 32 and playery > self.ypos and self.xpos + 8 > playerx and self.xpos < playerx + 32 and self.cooldownyouidot <= 0 and lives > -1:
                playerx = 512
                lives -= 1
                self.cooldownyouidot = 100
                self.power = 0
                pygame.mixer.Sound.play(blug)
                if lives == -1:
                    pygame.mixer.Sound.play(voice[2])
                    time.sleep(3)
                    speedto = 2
                    
                return True
            if (self.xpos >= playerx and self.xpos <= playerx + 32) and self.ypos >= playery:
                self.ypos = 1000
            if self.ypos > 768:
                self.power = 0
        else:
            for i in range(len(spacespiders)):
                if spacespiders[i].type == "boss":
                    if spacespiders[i].ypos < self.ypos + 32 and spacespiders[i].ypos+192 > self.ypos and self.xpos + 4 > spacespiders[i].xpos and self.xpos < spacespiders[i].xpos + 512 and self.ypos < playery and spacespiders[i].live == True:
                        spacespiders[i].health -= 1
                        if spacespiders[i].health <= 0:
                            spacespiders[i].live = False
                            score += 1000
                        pygame.mixer.Sound.play(boom[random.randrange(0,2)])
                        self.power = 0
                        self.xpos = playerx + 14
                        self.ypos = playery - 16
                else:
                    if spacespiders[i].ypos < self.ypos + 32 and spacespiders[i].ypos > self.ypos and self.xpos + 4 > spacespiders[i].xpos and self.xpos < spacespiders[i].xpos + 32 and self.ypos < playery and spacespiders[i].live == True:
                        pygame.mixer.Sound.play(boom[random.randrange(0,2)])
                        spacespiders[i].health -= 1
                        if spacespiders[i].health <= 0:
                            spacespiders[i].live = False
                            if spacespiders[i].type == "front":
                                score += 10
                            elif spacespiders[i].type == "middle":
                                score += 20
                            elif spacespiders[i].type == "back":
                                score += 40
                        self.power = 0
                        self.xpos = playerx + 14
                        self.ypos = playery - 16
                if extra.ypos < self.ypos + 32 and extra.ypos > self.ypos and self.xpos + 4 > extra.xpos-32 and self.xpos < extra.xpos + 32 and self.ypos < playery and extra.live == True:
                    extra.live = False
                    pygame.mixer.Sound.play(boom[random.randrange(0,2)])
                    pygame.mixer.Sound.play(cough)
                    self.power = 0
                    score += random.randrange(1,11)*100
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

def respawn(spiders):#Completely useless function as of now as I've learned that the aliens don't even reset their positions when you die
    space = []
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
    lava = [shoot()]
    for g in range(len(space)):
        lava.append(shoot(True,0,0,g))
    return [space,lava]
def restart(level):
    invaders = []
    bosss = False
    if level % 10 == 0:
        for i in range(3):
            pygame.mixer.Sound.play(warning)
            time.sleep(1)
        bosss = True
    if bosss:
        invaders.append(alien("boss", 0, 0, 0))
    else:
        for f in range(12):
            invaders.append(alien("back", (f*64)+64, 64, f*64))
        for p in range(2):
            for f in range(12):
                invaders.append(alien("middle", (f*64)+64, 192-(64*p), f*64))
        for p in range(2):
            for f in range(12):
                invaders.append(alien("front", (f*64)+64, 320-(64*p), f*64))
    return invaders


dothe = False
howdy = 0
def debugprint(thing):
    print(thing)
    return thing
blocker(64,576)
blocker(320,576)
blocker(576,576)
blocker(832,576)
#Sounds
pewpew = pygame.mixer.Sound('pew.mp3')#load in sound effect
boop1 = pygame.mixer.Sound('boop1.mp3')
boop2 = pygame.mixer.Sound('boop2.mp3')
boop3 = pygame.mixer.Sound('boop3.mp3')
boop4 = pygame.mixer.Sound('boop4.mp3')
boom = [pygame.mixer.Sound('boom0.mp3'),pygame.mixer.Sound('boom1.mp3')]
bwab = pygame.mixer.Sound('bwab.mp3')
blug = pygame.mixer.Sound('blug.mp3')
brbr = pygame.mixer.Sound('brbrbrbrb.mp3')
cough = pygame.mixer.Sound('cough.mp3')
oooo = [pygame.mixer.Sound('oooo0.mp3'),pygame.mixer.Sound('oooo1.mp3'),pygame.mixer.Sound('oooo2.mp3'),pygame.mixer.Sound('oooo3.mp3'),pygame.mixer.Sound('oooo4.mp3'),pygame.mixer.Sound('oooo5.mp3'),pygame.mixer.Sound('oooo6.mp3'),pygame.mixer.Sound('oooo7.mp3')]
voice = [pygame.mixer.Sound('killu.mp3'),pygame.mixer.Sound('rekill.mp3'),pygame.mixer.Sound('uded.mp3')]
warning = pygame.mixer.Sound('warning.mp3')
bossmusic = pygame.mixer.music.load('hosthoedown.mp3')

debug = True
dekey = [False]
#gaem loop
didyougetit = False
print("Press any button to continue")
while not didyougetit:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT:
            doExit = True
            didyougetit = doExit
        #inpoot
        
        if event.type == pygame.KEYDOWN: #keyboard input
            didyougetit = True
    clock.tick(10)
    
    
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    screen.blit(instructions, (0,0))
    pygame.display.flip()
gamestart = True
gamerest = False
pygame.mixer.music.play(-1)
#GAME loop (for realzies)
while not doExit:
    for event in pygame.event.get(): #2b- i mean event queue
        if event.type == pygame.QUIT:
            doExit = True;
        
        #inpoot-------------------------------------------------------
        
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0]=True
            elif event.key == pygame.K_RIGHT:
                keys[1]=True
            elif event.key == pygame.K_SPACE:
                keys[2]=True
            if event.key == pygame.K_k and debug:
                dekey[0]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0]=False
            elif event.key == pygame.K_RIGHT:
                keys[1]=False
            elif event.key == pygame.K_SPACE:
                keys[2]=False
            if event.key == pygame.K_k and debug:
                dekey[0]=False
    clock.tick(30)
    #U can't do anything once ur ded
    if lives <= -1:
        keys = [False, False, False]
    
    if keys[0]:
        vx = -6
    elif keys[1]:
        vx = 6
    else:
        vx = 0
    if keys[2]:
        if fire[0].power == 0 and fire[0].ypos > 0:
            pygame.mixer.Sound.play(pewpew)
        fire[0].pew(20)
    if dekey[0]:
        for g in range(len(spacespiders)):
            spacespiders[g].live = False
    #functional stufff???????????????????????????????????????STUFF I DON'T KNOW THE NAME OF!
    wedone = True
    for d in range(len(spacespiders)):
        if spacespiders[d].live:
            if spacespiders[d].type == "boss":
                if random.randrange(100) == 0:
                    fire[d+1].xpos = spacespiders[d].xpos + random.randrange(256)
                    fire[d+1 ].pew(12)
            else:
                if random.randrange((1000 + len(spacespiders)) ) == 0:
                    fire[d+1 ].pew(12)
            wedone = False
        
            
    if wedone:
        gamerest = True
        if not debug:
            time.sleep(2)
        if speedog > 10:
            speedog -= 2
        speedto = speedog
        playerx = 512
        spacespiders = restart(speedog)
        fire = [shoot()]
        if spacespiders[0].type == "boss":
            for g in range(len(spacespiders)):
                fire.append(shoot(True,0,0,0))
        else:
            for g in range(len(spacespiders)):
                fire.append(shoot(True,0,0,g))
    
    
    if not extraonscreen:
        if random.randrange(0,1000) == 0:
            extraonscreen = True
            pygame.mixer.Sound.play(oooo[random.randrange(0,8)])
            extra.live = True
            if random.randrange(0,2) == 0:
                extra.left = True
                extra.xpos = 1060
            else:
                extra.left = False
                extra.xpos = -32
    if not extra.live:
        extraonscreen = False
    
    if speedog % 10 != 0 or speedog == 40:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    #moving stuffff-==-=--==-=-=-= ???????????????!!!!!!!!!!!!!!!!!!!!!!!!!!
    if extraonscreen:
        if extra.moove():
            extraonscreen = False
    
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
    hi = 0
    for i in range(len(spacespiders)):#I'm not orginized in code at all
        if spacespiders[i].live:
            hi = i
            if dothe != spacespiders[i].frame:
                dothe = spacespiders[hi].frame
                howdy += 1
                if howdy > 3:
                    howdy = 0
                if howdy == 0:
                    pygame.mixer.Sound.play(boop1)
                elif howdy == 1:
                    pygame.mixer.Sound.play(boop2)
                elif howdy == 2:
                    pygame.mixer.Sound.play(boop3)
                else:
                    pygame.mixer.Sound.play(boop4)
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
    if not gamestart and lives > -1:
        screen.blit(defender, (playerx,playery))
    for i in range(lives):
        screen.blit(heart, (32+(i*48),700))
    
    
    for i in range(len(shield)):
        shield[i].rendie()
    
    
    for i in range(len(spacespiders)):
        if spacespiders[i].live:
            spacespiders[i].rendish()
    
    if extraonscreen:
        extra.rendish()
    
    for i in range(len(fire)):
        fire[i].rendong()
    
    print(score)
    pygame.display.flip()#this actually puts the pixel on the screen
    if gamestart:
        pygame.mixer.Sound.play(voice[0])
        if not debug:
            time.sleep(2)
        gamestart = False
    if gamerest:
        pygame.mixer.Sound.play(voice[1])
        if not debug:
            time.sleep(2)
        gamerest = False
        
#end
pygame.quit()