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
from AI.QLearner import QLearner
from CheapWave import CheapWave
from CollisionTestingWave import CollisionTestingWave
from DataStructures import DataStructures
from Game import Game
from AI.metaclass import a_star_player, a_star_search_times

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
algs = ["aStar", "aStarT", "qLearn"]
tps = 60
NODECOUNT = 100
SKIPSTART = False
running = True
SAVETOFILE = False
TESTWAVE = False
pygame.font.init()
clock = pygame.time.Clock()
game = Game()
if TESTWAVE:
    game.wave = CollisionTestingWave(pygame.display.get_window_size(), game.data)
else:
    # game.wave = CheapWave(pygame.display.get_window_size(), game.data)
    game.wave = Wave.Wave(pygame.display.get_window_size(), game.data)
pygame.display.init()
q = QLearner((100, 100), future_steps=100, itercount=5000, epsilon=0.8)  # calc board size based on player movespeed


def game_loop(alg: str):
    global running
    moves = []
    search = None
    if SKIPSTART:
        for i in range(120):
            game.update()
    while running:
        if InputHandler.Quit() or game.player.lives == 0:
            running = False
        if alg == "aStar":
            if len(moves) == 0:
                moves = a_star_player(game, NODECOUNT)
            game.update(moves.pop(0), save_to_file=SAVETOFILE)
        if alg == "aStarT":
            if search is None:
                search = a_star_search_times(game, 0.25)
            move = search()
            game.update(move, save_to_file=SAVETOFILE)
        elif alg == "qLearn":
            q.update_values(game)
            if game.frame == 50:
                x = 0
            move = q.get_next_turn(game)
            print(move)
            print(f"HP count: {game.player.lives}")
            game.update(move, save_to_file=SAVETOFILE)
        else:
            game.update(save_to_file=SAVETOFILE)
        clock.tick(tps)


if __name__ == '__main__':
    try:
        algorithm = sys.argv[1]
        if algorithm in algs:
            print(algorithm)
    except Exception:
        algorithm = None

    game_loop(algorithm)
    pygame.quit()
