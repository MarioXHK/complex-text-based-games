import pygame
import Mapgen
from Player import player
from Things import entity
from Collision import thing
import Maps
import random
#set up pygame stuff
pygame.init()  
pygame.display.set_caption("Pizzalike Platformer")  # sets the window title
screenH = 1000
screenV = 600
SHH = screenH/2
SHV = screenV/2
screen = pygame.display.set_mode((screenH, screenV))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock()#set up clock


ms = Maps.getmapsize(0)
print(ms)


#Function to check if something is in view. If it isn't, it'll return false
def checkifoff(ent,off,SH,SV):
    return ent.x >= off[0]-100 and ent.y >= off[1]-100 and ent.x <= off[0]+(SH+100) and ent.y <= off[1]+(SV+100)



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

ground = pygame.image.load('tilesets/ground.png')
ground = pygame.transform.scale(ground, (400,400))
players = [player(640,1440,"w")]#THe player you play as
p1dom = 1 #How much player 1 has dominance over scrolling
zoom = 1
zoomy = 1
maxdis = 600 #Max distance a player is allowed to be away from the other before they get pulled
mapID = 0
map = Maps.getmap(mapID, False)
print(Mapgen.scanspawn(Maps.getmap(mapID),9))

enemies = [entity(760, 1300,"cheese"),entity(560, 1300,"slime"),entity(720, 1080,"cherry"),entity(4280, 1480,"cheese"),entity(4280, 1480,"cherry"),entity(4180, 1480,"cherry"),entity(4080, 1480,"cherry"),entity(3980, 1480,"cherry"),entity(3880, 1480,"cherry")]
for a in range(100):
    enemies.append(entity(random.randint(500,4000), 1300,"cherry"))
for a in range(200):
    enemies.append(entity(random.randint(500,4000), 1400,"slime"))
for a in range(400):
    enemies.append(entity(random.randint(500,4000), 1000,"cheese"))
for o in range(len(players)-1):
    keys.append(keys[0])
for i in range(len(players)):
    players[i].getmap(map)
for i in range(len(enemies)):
    enemies[i].getmap(map)
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
        if players[i].y > ms[1]:
            players[i].repos(640,1440)
        players[i].retick()
    uhm = 0
    for i in range(len(enemies)):
        g = i-uhm
        if checkifoff(enemies[g],offset,screenH,screenV) or enemies[g].flang:
            enemies[g].move()
            for j in range(len(players)):
                if thing.objcollision(players[j].getinf(),enemies[g].getinf(),0) and players[j].pound and not enemies[g].flang:
                    enemies[g].fling(int(players[j].speed()),players[j].getdir())
        if enemies[g].y > ms[1]:
            del enemies[g]
            uhm += 1

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
    if average[0] > SHH*(1/zoom) and average[0] < len(map[0])*40-(SHH*(1/zoom)):
        offset[0] = (average[0] - SHH)*zoom+(SHH*(zoom-1))
    elif average[0] > SHH*(1/zoom):
        offset[0] = ((len(map[0])*40-(SHH*(1/zoom)))*zoom+(SHH*zoom*-1))-(SHH*(1-zoom))
    else:
        offset[0] = 0
    
    
    if average[1] > SHV*(1/zoom) and average[1] < len(map)*40-(SHV*(1/zoom)):
        offset[1] = (average[1] - SHV)*zoom+(SHV*(zoom-1))
    elif average[1] > SHV*(1/zoom):
        offset[1] = ((len(map)*40-(SHV*(1/zoom)))*zoom+(SHV*zoom*-1))-(SHV*(1-zoom))
    else:
        offset[1] = 0
    #ZOOMING?!?!?!?!? Is that even possible?
    
    zoom = 1
    if dozooming:
        maxdis = 900
        if len(players) > 1:
            for i in range(len(players)-1):
                if pdisx[i] > SHH or pdisy[i] > SHV:
                    if pdisx[i] > pdisy[i]:
                        zoom = 1.5-pdisx[i]/screenH
                    else:
                        zoom = 1.5-pdisy[i]/screenV
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
    for i in range(len(enemies)):
        if checkifoff(enemies[i],offset,screenH,screenV):
            enemies[i].draw(screen,offset,zoom)
    if debug:
        pygame.draw.circle(screen,(255,0,0),(SHH,SHV),20)
    pygame.display.flip()