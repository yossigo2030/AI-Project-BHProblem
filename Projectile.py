import pygame.sprite

from DataStructures import ProjectileSpriteGroup, Directions, ProjectileEnemyGroup, ProjectilePlayerGroup
from MovementPatterns import StraightPattern, MovePattern
from Spriteables import BulletHellSprite


class Projectile(BulletHellSprite):
    def __init__(self, location, sprite, movement_pattern: MovePattern = StraightPattern(Directions.Up(10)), playerProjectile = False):
        super().__init__(location, sprite, movement_pattern=movement_pattern)
        ProjectileSpriteGroup.add(self)
        if playerProjectile:
            ProjectilePlayerGroup.add(self)
        else:
            ProjectileEnemyGroup.add(self)


    @staticmethod
    def update_all():
        for sprite in ProjectileSpriteGroup.sprites():
            sprite.update()

    @staticmethod
    def draw_all():
        for sprite in ProjectileSpriteGroup.sprites():
            sprite.draw()
