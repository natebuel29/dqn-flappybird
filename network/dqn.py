from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten


class DQN:
    def __init__(self, input_shape, number_of_actions):
        self.input_shape = input_shape
        self.model = Sequential()
        self.model.add(Conv2D(filters=32, kernel_size=8,
                       strides=4, activation="relu", input_shape=input_shape))
        self.model.add(Conv2D(filters=64, kernel_size=4,
                       strides=2, activation="relu"))
        self.model.add(Conv2D(filters=64, kernel_size=3,
                       strides=1, activation="relu"))
        self.model.add(Flatten())
        self.model.add(Dense(number_of_actions, activation="sigmoid"))

    def forward(self, x):
        return self.model.predict(x)
