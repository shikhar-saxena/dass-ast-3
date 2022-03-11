from colorama import Fore, Back, Style
import numpy as np
import random
import os
import time

# class Building:
#     def __init__(self, grid):

#     def random_position(self):

# class Cell:
#     def __init__(self) -> None:
#         pass


class Village:
    """Village Class for the game"""

    def __init__(self):
        self.n = 40
        self.m = 40
        self.grid = np.array([[" " for _ in range(self.m)] for _ in range(self.n)])

        self.add_town_hall()
        self.add_walls()
        self.add_huts()

        # print(Fore.LIGHTBLACK_EX, end="")
        self.print_village()
        print(Style.RESET_ALL, end="")

    def add_huts(self):
        """
        Hut of size 1x1
        Adds 10  huts on the village randomly
        """

        i = 0
        while i != 10:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.m - 1)

            if self.grid[x, y] == " ":
                i += 1
                self.grid[x, y] = "H"

    def add_town_hall(self):
        """
        Adds town hall in the centre of the village
        """

        for x in range(19, 23):
            for y in range(19, 22):
                self.grid[x, y] = "T"
        # self.grid[20, 20] = "T"
        # self.grid[20, 20] = "T"
        # self.grid[20, 20] = "T"

    def add_walls(self):
        """
        Add Wall surrounding town hall
        """

        for x in range(16, 26):
            for y in range(16, 25):

                if x == 16 or x == 25 or y == 16 or y == 24:
                    self.grid[x, y] = "W"

    # def print_cell(self):
    #     print("__", end="|")

    # def print_row(self):
    #     for i in range(self.n):
    #         if i == 0:
    #             print("|", end="")  # row starting
    #         self.print_cell()
    #     print()

    # def print_spaces(self, number_of_spaces):
    #     """Print appropriate number of spaces"""
    #     for _ in range(number_of_spaces):
    #         print(" ", end="")

    def print_village(self, number_of_spaces=0):
        os.system("clear")

        # if self.m == 0:

        #     # self.print_spaces(number_of_spaces)

        #     # print boundary line
        #     for _ in range(self.n):
        #         print("___", end="")
        #     print()
        #     return

        # self.m -= 1

        # self.print_village(number_of_spaces + 1)

        # self.m += 1

        # # Display row (for this m)
        # # self.print_spaces(number_of_spaces)
        # self.print_row()

        switch = {
            "W": f"{Back.BLACK}{Fore.WHITE} W ",
            "T": f"{Back.CYAN}{Fore.BLACK} T ",
            "H": f"{Back.GREEN} H ",
            " ": f"___",
        }

        print("   ", end="")
        for i in range(self.m):
            print(switch[" "], end=" ")
        print()

        for i in range(self.n):

            print("  |" + Style.RESET_ALL, end="")
            for j in range(self.m):

                print(switch[self.grid[i, j]] + Style.RESET_ALL, end="")
                # if j == self.m - 1:
                print("|" + Style.RESET_ALL, end="")

            # print("|" + Style.RESET_ALL, end="")

            print()


class Canon:
    """
    Canon class for the Game
    Canon of size 1x1
    """

    def __init__(self, position):
        # Set position of the canon
        self.X = position.X
        self.Y = position.Y

        # Assuming range to be 7 tiles
        self.range = 7
        self.damage = 50  # Damage


def main():
    bla = Village()
    bla.print_village()
    bla.print_village()

    # t0= time.clock()
    # print("Hello")
    # t1 = time.clock() - t0
    # print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)


if __name__ == "__main__":
    main()
