import sys
import random
import time
import pygame
from pygame.locals import *

FPS = 25

def makeTextObjs(text, font, color):
    surf = font.render


def showTextScreen(text):
    tit

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("测试窗口")

    bg_color = (230, 230, 230)
    screen.fill(bg_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main()
