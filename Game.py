from typing import Tuple

import pygame

import Draw
import EnemyType
import Player
import Projectile
import Spriteables
import Wave
import CollisionManager
from DataStructures import DataStructures


class Game:
    """
    Documentation goes here
    """

    def __init__(self, curr_frame=0, visual=True):
        self.data = DataStructures()
        self.frame = curr_frame
        self.visual = visual
        self.board_ratio = pygame.display.get_window_size()
        self.player = Player.Player((self.board_ratio[0] / 2, self.board_ratio[1]), r"resources\ship.png", self.data)
        self.wave = Wave.Wave(1, self.board_ratio, self.data)

    def update(self):
        self.frame += 1
        # player input and actions
        self.player.update()
        # enemy moves and actions
        Projectile.update_all(self.data)
        EnemyType.update_all(self.data)

        # Discard objects that are out of bounds
        Spriteables.sprite_culling(self.data)

        # check collisions
        self.player.set_score(CollisionManager.collision_check_enemies(self.data))
        CollisionManager.collision_check_player(self.data)

        # check pickup collisions


        # screen visual updates
        if self.visual:
            self.visual_update()

        # enemy spawning
        if self.wave.update() == 1:
            self.wave = Wave.Wave(self.wave.number_of_wave + 1, self.board_ratio, self.data)
        pygame.display.flip()

    def visual_update(self):
        Draw.redrawGameWindow()
        Projectile.draw_all(self.data)
        EnemyType.draw_all(self.data)
        self.player.draw()

    def convert_to_array(self, dims: Tuple[int, int]):
        array = [[[] for i in range(dims[0])] for j in range(dims[1])]
        for enemy in self.data.EnemySpriteGroup:
            location = self.location_convert(enemy.location, dims)
            array[location[0]][location[1]].append(enemy)
        for projectile in self.data.ProjectileSpriteGroup:
            location = self.location_convert(projectile.location, dims)
            array[location[0]][location[1]].append(projectile)
        return array

    def location_convert(self, coords, dims) -> Tuple[int, int]:
        return coords[0] // dims[0], coords[1] // dims[1]
