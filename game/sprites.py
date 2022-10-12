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


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, gap, is_top):
        self.body = pygame.image.load("images/pipe_body.png")
        self.head = pygame.image.load("images/pipe_head.png")
        self.x = 250
        if is_top:
            self.y = 0
        else:
            self.y = 512
        self.height = 200
        self.width = 64
        self.offset = 10
        self.body = pygame.transform.scale(
            self.body, (self.width, self.height))
        self.head = pygame.transform.scale(
            self.head, (self.width+self.offset, 32))
        self.is_top = is_top

    def update(self):
        pass

    def draw(self, surface):
        if self.is_top:
            surface.blit(self.body, (self.x, self.y))
            print(self.y)
            surface.blit(self.head, (self.x - 5, self.height))
        else:
            surface.blit(self.body, (self.x, self.y - self.height+16))
            surface.blit(
                self.head, (self.x - self.offset/2, self.y-self.height))
