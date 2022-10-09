import pygame as pg
import os

FPS = 30
SCREEN_HEIGHT = 512
SCREEN_WIDTH = 320

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Flappy Bird")

background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((170, 238, 187))
clock = pg.time.Clock()


going = True
while going:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    pygame.display.flip()
