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
from Game import Game

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

running = True
clock = pygame.time.Clock()
game = Game()
# TODO: figure out the ratio with board
pygame.display.init()


def game_loop():
    while running:
        # TODO figure out what the situation with move is, we need it for successors
        game.update("Asdasd")
        clock.tick(60)


if __name__ == '__main__':
    game_loop()
