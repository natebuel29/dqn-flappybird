from network.dqn import DQN
import numpy as np


network = DQN((84, 84, 3,), 2)
test_data = np.random.rand(1, 84, 84, 3)
print(network.forward(test_data))
result = network.forward(test_data)
print(result.shape)
print(np.argmax(result))
