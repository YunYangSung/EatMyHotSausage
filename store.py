import pygame,sys,random,button,tkinter,time
from pygame.locals import *
def store(bg):
    WIDTH = 800
    HEIGHT = 600
    FPS = 30

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("EMHS")
    clock = pygame.time.Clock()
    # Game loop
    running = True

    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill(BLUE)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            # press esc to close the window
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= mouse[0] <= 450 and 475 <= mouse[1] <= 525:
                    return
                   


        # Update

        # Draw / render
        screen.blit(bg,(0,0))
        button.Button(screen, '返回',255,0,0, 400, 500).draw_button()


        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()