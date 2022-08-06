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

    def get_location(self):
        return self.location

    # not sure if it is wise to do accelerated movement
    def action(self, direction, shoot):
        self.location += direction
        if shoot:
            print("powpow")
            Projectile(self.location, "resources\ship.png")
