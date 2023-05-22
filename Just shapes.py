import pygame #bring in pygame library
pygame.init #initialize pygame

screen = pygame.display.set_mode((800, 800)) #create game screen
pygame.display.set_caption("A lovely House!") #window title

pygame.draw.rect(screen, (200, 0, 200), (200, 400, 300, 300))
pygame.draw.circle(screen, (200, 200, 0), (100, 100), 50)
pygame.draw.polygon(screen, (0, 200, 200), ((200, 200), (500, 200), (400, 100)))

pygame.display.flip() #update graphics 
