# supposed to display an image as pixelated that gets "enhanced" every time you click
# slow with bigger images, for loop moment
import pygame, sys
from PIL import Image

WIDTH, HEIGHT, TILESIZE = 0,0,0

def display(path, pixelSize=101):
    img = Image.open(path)
    WIDTH, HEIGHT, TILESIZE = img.width, img.height, pixelSize
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Image Drawing")

    class Tile(pygame.sprite.Sprite):
        def __init__(self, x, y, color):
            super().__init__()
            self.color = color
            self.image = pygame.Surface((TILESIZE,TILESIZE))
            self.image.fill(color)
            self.rect = self.image.get_rect(topleft=(x,y))

        def changeColor(self, color):
            self.image.fill(color, self.image.get_rect().inflate(-1,-1))
            self.color = color

    tiles = pygame.sprite.Group()
    for indY in range(0,HEIGHT,TILESIZE):
        for indX in range(0,WIDTH,TILESIZE):
            tiles.add(Tile(indX,indY,img.getpixel((indX, indY))))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN: # click to "enhance" the image
                TILESIZE -= 10
                tiles.empty()
                tiles = pygame.sprite.Group()
                for indY in range(0,HEIGHT,TILESIZE): # cursed nested for loop
                    for indX in range(0,WIDTH,TILESIZE):
                        tiles.add(Tile(indX,indY,img.getpixel((indX, indY))))


        tiles.draw(screen)
        pygame.display.flip()
        clock.tick(60)
