import pygame.sprite

from DataStructures import ProjectileSpriteGroup
from MovementDir import StraightPattern
from Spriteables import BulletHellSprite


class Projectile(BulletHellSprite):
    def __init__(self, location, sprite, direction=(0, -1), speed=5):
        super().__init__(location, sprite, velocity=StraightPattern((0, -1)))
        ProjectileSpriteGroup.add(self)


    @staticmethod
    def draw_all():
        for sprite in ProjectileSpriteGroup.sprites():
            sprite.update()
            sprite.draw()
        print("Done drawing!")
