import random
import sys

import numpy as np
import heatmap

from AI.mdp import MarkovDecisionProcess
from Game import Game


class QLearner:
    """
    # TODO - double check the logic, i think it's not right. especially regarding the shoot / no shoot split.
        There is the issue of whether or not i need to sample the current time or the next time in the Q matrix
        The updates might be wrong in some fashion.
        Discount factor... might want it to be higher?
        Maybe modify max_of_future to be a weighted average instead, which would backprop danger more effectively.
        Modify the heuristics to include extra motivation to remain in the center of the map
        Also consider either accounting for future hits
        Idea: instead of two Q matrices per time stamp, calculate the shooting rewards separately..?
    """

    def __init__(self, board_size, future_steps=10, itercount=1000, epsilon=0.8, negeps=0.5):
        # Q is a [board_size] matrix, by [shoot/notshoot], over [future_steps] turns
        self.Q = np.zeros((board_size[0], board_size[1], future_steps))  # index order is retardium. should be reversed.
        self.bs = board_size
        self.lr = 0.8  # TODO discount the LR into the future
        self.gamma = 0.9
        self.steps = future_steps
        self.itercount = itercount
        self.eps = epsilon
        self.negeps = negeps
        self.mdp = MarkovDecisionProcess()
        np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)

    def update_values(self, state: Game):
        Q = np.zeros_like(self.Q)
        Q[::, ::, :self.steps - 1] = self.Q[::, ::, 1:]
        self.Q = Q
        for i in range(self.itercount // self.steps):
            cs = state.__copy__(False)
            reward = 0
            for j in range(self.steps):
                pa = self.mdp.getPossibleActions(cs)
                xc, yc = cs.get_player_loc(self.bs)
                # TODO by removing the action matrix, i need a better way to determine when to shoot or not. probably a future hit based approach, in the meantime just perma shoot.
                if random.uniform(0, 1) < self.eps:  # TODO so, just more backprop..? take the average reward of future instead of best? who knows.
                    """ Explore: select a random action """
                    action = pa[round(random.uniform(0, max(len(pa) - 1, 0)))]
                elif random.uniform(0, 1) < self.negeps:
                    """ Exploit but negative """
                    action = self.get_best_action(xc, yc, pa, inverted=True, c_j=j)[0]
                else:
                    """ Exploit: select the action with max value (future reward) """
                    action = self.get_best_action(xc, yc, pa, c_j=j)[0]
                ns = cs.__copy__(False)
                ns.update(action)
                reward += self.mdp.getReward(cs, action, ns)
                xn, yn = ns.get_player_loc(self.bs)
                cs = ns

                # xlocs = [int(xn + x - 1) for x in range(3) if 0 <= xn + x - 1 < self.bs[0]]
                # ylocs = [int(yn + y - 1) for y in range(3) if 0 <= yn + y - 1 < self.bs[1]]
                if j <= self.steps:
                    # max_of_future = np.max([self.Q[x][y][j + 1] for x in xlocs for y in ylocs])  # TODO change this to the other thing
                    max_of_future = self.get_best_action(xn, yn, pa, c_j=j)[1]
                    # TODO reward should be calculated relative to the start, not relative to the next turn.
                    average_of_future = self.get_action_average(xn, yn, pa, c_j=j)
                else:
                    max_of_future = 0
                    average_of_future = 0

                # self.Q[xc][yc][j] += self.lr * (reward + self.gamma * max_of_future - self.Q[xc][yc][j])
                self.Q[xc][yc][j] += self.lr * (reward + self.gamma * average_of_future - self.Q[xc][yc][j])
        heatmap.show_map([self.Q[::, ::, i].T for i in range(self.steps)], True, f"mdp/{state.frame:04}.png")
        heatmap.show_map([self.Q[::, ::, i].T for i in range(self.steps)], True)

    def get_next_turn(self, state: Game):
        pa = self.mdp.getPossibleActions(state)
        x, y = state.get_player_loc(self.bs)
        act = self.get_best_action(x, y, pa, c_j=1)[0]
        return act[0], True

    def get_best_action(self, x, y, action_list, inverted=False, c_j=0):
        bestrew = np.inf if inverted else -np.inf
        act = None
        for action in action_list:
            nx, ny = self.clamp(x + action[0][0], self.bs[0] - 1), self.clamp(y + action[0][1], self.bs[1] - 1)
            rew = self.Q[nx][ny][c_j]
            if inverted:
                if rew < bestrew:
                    bestrew = rew
                    act = action
            else:
                if rew > bestrew:
                    bestrew = rew
                    act = action
        return act, bestrew

    def get_action_average(self, x, y, action_list, c_j=0):
        rew_acc = 0
        for action in action_list:
            nx, ny = self.clamp(x + action[0][0], self.bs[0] - 1), self.clamp(y + action[0][1], self.bs[1] - 1)
            rew = self.Q[nx][ny][c_j]
            rew_acc += rew
        return rew_acc / len(action_list)

    @staticmethod
    def clamp(val, max_, min_=0):
        return min(max(val, min_), max_)

    def print_at_depth(self, game, d=0):
        # np.unravel_index(self.Q.argmax(), self.Q.shape)
        # self.Q[0][99][1][0]
        x, y = game.get_player_loc(self.bs)

        mat_ya = self.Q[::, ::, d].T
        print(f"depth {d}\n:")
        print(np.array_str(mat_ya[y - 8:y + 9, x - 8:x + 9], precision=1, suppress_small=True))
        print(f"")
