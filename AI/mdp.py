import Draw
from AI import AStar
from Game import Game

actions_no_shoot = [([0, 0], False),
                    ([1, 0], False),
                    ([1, 1], False),
                    ([0, 1], False),
                    ([-1, 0], False),
                    ([-1, -1], False),
                    ([0, -1], False),
                    ([1, -1], False),
                    ([-1, 1], False)]
actions_shoot = [([0, 0], False),
                 ([1, 0], False),
                 ([1, 1], False),
                 ([0, 1], False),
                 ([-1, 0], False),
                 ([-1, -1], False),
                 ([0, -1], False),
                 ([1, -1], False),
                 ([-1, 1], False),
                 ([0, 0], True),
                 ([1, 0], True),
                 ([1, 1], True),
                 ([0, 1], True),
                 ([-1, 0], True),
                 ([-1, -1], True),
                 ([0, -1], True),
                 ([1, -1], True),
                 ([-1, 1], True)]


class MarkovDecisionProcess:
    @staticmethod
    def getPossibleActions(state: Game):
        """
        Return list of possible actions from 'state'.
        """
        dirs = MarkovDecisionProcess.directions_can_move(state)
        if state.player.cd.is_ready():
            return [(dir1, False) for dir1 in dirs] + [(dir1, True) for dir1 in
                                                       dirs]
        return [(dir1, False) for dir1 in dirs]

    @staticmethod
    def directions_can_move(state: Game):
        dirs = [[0, 0],
                [1, 0],
                [1, 1],
                [0, 1],
                [-1, 0],
                [-1, -1],
                [0, -1],
                [1, -1],
                [-1, 1]]
        for dir1 in dirs:
            if state.player.location[0] < 0 or state.player.location[
                0] > Draw.WIDTH or state.player.location[1] < 0 or \
                    state.player.location[1] > Draw.LENGTH:
                dirs.remove(dir1)
        return dirs

    def getReward(self, state: Game, action, next_state: Game, h=[1, 1, 1, 1]):
        """
        Get the reward for the state, action, nextState transition.

        Not available in reinforcement learning.
        """
        return h[0] * (next_state.player.score - state.player.score) + \
               h[1] * (10 if action[1] else 0) + \
               h[2] * (- 10000 if next_state.player.lives < state.player.lives else 0) + \
               h[3] * (AStar.distance(next_state.player.location, (Draw.WIDTH // 2, Draw.LENGTH // 2)) // 100)  # + 100 * AStar.hunt_close(state, action)
