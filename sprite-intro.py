#credits to Clear Code for the tutorial
import pygame, sys, os, random as rd

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1000,800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Introduction")

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
        pygame.sprite.spritecollide(crosshair, target_group, True)
        self.pew.play()

class Target(Crosshair): #target class, inherits from Crosshair
    def __init__(self, x, y, path):
        super().__init__(path)
        self.rect.center = (x, y)

class GameState():
    def __init__(self):
        self.state = "intro"

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
        
        screen.blit(ready, (WIDTH/2-ready.get_width()/2, HEIGHT/2-ready.get_height()/2))
    
    def main_game(self):
        target_group.draw(screen)
        

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        else:
            self.main_game()

game_state = GameState()

#crosshair stuff
crosshair = Crosshair(os.path.join("art", "crosshair.png"))
crosshair_group = pygame.sprite.Group() #a sprite group, the only way to display sprites
crosshair_group.add(crosshair)

#target stuff
target_group = pygame.sprite.Group()
for target in range(30):
    target = Target(rd.randrange(0,WIDTH), rd.randrange(0,HEIGHT), os.path.join("art", "target.png"))
    while pygame.sprite.spritecollideany(target, target_group):
        target = Target(rd.randrange(0,WIDTH), rd.randrange(0,HEIGHT), os.path.join("art", "target.png"))
    target_group.add(target)

#images
background = pygame.image.load(os.path.join("art", "background.png"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

ready = pygame.image.load(os.path.join("art", "ready.png"))

pygame.mouse.set_visible(False) #hide mouse
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    screen.blit(background, (0,0)) #display background
    game_state.state_manager()
    crosshair_group.update() #update crosshair
    crosshair_group.draw(screen) #draw sprites of chair_group
    pygame.display.flip()
    clock.tick(60)