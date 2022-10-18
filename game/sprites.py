import pygame
import numpy as np
import random


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.jump_force = 32
        self.x = 50
        self.y = 250
        self.dy = -30
        self.down_gravity = 4
        self.max_dy = 14
        self.min_dy = -25
        self.image = pygame.image.load("images/bird.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.x_offset = 15
        self.y_offset = 18
        self.rect_side = 25
        self.rect = pygame.Rect(self.x + self.x_offset, self.y+self.y_offset,
                                self.rect_side, self.rect_side)
        self.color = pygame.Color(255, 0, 0)
        self.mask = pygame.mask.from_surface(self.image)

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
        self.y = self.y + self.dy
        self.rect = pygame.Rect(self.x + self.x_offset, self.y+self.y_offset,
                                self.rect_side, self.rect_side)

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color(255, 0, 0), self.rect)
        surface.blit(self.image, (self.x, self.y))


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, height, is_top):
        self.image = pygame.image.load("images/pipe_body.png")
        self.head = pygame.image.load("images/pipe_head.png")
        self.x = x
        self.dx = 6
        if is_top:
            self.y = 0
        else:
            self.y = 512
        self.height = height
        self.width = 64
        self.offset = 10
        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))
        self.head = pygame.transform.scale(
            self.head, (self.width+self.offset, 32))
        self.head_rect = self.head.get_rect()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_top = is_top

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.x -= self.dx

    def draw(self, surface):
        if self.is_top:
            surface.blit(self.image, (self.x, self.y))
            self.rect = pygame.Rect(
                self.x, self.y, self.width, self.height)
            surface.blit(
                self.head, (self.x - 5, self.height-self.head_rect[3]))

        else:
            surface.blit(self.image, (self.x, self.y - self.height))
            self.rect = pygame.Rect(
                self.x, self.y - self.height+16, self.width, self.height)
            surface.blit(
                self.head, (self.x - self.offset/2, self.y-self.height))


class PipePair(pygame.sprite.Sprite):
    def __init__(self, surface_height, surface_width, starting_x):
        self.starting_x = starting_x
        self.surface_height = surface_height
        self.surface_width = surface_width
        self.gap = 125
        self.min_distance = 60
        self.create_pipes(starting_x)

    def update(self):
        self.top_pipe.update()
        self.bottom_pipe.update()
        if self.is_off_screen():
            self.create_pipes(self.surface_width)

    def draw(self, surface):
        self.top_pipe.draw(surface)
        self.bottom_pipe.draw(surface)

    def create_pipes(self, x):
        self.bottom_height = random.randint(
            self.min_distance, self.surface_height-self.min_distance - self.gap)
        self.top_height = self.surface_height - self.bottom_height - self.gap
        self.top_pipe = Pipe(x, self.top_height, True)
        self.bottom_pipe = Pipe(x, self.bottom_height, False)

    def is_off_screen(self):
        return self.top_pipe.x < 0 - self.top_pipe.width and self.bottom_pipe.x < 0 - self.bottom_pipe.width

    def collision(self, bird):
        if pygame.sprite.collide_mask(self.top_pipe, bird):
            return True
        elif pygame.sprite.collide_mask(self.bottom_pipe, bird):
            return True
        else:
            return False
