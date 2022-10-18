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
        self.pipe_pair_one = PipePair(self.height, self.width, self.width)
        self.pipe_pair_two = PipePair(
            self.height, self.width, self.width + 200)
        self.score = 0

    def reset(self):
        pass

    def draw_sprites(self):
        self.background.fill((0, 0, 187))
        self.bird.draw(self.background)
        self.pipe_pair_one.draw(self.background)
        self.pipe_pair_two.draw(self.background)
        text = self.show_score()
        self.background.blit(text, (0, 0))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    # display score
    def show_score(self):
        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        return text

    def update_score(self):
        if self.pipe_pair_one.passed_bird(self.bird) or self.pipe_pair_two.passed_bird(self.bird):
            self.score += 1

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
        self.pipe_pair_one.update()
        self.pipe_pair_two.update()
        self.update_score()
        if self.pipe_pair_one.collision(self.bird) or self.pipe_pair_two.collision(self.bird):
            print("yoo collision dumby")

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.update()
            self.draw_sprites()
