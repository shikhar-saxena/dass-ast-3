from colorama import Fore, Back, Style
import numpy as np


class Building:
    def __init__(self, size_n, size_m, display_character):
        self.hitpoints = 100

        # Add size of building
        self.size_n = size_n
        self.size_m = size_m
        self.display_character = display_character

    def add_building(self, position_n, position_m, grid):
        """
        position contains (n, m) coordinates (Top left cell of the building)

        Function assigns other cells to the building as well, based on its size
        """
        self.position = []

        self.position_start_row = position_n
        self.position_start_column = position_m

        for i in range(position_n, position_n + self.size_n):
            for j in range(position_m, position_m + self.size_m):
                self.position.append((i, j))
                grid[i, j] = self.display_character

        return self

    def remove_building(self, grid):
        """
        position contains (n, m) coordinates (Top left cell of the building)

        Function removes the building from the grid
        """

        for i in range(self.position_start_row, self.position_start_row + self.size_n):
            for j in range(
                self.position_start_column, self.position_start_column + self.size_m
            ):
                grid[i, j] = " "

        # return self

    # def alter_health(self, grid):

    def get_health(self):
        return self.hitpoints


class TownHall(Building):
    def __init__(self):
        super().__init__(4, 3, "T")
        # super().add_building()


class Hut(Building):
    def __init__(self):
        # Assuming huts to be of size 1x1
        super().__init__(1, 1, "H")


class Wall(Building):
    def __init__(self):
        super().__init__(1, 1, "W")


class Cannon(Building):
    def __init__(self):
        """
        Assuming cannon to be of size 2x2
        Assuming range of cannon to be about 7 tiles
        Assuming damage value to be 25
        """
        super().__init__(2, 2, "C")
        self.range = 7
        # town_hall = TownHall()
        self.damage = 25

    def attack(self):
        """
        Attacks any nearby troop or King
        """
        pass


class Village:
    def __init__(self):
        """
        Set n and m for village
        `grid` contains the character to be rendered at that cell
        `buildings` contains all not destroyed buildings (including Walls)
        """
        self.n = 40
        self.m = 40
        self.grid = np.array([[" " for _ in range(self.m)] for _ in range(self.n)])

        # Buildings in the Village
        # Contains positions of the building present
        self.buildings = []

        # Add Town Hall
        self.buildings.append(TownHall().add_building(19, 19, self.grid))

        # Add Cannon
        self.buildings.append(Cannon().add_building(19, 13, self.grid))
        self.buildings.append(Cannon().add_building(21, 26, self.grid))

        # Add 7 Huts
        huts_position = [
            (15, 15),
            (25, 25),
            (15, 25),
            (25, 15),
            (26, 26),
            (15, 20),
            (20, 23),
        ]

        for tup in huts_position:
            self.buildings.append(Hut().add_building(tup[0], tup[1], self.grid))

        # Add Walls
        # for wall_position_column in [12, 28]:

        wall_start_row = 10
        wall_end_row = 28

        wall_start_column = 12
        wall_end_column = 28

        for i in range(wall_start_row, wall_end_row + 1):
            for j in range(wall_start_column, wall_end_column + 1):

                # Get corner elements in these (i,j)
                if (
                    i == wall_start_row
                    or i == wall_end_row
                    or j == wall_start_column
                    or j == wall_end_column
                ):
                    self.buildings.append(Wall().add_building(i, j, self.grid))

    def get_building(self, position_row, position_column):
        """
        Get the building at this position
        """
        if self.grid[position_row, position_column] == " ":
            return None

        for obj in self.buildings:
            for tup in obj.position:
                if tup[0] == position_row and tup[1] == position_column:
                    return obj

        # For King and Characters
        return None

    def display_health(self, i, j):
        """Returns appropriate color to be displayed"""
        building = self.get_building(i, j)

        if building is None:
            health_ij = None
        else:
            health_ij = building.get_health()

        if health_ij is None:
            return Back.RESET
        if health_ij > 50:
            return Back.GREEN
        elif health_ij > 20:
            return Back.YELLOW
        elif health_ij > 0:
            return Back.RED
        else:
            # health_ij <= 0

            # Remove from the grid
            building.remove_building(self.grid)

            # Remove from buildings list
            self.buildings.remove(building)

            return Back.RESET

    def render(self):

        for i in range(self.n):

            for j in range(self.m):

                print(
                    Fore.LIGHTWHITE_EX
                    + self.display_health(i, j)
                    + " "
                    + self.grid[i, j]
                    + " "
                    + Style.RESET_ALL,
                    end="",
                )
            print()