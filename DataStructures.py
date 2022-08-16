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


AllSpritesGroup = pygame.sprite.Group()
EnemySpriteGroup = pygame.sprite.Group()
EnemyBossSpriteGroup = pygame.sprite.Group()
ProjectileSpriteGroup = pygame.sprite.Group()
ProjectileEnemyGroup = pygame.sprite.Group()
ProjectilePlayerGroup = pygame.sprite.Group()
PlayerSpriteGroup = pygame.sprite.Group()
