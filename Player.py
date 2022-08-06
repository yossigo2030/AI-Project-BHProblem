from abc import abstractmethod
from typing import List, Tuple

import numpy as np

import Draw
from MovementDir import MovePattern, PlayerMovementPattern
from Spriteables import BulletHellSprite


class Player(BulletHellSprite):
    def __init__(self, location, sprite):
        super().__init__(location, sprite, PlayerMovementPattern((1)))

    def get_location(self):
        return self.location

    # not sure if it is wise to do accelerated movement
    def action(self, direction, shoot):
        self.location += direction 
        if shoot:
            pass

    def draw(self):
        Draw.draw_blank_square_at_loc(self.location)
