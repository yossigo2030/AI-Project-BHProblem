from abc import abstractmethod
from typing import List, Tuple

import numpy as np

Action = List[bool, bool, bool, bool, bool]  # representing left, right, up, down (arrows), and shoot.


class AIInteractions:
    @abstractmethod
    def get_actions(self, state) -> List[Action]:
        """
        :param state: A Bullet Hell Game State
        :return: a list of moves possible from the current state of the game
        """
        return

    def get_actions(self, state) -> List[Action]:
        """
        :param state: A Bullet Hell Game State
        :return: a list of moves possible from the current state of the game
        """
        return

    @abstractmethod
    def get_score(self, state, move: Action) -> float:
        """
        :param state: A Bullet Hell Game State
        :param move: the move to be taken at the current state of the game
        :return: the score obtained after 'move' is executed
        """
        return

    @abstractmethod
    def get_hit_score(self, state, move: Action) -> Tuple[float, float]:
        """
        :param state: A Bullet Hell Game State
        :param move: the move to be taken at the current state of the game
        :return: a tuple containing (MissOrHitOrKill, score)
        """
        return

    @abstractmethod
    def get_pickup_score(self, state, move: Action) -> float:
        """
        :param state: A Bullet Hell Game State
        :param move: the move to be taken at the current state of the game
        :return: the obtained score from pickups by taking the move
        """
        return

    @abstractmethod
    def get_board_danger_state(self, state) -> np.array:
        """
        Returns the danger value of each tile on discretised version of the game board
        :param state: A Bullet Hell Game Instance
        :return: a 2D array representing danger values ranging from 0 to 1 on each board tile.
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
