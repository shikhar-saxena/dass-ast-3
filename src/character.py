from colorama import Fore, Back, Style


class Character:
    def __init__(self, damage, display_character):
        self.damage = damage
        self.health = 100
        self.display_character = display_character

    def init_position(self, position_n, position_m):
        self.position_n = position_n
        self.position_m = position_m

    def place_character(self, village):
        # self.temp = village.grid[self.position_n, self.position_m]
        village.grid[self.position_n, self.position_m] = self.display_character

    def clear_character(self, village):

        village.grid[self.position_n, self.position_m] = " "

    # def move(self, village):
    #     pass

    def move_up(self, village):

        up = self.position_n - 1

        if up >= 0 and village.grid[up, self.position_m] == " ":
            self.clear_character(village)
            self.position_n = up
            self.place_character(village)

    def move_left(self, village):

        left = self.position_m - 1

        if left >= 0 and village.grid[self.position_n, left] == " ":
            self.clear_character(village)
            self.position_m = left
            self.place_character(village)

    def move_down(self, village):

        down = self.position_n + 1

        if down < village.n and village.grid[down, self.position_m] == " ":
            self.clear_character(village)
            self.position_n = down
            self.place_character(village)

    def move_right(self, village):

        right = self.position_m + 1

        if right < village.m and village.grid[self.position_n, right] == " ":
            self.clear_character(village)
            self.position_m = right
            self.place_character(village)

    def attack(self, village):

        if self.check_death():
            return

        m = self.position_m
        n = self.position_n

        size_m = village.m
        size_n = village.n

        if m + 1 < size_m:
            building1 = village.get_building(n, m + 1)
        if m - 1 >= 0:
            building2 = village.get_building(n, m - 1)
        if n + 1 < size_n:
            building3 = village.get_building(n + 1, m)
        if n - 1 >= 0:
            building4 = village.get_building(n - 1, m)

        for building in [building1, building2, building3, building4]:
            if building is None:
                continue
            # Damage this building
            building.hitpoints -= self.damage

            # can only hit one building at one point
            return

    def check_death(self):
        if self.health <= 0:
            return True
        else:
            return False

    def get_position(self):
        return (self.position_n, self.position_m)


class King(Character):
    def __init__(self, village):
        """
        King's damage assumed to be 15
        King's position by default assumed to be (15, 1)
        """
        super().__init__(15, "K")
        self.init_position(15, 1)
        self.place_character(village)

    def leviathan_axe(self, village):
        """
        Deal damage to all buildings within 5 tile radius
        """

        i = self.position_n
        j = self.position_m

        for building in village.buildings:
            for tup in building.position:
                if (i - tup[0]) ** 2 + (j - tup[1]) ** 2 <= 25:
                    building.hitpoints -= self.damage
                    break

    def render_health(self):

        print(Fore.LIGHTRED_EX, end="")
        for i in range(self.health):
            print("=", end="")
        if self.health >= 0:
            print(f"> {self.health} {Style.RESET_ALL}")
        else:
            print(f"> 0 {Style.RESET_ALL}")


class Barbarian(Character):
    def __init__(self):
        super().__init__(damage=5, display_character="#")

    """
    Override parent class behaviour (Polymorphism)

    move methods
    """

    def attack(self, village, i, j):
        """
        Attack at position i, j
        """
        building = village.get_building(i, j)

        # Damage this building
        building.hitpoints -= self.damage

        # can only hit one building at one point
        return

    def move_up(self, village):

        up = self.position_n - 1

        if up >= 0:

            if (
                village.grid[up, self.position_m] == " "
                or village.grid[up, self.position_m] == "#"
            ):
                self.clear_character(village)
                self.position_n = up
                self.place_character(village)
            elif village.grid[up, self.position_m] == "W":
                self.attack(village, up, self.position_m)

    def move_left(self, village):

        left = self.position_m - 1

        if left >= 0:
            if (
                village.grid[self.position_n, left] == " "
                or village.grid[self.position_n, left] == "#"
            ):
                self.clear_character(village)
                self.position_m = left
                self.place_character(village)
            elif village.grid[self.position_n, left] == "W":
                self.attack(village, self.position_n, left)

    def move_down(self, village):

        down = self.position_n + 1

        if down < village.n:
            if (
                village.grid[down, self.position_m] == " "
                or village.grid[down, self.position_m] == "#"
            ):
                self.clear_character(village)
                self.position_n = down
                self.place_character(village)
            elif village.grid[down, self.position_m] == "W":
                self.attack(village, down, self.position_m)

    def move_right(self, village):

        right = self.position_m + 1

        if right < village.m:
            if (
                village.grid[self.position_n, right] == " "
                or village.grid[self.position_n, right] == "#"
            ):
                self.clear_character(village)
                self.position_m = right
                self.place_character(village)
            elif village.grid[self.position_n, right] == "W":
                self.attack(village, self.position_n, right)

    def move(self, village):
        if self.check_death():
            return

        """Get nearest building and move towards that"""

        min_distance = None
        min_distance_coordinate = None

        i = self.position_n
        j = self.position_m

        for building in village.buildings:
            if building.display_character == "W":
                continue

            for position in building.position:

                distance = (i - position[0]) ** 2 + (j - position[1]) ** 2

                if min_distance is None or min_distance > distance:
                    min_distance = distance
                    min_distance_coordinate = position

        if min_distance_coordinate is None:
            return

        # Move towards the min_distance_coordinate
        if i < min_distance_coordinate[0] - 1:
            self.move_down(village)
        elif i > min_distance_coordinate[0] + 1:
            self.move_up(village)
        else:
            # same row
            if j < min_distance_coordinate[1] - 1:
                self.move_right(village)

            elif j > min_distance_coordinate[1] + 1:
                self.move_left(village)
            else:
                if (
                    i == min_distance_coordinate[0] - 1
                    and j == min_distance_coordinate[1] + 1
                ):
                    self.move_left(village)
                elif (
                    i == min_distance_coordinate[0] - 1
                    and j == min_distance_coordinate[1] - 1
                ):
                    self.move_right(village)
                elif (
                    i == min_distance_coordinate[0] + 1
                    and j == min_distance_coordinate[1] - 1
                ):
                    self.move_right(village)
                elif (
                    i == min_distance_coordinate[0] + 1
                    and j == min_distance_coordinate[1] + 1
                ):
                    self.move_left(village)
                else:
                    self.attack(
                        village, min_distance_coordinate[0], min_distance_coordinate[1]
                    )
