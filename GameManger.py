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
import pygame
import Draw
from Projectile import Projectile

import keybinds
import Player

# TODO: figure out the ratio with board
running = True
pygame.init()
player = Player.Player((10, 10), "resources\ship.png")


def game_loop():
    while running:
        # player input and actions
        dir, shoot = keybinds.get_input()
        player.action(dir, shoot)
        # enemy moves and actions
        # check collisions
        # screen visual updates
        Draw.redrawGameWindow()

        Projectile.draw_all()
        player.draw()

        pygame.display.flip()
        pass


if __name__ == '__main__':
    game_loop()
