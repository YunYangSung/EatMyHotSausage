import pygame,sys,random,button,eighteen,tkinter,time
from pygame.locals import *

def game(bg, moneyandhotdog):
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
    result = []
    # Game loop
    running = True
    dice_dict = dict()
    dice_dict[1] = pygame.image.load('Pic\\dice1.png')
    dice_dict[2] = pygame.image.load('Pic\\dice2.png')
    dice_dict[3] = pygame.image.load('Pic\\dice3.png')
    dice_dict[4] = pygame.image.load('Pic\\dice4.png')
    dice_dict[5] = pygame.image.load('Pic\\dice5.png')
    dice_dict[6] = pygame.image.load('Pic\\dice6.png')
    sausage_stand = pygame.image.load('Pic\\香腸攤.png')
    screen.blit(bg,(0,0))
    screen.blit(sausage_stand,(200,150))
    button.Button(screen, '返回',255,0,0, 700, 550).draw_button()
    button.Button(screen, '我的',255,0,0, 50, 50).draw_button()
    button.Button(screen, '十八喇',255,0,0, 100, 550, 120).draw_button()
    button.Button(screen, str(moneyandhotdog[0]),255,0,0, 700, 25).draw_button()
    button.Button(screen, str(moneyandhotdog[1]),255,0,0, 700, 75).draw_button()


    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        # Process input (events)
        if 650 <= mouse[0] <= 750 and 525 <= mouse[1] <= 575:
            button.Button(screen, '返回',255,0,0, 700, 550,fontsize=40).draw_button()
        else:
            button.Button(screen, '返回',255,0,0, 700, 550).draw_button()
        if 50 <= mouse[0] <= 150 and 525 <= mouse[1] <= 575:
            button.Button(screen, '十八喇',255,0,0, 100, 550,fontsize=40).draw_button()
        else:
            button.Button(screen, '十八喇',255,0,0, 100, 550, 120).draw_button()
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            # press esc to close the window
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 650 <= mouse[0] <= 750 and 525 <= mouse[1] <= 575:
                    return
                if 50 <= mouse[0] <= 150 and 525 <= mouse[1] <= 575:
                    result = eighteen.play()
                    screen.blit(dice_dict[result[1][0]],(20,70)) 
                    screen.blit(dice_dict[result[1][1]],(120,70))
                    screen.blit(dice_dict[result[1][2]],(220,70))
                    screen.blit(dice_dict[result[1][3]],(320,70))
                    button.Button(screen, '再骰一次',255,0,0, 100, 550, 150).draw_button()
                    if result[0] != 0:
                        running = False

        # Update
        # Draw / render

        # *after* drawing everything, flip the display
        pygame.display.flip()
    screen.blit(bg,(0,0))
    screen.blit(sausage_stand,(200,150))
    screen.blit(dice_dict[result[1][0]],(20,70)) 
    screen.blit(dice_dict[result[1][1]],(120,70))
    screen.blit(dice_dict[result[1][2]],(220,70))
    screen.blit(dice_dict[result[1][3]],(320,70))
    button.Button(screen, '老闆',255,0,0, 50, 400).draw_button()
    button.Button(screen, '我的',255,0,0, 50, 50).draw_button()
    button.Button(screen, '等老闆骰',255,0,0, 100, 550, 150).draw_button()
    button.Button(screen, str(moneyandhotdog[0]),255,0,0, 700, 25).draw_button()
    button.Button(screen, str(moneyandhotdog[1]),255,0,0, 700, 75).draw_button()
    pygame.display.flip()
    pygame.time.delay(500)

    boss_running = True
    boss_result = []
    while boss_running:
        # keep loop running at the right speed
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            # press esc to close the window
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        while True:
            boss_result = eighteen.play()
            screen.blit(dice_dict[boss_result[1][0]],(20,420)) 
            screen.blit(dice_dict[boss_result[1][1]],(120,420))
            screen.blit(dice_dict[boss_result[1][2]],(220,420))
            screen.blit(dice_dict[boss_result[1][3]],(320,420))
            time.sleep(0.5)
            if boss_result[0] != 0:
                boss_running = False
                break

        pygame.display.flip()

    screen.blit(bg,(0,0))
    screen.blit(sausage_stand,(200,150))
    screen.blit(dice_dict[result[1][0]],(20,70)) 
    screen.blit(dice_dict[result[1][1]],(120,70))
    screen.blit(dice_dict[result[1][2]],(220,70))
    screen.blit(dice_dict[result[1][3]],(320,70))
    button.Button(screen, '老闆',255,0,0, 50, 400).draw_button()
    button.Button(screen, '我的',255,0,0, 50, 50).draw_button()
    screen.blit(dice_dict[boss_result[1][0]],(20,420)) 
    screen.blit(dice_dict[boss_result[1][1]],(120,420))
    screen.blit(dice_dict[boss_result[1][2]],(220,420))
    screen.blit(dice_dict[boss_result[1][3]],(320,420))
    button.Button(screen, '返回',255,0,0, 700, 550).draw_button()
    print(result[0])
    print(boss_result[0])
    
    if result[0] > boss_result[0]:
        moneyandhotdog[0] -= 30
        moneyandhotdog[1] += 2
    else:
        moneyandhotdog[0] -= 30

    while True:
        # keep loop running at the right speed
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        if 650 <= mouse[0] <= 750 and 525 <= mouse[1] <= 575:
            button.Button(screen, '返回',255,0,0, 700, 550,fontsize=40).draw_button()
        else:
            button.Button(screen, '返回',255,0,0, 700, 550).draw_button()

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            # press esc to close the window
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 650 <= mouse[0] <= 750 and 525 <= mouse[1] <= 575:
                    return
        if result[0] > boss_result[0]:
            button.Button(screen, '爽啊!贏啦!',255,0,0, 600, 300, 200, 50).draw_button()
            button.Button(screen, str(moneyandhotdog[0]),255,0,0, 700, 25).draw_button()
            button.Button(screen, str(moneyandhotdog[1]),255,0,0, 700, 75).draw_button()
        else:
            button.Button(screen, '哭啊!輸啦!',255,0,0, 600, 300, 200, 50).draw_button()
            button.Button(screen, str(moneyandhotdog[0]),255,0,0, 700, 25).draw_button()
            button.Button(screen, str(moneyandhotdog[1]),255,0,0, 700, 75).draw_button() 
        pygame.display.flip()

