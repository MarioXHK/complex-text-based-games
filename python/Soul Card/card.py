import pygame
import random
pygame.init()  
pygame.display.set_caption("a letter")  # sets the window title
screen = pygame.display.set_mode((900, 900))  # creates game screen
screen.fill((250,250,250))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
font = pygame.font.Font('splatoon.ttf', 32) #load font
text0 = font.render("I Love You, but I don't have any hearts available,", True, (250, 100, 100))
text1 = font.render("so instead have these rocks!", True, (250, 100, 100)) #numbers give color
text2 = font.render('Just kidding ;)', True, (250, 0, 0), (200,150,150)) #this one includes background color
#HEEEEEEAAAAAARRRRRRTTTTT
class heart:
    def __init__(self,xpos,ypos,type = "hort"):
        self.xpos = xpos
        self.ypos = ypos
        self.type = type
        self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        if self.type == "rock":
            self.iraq = random.randrange(1,5)
        else:
            self.iraq = 0
        self.images = [pygame.image.load("rock1.png"),pygame.image.load("rock2.png"),pygame.image.load("rock3.png"),pygame.image.load("rock4.png")]
        self.vx = random.randrange(-5,6)
        self.vy = random.randrange(0,20)
    def draw(self):
        if self.type == "hort":
            pygame.draw.circle(screen, (self.color), (self.xpos-20, self.ypos), 20) #top left circle
            pygame.draw.circle(screen, (self.color), (self.xpos+20, self.ypos), 20) #top right circle
            pygame.draw.polygon(screen, (self.color), ((self.xpos-40, self.ypos+5),(self.xpos+39, self.ypos+5), (self.xpos, self.ypos+50))) #triangle to form base
        elif self.type == "rock":
            if self.iraq == 1:
                screen.blit(self.images[0], (self.xpos-32, self.ypos-32))
            elif self.iraq == 2:
                screen.blit(self.images[1], (self.xpos-32, self.ypos-32))
            elif self.iraq == 3:
                screen.blit(self.images[2], (self.xpos-32, self.ypos-32))
            elif self.iraq == 4:
                screen.blit(self.images[3], (self.xpos-32, self.ypos-32))
            else:
                pygame.draw.circle(screen, (150,150,150), (self.xpos, self.ypos), 32)
    def move(self):
        self.vy += 1
        if self.type != "rock":
            self.vy -= 0.5
        self.xpos += self.vx
        self.ypos += self.vy

def typechange(lelist,typing):
    savepos = []
    for i in range(len(lelist)):
        savepos.append((lelist[i].xpos,lelist[i].ypos))
    lelist = []
    for i in range(len(savepos)):
        lelist.append(heart(savepos[i][0],savepos[i][1],typing))
    return lelist
hearts = []
output = input("How many hearts would you like?\n")
for i in range(int(output)):
    hearts.append(heart(random.randrange(0,900),-50,"rock"))
shift=False
shifted = False
cooldown = 0
while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    #INPUT!
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_SPACE:
                shift=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shift=False
    if cooldown <= 0 and shift:
        if hearts[0].type == "rock":
            hearts = typechange(hearts,"hort")
        else:
            hearts = typechange(hearts,"rock")
        cooldown = 100
        shifted = True  
    cooldown -= 1
    #physics
    for i in range(len(hearts)):
        hearts[i].move()
        if hearts[i].ypos > 950:
            temptype = hearts[i].type
            hearts.remove(hearts[i])
            hearts.append(heart(random.randrange(0,900),-50,temptype))
    #RENDER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    screen.fill((250,250,250))
    for i in range(len(hearts)):
        hearts[i].draw()
    screen.blit(text0, (200, 100))
    screen.blit(text1, (200, 200))
    if shifted:
        screen.blit(text2, (400, 300))
    pygame.display.flip()#Done in under 100 lines of code!