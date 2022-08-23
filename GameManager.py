import math
import time
from queue import Queue

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
import AI.metaclass
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
qlearn = False
aStar = True

running = True
clock = pygame.time.Clock()
game = Game()
# TODO: figure out the ratio with board
pygame.display.init()
q = QLearner((100, 100), future_steps=10) # calc board size based on player movespeed
game.update()


def game_loop():
    # gamecopy = game.__copy__(True)
    while running:
        # TODO figure out what the situation with move is, we need it for successors
        if aStar:
            game.update(AI.metaclass.a_star_player(game))
        # gamecopy = gamecopy.__copy__(True)
        if qlearn:
            q.update_values(gamecopy)
            q.print_at_depth(1)
            q.print_at_depth(2)
            q.print_at_depth(3)
            q.print_at_depth(4)

        clock.tick(60)


if __name__ == '__main__':
    game_loop()
