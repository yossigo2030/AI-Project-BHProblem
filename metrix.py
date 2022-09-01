import numpy as np

LARGE = 19


class metrix:
    def __init__(self, neural_network, data=None):
        self.data = data
        self.array = []
        self.input_metrix = np.zeros((20, 20))
        self.neural_network = neural_network
        self.output = []

    def round(self):
        self.update_metrix()
        self.get_output()

    def update_metrix(self):
        self.input_metrix = np.ones((20, 20))
        for projectile in self.data.ProjectileSpriteGroup:
            location = projectile.location
            x = int(location[0] / 25)
            y = int(location[1] / 25)
            self.update_helper(x, y)
        for enemy in self.data.EnemySpriteGroup:
            location = enemy.location
            x = int(location[0] / 25)
            y = int(location[1] / 25)
            self.update_helper(x, y)

    def update_helper(self, x, y):
        if 0 <= x <= LARGE and 0 <= y <= LARGE:
            self.input_metrix[y][x] = 0
        if 0 <= x <= LARGE and 0 <= y - 1 <= LARGE:
            self.input_metrix[y - 1][x] = max(0, (self.input_metrix[y - 1][x] - 0.2))
        if 0 <= x <= LARGE and 0 <= y + 1 <= LARGE:
            self.input_metrix[y + 1][x] = max(0, (self.input_metrix[y + 1][x] - 0.2))
        if 0 <= x + 1 <= LARGE and 0 <= y - 1 <= LARGE:
            self.input_metrix[y - 1][x + 1] = max(0, (self.input_metrix[y - 1][x + 1] - 0.4))
        if 0 <= x + 1 <= LARGE and 0 <= y <= LARGE:
            self.input_metrix[y][x + 1] = max(0, (self.input_metrix[y][x + 1] - 0.6))
        if 0 <= x + 1 <= LARGE and 0 <= y + 1 <= LARGE:
            self.input_metrix[y + 1][x + 1] = max(0, (self.input_metrix[y + 1][x + 1] - 0.4))

    def get_output(self):
        input_vector = self.input_metrix.flatten()
        hidden_1 = self.relu(self.neural_network[0].dot(input_vector))
        hidden_2 = self.relu(self.neural_network[1].dot(hidden_1))
        self.output = self.neural_network[2].dot(hidden_2)

    def relu(self, x):
        return np.maximum(0, x)

    def softmax(self, x):
        return np.exp(x) / np.exp(x).sum()

    def get_final_output(self):
        return self.output

    def get_neural_network(self):
        return self.neural_network
