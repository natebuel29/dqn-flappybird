import pygame
from sprites import Bird, Pipe, PipePair


class FlappyBirdGameManager:
    def __init__(self, screen):
        self.fps = 30
        self.height = 512
        self.width = 320
        self.screen = screen
        pygame.display.set_caption("Flappy Bird")
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 187))
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipe_pair = PipePair(self.height, self.width)

    def reset(self):
        pass

    def draw_sprites(self):
        self.background.fill((0, 0, 187))
        self.bird.draw(self.background)
        self.pipe_pair.draw(self.background)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def update_score(self):
        pass

    def get_game_state(self):
        pass

    def game_over(self):
        pass

    def pause(self):
        pass

    def update(self):
        should_jump = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    should_jump = True
        self.bird.update(should_jump)
        self.pipe_pair.update()

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.update()
            self.draw_sprites()
