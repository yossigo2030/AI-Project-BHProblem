import numpy as np
import random
from random import randrange


class NeuralNetwork:

    def __init__(self, neural_network_array, score_array):
        self.neural_network = neural_network_array
        self.score = score_array
        self.new_neural_network = []
        self.sum_score = 0
        self.selection()

    def selection(self):
        self.sum_scoree()
        for i in range(len(self.neural_network)):
            if i == 0:
                self.select_best_network()
            else:
                parent_1 = self.choose_parent()
                parent_2 = self.choose_parent()
                child_network = self.crossover(parent_1, parent_2)
                self.new_neural_network.append(child_network)

    def select_best_network(self):
        max_score = 0
        index = 0
        for i in range(len(self.score)):
            if self.score[i] > max_score:
                max_score = self.score[i]
                index = i
        self.new_neural_network.append(self.neural_network[index])

    def sum_scoree(self):
        for i in range(len(self.score)):
            self.sum_score += self.score[i]

    def choose_parent(self):
        num = max(self.sum_score, 5)
        random_num = randrange(num)
        num = 0
        for i in range(len(self.neural_network)):
            num += self.score[i]
            if num > random_num:
                return self.neural_network[i]
        return self.new_neural_network[0]

    def crossover(self, parent_1, parent_2):
        child_network = []
        for i in range(len(parent_1)):
            metrix = self.crossover_metrix(parent_1[i], parent_2[i])
            mutate_metrix = self.mutation(metrix)
            child_network.append(mutate_metrix)
        return child_network

    def crossover_metrix(self, metrix_1, metrix_2):
        new_metrix = np.zeros((len(metrix_1), len(metrix_1[0])))
        random_col = randrange(len(metrix_1[0]))
        random_row = randrange(len(metrix_1))
        for i in range(len(metrix_1)):
            for j in range(len(metrix_1[0])):
                if i < random_row or (i == random_row and j <= random_col):
                    new_metrix[i][j] = metrix_1[i][j]
                else:
                    new_metrix[i][j] = metrix_2[i][j]
        return new_metrix

    def mutation(self, metrix):
        mutation_rate = 0.4
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
    
    def get_new_neural_network(self):
        return self.new_neural_network
