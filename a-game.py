# a simple game

import pygame, sys, random as rd
pygame.init()

#window setup
screenX, screenY = 900, 700
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("omnomnom.")

#score related
font = pygame.font.Font(None, 45)

#message related
msg = pygame.font.Font(None, 50)
msgFont = msg.render("", True, "#bbffbb")
msgRect = msgFont.get_rect()

#fps related
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite): #player main class
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((40,40))
        self.surf.fill("#ff5555")
        self.rect = self.surf.get_rect()
        self.speed = 5
        self.score = 0

    def move(self, directions):
        if directions[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        if directions[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if directions[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if directions[pygame.K_DOWN]:
            self.rect.move_ip(0,5)

class Food(pygame.sprite.Sprite): #food main class
    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill("#ff8833")
        self.rect = self.surf.get_rect()
        self.rect.center = (rd.randint(20, screenX-20), rd.randint(20, screenY-20))
        self.showMsg = False
        self.msgPosition = (screenX//2, 50)
        self.msgText = ""

    def move(self, p):
        self.msgPosition = (screenX//2, 50)
        self.msgText = rd.choice(["Awesome!", "Perfect!", "Good job!", "Great!", "Well done!"])
        p.score += 1
        while p.rect.colliderect(self.rect):
            self.rect.center = (rd.randint(50, screenX-50), rd.randint(50, screenY-50))
        print(self.rect.center, p.score)
        self.showMsg = True
        self.counter = 30

player = Player()
borgir = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    directions = pygame.key.get_pressed()
    
    player.move(directions)
    if player.rect.colliderect(borgir.rect):
        borgir.move(player)
    
    screen.fill('black')
    screen.blit(player.surf, player.rect)
    screen.blit(borgir.surf, borgir.rect)
    scoreFont = font.render(str(player.score), True, "#999999")
    scoreRect = scoreFont.get_rect(center=(player.rect.center))
    screen.blit(scoreFont, scoreRect)
    msgFont = msg.render(borgir.msgText, True, "#bbffbb")
    msgRect = msgFont.get_rect(center=borgir.msgPosition)
    if borgir.showMsg:
        borgir.counter -= 1
        if borgir.counter > 0:
            screen.blit(msgFont, msgRect)
            print(borgir.counter)
        else:
            borgir.showMsg = False
    pygame.display.flip()
    clock.tick(60)