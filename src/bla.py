from colorama import Fore, Back, Style
import numpy as np
import random
import os
import time


# class Map:
#     def __init__(self, m, n):
#         self.m = m
#         self.n = n
#         self.grid = np.array([["" for i in range(m)] for j in range(n)])


class Building:
    # def __init__(self):
    #     pass

    def __init__(self, size_n, size_m):
        self.hitpoints = 100

        # Add size of building
        self.size_n = size_n
        self.size_m = size_m

    def add_building(self, position):
        """
        position contains (x, y) coordinates

        Function assigns appropriate coordinates to the building based on its size
        """
        self.position = []

        for i in range(position.n, position.n + self.size_n):
            for j in range(position.m, position.m + self.size_m):
                self.position.append((i, j))


class TownHall(Building):
    def __init__(self):
        super().__init__(4, 3)
        super().add_building()


class Hut(Building):
    def __init__(self):
        # Assuming huts to be of size 1x1
        super().__init__(1, 1)


class Wall(Building):
    def __init__(self):
        super().__init__(1, 1)


class Cannon(Building):
    def __init__(self):
        """
        Assuming cannon to be of size 1x1
        Assuming range of cannon to be about 7 tiles
        Assuming damage value to be 30
        """
        super().__init__(1, 1)
        self.range = 7
        self.damage = 30


class Village(Map):
    def __init__(self):
        super().__init__(40, 40)

    def add_buildings(self):
        pass


if __name__ == "__main__":

    pass
