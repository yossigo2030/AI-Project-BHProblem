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
import Spriteables
import Projectile
import collisionManager
import keybinds
import Player
import EnemyType
import MovementPatterns

clock = pygame.time.Clock()
# TODO: figure out the ratio with board
running = True
pygame.init()
player = Player.Player((0, 0), r"resources\ship.png")
EnemyType.EnemyShooter([100, 100],
                       r"resources\en.png",
                       MovementPatterns.StraightPattern((0, 1)),
                       [MovementPatterns.StraightPattern((-1, 0))])


def game_loop():
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

        # screen visual updates
        Draw.redrawGameWindow()
        Projectile.draw_all()
        EnemyType.draw_all()
        player.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    game_loop()
