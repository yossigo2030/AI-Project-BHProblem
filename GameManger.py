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

# TODO: figure out the ratio with board
running = True
pygame.init()


def game_loop():
    color = (255,255,255)
    pygame.draw.rect(screen, color, pygame.Rect(100, 100, 10, 10))
    while running:
        # Drawing Rectangle
        pygame.display.flip()
        pass

if __name__ == '__main__':
    game_loop()