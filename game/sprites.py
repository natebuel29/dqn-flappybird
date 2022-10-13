import pygame
import numpy as np
import random


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.jump_force = 35
        self.x = 50
        self.y = 250
        self.dy = -30
        self.down_gravity = 4
        self.max_dy = 14
        self.min_dy = -30
        self.image = pygame.image.load("images/bird.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.color = pygame.Color(255, 0, 0)

    def jump(self):
        self.dy -= self.jump_force

    def gravity(self):
        self.dy += self.down_gravity

    def update(self, should_jump):
        if should_jump:
            self.jump()
        else:
            self.gravity()
        if self.dy > self.max_dy:
            self.dy = self.max_dy
        elif self.dy < self.min_dy:
            self.dy = self.min_dy

    def draw(self, surface):
        self.y = self.y + self.dy
        surface.blit(self.image, (self.x, self.y))


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, height, is_top):
        self.body = pygame.image.load("images/pipe_body.png")
        self.head = pygame.image.load("images/pipe_head.png")
        self.x = 400
        self.dx = 6
        if is_top:
            self.y = 0
        else:
            self.y = 512
        self.height = height
        self.width = 64
        self.offset = 10
        self.body = pygame.transform.scale(
            self.body, (self.width, self.height))
        self.head = pygame.transform.scale(
            self.head, (self.width+self.offset, 32))
        self.is_top = is_top

    def update(self):
        self.x -= self.dx

    def draw(self, surface):
        if self.is_top:
            surface.blit(self.body, (self.x, self.y))
            surface.blit(self.head, (self.x - 5, self.height))
        else:
            surface.blit(self.body, (self.x, self.y - self.height+16))
            surface.blit(
                self.head, (self.x - self.offset/2, self.y-self.height))


class PipePair(pygame.sprite.Sprite):
    def __init__(self, surface_height, surface_width):
        self.surface_height = surface_height
        self.surface_width = surface_width
        self.gap = 150
        self.min_distance = 60
        self.bottom_height = random.randint(
            self.min_distance, self.surface_height-self.min_distance - self.gap)
        self.top_height = self.surface_height - self.bottom_height - self.gap
        self.top_pipe = Pipe(self.surface_width, self.top_height, True)
        self.bottom_pipe = Pipe(self.surface_width, self.bottom_height, False)

    def update(self):
        self.top_pipe.update()
        self.bottom_pipe.update()

    def draw(self, surface):
        self.top_pipe.draw(surface)
        self.bottom_pipe.draw(surface)

    def set_pipe_heights(self):
        pass

    def collision(self, bird):
        pass
