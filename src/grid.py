from src.character import Barbarian
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

        self.position = np.array(self.position)

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
        Assuming range of cannon to be about 6 tiles
        Assuming damage value to be 7
        """
        super().__init__(2, 2, "C")
        self.range = 6
        self.damage = 7

    def attack(self, troops):
        """
        Attacks any nearby troop or King
        """

        for troop in troops:
            if troop.check_death():
                continue

            (x, y) = troop.get_position()

            if (x - self.position_start_row) ** 2 + (
                y - self.position_start_column
            ) ** 2 <= self.range**2:
                troop.health -= self.damage
                return
        return


class Spawning_Point:
    """
    Three Predefined spawning points at the borders of the village

    (n,m): position around the grid
    """

    def __init__(self, n, m):
        self.position_n = n
        self.position_m = m
        # key for the spawning point (set using the spawn pts array indices)

    def get_position(self):
        return (self.position_n, self.position_m)

    # TODO:
    def add_troop(self, village, game, troop_to_add=Barbarian):
        """
        Add troop to the nearest point on the village
        for this spawning point
        """

        if game.count_troop(troop_to_add) >= 6:
            return

        # Decide init position

        if self.position_n == -1:
            i = 0
            j = self.position_m
        elif self.position_n == village.n:
            i = village.n - 1
            j = self.position_m
        elif self.position_m == -1:
            i = self.position_n
            j = 0
        else:
            i = self.position_n
            j = village.m - 1

        if village.grid[i, j] != " ":
            return None

        barbarian = troop_to_add()
        barbarian.init_position(i, j)
        barbarian.place_character(village)

        return barbarian


class Village:
    def __init__(self):
        """
        Set n and m for village
        `grid` contains the character to be rendered at that cell
        `buildings` contains all not destroyed buildings (including Walls)
        """
        self.n = 38
        self.m = 40
        self.grid = np.array([[" " for _ in range(self.m)] for _ in range(self.n)])

        # Add Spawning points around the village
        self.spawn_pts = [
            Spawning_Point(-1, 20),
            Spawning_Point(17, 40),
            Spawning_Point(38, 12),
        ]

        # Buildings in the Village
        # Contains positions of the building present
        self.buildings = []

        # Add Town Hall
        self.buildings.append(TownHall().add_building(19, 19, self.grid))

        # Add Cannon
        self.buildings.append(Cannon().add_building(19, 13, self.grid))
        self.buildings.append(Cannon().add_building(21, 26, self.grid))
        self.buildings.append(Cannon().add_building(11, 20, self.grid))

        # Add 9 Huts
        huts_position = [
            (15, 15),
            (25, 25),
            (15, 25),
            (25, 15),
            (26, 26),
            (15, 20),
            (20, 23),
            (16, 11),
            (28, 19),
        ]

        for tup in huts_position:
            self.buildings.append(Hut().add_building(tup[0], tup[1], self.grid))

        # Add Walls
        # for wall_position_column in [12, 28]:

        wall_start_row = 6
        wall_end_row = 33

        wall_start_column = 9
        wall_end_column = 31

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
        if 0 > position_row or position_row >= self.n:
            return None

        if 0 > position_column or position_column >= self.m:
            return None

        if self.grid[position_row, position_column] == " ":
            return None

        for obj in self.buildings:
            for tup in obj.position:
                if tup[0] == position_row and tup[1] == position_column:
                    return obj

        # For King and Characters
        return None

    def display_barb_health(self, i, j, troops):
        """Returns appropriate color to be displayed (health of Barbarian)"""

        for troop in troops:
            if troop.get_position() == (i, j):
                health_ij = troop.health
                if health_ij > 50:
                    return Fore.BLUE
                elif health_ij > 20:
                    return Fore.LIGHTBLUE_EX
                elif health_ij > 0:
                    return Fore.LIGHTCYAN_EX
                else:
                    return Fore.WHITE

        return Style.RESET_ALL

    def display_health(self, i, j):
        """Returns appropriate color to be displayed (health of building)"""
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

    def check_spawning_point(self, i, j):

        tup_ij = (i, j)

        for i in range(3):
            if self.spawn_pts[i].get_position() == tup_ij:
                return i + 1

        return None

    def render(self, troops):

        output = "{}{} {} {}"

        for i in range(-1, self.n + 1):

            for j in range(-1, self.m + 1):

                # Display the spawning points
                val = self.check_spawning_point(i, j)

                if val:
                    print(output.format(Fore.CYAN, "", val, Style.RESET_ALL), end="")
                    continue

                # Borders of village
                if j == -1 or j == self.m:
                    print(Fore.RED, "|", Style.RESET_ALL, sep="", end="")
                    continue

                if i == -1 or i == self.n:
                    print(
                        Fore.RED,
                        "---",
                        Style.RESET_ALL,
                        sep="",
                        end="",
                    )
                else:

                    building_color = self.display_health(i, j)

                    if building_color == Back.RESET:

                        # Check barbarian health
                        # if self.grid[i, j] == "#":
                        barb_health_color = self.display_barb_health(i, j, troops)
                        # if barb_health_color == Fore.WHITE:
                        #     self.grid[i, j] = " "

                        if barb_health_color != Style.RESET_ALL:
                            if self.grid[i, j] != "K" and self.grid[i, j] != "Q":
                                self.grid[i, j] = "#"
                            else:
                                barb_health_color = ""

                        print(
                            output.format(
                                Fore.LIGHTWHITE_EX,
                                barb_health_color,
                                self.grid[i, j],
                                Style.RESET_ALL,
                            ),
                            end="",
                        )

                    else:
                        print(
                            output.format(
                                Fore.LIGHTWHITE_EX,
                                building_color,
                                self.grid[i, j],
                                Style.RESET_ALL,
                            ),
                            end="",
                        )

            print()
