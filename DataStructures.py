from enum import Enum

import numpy as np
import pygame.sprite


class Directions(Enum):
    Up = np.array([0, -1])
    Down = np.array([0, 1])
    Left = np.array([-1, 0])
    Right = np.array([1, 0])

    def __call__(self, multiplier: float):
        return tuple(x * i for i, x in enumerate(self.value))


AllSpritesGroup = pygame.sprite.Group()
EnemySpriteGroup = pygame.sprite.Group()
ProjectileSpriteGroup = pygame.sprite.Group()
PlayerSpriteGroup = pygame.sprite.Group()
