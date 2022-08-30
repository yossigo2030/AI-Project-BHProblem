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
SAVETOFILE = False
clock = pygame.time.Clock()
pygame.display.init()
pygame.font.init()
brain_array = []
score_array = []
flag = True


def create_neural_network():
    return [2 * np.random.random_sample((24, 100 * 100)) - 1, 2 * np.random.random_sample((24, 24)) - 1,
            2 * np.random.random_sample((5, 24)) - 1]


def genetic_algorithm(brain_file=None, score=None):
    neural_network_array = []
    if brain_file is None:
        for i in range(100):
            neural_network_array.append(create_neural_network())
    else:
        # todo read networks from file, and append them to neural network array
        neural_network = NeuralNetwork(brain_file, score)
        neural_network_array = neural_network.new_neural_network()
    q_genetic(neural_network_array)
    # todo save to file
    pass


def choose_action(array):
    shot = False
    dir = np.array([0, 0])
    max_num = 0
    action = 0
    for i in range(5):
        if array[i] < max_num:
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


def q_genetic(brains):
    brains_array = brains
    for i in range(3):
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
        print("end_game")


if __name__ == '__main__':
    genetic_algorithm()
