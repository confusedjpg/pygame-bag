import pygame
pygame.init()

def mainDebug(clock, x=0,y=0): #clock for fps
    """Show default debug info needed for most programs."""
    screen = pygame.display.get_surface() #get current window surface
    fontSize = 20 if screen.get_height() >= 500 or screen.get_width() >= 500 else 15

    #main rect
    debugSurf = pygame.Surface((screen.get_width(), screen.get_height()*0.2))
    debugSurf.fill((20,20,20,30))
    debugRect = debugSurf.get_rect(topleft=(x,y))
    screen.blit(debugSurf, debugRect)

    #current time since launch
    timeSurf = pygame.font.Font(None, fontSize).render(f"Time: {pygame.time.get_ticks()//1000}s", True, (180,0,0))
    timeRect = timeSurf.get_rect(topleft=(x,y))
    screen.blit(timeSurf, timeRect)

    #get window size
    sizeSurf = pygame.font.Font(None, fontSize).render(f"Screen: ({pygame.display.get_caption()[0]})", True, (180,0,0))
    sizeRect = sizeSurf.get_rect(topleft=(x,y+fontSize))
    screen.blit(sizeSurf, sizeRect)

    #mouse pos
    mouseSurf = pygame.font.Font(None, fontSize).render(f"Mouse: {pygame.mouse.get_pos()}; {pygame.mouse.get_pressed()}", True, (180,0,0))
    mouseRect = mouseSurf.get_rect(topleft=(x,y+fontSize*2))
    screen.blit(mouseSurf, mouseRect)

    #pixel color at mouse pos
    colorSurf = pygame.font.Font(None, fontSize).render(f"RGBA (at mouse pos): {screen.get_at(pygame.mouse.get_pos())}", True, (180,0,0))
    colorRect = colorSurf.get_rect(topleft=(x,y+fontSize*3))
    screen.blit(colorSurf, colorRect)
    previewSurf = pygame.Surface((15,15))
    previewSurf.fill(screen.get_at(pygame.mouse.get_pos()))
    previewRect = previewSurf.get_rect(topleft=(colorRect.topright[0]+10,colorRect.topright[1]))
    screen.blit(previewSurf, previewRect)

    #fps
    fpsSurf = pygame.font.Font(None, fontSize).render(f"FPS: {int(clock.get_fps())}", True, (180,0,0))
    fpsRect = fpsSurf.get_rect(topleft=(x,y+fontSize*4))
    screen.blit(fpsSurf, fpsRect)
