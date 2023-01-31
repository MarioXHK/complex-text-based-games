import pygame
from math import sin #this is so we don't have to say "math." in front of sin()

pygame.init()

gamescreen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Wave Beam")
clocky = pygame.time.Clock()
PlayingGame = True #variable used to quit game loop

#player position
xpos = 50
ypos = 75
#player speed
vx = 0
vy = 0
#variables to control wave beam
beam = False
beamx = [0,0,0,0,0,0]
beamy = [0,0,0,0,0,0]
angle = [0,0,0,0,0,0]
A = [20,70,20,20,20,10]
B = [.2,.2,.5,.2,.2,1]
C = [0,0,0,5,0,10]
D = [0,0,0,0,10,-10]

#ship image load
ship = pygame.image.load("ship.png") #artwork credit: Mr. Mo
shipRect = ship.get_rect(topleft = (xpos, ypos))

#BEGIN GAME LOOP#################################################################
while PlayingGame:
  
  clocky.tick(60)
  
  events = pygame.event.get()
 
  for event in events:
    if event.type == pygame.QUIT:
      PlayingGame = False
      
  keys = pygame.key.get_pressed()
      
        
  if keys[pygame.K_LEFT]:
      vx=-5
  elif keys[pygame.K_RIGHT]:
      vx=5
  else:
      vx = 0

  if keys[pygame.K_DOWN]:
      vy =5
  elif keys[pygame.K_UP]:
      vy=-5
  else:
      vy=0

  #fire wave beam
  if keys[pygame.K_SPACE]:
      beam = True
  else:
      beam = False
        
  #PHYSICS SECTION-------------------------------------------------------------
  if beam is True:
      for i in range(len(angle)):
          angle[i]+=1 #rotate angle
          beamx[i] = xpos+angle[i]*5 #this handles how fast the beam moves to the right
          beamy[i] = A[i]*sin(B[i]*(angle[i]-C[i]))+D[i] #this handles the shape and size of the wave
  else:
      angle = [0,0,0,0,0,0]
        
  #update player position by adding velocity to position      
  xpos += vx
  ypos += vy
  shipRect = ship.get_rect(topleft = (xpos, ypos))
  
  
  #RENDER SECTION-------------------------------------------------------------      
  #gamescreen.fill((0,0,0))

  #draw spaceship
  gamescreen.blit(ship, shipRect)
  
  #draw beam when fired
  if beam is True:
      pygame.draw.circle(gamescreen, (200, 0, 100), (beamx[0]+10, beamy[0]+ypos+20), 5)
      pygame.draw.circle(gamescreen, (200, 200, 0), (beamx[1]+10, beamy[1]+ypos+20), 5)
      pygame.draw.circle(gamescreen, (0, 200, 0), (beamx[2]+10, beamy[2]+ypos+20), 5)
      pygame.draw.circle(gamescreen, (0, 100, 200), (beamx[3]+10, beamy[3]+ypos+20), 5)
      pygame.draw.circle(gamescreen, (100, 0, 200), (beamx[4]+10, beamy[4]+ypos+20), 5)
      pygame.draw.circle(gamescreen, (200, 100, 0), (beamx[5]+10, beamy[5]+ypos+20), 5)
      
  pygame.display.flip()




  #END GAME LOOP#################################################################
pygame.quit()
        