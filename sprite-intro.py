#credits to Clear Code for the tutorial
import pygame, sys, os

#crosshair class
class Crosshair(pygame.sprite.Sprite): #inherit from pygame.sprite.Sprite
    def __init__(self, path):
        super().__init__()
        
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.pew = pygame.mixer.Sound(os.path.join("art", "pew.wav"))
        self.pew.set_volume(0.2)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        self.pew.play()

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Introduction")

#crosshair stuff
crosshair = Crosshair(os.path.join("art", "crosshair.png"))
crosshair_group = pygame.sprite.Group() #a sprite group, the only way to display sprites
crosshair_group.add(crosshair)

#images
background = pygame.image.load(os.path.join("art", "background.png"))

pygame.mouse.set_visible(False) #hide mouse
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
        
    screen.blit(background, (0,0)) #display background
    crosshair_group.draw(screen) #draw sprites of chair_group
    crosshair_group.update()
    pygame.display.flip()
    clock.tick(60)