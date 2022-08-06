from abc import abstractmethod
from typing import List, Tuple
import numpy as np
import pygame.sprite
import Draw
from DataStructures import PlayerSpriteGroup
from MovementDir import MovePattern, PlayerMovementPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite


class Player(BulletHellSprite):
    def __init__(self, location, sprite):
        super().__init__(location, sprite, PlayerMovementPattern((1, 1)))
        PlayerSpriteGroup.add(self)
        self.shot_cd = 60
        self.curr_cd = 0

    def get_location(self):
        return self.location

    # not sure if it is wise to do accelerated movement
    def action(self, direction, shoot):
        self.location += direction
        self.curr_cd += 1
        if shoot and self.curr_cd > self.shot_cd:
            print("powpow")
            Projectile(self.location, "resources\\ball.png")
            self.curr_cd = 0
