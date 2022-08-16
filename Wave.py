import math
import random

import EnemyType
import MovementPatterns
COOLDOWN = 100

class Wave:
    def __init__(self, number_of_wave, board_ratio):
        self.EnemySpawnQueue = []
        self.number_of_wave = number_of_wave
        self.cooldownCounter = COOLDOWN
        for i in range(3):
            rnd = random.randint(0, 2)
            if rnd == 0:
                self.enemy_DNA(self.EnemySpawnQueue,
                               2,
                               (board_ratio[0] / 2),
                               (board_ratio[0] / 12),
                               20)
            if rnd == 1:
                self.enemy_double_DNA(self.EnemySpawnQueue,
                                      3,
                                      (board_ratio[0] / 4),
                                      ((3 * board_ratio[0]) / 4),
                                      (board_ratio[0] / 12),
                                      30)

    def number_getter(self):
        return self.number_of_wave



    def enemy_DNA(self, EnemySpawnQueue, number_of_arches, offset, change_factor, frames):
        for i in range(number_of_arches * 12):
            factor = math.cos(i * (math.pi) / 12) * change_factor
            EnemySpawnQueue.append([offset + factor, frames])

            if (factor is not 0):
                EnemySpawnQueue.append([offset - factor, 0])

    def enemy_double_DNA(self, EnemySpawnQueue, number_of_arches, offset1, offset2, change_factor, frames):
        for i in range(number_of_arches * 12):
            factor = math.cos(i * (math.pi) / 12) * change_factor
            EnemySpawnQueue.append([offset1 + factor, frames])
            EnemySpawnQueue.append([offset2 + factor, 0])

            if (factor is not 0):
                EnemySpawnQueue.append([offset1 - factor, 0])
                EnemySpawnQueue.append([offset2 - factor, 0])


    def Update(self):
        if len(self.EnemySpawnQueue) == 0:
            if(self.cooldownCounter == COOLDOWN):
                print("end of wave")
            if(self.cooldownCounter == 0):
                return 1
            self.cooldownCounter-=1
        else:
            while self.EnemySpawnQueue[0][1] <= 0:
                head = self.EnemySpawnQueue.pop(0)
                EnemyType.EnemyShooter([head[0], 0],
                                       r"resources\en.png",
                                       MovementPatterns.StraightPattern((0, 1)),
                                       [MovementPatterns.StraightPattern((0, 2))])
                if len(self.EnemySpawnQueue) == 0:
                    break
            else:
                self.EnemySpawnQueue[0][1] -= 1
