import pygame.sprite
import Draw
from MovementDir import *


class BulletHellSprite(pygame.sprite.Sprite):
    def __init__(self, location, sprite, velocity: MovePattern = StraightPattern((1.0)), hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__()
        self.location = location
        self.image = pygame.transform.scale(pygame.image.load(sprite).convert(), image_size)
        self.imsize = image_size
        self.hitbox = hitbox_size
        self.vel = velocity

    def update(self):
        self.location = self.location + self.vel.get_next_position(self.location)

    def draw(self):
        Draw.draw_sprite(self.image, self.location)
