import pygame, sys

WIDTH, HEIGHT = 400,400
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input Demo")

user_text = ""

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE: #add possibility to remove text
                user_text = user_text[:-1]
            else:
                user_text += event.unicode #render the pressed keys
    
    screen.fill((0,0,0))
    text_surf = pygame.font.Font(None, 32).render(user_text, True, (255,255,255))
    screen.blit(text_surf, (0,0))
    pygame.display.flip()
    clock.tick(60)