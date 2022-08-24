from abc import abstractmethod
from typing import List, Tuple

import numpy as np

from Game import Game


Action = List[bool, bool, bool, bool, bool]  # representing left, right, up, down (arrows), and shoot.
State = object


# TODO: make an object that has the contents of the gameplay loop, and then
#  copy it for Ai use. simulate it playing theoretical scenerios
#  to choose the correct move for this frame, this object will be named
#  gameState

# also TODO: change functions that take (state, movement) pairs to instead.. uhh, idk. do something else.
# consider that we have another issue - we cannot determine inside A* whether or not a shoot action led to a hit immediately.

class BHProblem:
    """
    The basic Bullet Hell Problem wrapper class. Handles the AI <- Game communication
    necessary for solving the problem.
    """
    @abstractmethod
    def get_next_start_state(self) -> Game:
        """
        :return: returns the current starting state.
        On the first call, it's the default starting state. any successive calls are expected to be done with
        a new position set.
        """
        return

    @abstractmethod
    def get_successors(self, state: Game) -> List[Tuple[State, Action, int]]:
        """
        :param state: A Bullet Hell Game State
        :return: a list of (curr_state, move, score) resulting for all possible moves from the current state of the game
        move is the move which takes state to curr_state
        """
        return

    @abstractmethod
    def get_state_score(self, state: Game) -> float:
        """
        :param state: A Bullet Hell Game State
        :return: the total score accrued over the course of the game.
        """
        return

    @abstractmethod
    def get_score(self, state: Game, move: Action) -> float:
        """
        :param state: A Bullet Hell Game State
        :param move: the move to be taken at the current state of the game
        :return: the score obtained by executing 'move'
        this is effectively the sum of get_hit_score[1] and get_pickup_score.
        """
        return

    @abstractmethod
    def get_hit_score(self, state: Game, move: Action) -> Tuple[float, float]:
        """
        :param state: A Bullet Hell Game State
        :param move: the move to be taken at the current state of the game
        :return: a tuple containing (MissOrHitOrKill, hit_score)
        """
        return

    @abstractmethod
    def get_pickup_score(self, state: Game, move: Action) -> float:
        """
        :param state: A Bullet Hell Game State
        :param move: the move to be taken at the current state of the game
        :return: the obtained score from pickups by taking the move
        """
        return

    @abstractmethod
    def get_board_danger_state(self, state: Game, n_turns: int) -> np.array:
        """
        Returns the danger value of each tile on discretised version of the game board
        :param n_turns: The number of turns into the future over which the danger is calculated
        :param state: A Bullet Hell Game Instance
        :return: a 2D array representing danger values ranging from 0 to 1 on each board tile.
        """
        return

    @abstractmethod
    def get_actions(self, state: Game) -> List[Action]:
        """
        :param state: A Bullet Hell Game State
        :return: a list of moves possible from the current state of the game
        """
        return


class RunnerAPI:
    @abstractmethod
    def execute_action(self, move: Action):
        """
        Executes the given action.
        :param move: Action to execute
        """
        return
