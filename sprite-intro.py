#credits to Clear Code for the tutorial
import pygame, sys

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 900,900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Introduction")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.flip()
    clock.tick(60)