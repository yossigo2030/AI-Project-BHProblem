import random

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

    def update_values(self, state: Game):
        for i in range(self.itercount // self.steps):
            cs = state.__copy__()
            for j in range(self.steps):
                pa = self.mdp.getPossibleActions(cs)
                if random.uniform(0, 1) < self.eps:
                    """ Explore: select a random action """
                    action = pa[round(random.uniform(0, max(len(pa) - 1, 0)))]
                else:
                    """ Exploit: select the action with max value (future reward) """
                    action = pa[round(random.uniform(0, max(len(pa) - 1, 0)))]  # TODO
                ns = cs.__copy__()
                ns.update(action)
                reward = self.mdp.getReward(cs, action, ns)
                cs = ns

                xc, yc = cs.get_player_loc(self.bs)
                xn, yn = ns.get_player_loc(self.bs)
                xlocs = [int(xn + x - 1) for x in range(3) if 0 <= xn + x - 1 < self.bs[0]]
                ylocs = [int(yn + y - 1) for y in range(3) if 0 <= yn + y - 1 < self.bs[1]]
                if j + 1 < self.steps:
                    max_of_future = np.max([self.Q[x][y][1][j + 1] for x in xlocs for y in ylocs])  # TODO check logic
                else:
                    max_of_future = 0
                self.Q[xc][yc][int(action[1])][j] += self.lr * (reward + self.gamma * max_of_future - self.Q[xc][yc][int(action[1])][j])

    def next_turn(self):
        pass

    def print_at_depth(self, d=0):
        # np.unravel_index(self.Q.argmax(), self.Q.shape)
        # self.Q[0][99][1][0]

        mat_ya = self.Q[:][:][0][d]
        mat_na = self.Q[:][:][1][d]
        print(f"depth {d}")
        print(mat_ya)
        print(mat_na)
