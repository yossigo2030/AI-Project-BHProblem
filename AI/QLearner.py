import random
import sys

import numpy as np

from AI.mdp import MarkovDecisionProcess
from Game import Game


class QLearner:
    def __init__(self, board_size, future_steps=10, itercount=1000, epsilon=0.1):
        # Q is a [board_size] matrix, by [shoot/notshoot], over [future_steps] turns
        self.Q = np.zeros((board_size[0], board_size[1], 2, future_steps))  # index order is retardium. should be reversed.
        self.bs = board_size
        self.lr = 0.8  # TODO discount the LR into the future
        self.gamma = 0.9
        self.steps = future_steps
        self.itercount = itercount
        self.eps = epsilon
        self.mdp = MarkovDecisionProcess()
        np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)

    def update_values(self, state: Game):
        for i in range(self.itercount // self.steps):
            cs = state.__copy__(False)
            for j in range(self.steps):
                pa = self.mdp.getPossibleActions(cs)
                if random.uniform(0, 1) < self.eps:
                    """ Explore: select a random action """
                    action = pa[round(random.uniform(0, max(len(pa) - 1, 0)))]
                else:
                    """ Exploit: select the action with max value (future reward) """
                    action = pa[round(random.uniform(0, max(len(pa) - 1, 0)))]  # TODO
                ns = cs.__copy__(False)
                ns.update(action)
                reward = self.mdp.getReward(cs, action, ns)

                xc, yc = cs.get_player_loc(self.bs)
                xn, yn = ns.get_player_loc(self.bs)

                cs = ns
                xlocs = [int(xn + x - 1) for x in range(3) if 0 <= xn + x - 1 < self.bs[0]]
                ylocs = [int(yn + y - 1) for y in range(3) if 0 <= yn + y - 1 < self.bs[1]]
                if j + 1 < self.steps:
                    max_of_future = np.max([self.Q[x][y][int(action[1])][j + 1] for x in xlocs for y in ylocs])  # TODO check logic. action might need to be abs(action[1] - 1)
                else:
                    max_of_future = 0
                self.Q[xc][yc][int(action[1])][j] += self.lr * (reward + self.gamma * max_of_future - self.Q[xc][yc][int(action[1])][j])

    def next_turn(self, game):
        x, y = game.get_player_loc(self.bs)
        # we get value from max_of_future = np.max([self.Q[x][y][shoot][1] for x in xlocs for y in ylocs for shoot in range (2)])
        # TODO might be better to rely on the possible actions and pickt he one with the highest value instead of scanning the array.
        xlocs = [int(x + a - 1) for a in range(3) if 0 <= x + a - 1 < self.bs[0]]
        ylocs = [int(y + b - 1) for b in range(3) if 0 <= y + b - 1 < self.bs[1]]
        max_of_future = np.max([self.Q[x][y][shoot][1] for x in xlocs for y in ylocs for shoot in range(2)])
        loc = np.where(self.Q == max_of_future)
        nx, ny, a = loc[0][0], loc[1][0], loc[2][0]

        move1 = max(min(nx - x, 1), -1)
        move2 = max(min(ny - y, 1), -1)
        return (move1, move2), a

    def print_at_depth(self, game, d=0):
        # np.unravel_index(self.Q.argmax(), self.Q.shape)
        # self.Q[0][99][1][0]
        x, y = game.get_player_loc(self.bs)

        mat_ya = self.Q[::, ::, 0, d].T
        mat_na = self.Q[::, ::, 1, d].T
        print(f"depth {d}\nNo shoot:")
        print(np.array_str(mat_ya[x - 8:x + 9, y - 8:y + 9], precision=1, suppress_small=True))
        print("Yes Shoot:")
        print(np.array_str(mat_na[x - 8:x + 9, y - 8:y + 9], precision=1, suppress_small=True))
        print(f"")
