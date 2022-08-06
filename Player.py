from abc import abstractmethod
from typing import List, Tuple
import numpy as np
import pygame.sprite
import Draw
from DataStructures import PlayerSpriteGroup
from MovementDir import MovePattern, PlayerMovementPattern
from Projectile import Projectile
<<<<<<< HEAD
from Spriteables import BulletHellSprite
import cooldown
=======
from Spriteables import BulletHellSprite, out_of_bounds

>>>>>>> d19d5b3a0996d81dd29a3d13f6794b65b8db1162

class Player(BulletHellSprite):
    def __init__(self, location, sprite, speed = 10):
        super().__init__(location, sprite, PlayerMovementPattern((1, 1)))
        PlayerSpriteGroup.add(self)
<<<<<<< HEAD
        self.cd = cooldown.cooldown(10)
        self.speed = 10
=======
        self.shot_cd = 10
        self.curr_cd = 0
>>>>>>> d19d5b3a0996d81dd29a3d13f6794b65b8db1162

    def get_location(self):
        return self.location

<<<<<<< HEAD
    # not sure if it is wise to do accelerated movement
    def action(self, direction, shoot):
        self.cd.update()
        self.location += direction * self.speed
        if shoot and self.cd.is_ready():
            self.cd.use()
=======
    def action(self, direction, shoot):  # TODO: change the direction implementation to return the dict, and pass that to PlayerMovementPattern via varargs, which will handle the bound checks. this function should probably be update instead of action.
        newloc = self.location + direction * 10
        if not out_of_bounds(newloc, self.imsize):
            self.location += direction * 10
        self.curr_cd += 1
        if shoot and self.curr_cd > self.shot_cd:
>>>>>>> d19d5b3a0996d81dd29a3d13f6794b65b8db1162
            print("powpow")
            Projectile(self.location, "resources\\ball.png")