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
        """
        Okay okay new plan: move all the sprite groups into a dictionary, then dynamically create accessor methods with the correct name to access the groups. and then the copy can just use the dictionary to copy properly.
        """
        self.AllSpritesGroup = pygame.sprite.Group()
        self.EnemySpriteGroup = pygame.sprite.Group()
        self.EnemyBossSpriteGroup = pygame.sprite.Group()
        self.ProjectileSpriteGroup = pygame.sprite.Group()
        self.ProjectileEnemyGroup = pygame.sprite.Group()
        self.ProjectilePlayerGroup = pygame.sprite.Group()
        self.PlayerSpriteGroup = pygame.sprite.Group()

    def copy(self, players=True, enemies=True, projectiles_hostile=True, projectile_friendly=True):
        data_structure = DataStructures()
        for sprite in self.AllSpritesGroup:
            sprite_new = sprite.__copy__(data_structure)
            if enemies and sprite in self.EnemySpriteGroup:
                data_structure.EnemySpriteGroup.add(sprite_new)
            if enemies and sprite in self.EnemyBossSpriteGroup:
                data_structure.EnemyBossSpriteGroup.add(sprite_new)
            if projectiles_hostile and sprite in self.ProjectileEnemyGroup:
                data_structure.ProjectileEnemyGroup.add(sprite_new)
                data_structure.ProjectileSpriteGroup.add(sprite_new)
            if projectile_friendly and sprite in self.ProjectilePlayerGroup:
                data_structure.ProjectilePlayerGroup.add(sprite_new)
                data_structure.ProjectileSpriteGroup.add(sprite_new)
            if players and sprite in self.PlayerSpriteGroup:
                data_structure.PlayerSpriteGroup.add(sprite_new)
        return data_structure

    def __copy__(self):
        return self.copy()
