import pygame,sys,random,button,sausage,store,eighteen,tkinter,time
from pygame.locals import *

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
bg = pygame.image.load('Pic\\sky.png')
moneyandhotdog = [300, 0]


# Game loop
running = True

while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    mouse = pygame.mouse.get_pos()
    screen.blit(bg,(0,0))   
    button.Button(screen, '商店',255,0,0, 200, 500).draw_button()
    button.Button(screen, '遊戲',255,0,0, 600, 500).draw_button()
    button.Button(screen, str(moneyandhotdog[0]),255,0,0, 700, 25).draw_button()
    button.Button(screen, str(moneyandhotdog[1]),255,0,0, 700, 75).draw_button()
    if 150 <= mouse[0] <= 250 and 475 <= mouse[1] <= 525:
        button.Button(screen, '商店',255,0,0, 200, 500, fontsize=40).draw_button()

    if 550 <= mouse[0] <= 650 and 475 <= mouse[1] <= 525:
        button.Button(screen, '遊戲',255,0,0, 600, 500, fontsize=40).draw_button()

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
            if 550 <= mouse[0] <= 650 and 475 <= mouse[1] <= 525:
                sausage.game(bg, moneyandhotdog)
            if 150 <= mouse[0] <= 250 and 475 <= mouse[1] <= 525:
                store.store(bg)


    # Update

    # Draw / render
    

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()