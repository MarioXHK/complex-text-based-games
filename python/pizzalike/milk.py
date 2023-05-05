import pygame
import Mapgen
from math import sqrt
from Player import player
from Things import entity
import Maps
#set up pygame stuff
pygame.init()  
pygame.display.set_caption("Pizzalike Platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock()#set up clock




    


#Setting up the classes



#Some fun ctions

def smooth(inn, target, tipe, positive = True, speed = 0.1):
    if (inn > target and positive) or (inn < target and not positive):
        return inn
    if tipe == "line":
        return inn + speed

#SETTING UP THE VARIABLES!
keys = [[False,False,False,False,False,False,False]]#For input
gaming = True#Alright, we're gaming
debug = False
offset = [0,0]
dozooming = False #if true, zooming will be enabled
#MAP: 1 is grass, 2 is brick

ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, (400,400))
players = [player(320,1380,"w")]#THe player you play as
p1dom = 1 #How much player 1 has dominance over scrolling
zoom = 1
zoomy = 1
maxdis = 600 #Max distance a player is allowed to be away from the other before they get pulled
mapID = 0
map = Maps.getmap(mapID)
print(Mapgen.scanspawn(Maps.getmap(mapID),9))
enemies = []
for o in range(len(players)-1):
    keys.append(keys[0])
for i in range(len(players)):
    players[i].getmap(map)
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
        if keys[i][6]:
            players[i].punch(keys[i][0],keys[i][1],keys[i][2],keys[i][3])
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
            if dozooming:
                if map[i][j][0]==2:
                    pygame.draw.rect(screen, (120, 67, 10), (myx,myy, 40*zoom, 40*zoom))
                if map[i][j][0]==2:
                    pygame.draw.rect(screen, (181, 58, 31), (myx,myy, 40*zoom, 40*zoom))
                if map[i][j][0]==3:
                    pygame.draw.rect(screen, (255, 255, 255), (myx,myy, 40*zoom, 5*zoom))
                if map[i][j][0]==5:
                    pygame.draw.rect(screen, (0, 0, 0), (myx,myy, 40*zoom, 5*zoom))
            else:
                if map[i][j][0] != 0:
                    if map[i][j][0] in {2,4}:
                        screen.blit(ground, (myx, myy), (map[i][j][5][0]*40, (map[i][j][5][1]+5)*40, 40, 40))
                    else:
                        screen.blit(ground, (myx, myy), (map[i][j][5][0]*40, map[i][j][5][1]*40, 40, 40))
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
        players[k].draw(screen,offset,zoom)
    pygame.display.flip()