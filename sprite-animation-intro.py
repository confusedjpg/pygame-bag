#credits to Clear Code for the tutorial
import pygame, sys

#constants and window
WIDTH, HEIGHT = 800,800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Animation Introduction")
clock = pygame.time.Clock()

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill((155,255,255))
        self.rect = self.image.get_rect(center = (x,y))

#create player and add it to sprite group
player = Player(WIDTH//2, HEIGHT//2)
player_group = pygame.sprite.Group()
player_group.add(player)

#game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    player_group.draw(screen) #draw player
    clock.tick(60)
