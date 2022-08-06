from abc import abstractmethod
from typing import List, Tuple

import numpy as np

class Player:

    def __init__(self, location):
        self.location = location

    def get_location(self):
        return self.location

    # not sure if it is wise to do accelerated movement
    def action(self, direction, shoot):
        self.location += direction * 10
        if shoot:
            pass