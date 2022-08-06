from abc import abstractmethod
from typing import List, Tuple
import numpy as np
import pygame.sprite
import Draw
from DataStructures import PlayerSpriteGroup
from MovementDir import MovePattern, PlayerMovementPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite
import cooldown

class Player(BulletHellSprite):
    def __init__(self, location, sprite, speed = 10):
        super().__init__(location, sprite, PlayerMovementPattern((1, 1)))
        PlayerSpriteGroup.add(self)
        self.cd = cooldown.cooldown(10)
        self.speed = 10

    def get_location(self):
        return self.location

    # not sure if it is wise to do accelerated movement
    def action(self, direction, shoot):
        self.cd.update()
        self.location += direction * self.speed
        if shoot and self.cd.is_ready():
            self.cd.use()
            print("powpow")
            Projectile(self.location, "resources\\ball.png")