import math
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
from AI.QLearner import QLearner
from Game import Game
from AI.metaclass import a_star_player

# this file is currently empty it is a detailed explanation of how the game will
# be built code wise, then we will use the code elements to build a graphic gui
# after we decide weather we want to use pygame tkinter or another program

# enemy - abstract type which has an enemy behaivour method that is
# different for every enemy and will be defined in a case to case basis

# projectile, gets a direction location and speed and yeats off

# player - has hp speed and more values, can use his act function to
# move around and shoot

# board has an array of enemies projectiles a player object and the limits,
# in its update function we will track score and update the units locations
algs = ["aStar", "qLearn"]
alg = "qLearn"

running = True
clock = pygame.time.Clock()
game = Game()
pygame.display.init()
q = QLearner((100, 100), future_steps=10)  # calc board size based on player movespeed
game.update()


def game_loop():
    moves = []
    while running:
        if alg == "aStar":
            # if moves == []:
            moves = a_star_player(game)
            game.update(moves.pop(0))
        elif alg == "qLearn":
            q.update_values(game)
            move = q.next_turn(game)
            print(move)
            game.update(move)
            q.print_at_depth(game, 0)
            # q.print_at_depth(game, 1)
            # q.print_at_depth(game, 2)
            # q.print_at_depth(game, 3)
            # q.print_at_depth(game, 4)

        clock.tick(60)


if __name__ == '__main__':
    game_loop()
