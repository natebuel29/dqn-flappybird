from network.dqn import DQN
import collections
# from game.game_manager import FlappyBirdGameManager
import pygame
import random
import numpy as np

# pygame.init()
SCREEN_HEIGHT = 512
SCREEN_WIDTH = 320
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
max_len = 1000
# buffer = collections.deque(maxlen=max_len)
buffer = []
action_network = DQN((3, 84, 84), 2)
target_network = DQN((3, 84, 84), 2)
target_network.model.set_weights(action_network.model.get_weights())
epsilon = 0.99
decay_rate = 0.001
epsilon_min = 0.02
training = True
C = 1000
mini_batch_size = 15
lambda_ = 0.2
# game_manager = FlappyBirdGameManager(screen)
# while training:
#     game_manager.reset()
#     # obs = game_manager.get_screen()
#     # need to preprocess init_img
#     # current_state = [init_img,init_img,init_img]
#     # done = False

#     while not done:
#         if random.uniform(0, 1) < epsilon:
#             action = random.randrange(0, 2)
#         else:
#             q_values = action_network.forward(current_state)
#             action = np.argmax(q_values)

#         reward, is_done = game_manager.play_step(action)
#         new_obs = game_manager.get_screen()
#         new_state = [current_state[1:], new_obs]
#         buffer.append({
#             "current_state", current_state,
#             "action", action,
#             "reward", reward,
#             "finished", finished,
#             "next_state", next_state
#         })

#         random_batch = np.random.choice(buffer, mini_batch_size)

#         for sample in random_batch:
#             sam_current = sample.get("current_state")
#             sam_action = sample.get("action")
#             sam_reward = sameple.get("reward")
#             sam_finished = sample.get("finished")
#             sam_future = sample.get("future_state")

#             y = action_network.predict(sam_current)
#             if finished:
#                 r_sample = sam_reward
#             else:
#                 r_sample = sam_reward + lambda_ * \
#                     np.argmax(target_network.forward(sam_future))

#             y[sam_action] = r_sample

# h = action_network.model.fit(sam_current, y, batch_size=1)


current_state = np.random.rand(1, 3, 84, 84)

if random.uniform(0, 1) < epsilon:
    action = random.randrange(0, 2)
else:
    q_values = action_network.forward(current_state)
    action = np.argmax(q_values)
# reward, is_done = game_manager.play_step(action)
reward = 2
finished = False
next_obs = np.random.rand(1, 1, 84, 84)
print(current_state[:, 1:].shape)
next_state = np.append([current_state[1:], new_obs])

buffer.append({
    "current_state": current_state,
    "action": action,
    "reward": reward,
    "finished": finished,
    "next_state": next_state
})

random_batch = np.random.choice(buffer, 1)
print(len(random_batch))
for sample in random_batch:
    sam_current = sample.get("current_state")
    sam_action = sample.get("action")
    sam_reward = sample.get("reward")
    sam_finished = sample.get("finished")
    sam_future = sample.get("next_state")
    print(sam_current.shape)
    print(sam_future.shape)
    y = action_network.forward(sam_current)
    print(y)
    print(sam_action)
    if finished:
        r_sample = sam_reward
    else:
        r_sample = sam_reward + lambda_ * \
            np.argmax(target_network.forward(sam_future))
    print(r_sample)
    y[0][sam_action] = r_sample
    print(y[0])
    h = action_network.model.fit(sam_current, y, batch_size=1)
