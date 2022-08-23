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
from AI.mdp import MarkovDecisionProcess as MDP

class Game:
    """
    Documentation goes here
    """

    def __init__(self, curr_frame=0, visual=True, player=None, board_ratio=pygame.display.get_window_size(), wave=None, data=DataStructures()):
        self.frame = curr_frame
        self.visual = visual
        self.board_ratio = board_ratio
        self.data = data
        if player is None:
            player = Player.Player((self.board_ratio[0] / 2, self.board_ratio[1] / 2), r"resources\ship.png", self.data)
        self.player = player
        if wave is None:
            wave = Wave.Wave(1, self.board_ratio, self.data)
        self.wave = wave

    def __copy__(self, visuals=True):
        data = self.data.__copy__()
        return Game(self.frame, visuals, [x for x in data.PlayerSpriteGroup][0], self.board_ratio, self.wave.__copy__(data), data)

    def update(self, move=None):
        self.frame += 1
        self.player.set_score(1)
        # player input and actions
        self.player.updateWrapper(move)
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

    def get_player_loc(self, dims: Tuple[int, int]):
        return self.location_convert(self.player.location, dims)

    def location_convert(self, coords, dims) -> Tuple[int, int]:
        return min(int(coords[0] / self.board_ratio[0] * dims[0]), dims[0] - 1), \
               min(int(coords[1] / self.board_ratio[1] * dims[1]), dims[1] - 1)

    def get_next_start_state(self):
        """
        :return: returns the current starting state.
        On the first call, it's the default starting state. any successive calls are expected to be done with
        a new position set.
        """
        return self

    def get_successors(self):
        """
        :param state: A Bullet Hell Game State
        :return: a list of (curr_state, move, score) resulting for all possible moves from the current state of the game
        move is the move which takes state to curr_state
        """
        # get player moves
        games = [[Game.__copy__(self), move, 0] for move in MDP.getPossibleActions(self)]
        for game in games:
            game[0].update(game[1])
            game[2] = self.delta_score(game[0])
        return [tuple(i) for i in games]

    def delta_score(self, after_play, move=None):
        return after_play.player.score - self.player.score

    def get_state_score(self):
        return self.player.score

    def get_not_move(self, next_copy):
        return self.player.location == next_copy.player.location

    def predict_projectiles_Score(self, depth = 4):
        data = self.data.copy(True, True, False, True)
        copy = Game(self.frame, False, [x for x in data.PlayerSpriteGroup][0], self.board_ratio, self.wave.__copy__(data), data)
        score = 0
        while copy.data.ProjectilePlayerGroup and depth:
            copy.update()
            score += CollisionManager.collision_check_enemies(data)
            depth -= 1
        return score
