import sys

import pygame

import InputHandler
from AI.AStar import a_star_player, a_star_search_times
from AI.QLearner import QLearner
from CheapWave import CheapWave
from CollisionTestingWave import CollisionTestingWave
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
algs = ["aStar", "aStarT", "qLearn", "aStarT", "Genetic"]
tps = 60
NODECOUNT = 20
SKIPSTART = False
SAVETOFILE = False
TESTWAVE = False

running = True

pygame.font.init()
clock = pygame.time.Clock()
game = Game()
if TESTWAVE:
    game.wave = CollisionTestingWave(pygame.display.get_window_size(), game.data)
else:
    game.wave = CheapWave(pygame.display.get_window_size(), game.data)
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
        if InputHandler.quit() or game.player.lives == 0:
            running = False
        if alg == "aStar":
            if len(moves) < NODECOUNT * 0.25:
                moves = a_star_player(game, NODECOUNT)
            game.update(moves.pop(0), save_to_file=SAVETOFILE)
        elif alg == "aStarT":
            if search is None:
                search = a_star_search_times(game, 0.25)
            move = search()
            game.update(move, save_to_file=SAVETOFILE)
        elif alg == "qLearn" or alg == "qLearnFast":
            q.update_values(game)
            move = q.get_next_turn(game)
            game.update(move, save_to_file=SAVETOFILE)
        elif alg == "qLearnTest":
            q.update_values(game)
            move = q.get_next_turn(game)
            game.update(move, save_to_file=SAVETOFILE)
        else:
            game.update(save_to_file=SAVETOFILE)
        clock.tick(tps)
    print(game.player.score)
    print(game.frame)


if __name__ == '__main__':
    try:
        algorithm = sys.argv[1]
        if algorithm in algs:
            print(algorithm)
    except Exception:
        algorithm = None

    if type(algorithm) is str:
        if "qLearnTest" in algorithm:
            heuristics = [1, 1, 1, 1]
            print(len(sys.argv))
            if len(sys.argv) > 2:
                heuristics[0] = float(sys.argv[2])
            if len(sys.argv) > 3:
                heuristics[1] = float(sys.argv[3])
            if len(sys.argv) > 4:
                heuristics[2] = float(sys.argv[4])
            if len(sys.argv) > 5:
                heuristics[3] = float(sys.argv[5])
            q = QLearner((100, 100), future_steps=100, itercount=5000, epsilon=0.8, heuristics=heuristics)
        elif algorithm == "qLearnFast":
            q = QLearner((100, 100), future_steps=5, itercount=200, epsilon=0.8)  # calc board size based on player movespeed
        else:
            game_loop(algorithm)
            pygame.quit()
