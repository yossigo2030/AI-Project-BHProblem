from enum import Enum

import pygame.sprite
import numpy as np


class Directions(Enum):
    Up = (0, -1)
    Down = (0, 1)
    Left = (-1, 0)
    Right = (1, 0)

    def dir_multiply(self, dir: Directions, multiplier: float):
        return tuple()


AllSpritesGroup = pygame.sprite.Group()
EnemySpriteGroup = pygame.sprite.Group()
ProjectileSpriteGroup = pygame.sprite.Group()
PlayerSpriteGroup = pygame.sprite.Group()
