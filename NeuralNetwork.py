import numpy as np
import random
from random import randrange


class NeuralNetwork:

    def __init__(self, neural_network_array, score_array):
        self.neural_network = neural_network_array
        self.score = score_array
        self.new_neural_network = [[]]
        self.sum_score = 0

    def select_best_network(self):
        best_network = []
        max_score = 0
        for i in range(len(self.score)):
            if self.score[i] > max_score:
                max_score = score[i]
                best_network = self.neural_network[i]
        self.new_neural_network.append(best_network)

    def sum_scoree(self):
        for i in range(len(self.score)):
            self.sum_score += self.score[i]

    def choose_parent(self):
        random_num = randrange(self.sum_score)
        num = 0
        for i in range(len(self.neural_network)):
            num += self.score[i]
            if num > random_num:
                return self.neural_network[i]
        return self.neural_network[0]

    def crossover_metrix(self, metrix_1, metrix_2):
        new_metrix = [[]]
        random_col = randrange(len(metrix_1[0]))
        random_row = randrange(len(metrix_1))
        for i in range(len(metrix_1)):
            for j in range(len(metrix_1[0])):
                if i < random_row or (i == random_row and j <= random_col):
                    new_metrix[i][j] = metrix_1[i][j]
                else:
                    new_metrix[i][j] = metrix_2[i][j]
        return new_metrix

    def crossover(self, parent_1, parent_2):
        child_network = []
        for i in range(len(parent_1)):
            metrix = self.crossover_metrix(parent_1[i], parent_2[i])
            child_network.append(self.mutation(metrix))
        return child_network

    def mutation(self, metrix):
        mutation_rate = 0.05
        for i in range(len(metrix)):
            for j in range(len(metrix[0])):
                num = random.random()
                if num < mutation_rate:
                    metrix[i][j] += np.random.normal()/5
                    if metrix[i][j] > 1:
                        metrix[i][j] = 1
                    if metrix[i][j] < -1:
                        metrix[i][j] = -1
        return metrix

    def selection(self):
        self.sum_scoree()
        self.select_best_network()
        for i in range(len(self.neural_network)):
            new_network_1 = self.choose_parent()
            new_network_2 = self.choose_parent()
            child_network = self.crossover(new_network_1, new_network_2)
            self.new_neural_network.append(self.mutation(child_network))

    def create_neural_network(self):
        network = [2 * np.random.random_sample((24, 100 * 100)) - 1, 2 * np.random.random_sample((24, 24)) - 1,
                   2 * np.random.random_sample((5, 24)) - 1]
        self.array.append(network)
