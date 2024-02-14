# this is a weird color picker i made while messing around with colors and image manipulation
# it's not my proudest creation, enjoy

# you can launch this by itself (for whatever reason)
# or import it somewhere else
def launch(window_name="Color Picker"):
    import pygame

    SIZE = 256

    pygame.init()
    pygame.display.set_caption(window_name)
    screen = pygame.display.set_mode((SIZE, SIZE+50))
    clock = pygame.time.Clock()
    running = True

    font = pygame.font.Font(None, 30)
    tiny = pygame.font.Font(None, 15)

    def fill():
        for y in range(SIZE):
            for x in range(SIZE):
                screen.set_at((x, y), (x, y, (x+y)%256))

    fill()
    RGBA = (0, 0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_RETURN)):
                running = False

        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            if my < SIZE:
                fill()
                RGB = screen.get_at((mx%SIZE, my%SIZE))[:-1]
                pygame.draw.circle(screen, (0, 0, 0), (mx, my), 5, 2)
                preview = pygame.Surface((SIZE, 50))
                preview.fill(RGB)
                screen.blit(preview, pygame.Rect(0, SIZE, SIZE, SIZE+50))
                
                r, g, b = RGB
                text = font.render(f"rgb{RGB}", True, RGB, "black" if int((r+g+b)/3) > 127 else "white" )
                textpos = text.get_rect(centerx=int(SIZE/2), centery=SIZE+25)
                screen.blit(text, textpos)

                text = tiny.render(f"press ESC/ENTER or close this window to confirm", True, "white")
                textpos = text.get_rect(x=5, y=5)
                screen.blit(text, textpos)
        
        pygame.display.flip()
        clock.tick(60)
    return RGBA

if __name__ == "__main__":
    launch()
