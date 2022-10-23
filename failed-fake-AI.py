# this project was my take at making a bot that would try to learn to find its way towards food, like an AI basically
# except i have no actual knowledge of how to make or train an AI so it's something way worse
# i abandoned the project since i know i wouldn't have achieved anything, but at least i had fun and learned some new stuff

# so here's an unfinished project
# it has a working timer, displayed score, a "player" that can move and "eat food"
# it can store places where it shouldn't go and detect them later with some rays

import pygame, sys, random as rd, math

pygame.init()

WIDTH, HEIGHT = 800,800 #window initialize
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("'AI Learning'...kind of :)))")

#score related
font = pygame.font.Font(None, 45)

#timer related
timerFont = pygame.font.Font(None, 50)


class AI(pygame.sprite.Sprite): #player main class
    def __init__(self):
        super(AI, self).__init__()
        self.surf = pygame.Surface((40,40))
        self.surf.fill("#ff5555")
        self.rect = self.surf.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 5
        self.score = 0
        self.badPlaces = []
        self.vision = []

    def move(self, directions):
        if directions[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed,0)
        if directions[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed,0)
        if directions[pygame.K_UP]:
            self.rect.move_ip(0,-self.speed)
        if directions[pygame.K_DOWN]:
            self.rect.move_ip(0,self.speed)
    
    def back(self, change, becauseTimer = False):
        print(self.rect.center)
        if not becauseTimer:
            if change < 0:
                self.badPlaces.append(pygame.Rect(self.rect.center[0], self.rect.center[1], 10,10))
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.score += change
        global staticTime
        staticTime = pygame.time.get_ticks()
        print(self.badPlaces)


class Food(pygame.sprite.Sprite): #food main class
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill("#ff8833")
        self.rect = self.surf.get_rect(center=(rd.randint(20, WIDTH-20), rd.randint(20, HEIGHT-20)))

    def move(self, p):
        while p.rect.colliderect(self.rect):
            self.rect.center = (rd.randint(50, WIDTH-50), rd.randint(50, HEIGHT-50))


child = AI()
borgir = Food()

clock = pygame.time.Clock()

currentTime = 0
staticTime = 0
timer = 10000

gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #handle exit
            pygame.quit()
            sys.exit()

    currentTime = pygame.time.get_ticks()
    #print(currentTime, staticTime, (timer-(currentTime - staticTime))//1000)

    if currentTime - staticTime > timer:
        child.back(-10, True)

    directions = pygame.key.get_pressed()
    
    child.move(directions)

    if child.rect.colliderect(borgir.rect): #player and food collide?
        borgir.move(child)
        child.back(10)

    if not (0 <= child.rect.center[0] <= WIDTH) or not (0 <= child.rect.center[1] <= HEIGHT):
        child.back(-10)
    
    screen.fill('black')
    lines = []
    for deg in range(360):
        if deg % 20 == 0:
            lines.append(pygame.draw.line(screen, "#55ff55", child.rect.center, (child.rect.center[0]+50*math.cos(math.radians(deg)), child.rect.center[1]+50*math.sin(math.radians(deg))), 2))
    
    for place in child.badPlaces:
        for line in lines:
            if line.colliderect(place):
                child.speed = -child.speed

    screen.blit(child.surf, child.rect)
    screen.blit(borgir.surf, borgir.rect)

    scoreFont = font.render(str(child.score), True, "#999999") #score related
    scoreRect = scoreFont.get_rect(center=(child.rect.center))
    screen.blit(scoreFont, scoreRect)

    timerSurf = timerFont.render(str((timer-(currentTime-staticTime))//1000), True, "#bbffbb")
    timerRect = timerSurf.get_rect(center=(WIDTH//2, 40))
    screen.blit(timerSurf, timerRect)

    pygame.display.flip() #update window
    clock.tick(60) #set fixed framerate