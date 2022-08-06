from abc import abstractmethod
from typing import List, Tuple
import numpy as np
import pygame.sprite
import Draw
from DataStructures import PlayerSpriteGroup
from MovementDir import MovePattern, PlayerMovementPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite, out_of_bounds


class Player(BulletHellSprite):
    def __init__(self, location, sprite):
        super().__init__(location, sprite, PlayerMovementPattern((1, 1)))
        PlayerSpriteGroup.add(self)
        self.shot_cd = 10
        self.curr_cd = 0

    def get_location(self):
        return self.location

    def action(self, direction, shoot):  # TODO: change the direction implementation to return the dict, and pass that to PlayerMovementPattern via varargs, which will handle the bound checks. this function should probably be update instead of action.
        newloc = self.location + direction * 10
        if not out_of_bounds(newloc, self.imsize):
            self.location += direction * 10
        self.curr_cd += 1
        if shoot and self.curr_cd > self.shot_cd:
            print("powpow")
            Projectile(self.location, "resources\\ball.png")
            self.curr_cd = 0
