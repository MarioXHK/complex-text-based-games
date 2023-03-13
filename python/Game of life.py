import pygame
import random

pygame.init()
pygame.display.set_caption("Someone's game of life!")
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
"""
map = [[1,0,0,1,1,0,0,1],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [1,0,0,1,1,0,0,1],
       [1,0,0,1,1,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [1,0,0,1,1,0,0,1]]
"""

map = [[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,1,1,0,0,0],
       [0,0,0,1,1,0,0,0],
       [0,0,0,1,1,0,0,0],
       [0,0,0,1,1,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]

mxs = 800/len(map[0])
mys = 800/len(map)
frame = False
doExit = True
while doExit:
    clock.tick(1)
    event = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = False;
    pygame.time.wait(200)
    #Update-------------------------------------------------------
    oldmap = map
    if frame:
        for i in range(len(map)):
            for j in range(len(map[0])):
                counter = 0
                for k in range(-1,2):
                    for l in range(-1,2):
                        oof = True
                        ik=i+k
                        jl=j+l
                        if ik == i and jl == j:
                            oof == False
                        if ik > len(map)-1:
                            ik = 0
                        elif ik < 0:
                            ik = len(map)-1
                        if jl > len(map[0])-1:
                            jl = 0
                        elif jl < 0:
                            jl = len(map[0])-1
                        if oldmap[ik][jl] == 1 and oof:
                            counter +=1
                if oldmap[i][j]==1 and (counter == 2 or counter == 3):
                    map[i][j]=1
                if oldmap[i][j]==1 and (counter < 2 or counter > 3):
                    map[i][j]=0
                if oldmap[i][j]==0 and counter == 3:
                    map[i][j]=1
    frame = True
    #Render----------------------------------------
    screen.fill((0,0,0))
    
    for i in range (len(map)):
        for j in range (len(map[0])):
            if map[i][j]==0:
                pygame.draw.rect(screen, (0,0,0), (j*mxs, i*mys, mxs, mys))
                pygame.draw.rect(screen, (255,255,255), (j*mxs, i*mys, mxs, mys),1)
            if map[i][j]==1:
                pygame.draw.rect(screen, (0,200,200), (j*mxs, i*mys, mxs, mys))
    pygame.display.flip()
    
    
pygame.quit()
