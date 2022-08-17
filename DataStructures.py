from enum import Enum
import pygame.sprite

thingy = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]


class Directions(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3
    Static = 4

    def __call__(self, multiplier: float):
        return tuple(thingy[self.value][i] * multiplier for i in range(2))


# todo make data bases singular instead of global
class dataStructures:
    def __init__(self):
        self.AllSpritesGroup = pygame.sprite.Group()
        self.EnemySpriteGroup = pygame.sprite.Group()
        self.EnemyBossSpriteGroup = pygame.sprite.Group()
        self.ProjectileSpriteGroup = pygame.sprite.Group()
        self.ProjectileEnemyGroup = pygame.sprite.Group()
        self.ProjectilePlayerGroup = pygame.sprite.Group()
        self.PlayerSpriteGroup = pygame.sprite.Group()
