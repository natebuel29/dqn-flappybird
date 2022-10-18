import pygame
from game_manager import FlappyBirdGameManager
import os

SCREEN_HEIGHT = 512
SCREEN_WIDTH = 320

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_manager = FlappyBirdGameManager(screen)
game_manager.run()
