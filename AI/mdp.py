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
    def getStartState(self):
        """
        Return the start state of the MDP.
        """
        return Game()

    @staticmethod
    def getPossibleActions(state: Game):
        """
        Return list of possible actions from 'state'.
        """
        if state.player.cd.is_ready():
            return actions_shoot
        return actions_no_shoot

    def getTransitionStatesAndProbs(self, state: Game, action):
        """
        Returns list of (nextState, prob) pairs
        representing the states reachable
        from 'state' by taking 'action' along
        with their transition probabilities.

        Note that in Q-Learning and reinforcment
        learning in general, we do not know these
        probabilities nor do we directly model them.
        """
        # not as intended
        return state.__copy__().update(action)

    def getReward(self, state: Game, action, nextState: Game):
        """
        Get the reward for the state, action, nextState transition.

        Not available in reinforcement learning.
        """
        return nextState.player.score - state.player.score + (1 if action[1] else 0) - (10000 if nextState.player.lives < state.player.lives else 0)

    def isTerminal(self, state: Game):
        """
        Returns true if the current state is a terminal state.  By convention,
        a terminal state has zero future rewards.  Sometimes the terminal state(s)
        may have no possible actions.  It is also common to think of the terminal
        state as having a self-loop action 'pass' with zero reward; the formulations
        are equivalent.
        """
        return state.player.lives == 0
