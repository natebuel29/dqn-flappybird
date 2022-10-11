import pygame
from sprites import Bird
import os

FPS = 30
SCREEN_HEIGHT = 512
SCREEN_WIDTH = 320

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 187))
clock = pygame.time.Clock()
bird = Bird()

going = True
while going:
    clock.tick(FPS)
    should_jump = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                should_jump = True
    background.fill((0, 0, 187))
    bird.draw(background, should_jump=should_jump)
    screen.blit(background, (0, 0))
    pygame.display.flip()
