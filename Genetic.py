import math
import sys
import time
from queue import Queue

import numpy as np
import pygame
import Draw
import Spriteables
import Projectile
import CollisionManager
import InputHandler
import Player
import Wave
import EnemyType
import MovementPatterns
import metrix
from AI.QLearner import QLearner
from CollisionTestingWave import CollisionTestingWave
from DataStructures import DataStructures
from Game import Game
from AI.metaclass import a_star_player


import random
from NeuralNetwork import *
from Game import *


tps = 60
SAVETOFILE = True
clock = pygame.time.Clock()
pygame.display.init()
pygame.font.init()
brain_array = []
score_array = []
flag = True


# def write_matrix_to_textfile(matrix, number):
#     with open("matrix_" + str(number) + ".txt", 'w') as testfile:
#         for row in matrix:
#             testfile.write(' '.join([str(a) for a in row]) + '\n')


# def read_neural_network(matrix_1, metrix_2, metrix_3):
#     network = []
#     with open(matrix_1, 'r') as f:
#         a = [[float(num) for num in line.split(' ')] for line in f]
#         network.append(a)
#     with open(metrix_2, 'r') as f:
#         b = [[float(num) for num in line.split(' ')] for line in f]
#         network.append(b)
#     with open(metrix_3, 'r') as f:
#         c = [[float(num) for num in line.split(' ')] for line in f]
#         network.append(c)
#     return network


def create_neural_network():
    return [2 * np.random.random_sample((24, 20 * 20)) - 1, 2 * np.random.random_sample((24, 24)) - 1,
            2 * np.random.random_sample((5, 24)) - 1]


def best_neural():
    max_score = 0
    index = 0
    for i in range(len(score_array)):
        if score_array[i] > max_score:
            max_score = score_array[i]
            index = i
    return index, max_score


def choose_action(array):
    shot = False
    dir = np.array([0, 0])
    max_num = 0
    action = 0
    for i in range(5):
        if array[i] > max_num:
            max_num = array[i]
            action = i
    if action == 0:
        dir -= [1, 0]  # left
    if action == 1:
        dir += [1, 0]  # right
    if action == 2:
        dir -= [0, 1]  # up
    if action == 3:
        dir += [0, 1]  # down
    if action == 4:
        shot = True  # shot
    return dir, shot


def genetic_algorithm(num_of_gen, num_of_net_in_gen):
    generation = 0
    numm = 0
    final_game = False
    while generation < num_of_gen + 1:
        if generation == num_of_gen:
            final_game = True
        neural_network_array = []
        if len(brain_array) == 0:
            for i in range(num_of_net_in_gen):
                neural_network_array.append(create_neural_network())
        elif not final_game:
            neural_network = NeuralNetwork(brain_array, score_array)
            neural_network_array = neural_network.get_new_neural_network()
        else:
            neural_network_array = brain_array
        q_genetic(neural_network_array, num_of_net_in_gen, final_game)
        generation += 1
        # numm = save(numm)


# def save(num):
#     numm = num
#     index, score = best_neural()
#     smart_neural = brain_array[index]
#     for metrix in smart_neural:
#         write_matrix_to_textfile(metrix, numm)
#         numm += 1
#     f = open("matrix_" + str(num) + ".txt", "a")
#     f.write(str(score))
#     f.close()
#     return numm + 1


def q_genetic(brains, num_of_net_in_gen, final_game):
    brains_array = brains
    global brain_array
    global score_array
    brain_array = []
    score_array = []
    for i in range(num_of_net_in_gen):
        game = Game(0, True, None, pygame.display.get_window_size(), None, None, brains_array[i])
        running = True
        while running:
            metrix = game.m
            output_array = metrix.get_final_output()
            move = ([0, 0], False)
            if len(output_array) > 0:
                move = choose_action(output_array)
            game.update(move)
            clock.tick(tps)
            if game.get_lives() == 0:
                brain_array.append(metrix.get_neural_network())
                score_array.append(game.get_state_score())
                running = False
        if final_game:
            break


########### to record algorithm


# def genetic_algorithm(input_neural_file):
#     q_genetic(read_neural_network("first_matrix.txt", "second_matrix.txt", "third_matrix.txt"))
#
#
# def q_genetic(brains):
#     brains_array = brains
#     np_arrays = []
#     for array in brains_array:
#         np_arrays.append(np.array(array))
#     game = Game(0, True, None, pygame.display.get_window_size(), None, None, np_arrays)
#     running = True
#     while running:
#         metrix = game.m
#         output_array = metrix.get_final_output()
#         move = ([0, 0], False)
#         if len(output_array) > 0:
#             move = choose_action(output_array)
#         game.update(move, SAVETOFILE)
#         clock.tick(tps)
#         if game.get_lives() == 0:
#             running = False


if __name__ == '__main__':
    genetic_algorithm(2, 3)
