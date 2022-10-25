#credits to Clear Code for the tutorial
import pygame, sys, os

#constants and window
WIDTH, HEIGHT = 300,300
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Animation Introduction")
clock = pygame.time.Clock()

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = [] #container for the sprites
        for nr in range(1,11):
            self.sprites.append(pygame.image.load(os.path.join("art", "frog", f"attack_{nr}.png"))) #load all frames
        self.current_sprite = 0
        self.image = pygame.transform.scale2x(self.sprites[self.current_sprite]) #set sprite to initial frame
        self.niom = pygame.mixer.Sound(os.path.join("art", "frog", "niom.wav"))
        self.niom.set_volume(.5) #lower volume to reduce my nightmares

        self.rect = self.image.get_rect(center=(x,y))
        self.is_animating = False

    def update(self, speed): #run animation
        if self.is_animating == True:
            self.current_sprite += speed #.1 instead of 1 to slow down the animation to a decent speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = pygame.transform.scale2x(self.sprites[int(self.current_sprite)])

    def animate(self):
        self.is_animating = True

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

        if event.type == pygame.KEYDOWN: #run animation only on keypress
            player.animate()
            player.niom.play() #niom
    
    pygame.display.flip()
    screen.fill((0,0,0))
    player_group.update(.25) #change frames
    player_group.draw(screen) #draw player
    clock.tick(60)
