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


class DataStructures:
    def __init__(self):
        self.AllSpritesGroup = pygame.sprite.Group()
        self.EnemySpriteGroup = pygame.sprite.Group()
        self.EnemyBossSpriteGroup = pygame.sprite.Group()
        self.ProjectileSpriteGroup = pygame.sprite.Group()
        self.ProjectileEnemyGroup = pygame.sprite.Group()
        self.ProjectilePlayerGroup = pygame.sprite.Group()
        self.PlayerSpriteGroup = pygame.sprite.Group()

    def __copy__(self):
        datastructures = DataStructures()
        DataStructures.copy_bullet_hell_sprite(self.AllSpritesGroup, datastructures)
        DataStructures.copy_bullet_hell_sprite(self.EnemySpriteGroup, datastructures)
        DataStructures.copy_bullet_hell_sprite(self.EnemyBossSpriteGroup, datastructures)
        DataStructures.copy_bullet_hell_sprite(self.ProjectileSpriteGroup, datastructures)
        DataStructures.copy_bullet_hell_sprite(self.ProjectileEnemyGroup, datastructures)
        DataStructures.copy_bullet_hell_sprite(self.ProjectilePlayerGroup, datastructures)
        DataStructures.copy_bullet_hell_sprite(self.PlayerSpriteGroup, datastructures)
        return datastructures

    @staticmethod
    def copy_bullet_hell_sprite(array1, array2):
        for sprite in array1:
            sprite.__copy__(array2)
