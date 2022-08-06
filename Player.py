import InputHandler
from DataStructures import PlayerSpriteGroup
import cooldown
from DataStructures import PlayerSpriteGroup, Directions
from MovementPatterns import PlayerMovementPattern, StraightPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite


class Player(BulletHellSprite):
    def __init__(self, location, sprite, speed=10, shoot_cd=10, hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__(location, sprite, PlayerMovementPattern(speed, image_size), hitbox_size, image_size)
        PlayerSpriteGroup.add(self)
        self.cd = cooldown.cooldown(shoot_cd)
        self.iframe = cooldown.cooldown(20)
        self.speed = speed
        self.hitbox_backup = self.hitbox
        self.lives = 3

    def get_location(self):
        return self.location

    def on_hit(self):
        if self.iframe.is_ready():
            self.iframe.use()
            self.hitbox = (0, 0)
            self.lives -= 1
        return self.lives > 0

    def update(self):
        super().update()
        shoot = keybinds.get_shot()

        # Handle iFrames by removing the hitbox
        self.iframe.update()
        if self.iframe.is_ready():
            self.hitbox = self.hitbox_backup

        # Handle the shooting
        self.cd.update()
        if shoot and self.cd.is_ready():
            self.cd.use()
            Projectile(self.location, "resources\\ball.png", movement_pattern=StraightPattern(Directions.Up(10)), player_projectile=True)
