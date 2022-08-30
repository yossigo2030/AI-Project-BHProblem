import numpy as np
import random
from DataStructures import DataStructures


class metrix:
    def __init__(self, neural_network, data=None):
        self.data = data
        self.array = []
        self.input_metrix = np.zeros((100, 100))
        self.neural_network = neural_network
        self.output = []

    def round(self):
        self.update_metrix()
        self.get_output()

    def update_metrix(self):
        self.input_metrix = np.zeros((100, 100))
        for projectile in self.data.ProjectileSpriteGroup:
            location = projectile.location
            x = int(location[0]/5)
            y = int(location[1]/5)
            if 0 <= x <= 99 and 0 <= y <= 99:
                self.input_metrix[y][x] = 1
                # print(location, "location")
                # print(x, y, "x_y")
            # x_1 = int(x - 0.5)
            # x_2 = int(x + 0.5)
            # y_1 = int(y + 0.5)
            # y_2 = int(y - 0.5)
            # if x_1 >= 0:
            #     self.zeors_array[int(x - 0.5)][int(y)] = 1
            # if x_2 <= 100:
            #     self.zeors_array[int(x + 0.5)][int(y)] = 1
            #
            # self.zeors_array[int(x)][int(y + 0.5)] = 1
            # self.zeors_array[int(x)][int(y - 0.5)] = 1
            # print(x, y)
            # print(location)
        for enemy in self.data.EnemySpriteGroup:
            location = enemy.location
            x = int(location[0] / 5)
            y = int(location[1] / 5)
            if 0 <= x <= 99 and 0 <= y <= 99:
                self.input_metrix[y][x] = 1
                # print(location, "location")
                # print(x, y, "x_y")

    def get_output(self):
        input_vector = self.input_metrix.flatten()
        hidden_1 = self.relu(self.neural_network[0].dot(input_vector))
        hidden_2 = self.relu(self.neural_network[1].dot(hidden_1))
        self.output = self.softmax(self.neural_network[2].dot(hidden_2))

    def relu(self, x):
        return np.maximum(0, x)

    def softmax(self, x):
        return np.exp(x) / np.exp(x).sum()

    def get_final_output(self):
        return self.output

    def get_neural_network(self):
        return self.neural_network
