from abc import abstractmethod
from typing import Tuple

import Draw
import InputHandler
from metrix import *

Position = Tuple[int or float]
Velocity = Tuple[int or float]


class MovePattern:
    def __init__(self, velocity: Velocity):
        self.velocity = velocity

    def __copy__(self):
        return self

    @abstractmethod
    def get_next_position(self, current_position: Position):
        pass


class StraightPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        return tuple(x + self.velocity[i] for i, x in enumerate(current_position))


class CurvedPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        pass


class WavyPattern(MovePattern):
    """ WIP """

    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        pass


class TargetComplexPosPattern(MovePattern):
    def __init__(self, speed, target_obj): # target obj is a Spriteables
        super().__init__(speed)
        self.counter = 0
        self.target = target_obj

    def get_next_position(self, current_position: Position):
        target_pos = self.target.location
        # print(f"Player position: {target_pos}, and current position: {current_position}")
        vel = np.array([target_pos[i] - current_position[i] for i in range(2)])
        vel = -vel / abs(vel.sum()) * self.velocity
        return [current_position[i] + vel[i] for i in range(2)]


class TargetPosPattern(MovePattern):
    def __init__(self, speed, target_pos: Tuple[int, int]):
        super().__init__(speed)
        self.target = target_pos
        self.counter = 0
        self.vel = (0, 0)
        self.is_first_time = True

    def get_next_position(self, current_position: Position):
        if self.is_first_time:
            self.is_first_time = False
            target_pos = self.target
            vel = np.array([target_pos[i] - current_position[i] for i in range(2)])
            vel = vel / (np.linalg.norm(vel))
            self.vel = vel * self.velocity
        return [current_position[i] + self.vel[i] for i in range(2)]


class CrazyPattern(MovePattern):
    def __init__(self, velocity: Velocity):
        super().__init__(velocity)
        self.counter = 0

    def get_next_position(self, current_position: Position):
        pass


class PlayerMovementPattern(MovePattern):
    def __init__(self, speed, image_size):
        super().__init__(tuple())
        self.speed = speed
        self.imsize = image_size

    def get_next_position(self, current_position: Position):
        direction = InputHandler.get_input()
        new_loc = current_position + direction * self.speed
        final_loc = list(current_position)
        if not out_of_bounds_player((new_loc[0], current_position[1]), (self.imsize[0] / 2, self.imsize[1] / 2)):
            final_loc[0] = new_loc[0]
        if not out_of_bounds_player((current_position[0], new_loc[1]), (self.imsize[0] / 2, self.imsize[1] / 2)):
            final_loc[1] = new_loc[1]
        return final_loc


def out_of_bounds_player(location, sprite_size):
    return location[0] < 0 or location[0] > Draw.WIDTH or location[1] < 0 or location[1] > Draw.LENGTH
