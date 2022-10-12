import pygame
from game_manager import FlappyBirdGameManager
import os

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_manager = FlappyBirdGameManager(screen)
game_manager.run()
