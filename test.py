from network.dqn import DQN
import numpy as np


network = DQN((84, 84, 3,), 2)
test_data = np.random.rand(50, 84, 84, 3)
print(test_data[1, :, :, :])
print(network.input_shape)
print(test_data.shape)
print(network.forward(test_data))
