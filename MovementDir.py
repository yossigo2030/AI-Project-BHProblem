from abc import abstractmethod
from enum import Enum
from typing import List, Tuple

Position = Tuple[float]
Velocity = Tuple[float]


class MovePattern:
    def __init__(self, velocity: Velocity):
        self.velocity = velocity

    @abstractmethod
    def get_next_position(self, current_position: Position):
        pass


class StraightPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        return tuple(x + self.velocity[0] for x in current_position)


class CurvedPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        pass


class WavyPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        pass


class CrazyPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        pass


class PlayerMovementPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)

    def get_next_position(self, current_position: Position):
        return current_position
