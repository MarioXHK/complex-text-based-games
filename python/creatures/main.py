import pygame
from buttons import button
from interest import creature
from interest import move

pygame.init()  
pygame.display.set_caption("Animals Fighting")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))
screen.fill((0,0,0))
clock = pygame.time.Clock()

#mouse variables--------------------------------
mousePos = (0,0)
fire = False
tap = True

tackle = move(40,("paper","normal"))
testers = [creature(0,5),creature(1,5),creature(2,5)]

attackButton = button((0,200,0),(50,700,200,200),"Test",(0,0,0))



testers[0].printInfo()
#testers[1].printInfo()
#testers[2].printInfo()

testers[0].printBattleInfo()


testers[1].printBattleInfo()

surviving = True
while surviving:
    #The input you have
    for event in pygame.event.get(): #Event queue
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            surviving = False
        if event.type == pygame.MOUSEBUTTONDOWN and tap:
            fire = True
            tap = False
        if event.type == pygame.MOUSEBUTTONUP:
            tap = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    clock.tick(60)
    
    if attackButton.tick(fire,mousePos):
        testers[1].tempstats[0] -= testers[0].attack(testers[1],tackle)
        testers[1].printBattleInfo()
    
    #Rendering is what I do!
    screen.fill((2,20,200))
    


    attackButton.render(screen)
    pygame.display.flip()
    fire = False
pygame.quit()