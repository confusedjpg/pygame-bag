#code provided by Pete Shinners on pygame.org
#simplest ball bouncing animation there is

import sys, pygame, os
pygame.init()

size = width, height = 400,400
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load(os.path.join("art", "target.png"))
ballrect = ball.get_rect(center = (150,265)) #random center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed) #i didn't see this method in any tutorial...why? it's very cool
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()