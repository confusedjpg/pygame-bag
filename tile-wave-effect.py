import pygame, sys, random as rd

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT, TILESIZE = 500,500,20 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tile Wave Effect")

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, outline="black"):
        super().__init__()
        self.color = color
        self.outline = outline
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(outline)
        self.image.fill(color, self.image.get_rect().inflate(-1,-1))
        self.rect = self.image.get_rect(topleft=(x,y))

    def changeColor(self, color):
        self.image.fill(color, self.image.get_rect().inflate(-1,-1))
        self.color = color

tiles = pygame.sprite.Group()
for indY in range(0,HEIGHT,TILESIZE):
    for indX in range(0,WIDTH,TILESIZE):
        tiles.add(Tile(indX,indY,"white"))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in tiles.sprites():
                if tile.rect.collidepoint(pygame.mouse.get_pos()):
                    tile.changeColor("red")
                    break

    tiles.draw(screen)
    pygame.display.flip()
    clock.tick()
#not finished
