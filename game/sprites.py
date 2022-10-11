import pygame
import numpy as np


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.jump_force = 40
        self.x = 50
        self.y = 250
        self.dy = -30
        self.down_gravity = 5
        self.max_dy = 14
        self.min_dy = -30
        self.image = pygame.Surface([20, 20])
        self.image = pygame.image.load("images/bird.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.color = pygame.Color(255, 0, 0)

    def jump(self):
        self.dy -= self.jump_force

    def gravity(self):
        self.dy += self.down_gravity

    def draw(self, surface, should_jump):
        if should_jump:
            self.jump()
        else:
            self.gravity()

        if self.dy > self.max_dy:
            self.dy = self.max_dy
        elif self.dy < self.min_dy:
            self.dy = self.min_dy

        self.y = self.y + self.dy
        surface.blit(self.image, (self.x, self.y))
