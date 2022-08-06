from abc import abstractmethod
from typing import List, Tuple

import numpy as np

class Player:

    def __init__(self, location):
        self.location = location

    # not sure if it is wise to do accelerated movement
    def action(self, direction, shoot):
        self.location += direction
        if shoot:
            pass