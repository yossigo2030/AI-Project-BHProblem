import copy
import math
import random

import EnemyType
import MovementPatterns
import pygame
import cooldown
from copy import copy
import linecache

COOLDOWN = 100
FILE_NAME = 'EnemySpawnQueue.txt'


class Wave:
    def __init__(self, board_size, data, isCopy = False, __current_item = None, courser = 0):
        self.data = data
        self.number_of_wave = 0
        self.board_size = board_size
        self.courser = courser
        self.isCopy = isCopy
        self.__current_item = copy(__current_item)
        self.number_of_lines = 0
        self.cooldownCounter = COOLDOWN
        open(FILE_NAME, 'w').close()
        self.start_new_wave()

    def __copy__(self, data):
        wave = Wave(self.board_size, data, True)
        wave.cooldownCounter = self.cooldownCounter
        return wave

    def number_getter(self):
        return self.number_of_wave

    def enemy_DNA(self, number_of_arches, offset, change_factor, frames):
        for i in range(number_of_arches * 12):
            factor = math.cos(i * math.pi / 12) * change_factor
            if not i:
                self.write_to_file([offset + factor, frames + 75, False])
            else:
                self.write_to_file([offset + factor, frames, False])

            if factor != 0:
                self.write_to_file([offset - factor, 0, False])

    def enemy_double_DNA(self, number_of_arches, offset1, offset2, change_factor, frames):
        for i in range(number_of_arches * 12):
            factor = math.cos(i * math.pi / 12) * change_factor
            if not i:
                self.write_to_file([offset1 + factor, frames + 75, False])
            else:
                self.write_to_file([offset1 + factor, frames, False])
            self.write_to_file([offset2 + factor, 0, False])
            if factor != 0:
                self.write_to_file([offset1 - factor, 0, False])
                self.write_to_file([offset2 - factor, 0, False])

    def enemy_collision_formation(self, c):
        for i in range(c):
            self.write_to_file([(i * self.board_size[0] / c + 20), (self.board_size[1] / 3), False])
            #EnemyType.EnemyShooter(pos, r"resources\en.png", self.data, MovementPatterns.StraightPattern((0, 0)),[MovementPatterns.TargetPosPattern(2, self.data.PlayerSpriteGroup.sprites()[0].location)])

    def start_new_wave(self):
        self.number_of_wave += 1
        self.cooldownCounter = COOLDOWN
        self.courser = self.number_of_lines
        if not self.isCopy:
            shape = (((self.number_of_wave - 1) * self.number_of_wave) / 2) + 1
            shape %= 4
            for i in range(self.number_of_wave):
                if shape == 0:
                    self.write_to_file([self.board_size[0] / 2, 100, True])

                if shape == 1:
                    self.enemy_collision_formation(10)

                if shape == 2:
                    self.enemy_DNA(2,
                                   (self.board_size[0] / 2),
                                   (self.board_size[0] / 12),
                                   20)
                if shape == 3:
                    self.enemy_double_DNA(3,
                                          (self.board_size[0] / 4),
                                          ((3 * self.board_size[0]) / 4),
                                          (self.board_size[0] / 12),
                                          30)
                shape = (shape + 1) % 4
        self.read_from_file()

    def update(self):
        if self.courser == self.number_of_lines:
            if self.cooldownCounter == COOLDOWN:
                pass
                print("end of wave")

            if self.cooldownCounter == 0:
                self.start_new_wave()
            self.cooldownCounter -= 1
        else:
            while self.__current_item[1] <= 0:
                head = self.__current_item
                if head[2]:
                    gato = pygame.image.load(r"resources\en_boss.png")
                    EnemyType.BossShooter([head[0], 0], pygame.transform.scale(gato, [75, 75]),
                                          self.data, MovementPatterns.StraightPattern((0, 2 * 0.25)),
                                          [MovementPatterns.StraightPattern((0, 3)),
                                           MovementPatterns.StraightPattern((-1, 3)),
                                           MovementPatterns.StraightPattern((1, 3)),
                                           MovementPatterns.StraightPattern((-2, 3)),
                                           MovementPatterns.StraightPattern((2, 3)),
                                           MovementPatterns.StraightPattern((-3, 3)),
                                           MovementPatterns.StraightPattern((3, 3)),
                                           MovementPatterns.StraightPattern((0, -1)),
                                           MovementPatterns.StraightPattern((1, 0)),
                                           MovementPatterns.StraightPattern((-1, 0)),
                                           MovementPatterns.StraightPattern((1, 1)),
                                           MovementPatterns.StraightPattern((-1, 1)),
                                           MovementPatterns.StraightPattern((1, -1)),
                                           MovementPatterns.StraightPattern((-1, -1))])
                else:
                    # EnemyType.EnemyShooter([head[0], 0], r"resources\en.png", self.data, MovementPatterns.StraightPattern((0, 1)), [MovementPatterns.StraightPattern(((random.random(), 4 * random.random())))])


                    EnemyType.EnemyShooter([head[0], 0], r"resources\en.png", self.data,
                                           MovementPatterns.StraightPattern((0, 1)),
                                           [MovementPatterns.StraightPattern((random.uniform(0, 2)-1, 1.5))])
                if self.courser == self.number_of_lines:
                    break
                else:
                    self.read_from_file()
            else:
                self.__current_item[1] -= 1

    def write_to_file(self, item):
        if len(item) != 3:
            print('error')
            return
        with open(FILE_NAME, 'a') as fp:
            fp.write("%s\t" % str(item[0]))
            fp.write("%s\t" % str(item[1]))
            fp.write("%s\n" % str(item[2]))
            self.number_of_lines += 1


    def read_from_file(self):
        file = open(FILE_NAME)
        item = []
        for pos, l_num in enumerate(file):
            # check if the line number is specified in the lines to read array
            if pos == self.courser:
                # print the required line number
                item = l_num.split()
        # item = linecache.getline(FILE_NAME, self.courser+1).split()
        if len(item) != 3:
            return 0
        self.courser += 1
        if item[2] == 'True':
            self.__current_item = [float(item[0]), int(item[1]), True]
        self.__current_item = [float(item[0]), float(item[1]), False]

    def next_wave_args(self):
        return self.number_of_wave + 1, self.board_size, self.data, self.isCopy, self.courser
