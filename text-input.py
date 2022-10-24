import pygame, sys

WIDTH, HEIGHT = 600,600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input Demo")

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)