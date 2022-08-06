from abc import abstractmethod
from typing import List, Tuple
import numpy as np
import pygame.sprite
import Draw
from DataStructures import PlayerSpriteGroup
from MovementPatterns import MovePattern, PlayerMovementPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite
import cooldown
from Spriteables import BulletHellSprite, out_of_bounds


class Player(BulletHellSprite):
    def __init__(self, location, sprite, speed=10):
        super().__init__(location, sprite, PlayerMovementPattern((1, 1)))
        PlayerSpriteGroup.add(self)
        self.shot_cd = 10
        self.curr_cd = 0
        self.cd = cooldown.cooldown(10)
        self.speed = 10

    def get_location(self):
        return self.location

    def action(self, direction, shoot):  # TODO: change the direction implementation to return the dict, and pass that to PlayerMovementPattern via varargs, which will handle the bound checks. this function should probably be update instead of action.
        newloc = self.location + direction * self.speed
        if not out_of_bounds(newloc, self.imsize):
            self.location = newloc
        self.cd.update()
        if shoot and self.cd.is_ready():
            self.cd.use()
            print("powpow")
            Projectile(self.location, "resources\\ball.png")
            self.curr_cd = 0
