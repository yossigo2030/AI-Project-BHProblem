from typing import Tuple

import InputHandler
import cooldown
from DataStructures import Directions, DataStructures
from MovementPatterns import PlayerMovementPattern, StraightPattern, out_of_bounds_player
from Projectile import Projectile
from Spriteables import BulletHellSprite


class Player(BulletHellSprite):
    def __init__(self, location, sprite, data, speed=10, shoot_cd=10, hitbox_size=(25, 25), image_size=(40, 40), shoot_cc=None):
        super().__init__(location, sprite, data, PlayerMovementPattern(speed, image_size), hitbox_size, image_size)
        self.data.PlayerSpriteGroup.add(self)
        self.cd = cooldown.cooldown(shoot_cd, shoot_cc)
        self.iframe = cooldown.cooldown(20)
        self.speed = speed
        self.hitbox_backup = self.hitbox
        self.lives = 3
        self.score = 0

    def get_location(self):
        return self.location

    def set_score(self, add):
        self.score += add

    def __copy__(self, data):
        return Player(self.location, self.sprite, data, speed=self.speed, shoot_cd=self.cd.time, hitbox_size=self.hitbox_backup, image_size=self.imsize, shoot_cc=self.cd.counter)

    def on_hit(self):
        if self.iframe.is_ready():
            self.iframe.use()
            self.hitbox = (0, 0)
            self.lives -= 1
        return self.lives > 0

    def update(self):
        super().update()
        shoot = InputHandler.get_shot()

        # Handle iFrames by removing the hitbox
        self.iframe.update()
        if self.iframe.is_ready():
            self.hitbox = self.hitbox_backup

        # Handle the shooting
        self.cd.update()
        if shoot and self.cd.is_ready():
            self.cd.use()
            Projectile(self.location, "resources\\ball.png", self.data, movement_pattern=StraightPattern(Directions.Up(10)), player_projectile=True)

    def updateWrapper(self, move: Tuple[Tuple[int, int], bool] = None):
        if move is None:
            self.update()
        else:
            current_position = self.location
            new_loc = current_position + move[0] * self.speed
            final_loc = list(current_position)
            if not out_of_bounds_player((new_loc[0], current_position[1]), (self.imsize[0] / 2, self.imsize[1] / 2)):
                final_loc[0] = new_loc[0]
            if not out_of_bounds_player((current_position[0], new_loc[1]), (self.imsize[0] / 2, self.imsize[1] / 2)):
                final_loc[1] = new_loc[1]

            shoot = move[1]

            # Handle iFrames by removing the hitbox
            self.iframe.update()
            if self.iframe.is_ready():
                self.hitbox = self.hitbox_backup

            # Handle the shooting
            self.cd.update()
            if shoot and self.cd.is_ready():
                self.cd.use()
                Projectile(self.location, "resources\\ball.png", self.data, movement_pattern=StraightPattern(Directions.Up(10)), player_projectile=True)
