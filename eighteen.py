import pygame,sys,random,button,tkinter,time
from pygame.locals import *

def play():
    dice = []
    for x in range(4):
        dice.append(random.randint(1,6))
    for x in range(1,7):
        if dice.count(x) == 4:
            return [x * 100, dice]
            break
        if dice.count(x) == 3:
            for y in range(1,7):
                if dice.count(y) == 1:
                    return [x + y, dice]
                    break
        if dice.count(x) == 2:
            for y in range(x + 1,7):
                if dice.count(y) == 2:
                    return [2*x if x>y else 2*y, dice]
            return [dice[0] + dice[1] + dice[2] + dice[3] - 2*x, dice]
        if x == 6:
            return[0,dice]



    