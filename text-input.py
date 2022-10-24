import pygame, sys

WIDTH, HEIGHT = 400,400
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Input Demo")

user_text = ""

input_rect = pygame.Rect(100,100,140,32) #create rect
color_active = (150,255,255)
color_passive = (50,50,50)
active = False

clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            active = True if input_rect.collidepoint(event.pos) else False #focused or not

        if event.type == pygame.KEYDOWN:
            if active: #only if the textbox is focused
                if event.key == pygame.K_BACKSPACE: #add possibility to remove text
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode #render the pressed keys
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, color_active if active else color_passive, input_rect, 2) #draw the rect, the 2 is for an outline
    text_surf = pygame.font.Font(None, 32).render(user_text+"|" if active else user_text, True, (255,255,255))

    input_rect.w = max(100, text_surf.get_width()+10) #change rect width accordingly, 100 is the minimum width
    screen.blit(text_surf, (input_rect.x+5, input_rect.y+5))
    pygame.display.flip()
    clock.tick(60)