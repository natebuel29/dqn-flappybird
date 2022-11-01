from network.dqn import DQN
import collections
from game.game_manager import FlappyBirdGameManager
import pygame
import random

pygame.init()
SCREEN_HEIGHT = 512
SCREEN_WIDTH = 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
max_len = 1000
buffer = collections.deque(maxlen=max_len)
action_network = DQN((84, 84, 3,), 2)
target_network = DQN((84, 84, 3,), 2)
target_network.model.set_weights(action_network.model.get_weights())
epsilon = 0.99
decay_rate = 0.001
epsilon_min = 0.02
training = True
game_manager = FlappyBirdGameManager(screen)
while training:
    game_manager.reset()
    # obs = game_manager.get_screen()
    # need to preprocess init_img
    # current_state = [init_img,init_img,init_img]
    # done = False

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = random.randrange(0, 2)
        else:
            q_values = action_network.forward(current_state)
            action = np.argmax(q_values)
