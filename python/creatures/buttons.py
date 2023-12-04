import pygame
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

class button:
    def __init__(self,color,rectangle,text,textcolor = (0,0,0)):
        print("hi")
        self.color = color
        self.box = rectangle
        self.text = font.render(str(text), 1, textcolor)
        self.clicked = False
    def tick(self,mdown,mousePos) -> bool:
        if mousePos[0] >= self.box[0] and mousePos[0] <= self.box[0]+self.box[2] and mousePos[1] >= self.box[1] and mousePos[1] <= self.box[1]+self.box[3] and mdown:
            return True
        return False

    def render(self,screen: pygame.surface):
        pygame.draw.rect(screen,self.color,self.box)