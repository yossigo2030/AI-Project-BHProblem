# this file is currently empty it is a detailed explanation of how the game will
# be built code wise, then we will use the code elements to build a graphic gui
# after we decide weather we want to use pygame tkinter or another program

# enemy - abstract type which has an enemybehaivour method that is
# diffrent for every enemy and will be defind in a case to case basis

# projectile, gets a direction location and speed and yeats off

# player - has hp speed and more values, can use his act function to
# move around and shoot

# board has an array of enemies projectiles a player object and the limits
# , in its update function we will track score and update the units locations
import math
import time
from queue import Queue

import pygame
import Draw
import Spriteables
import Projectile
import collisionManager
import InputHandler
import Player
import Wave
import EnemyType
import MovementPatterns


################################################ Start ################################################

running = True
board_ratio = pygame.display.get_window_size()
player = Player.Player((board_ratio[0]/2, board_ratio[1]), r"resources\ship.png")
clock = pygame.time.Clock()
# TODO: figure out the ratio with board
pygame.init()

def game_loop():
    wave = Wave.Wave(1, board_ratio)
    while running:
        # player input and actions
        player.update()
        # enemy moves and actions
        Projectile.update_all()
        EnemyType.update_all()

        # Discard objects that are out of bounds
        Spriteables.sprite_culling()

        # check collisions
        collisionManager.collision_check_enemies()
        collisionManager.collision_check_player()
        # check pickup collisions

        # screen visual updates
        Draw.redrawGameWindow()
        Projectile.draw_all()
        EnemyType.draw_all()
        player.draw()

        #enemy spawning
        if wave.Update() == 1:
            wave = Wave.Wave(wave.number_of_wave+1, board_ratio)

        pygame.display.flip()
        clock.tick(60)





if __name__ == '__main__':
    game_loop()
