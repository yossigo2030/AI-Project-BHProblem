import random
from typing import Tuple

import pygame

import CheapWave
import CollisionTestingWave
import Draw
import EnemyType
import Player
import Projectile
import Spriteables
import Wave
import CollisionManager
from DataStructures import DataStructures
import AI
from metrix import *


class Game:
    """
    Documentation goes here
    """

    def __init__(self, curr_frame=0, visual=True, player=None, board_ratio=pygame.display.get_window_size(), wave=None, data=None,  brain=None):
        self.frame = curr_frame
        self.visual = visual
        self.board_ratio = board_ratio
        self.data = DataStructures() if data is None else data
        ################
        self.neural_network = brain
        self.m = metrix(self.neural_network, self.data)
        #################
        if player is None:
            player = Player.Player((self.board_ratio[0] / 2, self.board_ratio[1] / 2), r"resources\ship.png", self.data)
        self.player = player
        if wave is None:
            # wave = Wave.Wave(1, self.board_ratio, self.data)
            wave = CheapWave.CheapWave(self.board_ratio, self.data)
        self.wave = wave
        self.is_genetic = bool(brain)

    #     self._hash = int(random.uniform(-10000000000, 10000000000))
    #
    # def __hash__(self):
    #     return self._hash

    def __copy__(self, visuals=False):
        data = self.data.__copy__()
        return Game(self.frame, visuals, [x for x in data.PlayerSpriteGroup][0], self.board_ratio, self.wave.__copy__(data), data)

    def update(self, move=None, save_to_file=False):
        self.frame += 1
        # self.player.increment_score(1)
        # player input and actions
        self.player.updateWrapper(move)
        # enemy moves and actions
        Projectile.update_all(self.data)
        EnemyType.update_all(self.data)

        #################
        if self.is_genetic:
            self.m.round()
        ################

        # Discard objects that are out of bounds
        Spriteables.sprite_culling(self.data)

        # check collisions
        lives = self.player.lives
        self.player.increment_score(CollisionManager.collision_check_enemies(self.data))
        CollisionManager.collision_check_player(self.data)
        if self.visual and lives > self.player.lives:
            print(f"Player hit :(, now at {self.player.lives} lives")

        # check pickup collisions

        # screen visual updates
        if self.visual:
            self.visual_update()

        # enemy spawning
        if self.wave.update() == 1:
            pass
            # self.wave = Wave.Wave(self.wave.number_of_wave + 1, self.board_ratio, self.data)

        if self.visual:
            pygame.display.flip()

        if self.visual and save_to_file:
            pygame.image.save(pygame.display.get_surface(), f"results/{self.frame:05}.png")


    def visual_update(self):
        Draw.redrawGameWindow()
        Projectile.draw_all(self.data)
        EnemyType.draw_all(self.data)
        for i in self.data.BonusGroup: i.draw()
        self.player.draw()
        Draw.write_score_and_hp(self.player.score, self.player.lives)

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
        games = [[self.__copy__(), move, 0] for move in AI.mdp.MarkovDecisionProcess.getPossibleActions(self)]
        for game in games:
            game[0].update(game[1])
            game[2] = self.delta_score(game[0], game[1])
        return [tuple(i) for i in games]

    def delta_score(self, after_play, move=None):
        return after_play.player.score - self.player.score + self.get_not_move(move) * 100

    def get_state_score(self):
        return self.player.score

    @staticmethod
    def get_not_move(move):
        return move[0] == [0, 0]

    def predict_projectiles_Score(self, depth=40):
        data = self.data.copy(True, True, False, True)
        copy = Game(self.frame, False, [x for x in data.PlayerSpriteGroup][0], self.board_ratio, self.wave.__copy__(data), data)
        score = 0
        while copy.data.ProjectilePlayerGroup and depth:
            copy.update()
            score += CollisionManager.collision_check_enemies(data)
            depth -= 1
        return score

    def get_lives(self):
        return self.player.lives
