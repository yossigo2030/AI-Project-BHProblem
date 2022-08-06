import pygame.sprite

from DataStructures import ProjectileSpriteGroup, Directions
from MovementPatterns import StraightPattern, MovePattern
from Spriteables import BulletHellSprite


class Projectile(BulletHellSprite):
    def __init__(self, location, sprite, movement_pattern: MovePattern):
        super().__init__(location, sprite, movement_pattern=StraightPattern(Directions.Up * 10))
        ProjectileSpriteGroup.add(self)


    @staticmethod
    def draw_all():
        for sprite in ProjectileSpriteGroup.sprites():
            sprite.update()
            sprite.draw()
