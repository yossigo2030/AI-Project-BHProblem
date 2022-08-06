import pygame.sprite
import Draw
from MovementDir import *


class BulletHellSprite(pygame.sprite.Sprite):
    def __init__(self, location, sprite, velocity: MovePattern = StraightPattern((1.0)), rect=pygame.rect.Rect(1, 1, 1, 1)):
        super().__init__()
        self.location = location
        self.image = pygame.image.load(sprite)
        self.rect = rect
        self.vel = velocity

    def update(self):
        self.location = self.location + self.vel.get_next_position(self.location)

    def draw(self):
        Draw.draw_sprite(self.image, self.location)
