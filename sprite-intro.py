#credits to Clear Code for the tutorial
import pygame, sys

class Crosshair(pygame.sprite.Sprite): #inherit from pygame.sprite.Sprite
    def __init__(self, width, height, x, y, color):
        super().__init__()
        
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x,y))

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 900,800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Introduction")

crosshair = Crosshair(40,40,WIDTH//2, HEIGHT//2, (155,255,255))
chair_group = pygame.sprite.Group() #a sprite group, the only way to display sprites
chair_group.add(crosshair)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    chair_group.draw(screen) #draw sprites of chair_group
    pygame.display.flip()
    clock.tick(60)